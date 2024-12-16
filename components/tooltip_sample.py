from dash import html
import dash_bootstrap_components as dbc

def input_format_tooltip():
    """
    Tooltip component to show the expected input format for sample data.
    """
    return html.Div(
        className="tooltip-container",
        children=[
            # Texto do Tooltip
            html.Span("your dataset in this format", className="tooltip-text"),
            html.Div(
                className="tooltip-content",
                children=[
                    html.P("Input data must be formatted as below", className="tooltip-header"),
                    
                    # Exemplo de formato esperado
                    html.Pre(
                        ">Sample1\nK00031\nK00032\nK00090\nK00042\nK00052\n"
                        ">Sample2\nK00031\nK00032\nK00090\nK00042\nK00052\n"
                        ">Sample3\nK00031\nK00032\nK00090\nK00042\nK00052",
                        className="tooltip-example"
                    ),
                    
                    # Alerta ajustado com texto claro
                    dbc.Alert(
                        "Note: This is just an example. Your actual dataset should contain all KO IDs from the real sample",
                        color="danger",
                        className="tooltip-alert"
                    ),
                ]
            )
        ]
    )
