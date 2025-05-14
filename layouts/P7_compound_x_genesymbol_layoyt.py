"""
P7_compound_x_genesymbol_layout.py
-----------------------------------
This script defines the layout for a scatter plot visualizing the relationship between genes and compounds. 
It includes dropdown filters for selecting specific compounds and genes and an initial message displayed 
until the filters are applied.

The layout is designed to dynamically update based on user selections.
"""

# ----------------------------------------
# Imports
# ----------------------------------------

from dash import html, dcc  # Dash HTML and core components for layout creation
import dash_bootstrap_components as dbc
# ----------------------------------------
# Function: get_gene_compound_scatter_layout
# ----------------------------------------
def get_gene_compound_scatter_layout():
    """
    Constructs a Bootstrap-based layout for the scatter plot showing gene-compound relationships.

    Includes:
    - Two dropdown filters: one for compound names and another for gene symbols.
    - A display container for the scatter plot or a message.

    Returns:
        dbc.Card: A styled layout with filtering controls and graph container.
    """

    return dbc.Card([

        dbc.CardHeader("Filter by Compound and Gene", class_name="fw-semibold text-muted"),

        dbc.CardBody([

            dbc.Row([
                dbc.Col([
                    html.Label("Compound Name", className="form-label text-muted"),
                    dcc.Dropdown(
                        id='p7-compound-dropdown',
                        multi=True,
                        placeholder='Select Compound(s)',
                        className='mb-3'
                    )
                ], md=6),

                dbc.Col([
                    html.Label("Gene Symbol", className="form-label text-muted"),
                    dcc.Dropdown(
                        id='p7-gene-dropdown',
                        multi=True,
                        placeholder='Select Gene(s)',
                        className='mb-3'
                    )
                ], md=6),
            ], class_name="mb-4"),

            dbc.Row([
                dbc.Col(
                    html.Div(
                        id='p7-gene-compound-scatter-container',
                        style={'height': 'auto', 'overflowY': 'auto'},
                        children=html.P(
                            "Select compound or gene to view results",
                            style={
                                'textAlign': 'center',
                                'color': 'gray',
                                'fontSize': '16px'
                            }
                        )
                    )
                )
            ])
        ])
    ],
    class_name="shadow-sm border-0 my-3")
