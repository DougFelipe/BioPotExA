from dash import callback,html,dcc
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
import pandas as pd

from app import app
from utils.data_processing import merge_input_with_database_hadegDB, process_gene_sample_data
from utils.plot_processing import plot_sample_gene_heatmap

# Inicializar o dropdown de Compound Pathway
@app.callback(
    [Output('compound-pathway-dropdown-p11', 'options'),
     Output('compound-pathway-dropdown-p11', 'value')],
    [Input('process-data', 'n_clicks')],
    [State('stored-data', 'data')]
)
def initialize_compound_pathway_dropdown(n_clicks, stored_data):
    if n_clicks < 1 or not stored_data:
        raise PreventUpdate

    input_df = pd.DataFrame(stored_data)
    merged_df = merge_input_with_database_hadegDB(input_df)

    compound_pathways = sorted(merged_df['compound_pathway'].unique())
    dropdown_options = [{'label': pathway, 'value': pathway} for pathway in compound_pathways]

    return dropdown_options, None  # Nenhuma seleção inicial

# Inicializar o dropdown de Pathway com base na seleção de Compound Pathway
@app.callback(
    [Output('pathway-dropdown-p11', 'options'),
     Output('pathway-dropdown-p11', 'value')],
    [Input('compound-pathway-dropdown-p11', 'value')],
    [State('stored-data', 'data')]
)
def initialize_pathway_dropdown(selected_compound_pathway, stored_data):
    if not selected_compound_pathway or not stored_data:
        return [], None

    input_df = pd.DataFrame(stored_data)
    merged_df = merge_input_with_database_hadegDB(input_df)

    pathways = sorted(merged_df[merged_df['compound_pathway'] == selected_compound_pathway]['Pathway'].unique())
    dropdown_options = [{'label': pathway, 'value': pathway} for pathway in pathways]

    return dropdown_options, None  # Nenhuma seleção inicial

# Atualizar o heatmap de genes e samples com base na seleção de Pathway
@app.callback(
    Output('gene-sample-heatmap-container', 'children'),
    [Input('pathway-dropdown-p11', 'value')],
    [State('stored-data', 'data')]
)
def update_gene_sample_heatmap(selected_pathway, stored_data):
    if not selected_pathway or not stored_data:
        return html.P(
            "No data available. Please select a compound pathway and pathway",
            id="no-gene-sample-heatmap-message",
            style={"textAlign": "center", "color": "gray"}
        )

    input_df = pd.DataFrame(stored_data)
    merged_df = merge_input_with_database_hadegDB(input_df)

    grouped_df = process_gene_sample_data(merged_df)
    filtered_df = grouped_df[grouped_df['Pathway'] == selected_pathway].fillna(0)

    if filtered_df.empty:
        return html.P(
            "No data available for the selected pathway",
            id="no-gene-sample-heatmap-message",
            style={"textAlign": "center", "color": "gray"}
        )

    # Gera o gráfico e retorna como `dcc.Graph`
    fig = plot_sample_gene_heatmap(filtered_df)
    return dcc.Graph(figure=fig, style={"height": "600px", "overflowY": "auto"})
