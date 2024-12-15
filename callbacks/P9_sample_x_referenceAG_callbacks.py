from dash import callback
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
import pandas as pd

from app import app
from utils.data_processing import merge_input_with_database, process_sample_reference_heatmap
from utils.plot_processing import plot_sample_reference_heatmap

@app.callback(
    Output('sample-reference-heatmap', 'figure'),
    [Input('process-data', 'n_clicks')],
    [State('stored-data', 'data')]
)
def update_sample_reference_heatmap(n_clicks, stored_data):
    if n_clicks < 1 or not stored_data:
        raise PreventUpdate

    input_df = pd.DataFrame(stored_data)
    merged_df = merge_input_with_database(input_df)
    heatmap_data = process_sample_reference_heatmap(merged_df)
    
    fig = plot_sample_reference_heatmap(heatmap_data)
    return fig
