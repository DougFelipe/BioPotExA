"""
P8_sample_x_genesymbol_callbacks.py
-----------------------------------
This script defines the callbacks for managing dropdown options and updating a scatter plot 
showing the relationship between samples and genes in a Dash web application. 

Features:
- Initializes dropdown options for selecting samples and genes.
- Dynamically updates a scatter plot based on selected filters.
- Displays appropriate messages when no data or filters are applied.
"""

# ----------------------------------------
# Imports
# ----------------------------------------

from dash import callback, html, dcc
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate

from app import app

# Funções utilitárias de processamento (NOVA IMPORTAÇÃO)
from utils.entity_interactions.sample_gene_associations_processing import (
    extract_dropdown_options, filter_sample_gene_data
)
from utils.entity_interactions import plot_sample_gene_scatter

# ----------------------------------------
# Callback: Initialize Dropdown Options
# ----------------------------------------

@app.callback(
    [Output('p8-sample-dropdown', 'options'),
     Output('p8-gene-dropdown', 'options')],
    [Input('biorempp-merged-data', 'data')]
)
def initialize_dropdown_options(biorempp_data):
    """
    Inicializa opções dos dropdowns (usando função pura).
    """
    return extract_dropdown_options(biorempp_data)

# ----------------------------------------
# Callback: Update Scatter Plot or Display Initial Message
# ----------------------------------------

@app.callback(
    Output('p8-sample-gene-scatter-container', 'children'),
    [Input('p8-sample-dropdown', 'value'),
     Input('p8-gene-dropdown', 'value')],
    [State('biorempp-merged-data', 'data')]
)
def update_sample_gene_scatter(selected_samples, selected_genes, biorempp_data):
    """
    Atualiza o gráfico de dispersão, usando funções puras para processamento.
    """
    if not biorempp_data:
        raise PreventUpdate

    # Caso inicial: nenhum filtro
    if not selected_samples and not selected_genes:
        return html.P(
            "Select sample or gene to view results",
            style={'textAlign': 'center', 'color': 'gray', 'fontSize': '16px'}
        )

    # Processamento modularizado
    filtered_df = filter_sample_gene_data(biorempp_data, selected_samples, selected_genes)

    if filtered_df.empty:
        return html.P(
            "No results found for the selected filters",
            style={'textAlign': 'center', 'color': 'gray', 'fontSize': '16px'}
        )

    fig = plot_sample_gene_scatter(filtered_df)
    return dcc.Graph(figure=fig)
