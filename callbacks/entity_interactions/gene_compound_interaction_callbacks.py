"""
P7_compound_x_genesymbol_callbacks.py
--------------------------------------
This script defines callbacks for the "Gene vs Compound" scatter plot functionality in a Dash web application. 
It includes:
1. Initializing dropdown options for compounds and genes.
2. Updating the scatter plot based on user-selected filters.

The script integrates data processing utilities to prepare and filter data and plotting utilities 
to generate the visualization.
"""

# ----------------------------------------
# Imports
# ----------------------------------------

from dash import callback, html, dcc  # Dash components and callback utilities
from dash.dependencies import Input, Output, State  # Dependencies for callback interactions
from dash.exceptions import PreventUpdate  # Exception to prevent unnecessary updates
import pandas as pd  # Pandas for data manipulation

# App instance and utility imports
from app import app  # Main Dash app instance
from utils.data_processing import merge_input_with_database  # Utility for data merging
from utils.entity_interactions.gene_compound_interaction_plot import plot_gene_compound_scatter  # Function to create scatter plots

# ----------------------------------------
# Callback: Initialize Dropdown Options
# ----------------------------------------

@app.callback(
    [
        Output('p7-compound-dropdown', 'options'),  # Dropdown for compounds
        Output('p7-gene-dropdown', 'options')       # Dropdown for genes
    ],
    [Input('process-data', 'n_clicks')],           # Triggered when the "process data" button is clicked
    [State('stored-data', 'data')]                 # Data stored in memory
)
def initialize_dropdown_options(n_clicks, stored_data):
    """
    Initializes the dropdown options for compounds and genes based on the processed data.

    Parameters:
    - n_clicks (int): Number of clicks on the "process data" button.
    - stored_data (list[dict]): Data stored in the application state.

    Returns:
    - tuple[list[dict], list[dict]]: Dropdown options for compounds and genes.
    """
    if n_clicks < 1 or not stored_data:
        raise PreventUpdate  # Prevent updates if no clicks or no data available

    input_df = pd.DataFrame(stored_data)  # Convert stored data into a DataFrame
    merged_df = merge_input_with_database(input_df)  # Merge input data with the database

    # Generate options for compounds (sorted alphabetically)
    compound_options = [{'label': compound, 'value': compound} for compound in sorted(merged_df['compoundname'].unique())]

    # Generate options for genes (sorted alphabetically)
    gene_options = [{'label': gene, 'value': gene} for gene in sorted(merged_df['genesymbol'].unique())]

    return compound_options, gene_options

# ----------------------------------------
# Callback: Update Scatter Plot
# ----------------------------------------

@app.callback(
    Output('p7-gene-compound-scatter-container', 'children'),  # Container for the scatter plot
    [
        Input('p7-compound-dropdown', 'value'),  # Selected compounds
        Input('p7-gene-dropdown', 'value')      # Selected genes
    ],
    [State('stored-data', 'data')]              # Data stored in memory
)
def update_gene_compound_scatter(selected_compounds, selected_genes, stored_data):
    """
    Updates the scatter plot or displays a message based on the selected filters.

    Parameters:
    - selected_compounds (list[str]): List of compounds selected by the user.
    - selected_genes (list[str]): List of genes selected by the user.
    - stored_data (list[dict]): Data stored in the application state.

    Returns:
    - dash.html.P or dcc.Graph: A message (if no data or no results) or the scatter plot.
    """
    if not stored_data:
        raise PreventUpdate  # Prevent updates if no data available

    # Display a message if no filters are applied
    if not selected_compounds and not selected_genes:
        return html.P(
            "Select compound or gene to view results",  # Message when no filters are applied
            style={'textAlign': 'center', 'color': 'gray', 'fontSize': '16px'}
        )

    input_df = pd.DataFrame(stored_data)  # Convert stored data into a DataFrame
    merged_df = merge_input_with_database(input_df)  # Merge input data with the database

    # Apply filter by compounds if selected
    if selected_compounds:
        merged_df = merged_df[merged_df['compoundname'].isin(selected_compounds)]
    
    # Apply filter by genes if selected
    if selected_genes:
        merged_df = merged_df[merged_df['genesymbol'].isin(selected_genes)]
    
    # Display a message if no results match the filters
    if merged_df.empty:
        return html.P(
            "No results found for the selected filters",  # Message when no results are found
            style={'textAlign': 'center', 'color': 'gray', 'fontSize': '16px'}
        )
    
    # Generate the scatter plot with the filtered data
    fig = plot_gene_compound_scatter(merged_df)
    return dcc.Graph(figure=fig)  # Return the plot as a Dash Graph component
