# my_dash_app/callbacks/P2_KO_20PATHWAY_callbacks.py

# Importações necessárias
from dash import callback, html, dcc
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
import pandas as pd

# Importações locais
from app import app
from utils.data_processing import merge_with_kegg, count_ko_per_pathway, count_ko_per_sample_for_pathway
from utils.plot_processing import plot_pathway_ko_counts, plot_sample_ko_counts


# Callback para inicializar o dropdown de amostras
@app.callback(
    [Output('pathway-sample-dropdown', 'options'),
     Output('pathway-sample-dropdown', 'value')],
    [Input('process-data', 'n_clicks')],
    [State('stored-data', 'data')]
)
def initialize_pathway_sample_dropdown(n_clicks, stored_data):
    if not stored_data or n_clicks < 1:
        raise PreventUpdate

    # Preparar dados
    input_df = pd.DataFrame(stored_data)
    merged_df = merge_with_kegg(input_df)
    samples = sorted(merged_df['sample'].unique())

    dropdown_options = [{'label': sample, 'value': sample} for sample in samples]

    return dropdown_options, None  # Nenhum valor padrão selecionado


# Callback para atualizar o gráfico de KOs por amostra
@app.callback(
    Output('pathway-ko-chart-container', 'children'),
    [Input('pathway-sample-dropdown', 'value')],
    [State('stored-data', 'data')]
)
def update_pathway_ko_chart(selected_sample, stored_data):
    if not stored_data:
        return html.P(
            "Nenhum gráfico disponível. Por favor, selecione uma amostra.",
            id="no-pathway-ko-chart-message",
            style={"textAlign": "center", "color": "gray"}
        )

    if not selected_sample:
        return html.P(
            "Nenhuma amostra selecionada. Por favor, escolha uma amostra.",
            id="no-pathway-ko-chart-message",
            style={"textAlign": "center", "color": "gray"}
        )

    # Preparar dados
    input_df = pd.DataFrame(stored_data)
    merged_df = merge_with_kegg(input_df)

    if merged_df.empty:
        return html.P(
            "Os dados processados estão vazios. Verifique os dados de entrada.",
            id="empty-data-message",
            style={"textAlign": "center", "color": "gray"}
        )

    pathway_count_df = count_ko_per_pathway(merged_df)

    if pathway_count_df.empty or selected_sample not in pathway_count_df['sample'].unique():
        return html.P(
            f"Nenhum dado disponível para a amostra '{selected_sample}'.",
            id="no-data-for-sample-message",
            style={"textAlign": "center", "color": "gray"}
        )

    # Gerar gráfico
    fig = plot_pathway_ko_counts(pathway_count_df, selected_sample)

    return dcc.Graph(figure=fig, style={"width": "100%", "margin-top": "20px"})


# Callback para inicializar o dropdown de vias
@app.callback(
    [Output('via-dropdown', 'options'),
     Output('via-dropdown', 'value')],
    [Input('process-data', 'n_clicks')],
    [State('stored-data', 'data')]
)
def initialize_via_dropdown(n_clicks, stored_data):
    if not stored_data or n_clicks < 1:
        raise PreventUpdate

    # Preparar dados
    input_df = pd.DataFrame(stored_data)
    merged_df = merge_with_kegg(input_df)
    pathways = sorted(merged_df['pathname'].unique())

    dropdown_options = [{'label': pathway, 'value': pathway} for pathway in pathways]

    return dropdown_options, None  # Nenhum valor padrão selecionado


# Callback para atualizar o gráfico de KOs por sample para uma via selecionada
@app.callback(
    Output('via-ko-chart-container', 'children'),
    [Input('via-dropdown', 'value')],
    [State('stored-data', 'data')]
)
def update_via_ko_chart(selected_via, stored_data):
    if not stored_data:
        return html.P(
            "Nenhum gráfico disponível. Por favor, selecione uma via.",
            id="no-via-ko-chart-message",
            style={"textAlign": "center", "color": "gray"}
        )

    if not selected_via:
        return html.P(
            "Nenhuma via selecionada. Por favor, escolha uma via.",
            id="no-via-ko-chart-message",
            style={"textAlign": "center", "color": "gray"}
        )

    # Preparar dados
    input_df = pd.DataFrame(stored_data)
    merged_df = merge_with_kegg(input_df)

    if merged_df.empty:
        return html.P(
            "Os dados processados estão vazios. Verifique os dados de entrada.",
            id="empty-data-message",
            style={"textAlign": "center", "color": "gray"}
        )

    sample_count_df = count_ko_per_sample_for_pathway(merged_df, selected_via)

    if sample_count_df.empty:
        return html.P(
            f"Nenhum dado disponível para a via '{selected_via}'.",
            id="no-data-for-pathway-message",
            style={"textAlign": "center", "color": "gray"}
        )

    # Gerar gráfico
    fig = plot_sample_ko_counts(sample_count_df, selected_via)

    return dcc.Graph(figure=fig, style={"width": "100%", "margin-top": "20px"})
