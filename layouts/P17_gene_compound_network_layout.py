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
import dash_bootstrap_components as dbc

# ----------------------------------------
# Function: get_gene_compound_network_layout
# ----------------------------------------
def get_gene_compound_network_layout():
    """
    Constructs a Bootstrap-based layout for the Gene-Compound Interaction Network graph.

    Returns:
        dbc.Card: A layout wrapped in a Bootstrap card, including the graph and a placeholder message.
    """

    return dbc.Card([
        dbc.CardBody([

            dbc.Row([
                dbc.Col(
                    dcc.Graph(
                        id="gene-compound-network-graph",
                        config={
                            "displayModeBar": True,
                            "scrollZoom": True
                        },
                        style={"height": "600px", "width": "100%"}
                    ),
                    width=12
                )
            ]),

            html.Div(
                id="gene-compound-placeholder",  # Opcional: para controle dinâmico via callback
                className="placeholder-container mt-3",
                children=[
                    html.Div(
                        className="placeholder-card",
                        children=[
                            html.P("No data to display", className="placeholder-text")
                        ]
                    )
                ]
            )

        ])
    ],
    class_name="shadow-sm border-0 my-3")
