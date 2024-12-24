"""
P5_rank_compounds_layout.py
---------------------------
This script defines the layout for the compound ranking graph in a Dash web application. 
The layout includes:
- A dropdown filter for selecting a compound class.
- A container for displaying the ranking graph or a placeholder message when no data is available.
"""

# ----------------------------------------
# Imports
# ----------------------------------------

from dash import html, dcc  # Dash components for HTML and interactive elements

# ----------------------------------------
# Function: get_rank_compounds_layout
# ----------------------------------------

def get_rank_compounds_layout():
    """
    Constructs the layout for the compound ranking graph based on the number of samples interacting with them. 
    Includes a dropdown filter for selecting a compound class.

    Returns:
        dash.html.Div: A Div containing the ranking graph and the compound class filter.
    """
    return html.Div(
        [
            # Filter Section
            html.Div(
                [
                    # Filter label
                    html.Div('Filter by Compound Class', className='menu-text'),

                    # Dropdown for compound class selection
                    dcc.Dropdown(
                        id='p5-compound-class-dropdown',  # Unique ID for the dropdown
                        multi=False,  # Allows single selection
                        placeholder='Select a Compound Class'  # Placeholder text for the dropdown
                    )
                ],
                className='navigation-menu'  # CSS class for styling the filter section
            ),

            # Graph or Placeholder Container
            html.Div(
                id='p5-compound-ranking-container',  # ID for dynamic updates to the container
                children=[
                    # Placeholder message when no data is available
                    html.P(
                        "No data available. Please select a compound class.",  # Placeholder text
                        id="p5-placeholder-message",  # Unique ID for the placeholder message
                        style={"textAlign": "center", "color": "gray"}  # Center-aligned gray text
                    )
                ],
                className='graph-container',  # CSS class for styling the graph container
                style={
                    'height': 'auto',  # Automatic height adjustment
                    'overflowY': 'auto'  # Enables vertical scrolling if content overflows
                }
            )
        ],
        className='graph-card'  # CSS class for styling the overall layout
    )
