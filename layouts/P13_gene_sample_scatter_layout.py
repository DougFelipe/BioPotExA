"""
P13_gene_sample_scatter_layout.py
---------------------------------
This script defines the layout for a scatter plot visualization in a Dash web application. 
The scatter plot shows the relationship between KOs (KEGG Orthologs) and samples for a selected pathway. 

The layout includes:
- A dropdown menu for filtering data by pathway.
- A container to display the scatter plot or a default message when no data is available.
"""

# ----------------------------------------
# Imports
# ----------------------------------------

from dash import html, dcc  # Dash components for building the UI

# ----------------------------------------
# Function: get_sample_ko_scatter_layout
# ----------------------------------------

def get_sample_ko_scatter_layout():
    """
    Constructs the layout for the scatter plot of KOs in samples for the selected pathway.

    The layout contains:
    - A navigation menu with a dropdown filter for selecting a pathway.
    - A container to display the scatter plot or a placeholder message if no data is available.

    Returns:
        html.Div: A Dash HTML Div component containing the scatter plot and the filter.
    """
    return html.Div(
        [
            # Navigation menu with dropdown filter
            html.Div(
                [
                    # Title for the navigation menu
                    html.Div('Filter by Pathway', className='menu-text'),

                    # Dropdown menu for pathway selection
                    dcc.Dropdown(
                        id='pathway-dropdown-p13',  # ID for the dropdown filter
                        multi=False,  # Single selection allowed
                        placeholder='Select a Pathway',  # Placeholder text for the dropdown
                        style={'margin-bottom': '20px'}  # Bottom margin for spacing
                    )
                ],
                className='navigation-menu'  # CSS class for styling the menu
            ),

            # Container for the scatter plot or default message
            html.Div(
                id='scatter-plot-container',  # ID for the scatter plot container
                children=[
                    # Default message displayed when no data is available
                    html.P(
                        "No data available. Please select a pathway",  # Default message text
                        id="no-data-message-p13",  # ID for the message
                        style={
                            "textAlign": "center",  # Center align the text
                            "color": "gray"  # Gray color for the message text
                        }
                    )
                ],
                className='graph-container',  # CSS class for styling the container
                style={
                    'height': 'auto',  # Automatically adjusts height
                    'overflowY': 'auto'  # Enables vertical scrolling if needed
                }
            )
        ],
        className='graph-card'  # CSS class for styling the overall layout card
    )
