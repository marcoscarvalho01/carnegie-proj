import dash
from dash import html, dcc, callback, Input, Output
import plotly.express as px
import dash_bootstrap_components as dbc
import pandas as pd
from utils.data_loader import get_f_campaign_performance
from components.cards import make_kpi_card
from components.dropdowns import make_drop_down
from utils.formatting import format_big_number

dash.register_page(__name__, path='/analytics')


def layout():
    f_performance = get_f_campaign_performance()

    all_regions = sorted(f_performance['Region'].dropna().unique())
    all_platforms = sorted(f_performance['Platform'].dropna().unique())
    all_campaings = sorted(f_performance['CampaignName'].dropna().unique())
    all_kpis = ["Revenue (₹)", "Impressions", "Clicks", "Leads", "Applications", "Enrollments"]

    return dbc.Container([
        dbc.Row([
            dbc.Col(html.H2("Campaign Performance"), width=12)
        ]),
        
        dbc.Row([
            dbc.Col(make_drop_down('kpi-dropdown', "Select KPI:", all_kpis, False), width=3),
            dbc.Col(make_drop_down('campaign-dropdown', "Campaign", all_campaings, True), width=3),
            dbc.Col(make_drop_down('region-dropdown', "Region", all_regions, True), width=3),
            dbc.Col(make_drop_down('platform-dropdown', "Platform", all_platforms, True), width=3),

        ], className="mb-4"),

        dbc.Row([
            dbc.Col(make_kpi_card("Total Revenue", "revenue-card")),
            dbc.Col(make_kpi_card("Total Spend", "spend-card")),
            dbc.Col(make_kpi_card("ROI (Revenue/Cost)", "roi-card")),
            dbc.Col(make_kpi_card("Total Enrollments", "enrollments-card")),
            dbc.Col(make_kpi_card("CPA (Cost/Enroll)", "cpa-card"))
        ], class_name="mb-4 row-cols-1 row-cols-md-5 g-3"),

        dbc.Row([
            dbc.Col(dcc.Graph(id='performance-by-campaign-graph'), width=6),
            dbc.Col(dcc.Graph(id="performance-over-time"), width=6)
        ]),

        dbc.Row([
            dbc.Col(dcc.Graph(id="marketing-funnel-graph"), width=12)
        ], className="mb-4")
    ])


@callback(
    Output('revenue-card', 'children'),
    Output('spend-card', 'children'),
    Output('roi-card', 'children'),
    Output('enrollments-card', 'children'),
    Output('cpa-card', 'children'),
    Output('performance-by-campaign-graph', 'figure'),
    Output('performance-over-time', 'figure'),
    Output('marketing-funnel-graph', 'figure'),
    Input('kpi-dropdown', 'value'),
    Input('campaign-dropdown', 'value'),
    Input('region-dropdown', 'value'),
    Input('platform-dropdown', 'value'),
)
def update_graph(selected_kpi, campaigns, regions, platforms):
    # loaders
    df = get_f_campaign_performance()

    # Global Filters
    if regions:
        df = df[df['Region'].isin(regions)]

    if platforms:
        df = df[df['Platform'].isin(platforms)]

    if campaigns:
        df = df[df['CampaignName'].isin(campaigns)]

    if df.empty:
        # Return an empty graph with a message
        fig_by_campaign = px.bar(title="No data available for this selection")
        fig_by_campaign.update_layout(xaxis={"visible": False}, yaxis={"visible": False})
        return "-", "-", "-", "-", "-", fig_by_campaign, fig_by_campaign

    # Totals Cards
    total_revenue = f"₹ {format_big_number(df['Revenue (₹)'].sum())}"
    total_spend = f"₹ {format_big_number(df['Cost (₹)'].sum())}"
    
    cost_sum = df["Cost (₹)"].sum()
    rev_sum = df["Revenue (₹)"].sum()
    roi = f"{rev_sum / cost_sum:.0%}" if cost_sum > 0 else "0%"

    enroll_sum = df['Enrollments'].sum()
    total_enrollments = format_big_number(enroll_sum)

    cpa_val = cost_sum / enroll_sum if enroll_sum > 0 else 0
    cpa = f"₹ {cpa_val:,.2f}"

    # performance by campaign
    performance_by_campaign = df.groupby(["CampaignName", "Platform"])[selected_kpi].sum().reset_index()
    performance_by_campaign = performance_by_campaign.sort_values(selected_kpi, ascending=True)

    fig_by_campaign = px.bar(
        performance_by_campaign,
        title="Performance by Campaign",
        x=selected_kpi,
        y="CampaignName",
        template="plotly_white",
        text_auto='.2s',
        orientation='h'
    )

    # performance by month
    performance_by_month = df.groupby(pd.Grouper(key='Date', freq='MS'))[selected_kpi].sum().reset_index()
    fig_by_month = px.line(
        performance_by_month,
        title="Monthly Performance",
        x="Date",
        y=selected_kpi,
        template="plotly_white"
    )

    # conversion funnel
    funnel_stages = ["Impressions", "Clicks", "Leads", "Applications", "Enrollments"]
    
    funnel_values = [df[stage].sum() for stage in funnel_stages]
    
    funnel_df = pd.DataFrame({
        'Stage': funnel_stages, 
        'Value': funnel_values
    })

    fig_funnel = px.funnel(
        funnel_df, 
        x='Value', 
        y='Stage', 
        title="Conversion Funnel (Impressions to Enrollments)",
        template="plotly_white",
    )
    
    fig_funnel.update_traces(texttemplate="%{value:.2s}<br>%{percentInitial:.2%} Initial<br>%{percentPrevious:.2%} Previous")

    return total_revenue, total_spend, roi, total_enrollments, cpa, fig_by_campaign, fig_by_month, fig_funnel