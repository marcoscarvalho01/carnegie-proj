from dash import html, dcc

def make_drop_down(id_name, label, options, multi):
    """
    Generates a reusable KPI Card.
    
    Args:
        id_name (str): The ID needed for the Callback to update the graphs.
        label (str): The label to be shown above the dropdown (e.g., "Total Revenue")
        options (list): List of options to be rendered
        multi (bool): whether the dropdown is multiselect or not
    """
    return html.Div([
                html.Label(label),
                dcc.Dropdown(
                    id=id_name,
                    options=options,
                    value=options[0] if not multi else options,
                    searchable=False,
                    multi=multi,
                )
            ])
