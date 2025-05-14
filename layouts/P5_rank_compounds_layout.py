"""
P5_rank_compounds_layout.py
---------------------------
This script defines the layout for the compound ranking graph in a Dash web application. 
The layout includes:
- A dropdown filter for selecting a compound class.
- A container for displaying the ranking graph or a placeholder message when no data is available.
"""

# ----------------------------------------
# Imports
# ----------------------------------------

from dash import html, dcc  # Dash components for HTML and interactive elements
import dash_bootstrap_components as dbc  # Bootstrap components for styling

# ----------------------------------------
# Function: get_rank_compounds_layout
# ----------------------------------------
from dash import dcc, html
import dash_bootstrap_components as dbc

def get_rank_compounds_layout():
    """
    Constructs a Bootstrap-styled layout for the compound ranking graph with dropdown filtering.

    Returns:
        dbc.Card: A styled layout with compound class filter and ranking graph area.
    """
    return dbc.Card([
        dbc.CardHeader("Filter by Compound Class", class_name="fw-semibold text-muted"),

        dbc.CardBody([
            dbc.Row([
                dbc.Col(
                    dcc.Dropdown(
                        id='p5-compound-class-dropdown',
                        multi=False,
                        placeholder='Select a Compound Class',
                        className="mb-4"
                    ),
                    width=12
                )
            ]),

            dbc.Row([
                dbc.Col(
                    html.Div(
                        id='p5-compound-ranking-container',
                        children=[
                            html.P(
                                "No data available. Please select a compound class.",
                                id="p5-placeholder-message",
                                style={"textAlign": "center", "color": "gray"}
                            )
                        ],
                        style={'height': 'auto', 'overflowY': 'auto'}
                    ),
                    width=12
                )
            ])
        ])
    ],
    class_name="shadow-sm border-0 my-3")
