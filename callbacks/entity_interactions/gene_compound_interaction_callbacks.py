"""
P7_compound_x_genesymbol_callbacks.py
--------------------------------------
This script defines callbacks for the "Gene vs Compound" scatter plot functionality in a Dash web application. 
It includes:
1. Initializing dropdown options for compounds and genes.
2. Updating the scatter plot based on user-selected filters.

The script integrates data processing utilities to prepare and filter data and plotting utilities 
to generate the visualization.
"""

# ----------------------------------------
# Imports
# ----------------------------------------

from dash import callback, html, dcc  # Dash components and callback utilities
from dash.dependencies import Input, Output, State  # Dependencies for callback interactions
from dash.exceptions import PreventUpdate  # Exception to prevent unnecessary updates
import pandas as pd  # Pandas for data manipulation

# App instance and utility imports
from app import app  # Main Dash app instance

# Funções utilitárias importadas dos pacotes organizados
from utils.entity_interactions import plot_gene_compound_scatter, extract_dropdown_options_from_data,filter_gene_compound_df   # Scatter entre genes e compostos


# ----------------------------------------
# Callback: Inicialização dos Dropdowns
# ----------------------------------------
@app.callback(
    [
        Output('p7-compound-dropdown', 'options'),
        Output('p7-gene-dropdown', 'options')
    ],
    [Input('biorempp-merged-data', 'data')]
)
def initialize_dropdown_options(biorempp_data):
    if not biorempp_data:
        return [], []
    compound_options = extract_dropdown_options_from_data(biorempp_data, 'compoundname')
    gene_options = extract_dropdown_options_from_data(biorempp_data, 'genesymbol')
    return compound_options, gene_options

# ----------------------------------------
# Callback: Atualização do Scatter Plot
# ----------------------------------------
@app.callback(
    Output('p7-gene-compound-scatter-container', 'children'),
    [
        Input('p7-compound-dropdown', 'value'),
        Input('p7-gene-dropdown', 'value')
    ],
    [State('biorempp-merged-data', 'data')]
)
def update_gene_compound_scatter(selected_compounds, selected_genes, biorempp_data):
    if not biorempp_data:
        raise PreventUpdate

    if not selected_compounds and not selected_genes:
        return html.P(
            "Select compound or gene to view results",
            style={'textAlign': 'center', 'color': 'gray', 'fontSize': '16px'}
        )

    filtered_df = filter_gene_compound_df(
        biorempp_data, selected_compounds, selected_genes
    )

    if filtered_df.empty:
        return html.P(
            "No results found for the selected filters",
            style={'textAlign': 'center', 'color': 'gray', 'fontSize': '16px'}
        )

    fig = plot_gene_compound_scatter(filtered_df)
    return dcc.Graph(figure=fig)
