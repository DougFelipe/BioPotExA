"""
P9_sample_x_referenceAG_layout.py
----------------------------------
This script defines a layout for a heatmap that visualizes the relationship between samples and referenceAG 
in a Dash web application.

The layout includes:
- A container for the heatmap graph (`dcc.Graph`).
- Styling to ensure the graph is scrollable if its content exceeds the available space.
"""

# ----------------------------------------
# Imports
# ----------------------------------------

from dash import html, dcc  # Dash components for HTML and interactive content

# ----------------------------------------
# Function: get_sample_reference_heatmap_layout
# ----------------------------------------

def get_sample_reference_heatmap_layout():
    """
    Constructs the layout for the heatmap displaying the relationship between samples and referenceAG.

    The layout:
    - Contains a `dcc.Graph` component for rendering the heatmap.
    - Includes styling to handle overflow and ensure responsiveness.

    Returns:
    - dash.html.Div: A container (`html.Div`) wrapping the heatmap graph.
    """
    return html.Div(
        [
            html.Div(
                dcc.Graph(id='sample-reference-heatmap'),  # Heatmap graph component with a unique ID
                className='graph-container',  # CSS class for styling the graph container
                style={  # Inline styles for responsiveness
                    'height': 'auto',  # Automatically adjusts height
                    'overflowY': 'auto'  # Enables vertical scrolling if content exceeds height
                }
            )
        ],
        className='graph-card'  # CSS class for styling the overall container
    )
