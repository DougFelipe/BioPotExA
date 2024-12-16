from dash import callback,html,dcc
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
import pandas as pd

from app import app
from utils.data_processing import merge_input_with_database, group_by_class, minimize_groups
from utils.plot_processing import plot_sample_groups

@app.callback(
    [Output('compound-class-dropdown-p10', 'options'),
     Output('compound-class-dropdown-p10', 'value')],
    [Input('process-data', 'n_clicks')],
    [State('stored-data', 'data')]
)
def initialize_compound_class_dropdown(n_clicks, stored_data):
    if n_clicks < 1 or not stored_data:
        raise PreventUpdate

    input_df = pd.DataFrame(stored_data)
    merged_df = merge_input_with_database(input_df)
    compound_classes = sorted(merged_df['compoundclass'].unique())

    dropdown_options = [{'label': cls, 'value': cls} for cls in compound_classes]

    return dropdown_options, None  # Nenhuma seleção inicial

@app.callback(
    Output('sample-groups-container', 'children'),
    [Input('compound-class-dropdown-p10', 'value')],
    [State('stored-data', 'data')]
)
def update_sample_groups_plot(compound_class, stored_data):
    if not compound_class or not stored_data:
        return html.P(
            "No data available. Please select a compound class",
            id="no-sample-groups-message",
            style={"textAlign": "center", "color": "gray"}
        )

    input_df = pd.DataFrame(stored_data)
    merged_df = merge_input_with_database(input_df)

    # Agrupar os dados pela classe de compostos selecionada
    grouped_df = group_by_class(compound_class, merged_df)

    # Minimizar os grupos (tratamento para dados excessivos)
    minimized_groups = minimize_groups(grouped_df)

    minimized_df = grouped_df[grouped_df['grupo'].isin(minimized_groups)]

    # Gera o gráfico apenas se houver dados processados
    if minimized_df.empty:
        return html.P(
            "No data available for the selected compound class",
            id="no-sample-groups-message",
            style={"textAlign": "center", "color": "gray"}
        )

    fig = plot_sample_groups(minimized_df)
    return dcc.Graph(figure=fig, style={"height": "auto", "overflowY": "auto"})
