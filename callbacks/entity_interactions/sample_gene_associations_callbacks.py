"""
P8_sample_x_genesymbol_callbacks.py
-----------------------------------
This script defines the callbacks for managing dropdown options and updating a scatter plot 
showing the relationship between samples and genes in a Dash web application. 

Features:
- Initializes dropdown options for selecting samples and genes.
- Dynamically updates a scatter plot based on selected filters.
- Displays appropriate messages when no data or filters are applied.
"""

# ----------------------------------------
# Imports
# ----------------------------------------

from dash import callback, html, dcc  # Dash components and callback framework
from dash.dependencies import Input, Output, State  # For handling callback inputs and states
from dash.exceptions import PreventUpdate  # Prevents unnecessary updates when conditions are not met
import pandas as pd  # For data manipulation

from app import app  # Dash application instance
from utils.core.data_processing import merge_input_with_database  # Utility for merging input data with a database
from utils.entity_interactions.sample_gene_associations_plot import plot_sample_gene_scatter  # Function to create scatter plots

# ----------------------------------------
# Callback: Initialize Dropdown Options
# ----------------------------------------

@app.callback(
    [Output('p8-sample-dropdown', 'options'),  # Dropdown for selecting samples
     Output('p8-gene-dropdown', 'options')],   # Dropdown for selecting genes
    [Input('process-data', 'n_clicks')],       # Triggered by the "Process Data" button
    [State('stored-data', 'data')]             # Uses stored data as the input state
)
def initialize_dropdown_options(n_clicks, stored_data):
    """
    Initializes the dropdown options for selecting samples and genes.

    Parameters:
    - n_clicks (int): Number of times the "Process Data" button has been clicked.
    - stored_data (dict): Stored data from previous processes.

    Returns:
    - list: Dropdown options for samples.
    - list: Dropdown options for genes.

    Raises:
    - PreventUpdate: If the button has not been clicked or no stored data is available.
    """
    if n_clicks < 1 or not stored_data:
        raise PreventUpdate

    input_df = pd.DataFrame(stored_data)  # Convert stored data into a DataFrame
    merged_df = merge_input_with_database(input_df)  # Merge with database

    # Generate sample options (alphabetically sorted)
    sample_options = [{'label': sample, 'value': sample} for sample in sorted(merged_df['sample'].unique())]

    # Generate gene options (alphabetically sorted)
    gene_options = [{'label': gene, 'value': gene} for gene in sorted(merged_df['genesymbol'].unique())]

    return sample_options, gene_options

# ----------------------------------------
# Callback: Update Scatter Plot or Display Initial Message
# ----------------------------------------

@app.callback(
    Output('p8-sample-gene-scatter-container', 'children'),  # Updates the scatter plot container
    [Input('p8-sample-dropdown', 'value'),                  # Selected samples
     Input('p8-gene-dropdown', 'value')],                   # Selected genes
    [State('stored-data', 'data')]                          # Uses stored data as the input state
)
def update_sample_gene_scatter(selected_samples, selected_genes, stored_data):
    """
    Updates the scatter plot based on the selected samples and genes, or displays an initial message.

    Parameters:
    - selected_samples (list or None): List of selected samples from the dropdown.
    - selected_genes (list or None): List of selected genes from the dropdown.
    - stored_data (dict): Stored data from previous processes.

    Returns:
    - dash.html.P: A message if no data or filters are applied.
    - dash.dcc.Graph: A scatter plot showing the filtered results.

    Raises:
    - PreventUpdate: If no stored data is available.
    """
    if not stored_data:
        raise PreventUpdate

    # Display an initial message if no filters are selected
    if not selected_samples and not selected_genes:
        return html.P(
            "Select sample or gene to view results",
            style={'textAlign': 'center', 'color': 'gray', 'fontSize': '16px'}
        )

    input_df = pd.DataFrame(stored_data)  # Convert stored data into a DataFrame
    merged_df = merge_input_with_database(input_df)  # Merge with database

    # Filter data by selected samples
    if selected_samples:
        merged_df = merged_df[merged_df['sample'].isin(selected_samples)]
    
    # Filter data by selected genes
    if selected_genes:
        merged_df = merged_df[merged_df['genesymbol'].isin(selected_genes)]
    
    # Display "no results" message if the filtered DataFrame is empty
    if merged_df.empty:
        return html.P(
            "No results found for the selected filters",
            style={'textAlign': 'center', 'color': 'gray', 'fontSize': '16px'}
        )
    
    # Generate a scatter plot with the filtered data
    fig = plot_sample_gene_scatter(merged_df)
    return dcc.Graph(figure=fig)
