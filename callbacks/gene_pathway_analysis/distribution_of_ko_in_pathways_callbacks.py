"""
P2_KO_20PATHWAY_callbacks.py
----------------------------
This script defines callbacks for a Dash web application to handle
interactions related to KO (KEGG Orthology) analysis and visualization
across pathways and samples.

Functions:
1. initialize_pathway_sample_dropdown
2. update_pathway_ko_chart
3. initialize_via_dropdown
4. update_via_ko_chart
"""

# ----------------------------------------
# Imports
# ----------------------------------------

# Dash modules for callbacks and components
from dash import html, dcc
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate

# Pandas for data manipulation
import pandas as pd

# App instance
from app import app

# Core data utilities
from utils.core.data_processing import merge_with_kegg

# KO distribution – Plotting and Processing
from utils.gene_pathway_analysis.distribution_of_ko_in_pathways_plot import (
    plot_pathway_ko_counts,
    plot_sample_ko_counts
)
from utils.gene_pathway_analysis.distribution_of_ko_in_pathways_processing import (
    count_ko_per_pathway,
    count_ko_per_sample_for_pathway
)

# ----------------------------------------
# Callback: Initialize the sample dropdown
# ----------------------------------------

@app.callback(  
    [Output('pathway-sample-dropdown', 'options'),  # Dropdown options  
     Output('pathway-sample-dropdown', 'value')],   # Default dropdown value  
    [Input('kegg-merged-data', 'data')]             # MUDANÇA: usar store específico do KEGG  
)  
def initialize_pathway_sample_dropdown(kegg_data):  
    """  
    Initializes the sample dropdown menu based on pre-processed KEGG data.  
  
    Parameters:  
    - kegg_data (list[dict]): Pre-processed data from KEGG store.  
  
    Returns:  
    - list[dict]: Options for the dropdown, each with a 'label' and 'value'.  
    - None: No default value selected.  
    """  
    if not kegg_data:  # Prevent update if no processed data is available  
        return [], None  
  
    # Convert stored processed data into a DataFrame (dados já processados)  
    merged_df = pd.DataFrame(kegg_data)  
    samples = sorted(merged_df['sample'].unique())  # Get unique sample names  
  
    dropdown_options = [{'label': sample, 'value': sample} for sample in samples]  
  
    return dropdown_options, None  # Return options and no default value

# ----------------------------------------
# Callback: Update KO chart per sample
# ----------------------------------------

@app.callback(  
    Output('pathway-ko-chart-container', 'children'),  # Chart container  
    [Input('pathway-sample-dropdown', 'value')],       # Selected sample  
    [State('kegg-merged-data', 'data')]                # MUDANÇA: usar store específico do KEGG  
)  
def update_pathway_ko_chart(selected_sample, kegg_data):  
    """  
    Updates the KO chart for the selected sample using pre-processed KEGG data.  
  
    Parameters:  
    - selected_sample (str): The selected sample.  
    - kegg_data (list[dict]): Pre-processed data from KEGG store.  
  
    Returns:  
    - dash.dcc.Graph: Chart displaying KO counts for pathways in the selected sample.  
    - dash.html.P: Placeholder message if no data is available or selected.  
    """  
    if not kegg_data:  
        return html.P(  
            "No chart available. Please select a sample",   
            id="no-pathway-ko-chart-message",   
            style={"textAlign": "center", "color": "gray"}  
        )  
  
    if not selected_sample:  
        return html.P(  
            "No sample selected. Please choose a sample",   
            id="no-pathway-ko-chart-message",   
            style={"textAlign": "center", "color": "gray"}  
        )  
  
    # Convert stored processed data into a DataFrame (dados já processados)  
    merged_df = pd.DataFrame(kegg_data)  
  
    if merged_df.empty:  
        return html.P(  
            "The processed data is empty. Please check the input data",   
            id="empty-data-message",   
            style={"textAlign": "center", "color": "gray"}  
        )  
  
    pathway_count_df = count_ko_per_pathway(merged_df)  
  
    if pathway_count_df.empty or selected_sample not in pathway_count_df['sample'].unique():  
        return html.P(  
            f"No data available for sample '{selected_sample}'",   
            id="no-data-for-sample-message",   
            style={"textAlign": "center", "color": "gray"}  
        )  
  
    # Generate chart  
    fig = plot_pathway_ko_counts(pathway_count_df, selected_sample)  
  
    return dcc.Graph(figure=fig, style={"width": "100%", "margin-top": "20px"})

# ----------------------------------------
# Callback: Initialize the pathway dropdown
# ----------------------------------------

@app.callback(  
    [Output('via-dropdown', 'options'),  # Dropdown options  
     Output('via-dropdown', 'value')],   # Default dropdown value  
    [Input('kegg-merged-data', 'data')]  # MUDANÇA: usar store específico do KEGG  
)  
def initialize_via_dropdown(kegg_data):  
    """  
    Initializes the pathway dropdown menu based on pre-processed KEGG data.  
  
    Parameters:  
    - kegg_data (list[dict]): Pre-processed data from KEGG store.  
  
    Returns:  
    - list[dict]: Options for the dropdown, each with a 'label' and 'value'.  
    - None: No default value selected.  
    """  
    if not kegg_data:  # Prevent update if no processed data is available  
        return [], None  
  
    # Convert stored processed data into a DataFrame (dados já processados)  
    merged_df = pd.DataFrame(kegg_data)  
    pathways = sorted(merged_df['pathname'].unique())  # Get unique pathways  
  
    dropdown_options = [{'label': pathway, 'value': pathway} for pathway in pathways]  
  
    return dropdown_options, None  # Return options and no default value

@app.callback(  
    Output('via-ko-chart-container', 'children'),  # Chart container  
    [Input('via-dropdown', 'value')],             # Selected pathway  
    [State('kegg-merged-data', 'data')]           # MUDANÇA: usar store específico do KEGG  
)  
def update_via_ko_chart(selected_via, kegg_data):  
    """  
    Updates the KO chart for the selected pathway using pre-processed KEGG data.  
  
    Parameters:  
    - selected_via (str): The selected pathway.  
    - kegg_data (list[dict]): Pre-processed data from KEGG store.  
  
    Returns:  
    - dash.dcc.Graph: Chart displaying KO counts for the selected pathway across samples.  
    - dash.html.P: Placeholder message if no data is available or selected.  
    """  
    if not kegg_data:  
        return html.P(  
            "No chart available. Please select a pathway",   
            id="no-via-ko-chart-message",   
            style={"textAlign": "center", "color": "gray"}  
        )  
  
    if not selected_via:  
        return html.P(  
            "No pathway selected. Please choose a pathway",   
            id="no-via-ko-chart-message",   
            style={"textAlign": "center", "color": "gray"}  
        )  
  
    # Convert stored processed data into a DataFrame (dados já processados)  
    merged_df = pd.DataFrame(kegg_data)  
  
    if merged_df.empty:  
        return html.P(  
            "The processed data is empty. Please check the input data",   
            id="empty-data-message",   
            style={"textAlign": "center", "color": "gray"}  
        )  
  
    sample_count_df = count_ko_per_sample_for_pathway(merged_df, selected_via)  
  
    if sample_count_df.empty:  
        return html.P(  
            f"No data available for pathway '{selected_via}'",   
            id="no-data-for-pathway-message",   
            style={"textAlign": "center", "color": "gray"}  
        )  
  
    # Generate chart  
    fig = plot_sample_ko_counts(sample_count_df, selected_via)  
  
    return dcc.Graph(figure=fig, style={"width": "100%", "margin-top": "20px"})
