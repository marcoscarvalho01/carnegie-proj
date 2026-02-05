import dash
from dash import html, dcc, callback, Input, Output
import plotly.express as px
import dash_bootstrap_components as dbc
import pandas as pd
from utils.data_loader import get_f_campaign_performance

# Register this page at the URL '/analytics'
dash.register_page(__name__, path='/analytics')

f_performance = get_f_campaign_performance()

# Define the layout (Just the content, no app.run_server)
layout = dbc.Container([
    dbc.Row([
        dbc.Col(html.H2("Campaign Performance Dashboard"), width=12)
    ]),
    
    dbc.Row([
        dbc.Col([
            html.Label("Select Variable:"),
            dcc.Dropdown(
                id='column-dropdown',
                options=[{'label': i, 'value': i} for i in ["Impressions", "Clicks", "Leads"]],
                value='Impressions',
                clearable=False
            ),
        ], width=4),
    ], className="mb-4"),

    dbc.Row([
        dbc.Col(dcc.Graph(id='analytics-graph'), width=12)
    ])
])

# Callbacks must be explicitly registered using 'callback' (not app.callback)
@callback(
    Output('analytics-graph', 'figure'),
    Input('column-dropdown', 'value')
)
def update_graph(selected_col):
    performance_by_campaign = f_performance.groupby(["CampaignName", "Platform"])[selected_col].sum().reset_index()

    fig = px.bar(performance_by_campaign, x=selected_col, color="Platform", y="CampaignName", template="plotly_white")


    return fig