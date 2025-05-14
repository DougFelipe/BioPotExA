"""
P17_gene_compound_network_layout.py
-----------------------------------
This script defines the layout for the Gene-Compound Interaction Network graph in a Dash web application. 

The layout includes:
- A graph component (`dcc.Graph`) for visualizing the network.
- A placeholder message displayed when no data is available.
"""

# ----------------------------------------
# Imports
# ----------------------------------------

from dash import dcc, html  # Dash components for graphs and HTML structure

# ----------------------------------------
# Function: get_gene_compound_network_layout
# ----------------------------------------
import dash_bootstrap_components as dbc
def get_gene_compound_network_layout():
    """
    Constructs the layout for the Gene-Compound Interaction Network graph.

    The layout includes:
    - A `dcc.Graph` component to render the network graph with configurable options.
    - A placeholder message that appears when no data is available to display.

    Returns:
    - html.Div: A container holding the graph and the placeholder message, styled using custom CSS classes.
    """
    return html.Div(
        [
            # Gene-Compound Network Graph
            html.Div(
                dcc.Graph(
                    id="gene-compound-network-graph",  # Unique ID for the graph
                    config={
                        "displayModeBar": True,  # Enable the mode bar for interactions
                        "scrollZoom": True  # Allow zooming with the scroll wheel
                    },
                    style={
                        "height": "600px",  # Set the height of the graph
                        "width": "100%"  # Make the graph take full width
                    }
                ),
                className="chart-container"  # CSS class for styling the graph container
            ),
            # Placeholder visual (displayed when no data is available)
            html.Div(
                className="placeholder-container",  # CSS class for styling the placeholder container
                children=[
                    html.Div(
                        className="placeholder-card",  # CSS class for styling the placeholder card
                        children=[
                            # Placeholder text
                            html.P(
                                "No data to display",  # Message displayed when there is no data
                                className="placeholder-text"  # CSS class for styling the placeholder text
                            )
                        ]
                    )
                ],
            )
        ],
        className="graph-card"  # Wrapper div with CSS class for consistent styling
    )
