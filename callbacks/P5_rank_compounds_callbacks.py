# my_Dash_app/callbacks/P5_rank_compounds_callbacks.py
from dash import callback
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
import pandas as pd

from app import app
from utils.data_processing import merge_input_with_database, process_compound_ranking
from utils.plot_processing import plot_compound_ranking

@app.callback(
    [Output('p5-compound-class-dropdown', 'options'),
     Output('p5-compound-class-dropdown', 'value')],
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
    Output('p5-rank-compounds-bar-plot', 'figure'),
    [Input('process-data', 'n_clicks'), Input('p5-compound-class-dropdown', 'value')],
    [State('stored-data', 'data')]
)
def update_compound_ranking_plot(n_clicks, selected_class, stored_data):
    if n_clicks < 1 or not stored_data or not selected_class:
        raise PreventUpdate

    input_df = pd.DataFrame(stored_data)
    merged_df = merge_input_with_database(input_df)
    
    # Filtrar os dados pela classe de composto selecionada
    filtered_df = merged_df[merged_df['compoundclass'] == selected_class]
    
    compound_ranking_df = process_compound_ranking(filtered_df)
    fig = plot_compound_ranking(compound_ranking_df)
    return fig
