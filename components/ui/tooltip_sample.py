# ----------------------------------------
# Imports
# ----------------------------------------

from dash import html  # Dash HTML components
import dash_bootstrap_components as dbc  # Dash Bootstrap components for styling and alerts
def input_format_tooltip():
    """
    Tooltip component to show the expected input format for sample data.
    """
    return html.Div(
        className="tooltip-container",
        children=[
            html.Span("short exemple", className="tooltip-text"),
            html.Div(
                className="tooltip-content",
                children=[
                    html.P("Input data must be formatted as below", className="tooltip-header"),
                    html.Pre(
                        ">Sample1\nK00031\nK00032\nK00090\nK00042\nK00052\n"
                        ">Sample2\nK00031\nK00032\nK00090\nK00042\nK00052\n"
                        ">Sample3\nK00031\nK00032\nK00090\nK00042\nK00052",
                        className="tooltip-example"
                    )
                ]
            )
        ]
    )
