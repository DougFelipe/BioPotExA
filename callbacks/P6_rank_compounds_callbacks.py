from dash import callback, html, dcc
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
import pandas as pd

from app import app
from utils.data_processing import merge_input_with_database, process_compound_gene_ranking
from utils.plot_processing import plot_compound_gene_ranking


@app.callback(
    [Output('p6-compound-class-dropdown', 'options'),
     Output('p6-compound-class-dropdown', 'value')],
    [Input('process-data', 'n_clicks')],
    [State('stored-data', 'data')]
)
def initialize_compound_class_dropdown(n_clicks, stored_data):
    # Caso os dados não estejam prontos ou o botão não tenha sido clicado
    if not stored_data or n_clicks < 1:
        return [], None

    input_df = pd.DataFrame(stored_data)
    merged_df = merge_input_with_database(input_df)
    compound_classes = sorted(merged_df['compoundclass'].unique())

    dropdown_options = [{'label': cls, 'value': cls} for cls in compound_classes]
    return dropdown_options, None  # Nenhum valor inicial selecionado


@app.callback(
    Output('p6-compound-ranking-container', 'children'),
    [Input('p6-compound-class-dropdown', 'value')],
    [State('stored-data', 'data')]
)
def update_compound_gene_ranking_plot(selected_class, stored_data):
    # Garantir que a mensagem de placeholder apareça quando nada for selecionado
    if not stored_data or not selected_class:
        return html.P(
            "No data available. Please select a compound class.",
            id="p6-placeholder-message",
            style={"textAlign": "center", "color": "gray", "marginTop": "20px"}
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
            id="p6-no-data-message",
            style={"textAlign": "center", "color": "gray", "marginTop": "20px"}
        )

    # Renderizar o gráfico
    compound_gene_ranking_df = process_compound_gene_ranking(filtered_df)
    fig = plot_compound_gene_ranking(compound_gene_ranking_df)

    return dcc.Graph(figure=fig, id="p6-rank-compounds-gene-bar-plot")
