# my_dash_app/callbacks/P1_COUNT_KO_callbacks.py

# Importações necessárias
from dash import callback, dash_table, html
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
import pandas as pd

# Importações locais
from app import app
from utils.data_processing import merge_input_with_database, process_ko_data, process_ko_data_violin
from utils.plot_processing import plot_ko_count, create_violin_plot

# Callback para o gráfico de barras de contagem de KO
@app.callback(
    Output('ko-count-bar-chart', 'figure'),
    [Input('ko-count-range-slider', 'value')],
    [State('stored-data', 'data')]
)
def update_ko_count_chart(range_slider_values, stored_data):
    if not stored_data:
        raise PreventUpdate

    input_df = pd.DataFrame(stored_data)
    merged_df = merge_input_with_database(input_df)
    ko_count_df = process_ko_data(merged_df)

    min_value, max_value = range_slider_values
    filtered_ko_count_df = ko_count_df[(ko_count_df['ko_count'] >= min_value) & (ko_count_df['ko_count'] <= max_value)]

    fig = plot_ko_count(filtered_ko_count_df)
    return fig

# Callback para atualizar os valores do RangeSlider baseado nos dados carregados
@app.callback(
    [Output('ko-count-range-slider', 'max'),
     Output('ko-count-range-slider', 'value'),
     Output('ko-count-range-slider', 'marks')],
    [Input('process-data', 'n_clicks')],
    [State('stored-data', 'data')]
)
def update_range_slider_values(n_clicks, stored_data):
    if n_clicks < 1 or not stored_data:
        raise PreventUpdate

    input_df = pd.DataFrame(stored_data)
    merged_df = merge_input_with_database(input_df)
    ko_count_df = process_ko_data(merged_df)
    max_ko_count = ko_count_df['ko_count'].max()
    marks = {i: str(i) for i in range(0, max_ko_count + 1, max(1, max_ko_count // 10))}

    return max_ko_count, [0, max_ko_count], marks

# Callback para atualizar o gráfico de violino e boxplot com base na seleção do dropdown
@app.callback(
    Output('ko-violin-boxplot-chart', 'figure'),
    [Input('process-data', 'n_clicks'), Input('sample-dropdown', 'value')],
    [State('stored-data', 'data')]
)
def update_ko_violin_boxplot_chart(n_clicks, selected_samples, stored_data):
    if n_clicks < 1 or not stored_data:
        raise PreventUpdate

    input_df = pd.DataFrame(stored_data)
    merged_df = merge_input_with_database(input_df)

    if not selected_samples:
        selected_samples = input_df['sample'].unique()

    filtered_df = merged_df[merged_df['sample'].isin(selected_samples)]
    ko_count_per_sample = process_ko_data_violin(filtered_df)
    fig = create_violin_plot(ko_count_per_sample)
    return fig

# Callback para atualizar as opções do dropdown baseado nos dados carregados
@app.callback(
    Output('sample-dropdown', 'options'),
    [Input('process-data', 'n_clicks')],
    [State('stored-data', 'data')]
)
def update_dropdown_options(n_clicks, stored_data):
    if n_clicks < 1 or not stored_data:
        raise PreventUpdate

    input_df = pd.DataFrame(stored_data)
    sample_options = [{'label': sample, 'value': sample} for sample in input_df['sample'].unique()]
    return sample_options
