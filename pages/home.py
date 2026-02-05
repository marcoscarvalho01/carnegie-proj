import dash
from dash import html
import dash_bootstrap_components as dbc

# This line is CRITICAL. It tells Dash: "This is the homepage (/)"
dash.register_page(__name__, path='/')

layout = dbc.Container(
    [
        dbc.Row(
            dbc.Col(
                html.H2("Welcome to Carnegie Analytics")
            )
        ),
        dbc.Row(
            dbc.Col(
                html.P("Select 'Analytics' to see the dashboard.")
            )
        )
    ]
)
    

html.Div([
    html.H1("Welcome to Carnegie Analytics"),
    html.P("Select 'Analytics' in the navigation bar to see the dashboard."),
])