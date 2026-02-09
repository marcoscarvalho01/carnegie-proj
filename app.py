import dash
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
from utils.caching import cache

app = Dash(__name__, use_pages=True, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server

cache_config = {
    "CACHE_TYPE": "SimpleCache",  
    "CACHE_DEFAULT_TIMEOUT": 300  # Default 5 minutes
}

cache.init_app(app.server, config=cache_config)

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
], className="px-0 pt-0", fluid=True)

if __name__ == '__main__':
    app.run(debug=True)