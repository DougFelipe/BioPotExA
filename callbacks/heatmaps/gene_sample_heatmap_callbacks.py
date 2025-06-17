"""
P11_gene_sample__heatmap_callbacks.py
-------------------------------------
This script contains Dash callbacks for handling dropdown initialization and updating a gene-sample heatmap visualization. 
It includes three main functionalities:
1. Initialize the dropdown for compound pathways.
2. Dynamically update the dropdown for pathways based on the selected compound pathway.
3. Generate and update a gene-sample heatmap based on the selected pathway.

Dependencies:
- Utilizes utilities for data processing and plot generation.
- Relies on Dash for user interactivity and callback handling.
"""

# ----------------------------------------
# Imports
# ----------------------------------------

from dash import callback, html, dcc
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
import pandas as pd

# Application-specific imports
from app import app
from utils import setup_logger
from utils.heatmaps import (
    plot_sample_gene_heatmap,
    process_gene_sample_data,
)


# ----------------------------------------
# Callback: Initialize Compound Pathway Dropdown
# ----------------------------------------

@app.callback(  
    [Output('compound-pathway-dropdown-p11', 'options'),  
     Output('compound-pathway-dropdown-p11', 'value')],  
    [Input('hadeg-merged-data', 'data')]  # MUDANÇA: usar store específico do HADEG  
)  
def initialize_compound_pathway_dropdown(hadeg_data):  
    """  
    Initializes the compound pathway dropdown options using pre-processed HADEG data.  
  
    Parameters:  
    - hadeg_data (list of dict): Pre-processed data from HADEG store.  
  
    Returns:  
    - list of dict: Options for the compound pathway dropdown, formatted as {'label': str, 'value': str}.  
    - None: No initial selection for the dropdown.  
    """  
    if not hadeg_data:  
        return [], None  # Return empty options if no processed data is available  
  
    # Convert stored processed data into a DataFrame (dados já processados)  
    merged_df = pd.DataFrame(hadeg_data)  
  
    # Extract unique compound pathways and sort them alphabetically  
    compound_pathways = sorted(merged_df['compound_pathway'].unique())  
    dropdown_options = [{'label': pathway, 'value': pathway} for pathway in compound_pathways]  
  
    return dropdown_options, None  # No initial selection

# ----------------------------------------
# Callback: Initialize Pathway Dropdown Based on Compound Pathway
# ----------------------------------------
@app.callback(  
    [Output('pathway-dropdown-p11', 'options'),  
     Output('pathway-dropdown-p11', 'value')],  
    [Input('compound-pathway-dropdown-p11', 'value')],  
    [State('hadeg-merged-data', 'data')]  # MUDANÇA: usar store específico do HADEG  
)  
def initialize_pathway_dropdown(selected_compound_pathway, hadeg_data):  
    """  
    Dynamically initializes the pathway dropdown options based on the selected compound pathway using pre-processed HADEG data.  
  
    Parameters:  
    - selected_compound_pathway (str): Selected compound pathway from the dropdown.  
    - hadeg_data (list of dict): Pre-processed data from HADEG store.  
  
    Returns:  
    - list of dict: Options for the pathway dropdown, formatted as {'label': str, 'value': str}.  
    - None: No initial selection for the dropdown.  
    """  
    if not selected_compound_pathway or not hadeg_data:  
        return [], None  # Empty options and no selection if conditions are not met  
  
    # Convert stored processed data into a DataFrame (dados já processados)  
    merged_df = pd.DataFrame(hadeg_data)  
  
    # Extract unique pathways within the selected compound pathway  
    pathways = sorted(merged_df[merged_df['compound_pathway'] == selected_compound_pathway]['Pathway'].unique())  
    dropdown_options = [{'label': pathway, 'value': pathway} for pathway in pathways]  
  
    return dropdown_options, None  # No initial selection

# ----------------------------------------
# Callback: Update Gene-Sample Heatmap Based on Selected Pathway
# ----------------------------------------

@app.callback(  
    Output('gene-sample-heatmap-container', 'children'),  
    [Input('pathway-dropdown-p11', 'value')],  
    [State('hadeg-merged-data', 'data')]  # MUDANÇA: usar store específico do HADEG  
)  
def update_gene_sample_heatmap(selected_pathway, hadeg_data):  
    """  
    Updates the gene-sample heatmap visualization based on the selected pathway using pre-processed HADEG data.  
  
    Parameters:  
    - selected_pathway (str): Selected pathway from the dropdown.  
    - hadeg_data (list of dict): Pre-processed data from HADEG store.  
  
    Returns:  
    - dash.html.P: A message indicating no data is available if conditions are not met.  
    - dash.dcc.Graph: A heatmap visualization of the gene-sample relationships.  
    """  
    if not selected_pathway or not hadeg_data:  
        # Return a message if no data or selection is available  
        return html.P(  
            "No data available. Please select a compound pathway and pathway.",  
            id="no-gene-sample-heatmap-message",  
            style={"textAlign": "center", "color": "gray"}  
        )  
  
    # Convert stored processed data into a DataFrame (dados já processados)  
    merged_df = pd.DataFrame(hadeg_data)  
  
    # Process data to group by genes and samples  
    grouped_df = process_gene_sample_data(merged_df)  
  
    # Filter the data for the selected pathway  
    filtered_df = grouped_df[grouped_df['Pathway'] == selected_pathway].fillna(0)  
  
    if filtered_df.empty:  
        # Return a message if no data exists for the selected pathway  
        return html.P(  
            "No data available for the selected pathway.",  
            id="no-gene-sample-heatmap-message",  
            style={"textAlign": "center", "color": "gray"}  
        )  
  
    # Generate the heatmap and return it as a `dcc.Graph`  
    fig = plot_sample_gene_heatmap(filtered_df)  
    return dcc.Graph(figure=fig, style={"height": "600px", "overflowY": "auto"})
