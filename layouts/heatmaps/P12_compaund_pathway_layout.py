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
import dash_bootstrap_components as dbc
# ----------------------------------------
# Function: get_pathway_heatmap_layout
# ----------------------------------------
def get_pathway_heatmap_layout():
    """
    Constructs a Bootstrap-based layout for the Pathway-Compound heatmap with sample filtering.

    Returns:
        dbc.Card: A styled layout containing the dropdown filter and heatmap container.
    """

    return dbc.Card([
        dbc.CardHeader("Filter by Sample", class_name="fw-semibold text-muted"),

        dbc.CardBody([
            dbc.Row([
                dbc.Col(
                    dcc.Dropdown(
                        id='sample-dropdown-p12',
                        multi=False,
                        placeholder='Select a Sample',
                        className='mb-3'
                    ),
                    width=12
                )
            ]),

            dbc.Row([
                dbc.Col(
                    html.Div(
                        id='pathway-heatmap-container',
                        children=[
                            html.P(
                                "No data available. Please select a sample",
                                id="placeholder-pathway-heatmap",
                                className="text-center text-muted",
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
