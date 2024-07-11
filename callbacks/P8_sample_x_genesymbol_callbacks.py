from dash import callback
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
import pandas as pd

from app import app
from utils.data_processing import merge_input_with_database, process_gene_sample_association
from utils.plot_processing import plot_sample_gene_scatter

@app.callback(
    [Output('p8-compound-association-dropdown', 'options'),
     Output('p8-compound-association-dropdown', 'value')],
    [Input('process-data', 'n_clicks')],
    [State('stored-data', 'data')]
)
def initialize_compound_association_dropdown(n_clicks, stored_data):
    if n_clicks < 1 or not stored_data:
        raise PreventUpdate

    input_df = pd.DataFrame(stored_data)
    merged_df = merge_input_with_database(input_df)
    gene_sample_association = process_gene_sample_association(merged_df)
    association_counts = sorted(gene_sample_association['num_compounds'].unique(), reverse=True)
    default_count = association_counts[0]

    dropdown_options = [{'label': f'Association with {count} compounds', 'value': count} for count in association_counts]

    return dropdown_options, default_count

@app.callback(
    Output('p8-sample-gene-scatter-plot', 'figure'),
    [Input('process-data', 'n_clicks'), Input('p8-compound-association-dropdown', 'value')],
    [State('stored-data', 'data')]
)
def update_sample_gene_scatter_plot(n_clicks, selected_count, stored_data):
    if n_clicks < 1 or not stored_data or not selected_count:
        raise PreventUpdate

    input_df = pd.DataFrame(stored_data)
    merged_df = merge_input_with_database(input_df)
    
    # Filtrar os dados pela quantidade de compostos associados selecionada
    filtered_df = merged_df.groupby('genesymbol').filter(lambda x: x['compoundname'].nunique() == selected_count)
    
    fig = plot_sample_gene_scatter(filtered_df)
    return fig
