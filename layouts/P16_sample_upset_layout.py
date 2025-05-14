"""
P16_sample_upset_layout.py
--------------------------
This script defines the layout for the UpSet Plot feature in a Dash web application.
The UpSet Plot visualizes the intersections of selected samples and their associated KO identifiers.

The layout includes:
- A dropdown for multi-selection of samples.
- A container for displaying the UpSet Plot or a placeholder message if no samples are selected.

Functions:
- `get_sample_upset_layout`: Constructs and returns the layout for the UpSet Plot.
"""

# ----------------------------------------
# Imports
# ----------------------------------------

from dash import html, dcc  # Dash components for HTML structure and interactivity
import dash_bootstrap_components as dbc
# ----------------------------------------
# Function: get_sample_upset_layout
# ----------------------------------------

def get_sample_upset_layout():
    """
    Constructs the layout for the UpSet Plot of samples and KO identifiers.

    The layout includes:
    - A dropdown for selecting multiple samples.
    - A placeholder message displayed when no plot is available.

    Returns:
    - dash.html.Div: A Div containing the dropdown and the UpSet Plot container.
    """
    return html.Div([
        # Navigation menu containing the dropdown
        html.Div([
            # Instructional text for the dropdown
            html.Div('Select Samples', className='menu-text'),
            dcc.Dropdown(
                id='upsetplot-sample-dropdown',  # Unique ID for the dropdown
                multi=True,  # Allows multiple selections
                placeholder="Select the samples",  # Instructional placeholder text
                style={"margin-bottom": "20px"}  # Adds spacing below the dropdown
            )
        ], className='navigation-menu'),  # CSS class for styling the navigation menu

        # Container for the UpSet Plot
        html.Div(
            id='upset-plot-container',  # Unique ID for the plot container
            children=[
                # Placeholder message when no plot is available
                html.P(
                    "No plot available. Please select samples.",  # Message displayed when no samples are selected
                    id="no-upset-plot-message",  # Unique ID for the message
                    style={"textAlign": "center", "color": "gray"}  # Center-aligned text with gray color
                )
            ],
            className='graph-card'  # CSS class for styling the graph container
        )
    ])
