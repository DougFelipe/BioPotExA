# my_dash_app/callbacks/P15_sample_clustering_callbacks.py
from dash import callback, html
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
import pandas as pd
from app import app
from utils.data_processing import calculate_sample_clustering
from utils.plot_processing import plot_dendrogram

@app.callback(
    Output('sample-clustering-graph-container', 'children'),
    [Input('clustering-distance-dropdown', 'value'),
     Input('clustering-method-dropdown', 'value')],
    [State('stored-data', 'data')]
)
def update_sample_clustering_graph(distance_metric, method, stored_data):
    # Verificar se os dropdowns estão vazios
    if not distance_metric or not method or not stored_data:
        raise PreventUpdate

    input_df = pd.DataFrame(stored_data)
    clustering_matrix = calculate_sample_clustering(input_df, distance_metric, method)

    # Obter os nomes das amostras a partir do DataFrame
    sample_labels = input_df['sample'].unique().tolist()

    # Criar o dendrograma com o título dinâmico
    dendrogram_image = plot_dendrogram(clustering_matrix, sample_labels, distance_metric, method)

    return dendrogram_image
