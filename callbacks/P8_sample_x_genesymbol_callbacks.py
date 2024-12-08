from dash import callback, html, dcc
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
import pandas as pd

from app import app
from utils.data_processing import merge_input_with_database
from utils.plot_processing import plot_sample_gene_scatter

@app.callback(
    [Output('p8-sample-dropdown', 'options'),
     Output('p8-gene-dropdown', 'options')],
    [Input('process-data', 'n_clicks')],
    [State('stored-data', 'data')]
)
def initialize_dropdown_options(n_clicks, stored_data):
    if n_clicks < 1 or not stored_data:
        raise PreventUpdate

    input_df = pd.DataFrame(stored_data)
    merged_df = merge_input_with_database(input_df)

    # Opções para samples (ordenadas alfabeticamente)
    sample_options = [{'label': sample, 'value': sample} for sample in sorted(merged_df['sample'].unique())]

    # Opções para genes (ordenadas alfabeticamente)
    gene_options = [{'label': gene, 'value': gene} for gene in sorted(merged_df['genesymbol'].unique())]

    return sample_options, gene_options

# Callback para atualizar o gráfico ou exibir a mensagem inicial
@app.callback(
    Output('p8-sample-gene-scatter-container', 'children'),
    [Input('p8-sample-dropdown', 'value'),
     Input('p8-gene-dropdown', 'value')],
    [State('stored-data', 'data')]
)
def update_sample_gene_scatter(selected_samples, selected_genes, stored_data):
    if not stored_data:
        raise PreventUpdate

    # Exibir mensagem inicial se nenhum filtro for selecionado
    if not selected_samples and not selected_genes:
        return html.P(
            "Select sample or gene to view results",
            style={'textAlign': 'center', 'color': 'gray', 'fontSize': '16px'}
        )

    input_df = pd.DataFrame(stored_data)
    merged_df = merge_input_with_database(input_df)

    # Filtrar os dados por samples selecionados
    if selected_samples:
        merged_df = merged_df[merged_df['sample'].isin(selected_samples)]
    
    # Filtrar os dados por genes selecionados
    if selected_genes:
        merged_df = merged_df[merged_df['genesymbol'].isin(selected_genes)]
    
    # Exibir mensagem de "sem resultados" caso o DataFrame esteja vazio após os filtros
    if merged_df.empty:
        return html.P(
            "No results found for the selected filters",
            style={'textAlign': 'center', 'color': 'gray', 'fontSize': '16px'}
        )
    
    # Gerar o gráfico com os dados filtrados
    fig = plot_sample_gene_scatter(merged_df)
    return dcc.Graph(figure=fig)
