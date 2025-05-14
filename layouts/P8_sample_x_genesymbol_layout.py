"""
P8_sample_x_genesymbol_layout.py
---------------------------------
This script defines the layout for a scatter plot that visualizes the relationship 
between samples and genes. It includes interactive filters for selecting specific 
samples and genes to refine the visualization.

The layout consists of:
- Dropdown menus for filtering by sample and gene.
- A container for displaying the scatter plot or a placeholder message when no selection is made.
"""

# ----------------------------------------
# Imports
# ----------------------------------------

from dash import html, dcc  # Dash HTML and DCC components for UI construction
import dash_bootstrap_components as dbc
# ----------------------------------------
# Function: get_sample_gene_scatter_layout
# ----------------------------------------
def get_sample_gene_scatter_layout():
    """
    Constructs a Bootstrap-based layout for the scatter plot visualizing 
    the relationship between samples and genes, with filters for both.

    Returns:
        dbc.Card: Layout container with filters and scatter plot section.
    """

    return dbc.Card([

        dbc.CardHeader("Filter by Sample and Gene", class_name="fw-semibold text-muted"),

        dbc.CardBody([

            # Dropdowns agrupados
            dbc.Row([

                dbc.Col([
                    html.Label("Sample", className="text-muted mb-1"),
                    dcc.Dropdown(
                        id='p8-sample-dropdown',
                        multi=True,
                        placeholder='Select samples',
                        className="mb-3"
                    )
                ], md=6),

                dbc.Col([
                    html.Label("Gene", className="text-muted mb-1"),
                    dcc.Dropdown(
                        id='p8-gene-dropdown',
                        multi=True,
                        placeholder='Select genes',
                        className="mb-3"
                    )
                ], md=6),

            ], class_name="gx-3"),

            dbc.Row([
                dbc.Col(
                    html.Div(
                        id='p8-sample-gene-scatter-container',
                        children=html.P(
                            "Select sample or gene to view results",
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
