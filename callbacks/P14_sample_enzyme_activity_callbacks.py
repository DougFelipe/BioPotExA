from dash import callback, html,dcc
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
import pandas as pd
from app import app
from utils.data_processing import merge_input_with_database, count_unique_enzyme_activities
from utils.plot_processing import plot_enzyme_activity_counts

# Callback para inicializar o dropdown com as amostras
@app.callback(
    [Output('sample-enzyme-dropdown', 'options'),
     Output('sample-enzyme-dropdown', 'value')],
    [Input('process-data', 'n_clicks')],
    [State('stored-data', 'data')]
)
def initialize_sample_dropdown(n_clicks, stored_data):
    if n_clicks < 1 or not stored_data:
        raise PreventUpdate

    input_df = pd.DataFrame(stored_data)
    merged_df = merge_input_with_database(input_df)

    # Obter amostras únicas
    samples = sorted(merged_df['sample'].unique())
    dropdown_options = [{'label': sample, 'value': sample} for sample in samples]

    return dropdown_options, None  # Nenhum valor padrão é definido inicialmente

# Callback para atualizar o gráfico de barras com base na amostra selecionada
@app.callback(
    Output('enzyme-bar-chart-container', 'children'),
    [Input('sample-enzyme-dropdown', 'value')],
    [State('stored-data', 'data')]
)
def update_enzyme_activity_chart(selected_sample, stored_data):
    if not selected_sample or not stored_data:
        return html.P(
            "No data available. Please select a sample.",
            id="no-enzyme-bar-chart-message",
            style={"textAlign": "center", "color": "gray"}
        )

    input_df = pd.DataFrame(stored_data)
    merged_df = merge_input_with_database(input_df)

    # Contar atividades enzimáticas únicas
    enzyme_count_df = count_unique_enzyme_activities(merged_df, selected_sample)

    if enzyme_count_df.empty:
        return html.P(
            "No data found for the selected sample.",
            id="no-enzyme-bar-chart-message",
            style={"textAlign": "center", "color": "gray"}
        )

    # Criar o gráfico
    fig = plot_enzyme_activity_counts(enzyme_count_df, selected_sample)

    return dcc.Graph(figure=fig, className='bar-chart-style')
