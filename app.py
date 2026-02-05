import dash
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc

app = Dash(__name__, use_pages=True, external_stylesheets=[dbc.themes.FLATLY])

app.layout = dbc.Container([
    dbc.NavbarSimple(
        brand="Carnegie Analytics",
        brand_href="/",
        color="primary",
        dark=True,
        children=[
            dbc.NavItem(dbc.NavLink("Home", href="/")),
            dbc.NavItem(dbc.NavLink("Analytics", href="/analytics")),
        ]
    ),
    
    dash.page_container 
], fluid=True)

if __name__ == '__main__':
    app.run(debug=True)