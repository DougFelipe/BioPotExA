from dash import callback, html
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
from app import app
from utils.data_processing import merge_input_with_database
from utils.plot_processing import render_upsetplot

import pandas as pd

@app.callback(
    [Output('upsetplot-sample-dropdown', 'options'),
     Output('upsetplot-sample-dropdown', 'value')],
    [Input('process-data', 'n_clicks')],
    [State('stored-data', 'data')]  # Alterado para 'stored-data'
)
def initialize_upsetplot_dropdown(n_clicks, merged_data):
    if not merged_data or n_clicks < 1:
        raise PreventUpdate


    # Preparar os dados e obter as amostras únicas
    unique_samples = pd.DataFrame(merged_data)['sample'].unique()
    options = [{'label': sample, 'value': sample} for sample in unique_samples]



    return options, None  # Nenhuma seleção inicial


@app.callback(
    Output('upset-plot-container', 'children'),
    [Input('upsetplot-sample-dropdown', 'value')],
    [State('stored-data', 'data')]
)
def update_upsetplot(selected_samples, stored_data):
    if not selected_samples or not stored_data:
        return html.P(
            "Nenhum gráfico disponível. Por favor, selecione as amostras.",
            id="no-upset-plot-message",
            style={"textAlign": "center", "color": "gray"}
        )



    # Converter stored-data para DataFrame
    input_df = pd.DataFrame(stored_data)

    # Mesclar os dados do input com o banco de dados
    merged_data = merge_input_with_database(input_df)


    # Renderizar o gráfico UpSet Plot com os dados mesclados
    image_src = render_upsetplot(merged_data.to_dict('records'), selected_samples)

    return html.Img(src=image_src, style={"width": "100%", "margin-top": "20px"})