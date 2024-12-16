from dash import callback, html,dcc
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
import pandas as pd

from app import app
from utils.data_processing import merge_input_with_database_hadegDB, process_pathway_data
from utils.plot_processing import plot_pathway_heatmap

@app.callback(
    [Output('sample-dropdown-p12', 'options'),
     Output('sample-dropdown-p12', 'value')],
    [Input('process-data', 'n_clicks')],
    [State('stored-data', 'data')]
)
def initialize_sample_dropdown(n_clicks, stored_data):
    if not stored_data or n_clicks < 1:
        raise PreventUpdate

    input_df = pd.DataFrame(stored_data)
    merged_df = merge_input_with_database_hadegDB(input_df)

    # Obter as opções do dropdown
    samples = sorted(merged_df['sample'].unique())
    dropdown_options = [{'label': sample, 'value': sample} for sample in samples]

    return dropdown_options, None  # Nenhuma seleção inicial

@app.callback(
    Output('pathway-heatmap-container', 'children'),
    [Input('sample-dropdown-p12', 'value')],
    [State('stored-data', 'data')]
)
def update_pathway_heatmap(selected_sample, stored_data):
    if not selected_sample or not stored_data:
        return html.P(
            "No data available. Please select a sample",
            id="placeholder-pathway-heatmap",
            style={"textAlign": "center", "color": "gray"}
        )

    input_df = pd.DataFrame(stored_data)
    merged_df = merge_input_with_database_hadegDB(input_df)
    
    # Processar os dados e verificar se há dados disponíveis
    grouped_df = process_pathway_data(merged_df)
    if grouped_df.empty or selected_sample not in grouped_df['sample'].unique():
        return html.P(
            "No data available for the selected sample",
            id="no-data-pathway-heatmap",
            style={"textAlign": "center", "color": "gray"}
        )

    # Gerar o gráfico de heatmap com os dados processados
    fig = plot_pathway_heatmap(grouped_df, selected_sample)
    return dcc.Graph(figure=fig, style={'height': 'auto'})
