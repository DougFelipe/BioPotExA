"""
P6_rank_compounds_layout.py
---------------------------
This script defines the layout for the compound ranking graph based on the number of unique genes acting on each compound.
It includes:
- A dropdown filter to select a compound class.
- A dynamic container to display the ranking graph or a placeholder message when no data is available.
"""

# ----------------------------------------
# Imports
# ----------------------------------------

from dash import dcc, html
import dash_bootstrap_components as dbc

# ----------------------------------------
# Function: get_rank_compounds_gene_layout
# ----------------------------------------


def get_rank_compounds_gene_layout():
    """
    Constructs a Bootstrap-based layout for the compound ranking graph by gene interactions.
    Includes a single-select dropdown to filter by compound class.
    
    Returns:
        dbc.Card: Layout with dropdown filter and conditional content for compound ranking.
    """

    dropdown_filter = dcc.Dropdown(
        id='p6-compound-class-dropdown',
        multi=False,
        placeholder='Select a Compound Class',
        className='mb-3'
    )

    placeholder_message = html.P(
        "No data available. Please select a compound class.",
        id="p6-placeholder-message",
        className="text-center text-muted mt-3"
    )

    return dbc.Card([
        dbc.CardHeader("Filter by Compound Class", class_name="fw-semibold text-muted"),
        
        dbc.CardBody([
            dbc.Row([
                dbc.Col(dropdown_filter, width=12)
            ]),

            html.Div(
                id='p6-compound-ranking-container',
                children=[placeholder_message],
                style={'height': 'auto', 'overflowY': 'auto'}
            )
        ])
    ],
    class_name="shadow-sm border-0 my-3")
