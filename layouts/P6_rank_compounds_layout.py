"""
P6_rank_compounds_layout.py
---------------------------
This script defines the layout for the compound ranking graph based on the number of unique genes acting on each compound.
It includes:
- A dropdown filter to select a compound class.
- A dynamic container to display the ranking graph or a placeholder message when no data is available.
"""

# ----------------------------------------
# Imports
# ----------------------------------------

from dash import html, dcc  # Dash HTML and DCC components for building the layout

# ----------------------------------------
# Function: get_rank_compounds_gene_layout
# ----------------------------------------

def get_rank_compounds_gene_layout():
    """
    Constructs the layout for the compound ranking graph based on the number of unique genes acting on each compound. 
    Includes a dropdown filter to allow users to select a compound class.

    Returns:
        html.Div: A Dash HTML Div containing the ranking graph and filter dropdown.
    """
    return html.Div(
        [
            # Dropdown Filter Section
            html.Div(
                [
                    # Label for the dropdown
                    html.Div(
                        'Filter by Compound Class',  # Instructional text for the filter
                        className='menu-text'  # CSS class for styling the menu text
                    ),
                    # Dropdown for selecting a compound class
                    dcc.Dropdown(
                        id='p6-compound-class-dropdown',  # Unique ID for the dropdown
                        multi=False,  # Single selection allowed
                        placeholder='Select a Compound Class',  # Placeholder text displayed when no option is selected
                        style={"margin-bottom": "20px"}  # Adds bottom spacing for visual separation
                    )
                ],
                className='navigation-menu'  # CSS class for styling the dropdown container
            ),
            # Dynamic Graph Container Section
            html.Div(
                id='p6-compound-ranking-container',  # Dynamic container for graph or placeholder message
                children=[
                    # Placeholder message displayed when no data is available
                    html.P(
                        "No data available. Please select a compound class",  # Message text
                        id="p6-placeholder-message",  # Unique ID for the message
                        style={
                            "textAlign": "center",  # Centers the text horizontally
                            "color": "gray",  # Gray text color for a subtle appearance
                            "marginTop": "20px"  # Adds top margin for spacing
                        }
                    )
                ],
                className='graph-container',  # CSS class for styling the graph container
                style={
                    'height': 'auto',  # Adjusts height dynamically based on content
                    'overflowY': 'auto'  # Enables vertical scrolling if content overflows
                }
            )
        ],
        className='graph-card'  # CSS class for the overall card containing the layout
    )
