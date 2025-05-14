"""
P13_gene_sample_scatter_layout.py
---------------------------------
This script defines the layout for a scatter plot visualization in a Dash web application. 
The scatter plot shows the relationship between KOs (KEGG Orthologs) and samples for a selected pathway. 

The layout includes:
- A dropdown menu for filtering data by pathway.
- A container to display the scatter plot or a default message when no data is available.
"""

# ----------------------------------------
# Imports
# ----------------------------------------

from dash import html, dcc  # Dash components for building the UI
import dash_bootstrap_components as dbc
# ----------------------------------------
# Function: get_sample_ko_scatter_layout
# ----------------------------------------

def get_sample_ko_scatter_layout():
    """
    Constructs a Bootstrap-based layout for the scatter plot of KOs in samples by pathway.

    Returns:
        dbc.Card: A styled layout containing the pathway filter and the scatter plot container.
    """
    return dbc.Card([

        dbc.CardHeader("Filter by Pathway", class_name="fw-semibold text-muted"),

        dbc.CardBody([

            dbc.Row([
                dbc.Col(
                    dcc.Dropdown(
                        id='pathway-dropdown-p13',
                        multi=False,
                        placeholder='Select a Pathway',
                        className='mb-3'
                    ),
                    width=12
                )
            ]),

            dbc.Row([
                dbc.Col(
                    html.Div(
                        id='scatter-plot-container',
                        children=[
                            html.P(
                                "No data available. Please select a pathway.",
                                id="no-data-message-p13",
                                className="text-center text-muted"
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
