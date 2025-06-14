"""
P15_sample_clustering_layout.py
--------------------------------
This script defines the layout for the sample clustering dendrogram in a Dash web application.
The layout includes dropdowns for selecting distance metrics and clustering methods, as well as
a container for displaying the dendrogram.

Functions:
- `get_sample_clustering_layout`: Constructs and returns the layout containing dropdown menus and the dendrogram graph container.
"""

# ----------------------------------------
# Imports
# ----------------------------------------

from dash import html, dcc  # Dash components for building HTML and interactive elements
import dash_bootstrap_components as dbc
# ----------------------------------------
# Function: get_sample_clustering_layout
# ----------------------------------------
def get_sample_clustering_layout():
    """
    Constructs the Bootstrap-styled layout for the sample clustering dendrogram,
    including dropdowns for distance metrics and clustering methods.

    Returns:
        dbc.Card: A styled layout with dropdown controls and a dynamic graph container.
    """
    return dbc.Card([
        dbc.CardHeader("Configure Clustering Options", class_name="fw-semibold text-muted"),

        dbc.CardBody([

            # Filtros de configuração
            dbc.Row([

                # Dropdown: Distance Metric
                dbc.Col([
                    html.Label("Distance Metric", className="text-muted fw-semibold"),
                    dcc.Dropdown(
                        id='clustering-distance-dropdown',
                        options=[
                            {'label': 'Euclidean', 'value': 'euclidean'},
                            {'label': 'Manhattan', 'value': 'cityblock'},
                            {'label': 'Cosine', 'value': 'cosine'}
                        ],
                        placeholder="Select a distance metric",
                        className="mb-3"
                    )
                ], md=6),

                # Dropdown: Clustering Method
                dbc.Col([
                    html.Label("Clustering Method", className="text-muted fw-semibold"),
                    dcc.Dropdown(
                        id='clustering-method-dropdown',
                        options=[
                            {'label': 'Single Linkage', 'value': 'single'},
                            {'label': 'Complete Linkage', 'value': 'complete'},
                            {'label': 'Average Linkage', 'value': 'average'},
                            {'label': 'Ward', 'value': 'ward'}
                        ],
                        placeholder="Select a clustering method",
                        className="mb-3"
                    )
                ], md=6)
            ]),

            # Placeholder para o dendrograma
            dbc.Row([
                dbc.Col(
                    html.Div(id='sample-clustering-graph-container'),
                    width=12
                )
            ])
        ])
    ],
    class_name="shadow-sm border-0 my-3")
