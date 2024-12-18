"""
tooltip_sample.py
-----------------
This script defines a tooltip component for a Dash web application. The tooltip provides users 
with an example of the expected input data format for sample data and includes explanatory text.

The component uses Dash HTML elements and Bootstrap components to ensure clear and visually 
appealing formatting of the tooltip.
"""

# ----------------------------------------
# Imports
# ----------------------------------------

from dash import html  # Dash HTML components
import dash_bootstrap_components as dbc  # Dash Bootstrap components for styling and alerts

# ----------------------------------------
# Function: input_format_tooltip
# ----------------------------------------

def input_format_tooltip():
    """
    Creates a tooltip component that displays the expected input format for sample data.

    This component includes:
    - A descriptive header.
    - A preformatted example showing the correct data structure.
    - A warning alert to clarify the example's purpose.

    Returns:
    - dash.html.Div: A Dash HTML Div component containing the formatted tooltip.
    """
    return html.Div(
        className="tooltip-container",  # Custom CSS class for styling the tooltip container
        children=[
            # Text displayed as part of the tooltip prompt
            html.Span(
                "providing your dataset in a .txt file in this format", 
                className="tooltip-text"  # Custom CSS class for tooltip text
            ),
            html.Div(
                className="tooltip-content",  # CSS class for the tooltip content block
                children=[
                    # Header text to explain the purpose of the tooltip
                    html.P(
                        "Input data must be formatted as below", 
                        className="tooltip-header"  # CSS class for header text
                    ),
                    
                    # Preformatted example of the expected input format
                    html.Pre(
                        ">Sample1\nK00031\nK00032\nK00090\nK00042\nK00052\n"
                        ">Sample2\nK00031\nK00032\nK00090\nK00042\nK00052\n"
                        ">Sample3\nK00031\nK00032\nK00090\nK00042\nK00052",
                        className="tooltip-example"  # CSS class for displaying preformatted code
                    ),
                    
                    # Alert box to clarify that the example is illustrative
                    dbc.Alert(
                        "Note: This is just an example. Your actual dataset should contain all KO IDs from the real sample",
                        color="danger",  # Bootstrap alert color (red for warning)
                        className="tooltip-alert"  # CSS class for the alert box
                    ),
                ]
            )
        ]
    )
