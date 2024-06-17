# callbacks/P4_rank_compounds_callbacks.py

from dash import callback
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
import pandas as pd
from app import app
from utils.data_processing import merge_input_with_database, process_sample_ranking
from utils.plot_processing import plot_sample_ranking

@app.callback(
    Output('rank-compounds-scatter-plot', 'figure'),
    [Input('process-data', 'n_clicks')],
    [State('stored-data', 'data')]
)
def update_rank_compounds_plot(n_clicks, stored_data):
    if n_clicks < 1 or not stored_data:
        raise PreventUpdate

    input_df = pd.DataFrame(stored_data)
    merged_df = merge_input_with_database(input_df)
    ranked_samples = process_sample_ranking(merged_df)
    fig = plot_sample_ranking(ranked_samples)
    return fig
