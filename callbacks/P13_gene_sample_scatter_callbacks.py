from dash import callback, Output, Input, State,html,dcc
from dash.exceptions import PreventUpdate
import pandas as pd

from app import app
from utils.data_processing import merge_with_kegg, get_ko_per_sample_for_pathway
from utils.plot_processing import plot_sample_ko_scatter

@app.callback(
    [Output('pathway-dropdown-p13', 'options'),
     Output('pathway-dropdown-p13', 'value')],
    [Input('process-data', 'n_clicks')],
    [State('stored-data', 'data')]
)
def initialize_pathway_dropdown(n_clicks, stored_data):
    if n_clicks < 1 or not stored_data:
        raise PreventUpdate

    input_df = pd.DataFrame(stored_data)
    merged_df = merge_with_kegg(input_df)
    pathways = sorted(merged_df['pathname'].unique())
    
    # Se nenhum pathway estiver disponível, evitar erro
    dropdown_options = [{'label': pathway, 'value': pathway} for pathway in pathways]
    return dropdown_options, None  # Nenhum valor padrão

@app.callback(
    Output('scatter-plot-container', 'children'),
    [Input('pathway-dropdown-p13', 'value')],
    [State('stored-data', 'data')]
)
def update_scatter_plot(selected_pathway, stored_data):
    if not selected_pathway or not stored_data:
        return html.P(
            "No data available. Please select a pathway",
            id="no-data-message-p13",
            style={"textAlign": "center", "color": "gray"}
        )

    input_df = pd.DataFrame(stored_data)
    merged_df = merge_with_kegg(input_df)

    # Obter os dados do scatter plot
    scatter_data = get_ko_per_sample_for_pathway(merged_df, selected_pathway)

    if scatter_data.empty:
        return html.P(
            "No data found for the selected pathway",
            id="no-data-message-p13",
            style={"textAlign": "center", "color": "gray"}
        )

    # Gerar o gráfico
    fig = plot_sample_ko_scatter(scatter_data, selected_pathway)
    return dcc.Graph(figure=fig, style={'height': '600px'})
