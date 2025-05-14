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
import dash_bootstrap_components as dbc

# ----------------------------------------
# Function: get_toxicity_heatmap_layout
# ----------------------------------------
def get_toxicity_heatmap_layout():
    """
    Constructs a Bootstrap-styled layout for the Toxicity Heatmap with scrollable support.

    Returns:
        dbc.Card: A Bootstrap card layout with the toxicity heatmap graph.
    """
    return dbc.Card([
        dbc.CardHeader("Toxicity Prediction Faceted Heatmap", class_name="fw-semibold text-muted"),
        dbc.CardBody([
            dcc.Graph(
                id="toxicity-heatmap-faceted",
                className="chart-container",
                style={"overflowX": "auto"}
            )
        ])
    ],
    class_name="shadow-sm border-0 my-3")
