from dash import callback
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
    default_class = compound_classes[0]

    dropdown_options = [{'label': cls, 'value': cls} for cls in compound_classes]

    return dropdown_options, default_class

@app.callback(
    Output('sample-groups-plot', 'figure'),
    [Input('compound-class-dropdown-p10', 'value')],
    [State('stored-data', 'data')]
)
def update_sample_groups_plot(compound_class, stored_data):
    if not compound_class or not stored_data:
        raise PreventUpdate

    input_df = pd.DataFrame(stored_data)
    merged_df = merge_input_with_database(input_df)
    grouped_df = group_by_class(compound_class, merged_df)
    minimized_groups = minimize_groups(grouped_df)

    minimized_df = grouped_df[grouped_df['grupo'].isin(minimized_groups)]

    fig = plot_sample_groups(minimized_df)
    return fig
