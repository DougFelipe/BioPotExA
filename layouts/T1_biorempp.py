"""
T1_biorempp.py
--------------
This script defines the layout for the "BioRemPP Results Table" section in a Dash web application. 
The layout includes:
- An initial placeholder message.
- A button for rendering the results table.
- A container for displaying the table once it is rendered.

The table layout is styled using Dash HTML components and Dash Bootstrap Components (DBC).
"""

# ----------------------------------------
# Imports
# ----------------------------------------

from dash import html  # Dash HTML components for layout structure
import dash_bootstrap_components as dbc  # Bootstrap components for styling and buttons

# ----------------------------------------
# Function: get_biorempp_results_table_layout
# ----------------------------------------

def get_biorempp_results_table_layout():
    """
    Creates the layout for the "BioRemPP Results Table" section.

    The layout includes:
    - A placeholder message prompting the user to view the results table.
    - A button styled with Bootstrap to trigger the display of the table.
    - A container for the results table, which is initially empty and styled for spacing.

    Returns:
    - html.Div: A Dash HTML Div containing the layout components.
    """
    return html.Div([
        # Initial message prompting the user to view the results table
        html.P(
            "Click the button below to view the BioRemPP Results Table",  # User-facing message
            className="placeholder-message",  # CSS class for styling the message
            id="biorempp-placeholder-message"  # Unique ID for the message element
        ),

        # Button to display the results table (styled using dbc.Button)
        dbc.Button(
            "View BioRemPP Results Table",  # Button text
            id="view-biorempp-results-button",  # Unique ID for the button
            color="success",  # Sets the button color to green (Bootstrap "success" theme)
            className="me-1 mt-2",  # Adds right margin (me-1) and top margin (mt-2) for spacing
            n_clicks=0  # Initializes the click counter to 0
        ),

        # Container for the results table (initially empty)
        html.Div(
            id="biorempp-results-table-container",  # Unique ID for the table container
            className="table-container",  # CSS class for styling the table container
            style={"marginTop": "20px"}  # Adds top margin for layout organization
        )
    ])
