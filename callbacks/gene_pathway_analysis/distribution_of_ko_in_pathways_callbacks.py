"""
P2_KO_20PATHWAY_callbacks.py
----------------------------
This script defines callbacks for a Dash web application to handle
interactions related to KO (KEGG Orthology) analysis and visualization
across pathways and samples.
The functionalities include:
- Initializing dropdown options for pathways and samples.
- Updating charts displaying KO counts for selected samples and pathways.
Functions:
1. `initialize_pathway_sample_dropdown`: Initializes the sample dropdown
   menu.
2. `update_pathway_ko_chart`: Updates the KO chart for a selected sample.
3. `initialize_via_dropdown`: Initializes the pathway dropdown menu.
4. `update_via_ko_chart`: Updates the KO chart for a selected pathway.

Dependencies:
- Dash for callbacks and HTML components.
- Pandas for data manipulation.
- Custom utilities for data processing and plotting.
"""

# ----------------------------------------
# Imports
# ----------------------------------------

# Dash modules for callbacks and components
from dash import html, dcc
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate  # Prevent updates when no valid input is provided

# Pandas for data manipulation
import pandas as pd

# Application and utilities
from app import app  # Dash application instance
from utils.core.data_processing import (
    merge_with_kegg  # Merges input data with KEGG databas
)
from utils.gene_pathway_analysis.distribution_of_ko_in_pathways_plot import (
    plot_pathway_ko_counts,  # Plots KO counts per pathway for a sample
    plot_sample_ko_counts  # Plots KO counts per sample for a specific pathway
)
from utils.gene_pathway_analysis.distribution_of_ko_in_pathways_processing import (
    count_ko_per_pathway,  # Counts unique KOs for each pathway
    count_ko_per_sample_for_pathway  # Counts unique KOs for a specific pathway in each sample
)
# ----------------------------------------
# Callback: Initialize the sample dropdown
# ----------------------------------------

@app.callback(
    [Output('pathway-sample-dropdown', 'options'),  # Dropdown options
     Output('pathway-sample-dropdown', 'value')],   # Default dropdown value
    [Input('process-data', 'n_clicks')],            # Triggered by the "Process Data" button
    [State('stored-data', 'data')]                  # Stored input data
)
def initialize_pathway_sample_dropdown(n_clicks, stored_data):
    """
    Initializes the sample dropdown menu based on the stored data.

    Parameters:
    - n_clicks (int): Number of clicks on the "Process Data" button.
    - stored_data (list[dict]): Stored data from user input.

    Returns:
    - list[dict]: Options for the dropdown, each with a 'label' and 'value'.
    - None: No default value selected.
    """
    if not stored_data or n_clicks < 1:  # Prevent update if data is missing or button not clicked
        raise PreventUpdate

    # Prepare data
    input_df = pd.DataFrame(stored_data)
    merged_df = merge_with_kegg(input_df)
    samples = sorted(merged_df['sample'].unique())  # Get unique sample names

    dropdown_options = [{'label': sample, 'value': sample} for sample in samples]

    return dropdown_options, None  # Return options and no default value

# ----------------------------------------
# Callback: Update KO chart per sample
# ----------------------------------------

@app.callback(
    Output('pathway-ko-chart-container', 'children'),  # Chart container
    [Input('pathway-sample-dropdown', 'value')],       # Selected sample
    [State('stored-data', 'data')]                    # Stored input data
)
def update_pathway_ko_chart(selected_sample, stored_data):
    """
    Updates the KO chart for the selected sample.

    Parameters:
    - selected_sample (str): The selected sample.
    - stored_data (list[dict]): Stored data from user input.

    Returns:
    - dash.dcc.Graph: Chart displaying KO counts for pathways in the selected sample.
    - dash.html.P: Placeholder message if no data is available or selected.
    """
    if not stored_data:
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

    # Prepare data
    input_df = pd.DataFrame(stored_data)
    merged_df = merge_with_kegg(input_df)

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
    [Input('process-data', 'n_clicks')], # Triggered by the "Process Data" button
    [State('stored-data', 'data')]       # Stored input data
)
def initialize_via_dropdown(n_clicks, stored_data):
    """
    Initializes the pathway dropdown menu based on the stored data.

    Parameters:
    - n_clicks (int): Number of clicks on the "Process Data" button.
    - stored_data (list[dict]): Stored data from user input.

    Returns:
    - list[dict]: Options for the dropdown, each with a 'label' and 'value'.
    - None: No default value selected.
    """
    if not stored_data or n_clicks < 1:  # Prevent update if data is missing or button not clicked
        raise PreventUpdate

    # Prepare data
    input_df = pd.DataFrame(stored_data)
    merged_df = merge_with_kegg(input_df)
    pathways = sorted(merged_df['pathname'].unique())  # Get unique pathways

    dropdown_options = [{'label': pathway, 'value': pathway} for pathway in pathways]

    return dropdown_options, None  # Return options and no default value

# ----------------------------------------
# Callback: Update KO chart per pathway
# ----------------------------------------

@app.callback(
    Output('via-ko-chart-container', 'children'),  # Chart container
    [Input('via-dropdown', 'value')],             # Selected pathway
    [State('stored-data', 'data')]                # Stored input data
)
def update_via_ko_chart(selected_via, stored_data):
    """
    Updates the KO chart for the selected pathway.

    Parameters:
    - selected_via (str): The selected pathway.
    - stored_data (list[dict]): Stored data from user input.

    Returns:
    - dash.dcc.Graph: Chart displaying KO counts for the selected pathway across samples.
    - dash.html.P: Placeholder message if no data is available or selected.
    """
    if not stored_data:
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

    # Prepare data
    input_df = pd.DataFrame(stored_data)
    merged_df = merge_with_kegg(input_df)

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
