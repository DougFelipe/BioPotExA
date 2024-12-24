"""
T3_toxcsm.py
------------
This script defines the layout for the ToxCSM Results Table section in a Dash web application.
It includes:
- An initial placeholder message.
- A button to render the ToxCSM results table.
- A container to display the results table.

The layout uses Dash HTML components and Bootstrap for styling.
"""

# ----------------------------------------
# Imports
# ----------------------------------------

from dash import html  # Dash HTML components for building UI
import dash_bootstrap_components as dbc  # Bootstrap components for styling
from components.alerts import toxcsm_alert  # Modularized alert for ToxCSM integration

# ----------------------------------------
# Function: get_toxcsm_results_table_layout
# ----------------------------------------

def get_toxcsm_results_table_layout():
    """
    Creates the layout for the ToxCSM Results Table section.

    The layout includes:
    - A placeholder message prompting users to view the ToxCSM results.
    - A button styled with Bootstrap to render the results table.
    - An initially empty container for displaying the results table.

    Returns:
    - html.Div: A Dash HTML Div component containing the section layout.
    """
    return html.Div([
        # Initial placeholder message
        html.P(
            "Click the button below to view the ToxCSM Results Table",
            className="placeholder-message",  # CSS class for styling the message
            id="toxcsm-placeholder-message"  # Unique ID for referencing the message
        ),

        # Button to render the results table (styled with dbc.Button)
        dbc.Button(
            "View ToxCSM Results Table",  # Button text
            id="view-toxcsm-results-button",  # Unique ID for the button
            color="success",  # Bootstrap color class for a green button
            className="me-1 mt-2",  # Bootstrap utility classes for margin (spacing)
            n_clicks=0  # Tracks the number of clicks (initial value is 0)
        ),

        # Container for the results table (initially empty)
        html.Div(
            id="toxcsm-results-table-container",  # Unique ID for referencing the table container
            className="table-container",  # CSS class for styling the container
            style={"marginTop": "20px"}  # Inline style for top margin to improve layout spacing
        )
    ])
