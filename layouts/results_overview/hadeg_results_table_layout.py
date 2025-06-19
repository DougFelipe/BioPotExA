"""
T2_toxcsm.py
------------
This script defines the layout for the HADEG Results Table section in a Dash web application. 
The layout includes:
- An introductory message prompting users to view the table.
- A button to trigger the rendering of the HADEG Results Table.
- A container to display the table dynamically.

Components:
- `get_hadeg_results_table_layout`: A function that returns the layout for this section.
"""

# ----------------------------------------
# Imports
# ----------------------------------------

from dash import html  # Dash HTML components for building UI
import dash_bootstrap_components as dbc  # Bootstrap components for styling
from components.ui.alerts import hadeg_alert  # Importing the HADEG alert from a modularized component

# ----------------------------------------
# Function: get_hadeg_results_table_layout
# ----------------------------------------

def get_hadeg_results_table_layout():
    """
    Creates the layout for the HADEG Results Table section.

    The layout includes:
    - A placeholder message prompting users to view the table.
    - A button for rendering the HADEG Results Table.
    - An empty container to dynamically display the table.

    Returns:
        html.Div: A Dash HTML Div containing the layout for the HADEG Results Table section.
    """
    return html.Div([
        # Placeholder message
        html.P(
            "Click the button below to view the HADEG Results Table",  # Informative message
            className="placeholder-message",  # CSS class for styling
            id="hadeg-placeholder-message"  # ID for CSS and interaction
        ),

        # Button to display the table (styled with dbc.Button)
        dbc.Button(
            "View HADEG Results Table",  # Button text
            id="view-hadeg-results-button",  # Unique ID for interaction
            color="success",  # Green button style (indicates action success)
            className="me-1 mt-2",  # Bootstrap utility classes for margin spacing
            n_clicks=0  # Initial click count
        ),

        # Container for the results table (initially empty)
        html.Div(
            id="hadeg-results-table-container",  # ID for the table container
            className="table-container",  # CSS class for styling the container
            style={"marginTop": "20px"}  # Top margin for layout spacing
        )
    ])
