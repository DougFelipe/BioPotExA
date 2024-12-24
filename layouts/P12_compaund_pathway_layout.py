"""
P12_compound_pathway_layout.py
------------------------------
This script defines the layout for the Pathway and Compound Pathway heatmap. 
The layout includes a dropdown filter for selecting a sample and a placeholder message displayed when no data is available.

Functionality:
- Allows users to filter the heatmap by sample using a dropdown.
- Displays a placeholder message when no sample is selected or data is unavailable.
"""

# ----------------------------------------
# Imports
# ----------------------------------------

from dash import html, dcc  # Dash components for layout and interactivity

# ----------------------------------------
# Function: get_pathway_heatmap_layout
# ----------------------------------------

def get_pathway_heatmap_layout():
    """
    Constructs the layout for the Pathway and Compound Pathway heatmap.

    The layout contains:
    - A dropdown for filtering by sample.
    - A placeholder message displayed when no data is available.

    Returns:
        dash.html.Div: A container with the heatmap and filter components.
    """
    return html.Div(
        [
            # Dropdown filter section
            html.Div(
                [
                    # Filter label
                    html.Div('Filter by Sample', className='menu-text'),
                    
                    # Dropdown for sample selection
                    dcc.Dropdown(
                        id='sample-dropdown-p12',  # Unique ID for callback identification
                        multi=False,  # Allows single selection only
                        placeholder='Select a Sample'  # Placeholder to guide the user
                    )
                ],
                className='navigation-menu'  # CSS class for styling the menu
            ),

            # Heatmap container
            html.Div(
                id='pathway-heatmap-container',  # Container for the heatmap
                children=[
                    # Placeholder message for when no data is available
                    html.P(
                        "No data available. Please select a sample",  # Message text
                        id="placeholder-pathway-heatmap",  # ID for dynamic updates
                        style={
                            "textAlign": "center",  # Center-align the text
                            "color": "gray"  # Gray color for the placeholder text
                        }
                    )
                ],
                className='graph-container',  # CSS class for the graph container
                style={
                    'height': 'auto',  # Automatically adjust height based on content
                    'overflowY': 'auto'  # Enable vertical scrolling if needed
                }
            )
        ],
        className='graph-card'  # CSS class for the overall card container
    )
