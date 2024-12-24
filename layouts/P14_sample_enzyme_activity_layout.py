"""
P14_sample_enzyme_activity_layout.py
------------------------------------
This script defines the layout for the sample enzyme activity bar chart in a Dash web application.
The layout includes a dropdown menu for sample selection and a container for the bar chart display.

The layout is designed to allow users to filter and view enzyme activity data based on the selected sample.
"""

# ----------------------------------------
# Imports
# ----------------------------------------

from dash import html, dcc  # Dash HTML and core components for building UI

# ----------------------------------------
# Function: get_sample_enzyme_activity_layout
# ----------------------------------------

def get_sample_enzyme_activity_layout():
    """
    Constructs the layout for the bar chart of enzyme activity counts per sample.

    The layout includes:
    - A dropdown menu for filtering by sample.
    - A container for the bar chart with a placeholder message when no data is available.

    Returns:
    - dash.html.Div: A Dash HTML Div component containing the dropdown and the bar chart container.
    """
    return html.Div(
        [
            # Dropdown menu for sample filtering
            html.Div(
                [
                    html.Div(
                        'Filter by Sample',  # Title for the dropdown menu
                        className='menu-text'  # CSS class for styling the title
                    ),
                    dcc.Dropdown(
                        id='sample-enzyme-dropdown',  # ID for the dropdown menu
                        placeholder="Select a Sample",  # Placeholder text for user instruction
                    ),
                ],
                className='navigation-menu'  # CSS class for styling the navigation menu
            ),
            
            # Container for the enzyme activity bar chart
            html.Div(
                id='enzyme-bar-chart-container',  # ID for the bar chart container
                children=[
                    # Placeholder message when no data is available
                    html.P(
                        "No data available. Please select a sample",  # Informational message
                        id="no-enzyme-bar-chart-message",  # ID for the message element
                        style={"textAlign": "center", "color": "gray"}  # Centered, gray text style
                    )
                ],
                className='graph-container'  # CSS class for styling the graph container
            )
        ],
        className='graph-card'  # CSS class for styling the overall card container
    )
