"""
P11_gene_sample__heatmap_layout.py
-----------------------------------
This script defines the layout for a gene-sample heatmap in a Dash web application. 
The layout includes dynamic messages and conditional rendering to handle cases where no data is available.

The layout features:
- Filters for selecting a compound pathway and pathway.
- A container for displaying the heatmap or a message when no data is available.
"""

# ----------------------------------------
# Imports
# ----------------------------------------

from dash import html, dcc  # Dash components for building layouts and interactivity

# ----------------------------------------
# Function: get_gene_sample_heatmap_layout
# ----------------------------------------

def get_gene_sample_heatmap_layout():
    """
    Builds the layout for the gene-sample heatmap with dynamic messages and conditional rendering.

    The layout includes:
    - Dropdown filters for selecting a compound pathway and a pathway.
    - A container for displaying the heatmap or a placeholder message if no data is available.

    Returns:
        dash.html.Div: A Div containing the heatmap and its associated filters.
    """
    return html.Div(
        [
            # Filter Section
            html.Div(
                [
                    # Dropdown for selecting a compound pathway
                    html.Div('Filter by Compound Pathway', className='menu-text'),
                    dcc.Dropdown(
                        id='compound-pathway-dropdown-p11',
                        multi=False,  # Allows single selection
                        placeholder='Select a Compound Pathway'  # Placeholder text
                    ),

                    # Dropdown for selecting a pathway
                    html.Div('Filter by Pathway', className='menu-text'),
                    dcc.Dropdown(
                        id='pathway-dropdown-p11',
                        multi=False,  # Allows single selection
                        placeholder='Select a Pathway'  # Placeholder text
                    )
                ],
                className='navigation-menu'  # CSS class for styling the filter section
            ),

            # Heatmap Container
            html.Div(
                id='gene-sample-heatmap-container',  # Unique ID for the heatmap container
                children=[
                    # Placeholder message displayed when no data is available
                    html.P(
                        "No data available. Please select a compound pathway and pathway",  # Informative message
                        id="no-gene-sample-heatmap-message",  # Unique ID for styling or interactivity
                        style={"textAlign": "center", "color": "gray"}  # Center alignment and gray color for the text
                    )
                ],
                className='graph-container',  # CSS class for the heatmap container
                style={'height': 'auto', 'overflowY': 'auto'}  # Adjust height and enable vertical scrolling if needed
            )
        ],
        className='graph-card'  # CSS class for the overall graph card container
    )
