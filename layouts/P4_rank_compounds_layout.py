"""
P4_rank_compounds_layout.py
---------------------------
This script defines the layout for the ranking chart of samples based on compound interaction in a Dash web application.

The layout includes:
- A filter for selecting a range of compound counts using a range slider.
- A scatter plot to display the ranking of compounds based on their interaction with samples.
"""

# ----------------------------------------
# Imports
# ----------------------------------------

from dash import html, dcc  # Dash components for creating UI
from utils.filters import create_range_slider  # Utility function to create a range slider

# ----------------------------------------
# Function: get_rank_compounds_layout
# ----------------------------------------

def get_rank_compounds_layout():
    """
    Constructs the layout for the ranking chart of samples based on their interaction with compounds.

    Layout includes:
    - A navigation menu containing a range slider for filtering by compound count range.
    - A scatter plot to display the ranking of compounds.

    Returns:
    - dash.html.Div: A container (`Div`) with the ranking chart and the filter.
    """
    # Create a range slider for filtering by compound count range
    range_slider = create_range_slider(slider_id='compound-count-range-slider')

    # Define the layout structure
    return html.Div(
        [
            # Navigation menu with the range slider
            html.Div(
                [
                    # Text label for the range slider
                    html.Div('Filter by Compound Count Range', className='menu-text'),
                    range_slider  # Range slider component
                ],
                className='navigation-menu'  # CSS class for styling the navigation menu
            ),
            # Container for the scatter plot
            html.Div(
                dcc.Graph(id='rank-compounds-scatter-plot'),  # Graph component for displaying the ranking scatter plot
                className='graph-container',  # CSS class for styling the graph container
                style={
                    'height': 'auto',  # Automatically adjusts the height of the graph container
                    'overflowY': 'auto'  # Enables vertical scrolling if the content overflows
                }
            )
        ],
        className='graph-card'  # CSS class for styling the entire layout card
    )
