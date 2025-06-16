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
    [Input('biorempp-merged-data', 'data')]    # MUDANÇA: usar store específico  
)  
def initialize_dropdown_options(biorempp_data):  
    """  
    Initializes the dropdown options for selecting samples and genes using pre-processed data.  
  
    Parameters:  
    - biorempp_data (list of dict): Pre-processed data from BioRemPP store.  
  
    Returns:  
    - list: Dropdown options for samples.  
    - list: Dropdown options for genes.  
    """  
    if not biorempp_data:  
        return [], []  
  
    # Convert stored processed data into a DataFrame (dados já processados)  
    merged_df = pd.DataFrame(biorempp_data)  
  
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
    [State('biorempp-merged-data', 'data')]                 # MUDANÇA: usar store específico  
)  
def update_sample_gene_scatter(selected_samples, selected_genes, biorempp_data):  
    """  
    Updates the scatter plot based on the selected samples and genes using pre-processed data.  
  
    Parameters:  
    - selected_samples (list or None): List of selected samples from the dropdown.  
    - selected_genes (list or None): List of selected genes from the dropdown.  
    - biorempp_data (list of dict): Pre-processed data from BioRemPP store.  
  
    Returns:  
    - dash.html.P: A message if no data or filters are applied.  
    - dash.dcc.Graph: A scatter plot showing the filtered results.  
    """  
    if not biorempp_data:  
        raise PreventUpdate  
  
    # Display an initial message if no filters are selected  
    if not selected_samples and not selected_genes:  
        return html.P(  
            "Select sample or gene to view results",  
            style={'textAlign': 'center', 'color': 'gray', 'fontSize': '16px'}  
        )  
  
    # Convert stored processed data into a DataFrame (dados já processados)  
    merged_df = pd.DataFrame(biorempp_data)  
  
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
