# my_dash_app/callbacks/P3_compounds_callbacks.py

from dash import callback, dash_table, html
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
import pandas as pd
from app import app
from utils.data_processing import merge_input_with_database
from utils.plot_processing import plot_compound_scatter

@app.callback(
    [Output('compound-class-dropdown', 'options'),
     Output('compound-class-dropdown', 'value')],
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

    return dropdown_options, [default_class]  # Retorna a primeira classe como lista

@app.callback(
    Output('compound-scatter-plot', 'figure'),
    [Input('compound-class-dropdown', 'value')],
    [State('stored-data', 'data')]
)
def update_compound_scatter_plot(selected_classes, stored_data):
    if not stored_data or not selected_classes:
        raise PreventUpdate

    # Garante que selected_classes seja uma lista
    if isinstance(selected_classes, str):
        selected_classes = [selected_classes]

    input_df = pd.DataFrame(stored_data)
    merged_df = merge_input_with_database(input_df)
    filtered_df = merged_df[merged_df['compoundclass'].isin(selected_classes)]
    fig = plot_compound_scatter(filtered_df)
    return fig
