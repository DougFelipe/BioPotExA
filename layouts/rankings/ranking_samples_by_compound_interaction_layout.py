"""
P4_rank_compounds_layout.py
---------------------------
This script defines the layout for the ranking chart of samples based on compound interaction in a Dash web application.

The layout includes:
- A filter for selecting a range of compound counts using a range slider.
- A scatter plot to display the ranking of compounds based on their interaction with samples.
"""

# ----------------------------------------
# Imports
# ----------------------------------------

from dash import html, dcc  # Dash components for creating UI
from components.ui.filters import create_range_slider  # Utility function to create a range slider
import dash_bootstrap_components as dbc

# ----------------------------------------
# Function: get_rank_compounds_layout
# ----------------------------------------
def get_rank_compounds_layout():
    """
    Returns a standardized Bootstrap layout for the ranking chart
    of compounds based on interaction with samples.
    """

    range_slider = create_range_slider(slider_id='compound-count-range-slider')

    return dbc.Card([
        dbc.CardHeader("Filter by Compound Count Range", class_name="fw-semibold text-muted"),

        dbc.CardBody([
            dbc.Row([
                dbc.Col(range_slider, width=12)
            ], class_name="mb-4"),

            dbc.Row([
                dbc.Col(
                    dcc.Graph(id='rank-compounds-scatter-plot'),
                    width=12
                )
            ])
        ])
    ],
    class_name="shadow-sm border-0 my-3")
