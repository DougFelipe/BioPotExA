# my_dash_app/callbacks/P16_sample_upset_callbacks.py
from dash import callback, html
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
from app import app
from utils.data_processing import prepare_upsetplot_data
from utils.plot_processing import render_upsetplot

@app.callback(
    [Output('upsetplot-sample-dropdown', 'options'),
     Output('upsetplot-sample-dropdown', 'value')],
    [Input('process-data', 'n_clicks')],
    [State('stored-data', 'data')]
)
def initialize_upsetplot_dropdown(n_clicks, stored_data):
    if not stored_data or n_clicks < 1:
        raise PreventUpdate

    print("DEBUG: Inicializando dropdown com stored_data:")
    print(stored_data)

    # Preparar os dados e obter as amostras únicas
    unique_samples = prepare_upsetplot_data(stored_data)['sample'].unique()
    options = [{'label': sample, 'value': sample} for sample in unique_samples]

    print("DEBUG: Opções geradas para o dropdown:")
    print(options)

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

    print("DEBUG: Atualizando gráfico UpSet Plot com as amostras selecionadas:")
    print(selected_samples)

    # Renderizar o gráfico UpSet Plot
    image_src = render_upsetplot(stored_data, selected_samples)

    print("DEBUG: Gráfico gerado com sucesso.")
    return html.Img(src=image_src, style={"width": "100%", "margin-top": "20px"})
