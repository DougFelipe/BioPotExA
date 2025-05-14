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
import dash_bootstrap_components as dbc
# ----------------------------------------
# Function: get_sample_reference_heatmap_layout
# ----------------------------------------

def get_sample_reference_heatmap_layout():
    """
    Constructs a Bootstrap-based layout for the heatmap between samples and reference agencies.

    Returns:
        dbc.Card: A styled layout containing the heatmap graph with responsive overflow handling.
    """
    return dbc.Card([
        dbc.CardBody([
            dbc.Row([
                dbc.Col(
                    dcc.Graph(id='sample-reference-heatmap'),
                    width=12
                )
            ])
        ], style={
            "height": "auto",
            "overflowY": "auto"
        })
    ], class_name="shadow-sm border-0 my-3")
