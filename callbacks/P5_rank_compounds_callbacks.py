from dash import callback, html, dcc
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
import pandas as pd

from app import app
from utils.data_processing import merge_input_with_database, process_compound_ranking
from utils.plot_processing import plot_compound_ranking


@app.callback(
    [Output('p5-compound-class-dropdown', 'options'),
     Output('p5-compound-class-dropdown', 'value')],
    [Input('process-data', 'n_clicks')],
    [State('stored-data', 'data')]
)
def initialize_compound_class_dropdown(n_clicks, stored_data):
    if not stored_data or n_clicks < 1:
        raise PreventUpdate

    input_df = pd.DataFrame(stored_data)
    merged_df = merge_input_with_database(input_df)
    compound_classes = sorted(merged_df['compoundclass'].unique())

    dropdown_options = [{'label': cls, 'value': cls} for cls in compound_classes]
    return dropdown_options, None  # Nenhum valor inicial selecionado


@app.callback(
    Output('p5-compound-ranking-container', 'children'),
    [Input('p5-compound-class-dropdown', 'value')],
    [State('stored-data', 'data')]
)
def update_compound_ranking_plot(selected_class, stored_data):
    # Se nenhum dado ou classe de composto for selecionada, exibir a mensagem placeholder
    if not selected_class or not stored_data:
        return html.P(
            "No data available. Please select a compound class.",
            id="p5-placeholder-message",
            style={"textAlign": "center", "color": "gray"}
        )

    # Preparar os dados
    input_df = pd.DataFrame(stored_data)
    merged_df = merge_input_with_database(input_df)

    # Filtrar os dados pela classe selecionada
    filtered_df = merged_df[merged_df['compoundclass'] == selected_class]

    # Caso não haja dados para a classe selecionada
    if filtered_df.empty:
        return html.P(
            "No data available for the selected compound class.",
            id="p5-no-data-message",
            style={"textAlign": "center", "color": "gray"}
        )

    # Renderizar o gráfico
    compound_ranking_df = process_compound_ranking(filtered_df)
    fig = plot_compound_ranking(compound_ranking_df)

    return dcc.Graph(figure=fig, id="p5-rank-compounds-bar-plot")
