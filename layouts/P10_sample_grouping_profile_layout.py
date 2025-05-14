"""
P10_sample_grouping_profile_layout.py
-------------------------------------
This script defines the layout for the scatter plot visualizing sample groups by compound class. 
It includes a dropdown for filtering by compound class and a container for displaying the plot or a 
message when no data is available.

Functions:
- `get_sample_groups_layout`: Creates the layout for the sample grouping visualization, including 
  a filter dropdown and a responsive container for the scatter plot.
"""

# ----------------------------------------
# Imports
# ----------------------------------------

from dash import html, dcc  # Dash components for building UI
import dash_bootstrap_components as dbc
# ----------------------------------------
# Function: get_sample_groups_layout
# ----------------------------------------

def get_sample_groups_layout():
    """
    Builds the layout for the scatter plot of sample groups by compound class.

    The layout includes:
    - A dropdown for filtering by compound class.
    - A container for displaying the scatter plot or a placeholder message.

    Returns:
    - html.Div: A Dash HTML Div component containing the dropdown filter and the scatter plot container.
    """
    return html.Div(
        [
            # Filter Section
            html.Div(
                [
                    # Label for the dropdown
                    html.Div(
                        'Filter by Compound Class',  # Dropdown label
                        className='menu-text'  # CSS class for styling the label
                    ),
                    # Dropdown for selecting a compound class
                    dcc.Dropdown(
                        id='compound-class-dropdown-p10',  # Unique ID for the dropdown
                        multi=False,  # Single selection allowed
                        placeholder='Select a Compound Class'  # Placeholder text displayed initially
                    )
                ],
                className='navigation-menu'  # CSS class for styling the filter section
            ),
            
            # Scatter Plot Container
            html.Div(
                id='sample-groups-container',  # Unique ID for the container
                children=[
                    # Placeholder message displayed when no data is available
                    html.P(
                        "No data available. Please select a compound class",  # Message text
                        id="no-sample-groups-message",  # Unique ID for the message
                        style={
                            "textAlign": "center",  # Center-align the text
                            "color": "gray"  # Set text color to gray
                        }
                    )
                ],
                className='graph-container',  # CSS class for styling the plot container
                style={
                    'height': 'auto',  # Adjust height automatically
                    'overflowY': 'auto'  # Enable vertical scrolling for overflow
                }
            )
        ],
        className='graph-card'  # CSS class for styling the entire layout card
    )
