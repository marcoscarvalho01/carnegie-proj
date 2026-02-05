from dash import html
import dash_bootstrap_components as dbc

def make_kpi_card(title, value_id, color="primary"):
    """
    Generates a reusable KPI Card.
    
    Args:
        title (str): The label (e.g., "Total Revenue")
        value_id (str): The ID needed for the Callback to update the number.
        color (str): Bootstrap color (primary, success, danger, warning, info)
    """
    return dbc.Card(
        dbc.CardBody([
            # Title Row
            html.H6(title, className="card-title text-muted text-uppercase", style={'fontSize': '0.8rem'}),
            
            # Value Row
            html.H2("...", id=value_id, className=f"display-6 fw-bold text-{color}"),
            
            # Decorative bottom border
            html.Div(className=f"border-top border-{color} border-3 mt-2 w-25")
        ]),
        className="shadow-sm h-100", 
        style={"border": "none", "borderRadius": "10px"}
    )