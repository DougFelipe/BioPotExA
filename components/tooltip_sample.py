# ----------------------------------------
# Imports
# ----------------------------------------

from dash import html  # Dash HTML components
import dash_bootstrap_components as dbc  # Dash Bootstrap components for styling and alerts

def input_format_tooltip(custom_text):
    """
    Creates a tooltip component that displays a custom explanatory text.

    Parameters:
    - custom_text (str): The text to display in the tooltip.

    Returns:
    - dash.html.Div: A Dash HTML Div component containing the formatted tooltip.
    """
    return html.Div(
        className="tooltip-container",
        children=[
            html.Span(
                "i",  # Pode ser um ícone ou ponto de interrogação
                className="tooltip-icon"  # Estilize com CSS para parecer um botão ou símbolo
            ),
            html.Div(
                className="tooltip-content",
                children=[
                    html.P(
                        custom_text,
                        className="tooltip-description"
                    )
                ]
            )
        ]
    )
