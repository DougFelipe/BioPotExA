"""
P2_KO_20PATHWAY.py
-------------------
This script defines layouts for two bar chart components in a Dash web application:
1. A bar chart for analyzing KOs (KEGG Orthologs) in pathways based on selected samples.
2. A bar chart for analyzing KOs in samples for a selected pathway.

Each layout includes:
- A filter dropdown for user selection.
- A placeholder message if no data is available for the selected filter.
"""

# ----------------------------------------
# Imports
# ----------------------------------------

from dash import html, dcc  # Dash components for building UI layouts
import dash_bootstrap_components as dbc
# ----------------------------------------
# Function: get_pathway_ko_bar_chart_layout
# ----------------------------------------

def get_pathway_ko_bar_chart_layout():
    """
    Constructs a Bootstrap-styled layout for the KO pathway bar chart, with sample filtering.

    Returns:
        dbc.Card: A Dash Bootstrap Card containing the dropdown filter and the chart container.
    """
    return dbc.Card([
        dbc.CardHeader("Filter by Sample", class_name="fw-semibold text-muted"),

        dbc.CardBody([
            dbc.Row([
                dbc.Col(
                    dcc.Dropdown(
                        id='pathway-sample-dropdown',
                        placeholder="Select a sample",
                        className="mb-3"
                    ),
                    width=12
                )
            ]),
            dbc.Row([
                dbc.Col(
                    html.Div(
                        id='pathway-ko-chart-container',
                        children=[
                            html.P(
                                "No chart available. Please select a sample",
                                id="no-pathway-ko-chart-message",
                                className="text-center text-muted"
                            )
                        ]
                    ),
                    width=12
                )
            ])
        ])
    ],
    class_name="shadow-sm border-0 my-3")

# ----------------------------------------
# Function: get_sample_ko_pathway_bar_chart_layout
# ----------------------------------------

def get_sample_ko_pathway_bar_chart_layout():
    """
    Constructs a Bootstrap-styled layout for the KO bar chart per sample based on selected pathway.

    Returns:
        dbc.Card: A Dash Bootstrap Card containing dropdown filter and chart container.
    """
    return dbc.Card([
        dbc.CardHeader("Filter by Pathway", class_name="fw-semibold text-muted"),

        dbc.CardBody([
            dbc.Row([
                dbc.Col(
                    dcc.Dropdown(
                        id='via-dropdown',
                        placeholder="Select a pathway",
                        className="mb-3"
                    ),
                    width=12
                )
            ]),

            dbc.Row([
                dbc.Col(
                    html.Div(
                        id='via-ko-chart-container',
                        children=[
                            html.P(
                                "No chart available. Please select a pathway",
                                id="no-via-ko-chart-message",
                                className="text-center text-muted"
                            )
                        ]
                    ),
                    width=12
                )
            ])
        ])
    ],
    class_name="shadow-sm border-0 my-3")
