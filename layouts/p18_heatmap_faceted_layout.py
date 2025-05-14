"""
p18_heatmap_faceted_layout.py
-----------------------------
This script defines the layout for the Toxicity Heatmap with facets in a Dash web application.

The layout includes:
- A graph displaying the Toxicity Heatmap.
- Scrollable styling to handle large or detailed datasets.
"""

# ----------------------------------------
# Imports
# ----------------------------------------

from dash import html, dcc  # Dash components for creating the layout and graphs

# ----------------------------------------
# Function: get_toxicity_heatmap_layout
# ----------------------------------------
import dash_bootstrap_components as dbc
def get_toxicity_heatmap_layout():
    """
    Constructs the layout for the Toxicity Heatmap with facets.

    This layout contains:
    - A `dcc.Graph` component to render the heatmap.
    - Styling for scrollable content if the heatmap overflows the container.

    Returns:
        html.Div: A Dash HTML Div containing the graph for the Toxicity Heatmap.
    """
    return html.Div([
        # Heatmap Graph Container
        html.Div(
            dcc.Graph(
                id="toxicity-heatmap-faceted",  # Unique ID for the heatmap graph
                className="chart-container",  # CSS class for styling the chart container
                style={"overflow": "auto"}  # Adds scrolling to the graph container
            ),
            className="graph-card"  # CSS class for the card containing the graph
        )
    ])
