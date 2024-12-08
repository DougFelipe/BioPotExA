# callbacks/P4_rank_compounds_callbacks.py

from dash import callback
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
import pandas as pd

from app import app
from utils.data_processing import merge_input_with_database, process_sample_ranking
from utils.plot_processing import plot_sample_ranking

# Callback para atualizar o gráfico de ranking das amostras
@app.callback(
    Output('rank-compounds-scatter-plot', 'figure'),
    [Input('compound-count-range-slider', 'value')],
    [State('stored-data', 'data')]
)
def update_sample_ranking_plot(range_slider_values, stored_data):
    if not stored_data:
        raise PreventUpdate

    # Processa os dados
    input_df = pd.DataFrame(stored_data)
    merged_df = merge_input_with_database(input_df)
    sample_ranking_df = process_sample_ranking(merged_df)

    # Aplica o filtro baseado no Range Slider
    min_value, max_value = range_slider_values
    filtered_df = sample_ranking_df[
        (sample_ranking_df['num_compounds'] >= min_value) &
        (sample_ranking_df['num_compounds'] <= max_value)
    ]

    # Plota o gráfico com os dados filtrados
    fig = plot_sample_ranking(filtered_df)
    return fig


# Callback para atualizar os valores do Range Slider dinamicamente
@app.callback(
    [Output('compound-count-range-slider', 'max'),
     Output('compound-count-range-slider', 'value'),
     Output('compound-count-range-slider', 'marks')],
    [Input('process-data', 'n_clicks')],
    [State('stored-data', 'data')]
)
def update_range_slider_values(n_clicks, stored_data):
    if n_clicks < 1 or not stored_data:
        raise PreventUpdate

    # Processa os dados
    input_df = pd.DataFrame(stored_data)
    merged_df = merge_input_with_database(input_df)
    sample_ranking_df = process_sample_ranking(merged_df)

    # Define o valor máximo para o Range Slider
    max_value = sample_ranking_df['num_compounds'].max()

    # Define os valores iniciais e as marcas
    marks = {i: str(i) for i in range(0, max_value + 1, max(1, max_value // 10))}
    return max_value, [0, max_value], marks
