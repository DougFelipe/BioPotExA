# my_dash_app/callbacks/P2_KO_20PATHWAY_callbacks.py

# Importações necessárias
from dash import callback
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
import pandas as pd

# Importações locais
from app import app
from utils.data_processing import merge_with_kegg, count_ko_per_pathway, count_ko_per_sample_for_pathway
from utils.plot_processing import plot_pathway_ko_counts, plot_sample_ko_counts

# Callback para inicializar o dropdown e o gráfico de barras após o processamento dos dados
@app.callback(
    [Output('pathway-sample-dropdown', 'options'),
     Output('pathway-sample-dropdown', 'value')],
    [Input('process-data', 'n_clicks')],
    [State('stored-data', 'data')]
)
def initialize_dropdown_and_chart(n_clicks, stored_data):
    if n_clicks < 1 or not stored_data:
        raise PreventUpdate

    input_df = pd.DataFrame(stored_data)
    merged_df = merge_with_kegg(input_df)
    pathway_count_df = count_ko_per_pathway(merged_df)

    samples = sorted(pathway_count_df['sample'].unique())
    default_sample = samples[0]

    dropdown_options = [{'label': sample, 'value': sample} for sample in samples]

    return dropdown_options, default_sample

# Callback exclusivo para atualizar o gráfico de barras com base na seleção do dropdown
@app.callback(
    Output('pathway-ko-bar-chart', 'figure'),
    [Input('pathway-sample-dropdown', 'value')],
    [State('stored-data', 'data')]
)
def update_bar_chart(selected_sample, stored_data):
    if not stored_data or not selected_sample:
        raise PreventUpdate

    input_df = pd.DataFrame(stored_data)
    merged_df = merge_with_kegg(input_df)
    pathway_count_df = count_ko_per_pathway(merged_df)
    fig = plot_pathway_ko_counts(pathway_count_df, selected_sample)
    return fig

# Callback para inicializar o dropdown das vias após o processamento dos dados
@app.callback(
    [Output('via-dropdown', 'options'),
     Output('via-dropdown', 'value')],
    [Input('process-data', 'n_clicks')],
    [State('stored-data', 'data')]
)
def initialize_via_dropdown(n_clicks, stored_data):
    if n_clicks < 1 or not stored_data:
        raise PreventUpdate

    input_df = pd.DataFrame(stored_data)
    merged_df = merge_with_kegg(input_df)
    pathways = sorted(merged_df['pathname'].unique())
    default_pathway = pathways[0]
    dropdown_options = [{'label': pathway, 'value': pathway} for pathway in pathways]

    return dropdown_options, default_pathway

# Callback para atualizar o gráfico de barras com base na seleção do dropdown das vias
@app.callback(
    Output('via-ko-bar-chart', 'figure'),
    [Input('via-dropdown', 'value')],
    [State('stored-data', 'data')]
)
def update_bar_chart_for_via(selected_via, stored_data):
    if not stored_data or not selected_via:
        raise PreventUpdate

    # Preparar os dados para o gráfico de barras
    input_df = pd.DataFrame(stored_data)
    
    if input_df.empty:
        raise PreventUpdate

    merged_df = merge_with_kegg(input_df)
    
    if merged_df.empty or 'pathname' not in merged_df.columns:
        raise PreventUpdate

    sample_count_df = count_ko_per_sample_for_pathway(merged_df, selected_via)
    
    if sample_count_df.empty:
        raise PreventUpdate

    fig = plot_sample_ko_counts(sample_count_df, selected_via)

    return fig