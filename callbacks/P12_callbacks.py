from dash import callback
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
import pandas as pd

from app import app
from utils.data_processing import merge_input_with_database_hadegDB, process_pathway_data
from utils.plot_processing import plot_pathway_heatmap

@app.callback(
    [Output('sample-dropdown-p12', 'options'),
     Output('sample-dropdown-p12', 'value')],
    [Input('process-data', 'n_clicks')],
    [State('stored-data', 'data')]
)
def initialize_sample_dropdown(n_clicks, stored_data):
    if n_clicks < 1 or not stored_data:
        raise PreventUpdate

    input_df = pd.DataFrame(stored_data)
    merged_df = merge_input_with_database_hadegDB(input_df)
    samples = sorted(merged_df['sample'].unique())
    default_sample = samples[0]

    dropdown_options = [{'label': sample, 'value': sample} for sample in samples]

    return dropdown_options, default_sample



@callback(
    Output('pathway-heatmap', 'figure'),
    [Input('sample-dropdown', 'value')],
    [State('stored-data', 'data')]
)
def update_pathway_heatmap(selected_sample, stored_data):
    if not selected_sample or not stored_data:
        raise PreventUpdate

    input_df = pd.DataFrame(stored_data)
    merged_df = merge_input_with_database_hadegDB(input_df)

    fig = plot_pathway_heatmap(merged_df, selected_sample)

    return fig