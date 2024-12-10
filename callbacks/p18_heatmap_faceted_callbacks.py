# callbacks/p18_heatmap_faceted_callbacks.py

from dash import callback, Input, Output, State
from dash.exceptions import PreventUpdate
import pandas as pd
from app import app
from utils.data_processing import process_heatmap_data, get_merged_toxcsm_data
from utils.plot_processing import plot_heatmap_faceted

@app.callback(
    Output('toxicity-heatmap-faceted', 'figure'),
    Input('stored-data', 'data')  # Trigger ao atualizar o stored-data
)
def update_heatmap_faceted(data):
    """
    Atualiza o heatmap com facetas com base nos dados armazenados.
    """
    if not data:
        raise PreventUpdate

    print("DEBUG: Callback acionado para o heatmap faceted...")  # Debug inicial

    # Processar os dados com o merge
    merged_data = get_merged_toxcsm_data(data)
    if merged_data.empty:
        print("WARNING: Dados após o merge estão vazios!")
        return {}

    # Processar os dados para o heatmap
    heatmap_data = process_heatmap_data(merged_data)
    if heatmap_data.empty:
        print("WARNING: Nenhum dado disponível para o gráfico de heatmap.")
        return {}

    # Gerar o gráfico
    fig = plot_heatmap_faceted(heatmap_data)
    return fig
