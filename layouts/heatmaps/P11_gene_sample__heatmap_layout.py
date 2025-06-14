"""
P11_gene_sample__heatmap_layout.py
-----------------------------------
This script defines the layout for a gene-sample heatmap in a Dash web application. 
The layout includes dynamic messages and conditional rendering to handle cases where no data is available.

The layout features:
- Filters for selecting a compound pathway and pathway.
- A container for displaying the heatmap or a message when no data is available.
"""

# ----------------------------------------
# Imports
# ----------------------------------------

from dash import html, dcc  # Dash components for building layouts and interactivity
import dash_bootstrap_components as dbc
# ----------------------------------------
# Function: get_gene_sample_heatmap_layout
# ----------------------------------------
def get_gene_sample_heatmap_layout():
    """
    Builds the layout for the gene-sample heatmap with Bootstrap styling,
    including filters and placeholder with proper muted formatting.

    Returns:
        dbc.Card: Layout with filters and a heatmap container.
    """
    return dbc.Card([

        dbc.CardHeader("Filter by Compound Pathway and Pathway", class_name="fw-semibold text-muted"),

        dbc.CardBody([

            dbc.Row([

                dbc.Col([
                    html.Label("Compound Pathway", className="text-muted mb-1"),
                    dcc.Dropdown(
                        id='compound-pathway-dropdown-p11',
                        multi=False,
                        placeholder='Select a Compound Pathway',
                        className="mb-3"
                    )
                ], md=6),

                dbc.Col([
                    html.Label("Pathway", className="text-muted mb-1"),
                    dcc.Dropdown(
                        id='pathway-dropdown-p11',
                        multi=False,
                        placeholder='Select a Pathway',
                        className="mb-3"
                    )
                ], md=6)

            ], class_name="gx-3"),

            dbc.Row([
                dbc.Col(
                    html.Div(
                        id='gene-sample-heatmap-container',
                        children=html.P(
                            "No data available. Please select a compound pathway and pathway.",
                            className="text-center text-muted fs-6"
                        ),
                        className='graph-container',
                        style={'height': 'auto', 'overflowY': 'auto'}
                    ),
                    width=12
                )
            ])

        ])

    ], class_name="shadow-sm border-0 my-3")
