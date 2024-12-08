from dash import callback,html,dcc
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
import pandas as pd

from app import app
from utils.data_processing import merge_input_with_database
from utils.plot_processing import plot_gene_compound_scatter

@app.callback(
    [Output('p7-compound-dropdown', 'options'),
     Output('p7-gene-dropdown', 'options')],
    [Input('process-data', 'n_clicks')],
    [State('stored-data', 'data')]
)
def initialize_dropdown_options(n_clicks, stored_data):
    if n_clicks < 1 or not stored_data:
        raise PreventUpdate

    input_df = pd.DataFrame(stored_data)
    merged_df = merge_input_with_database(input_df)

    # Opções para compostos (ordenadas alfabeticamente)
    compound_options = [{'label': compound, 'value': compound} for compound in sorted(merged_df['compoundname'].unique())]

    # Opções para genes (ordenadas alfabeticamente)
    gene_options = [{'label': gene, 'value': gene} for gene in sorted(merged_df['genesymbol'].unique())]

    return compound_options, gene_options

# Callback para atualizar o gráfico ou exibir a mensagem inicial
@app.callback(
    Output('p7-gene-compound-scatter-container', 'children'),
    [Input('p7-compound-dropdown', 'value'),
     Input('p7-gene-dropdown', 'value')],
    [State('stored-data', 'data')]
)
def update_gene_compound_scatter(selected_compounds, selected_genes, stored_data):
    if not stored_data:
        raise PreventUpdate

    # Verificar se nenhum filtro foi aplicado
    if not selected_compounds and not selected_genes:
        return html.P(
            "Select compound or gene to view results",
            style={'textAlign': 'center', 'color': 'gray', 'fontSize': '16px'}
        )

    input_df = pd.DataFrame(stored_data)
    merged_df = merge_input_with_database(input_df)

    # Aplicar filtro por compostos, se selecionado
    if selected_compounds:
        merged_df = merged_df[merged_df['compoundname'].isin(selected_compounds)]
    
    # Aplicar filtro por genes, se selecionado
    if selected_genes:
        merged_df = merged_df[merged_df['genesymbol'].isin(selected_genes)]
    
    # Se o DataFrame filtrado estiver vazio, exibir mensagem de "sem resultados"
    if merged_df.empty:
        return html.P(
            "No results found for the selected filters",
            style={'textAlign': 'center', 'color': 'gray', 'fontSize': '16px'}
        )
    
    # Gerar o gráfico com os dados filtrados
    fig = plot_gene_compound_scatter(merged_df)
    return dcc.Graph(figure=fig)
