"""
p18_heatmap_faceted_callbacks.py
--------------------------------
This script defines a callback for updating a faceted heatmap in a Dash web application. 

The callback:
- Listens for updates to the `stored-data` input.
- Processes the data by merging it with ToxCSM-related information.
- Generates a faceted heatmap using the processed data.

Functions:
- `update_heatmap_faceted`: Handles the creation of the faceted heatmap based on the stored data.
"""

# ----------------------------------------
# Imports
# ----------------------------------------

from dash import callback, Input, Output, State  # Dash callback and component interaction utilities
from dash.exceptions import PreventUpdate  # Exception to prevent unnecessary updates
import pandas as pd  # Data manipulation
from app import app  # Dash application instance
from utils.toxicity_prediction_heatmap_processing import process_heatmap_data
from utils.data_processing import get_merged_toxcsm_data  # Utility functions for data processing
from utils.toxicity_prediction_heatmap_plot import plot_heatmap_faceted  # Utility function for generating the heatmap plot

# ----------------------------------------
# Callback for Faceted Heatmap Update
# ----------------------------------------

@app.callback(
    Output('toxicity-heatmap-faceted', 'figure'),  # Output: Figure for the heatmap component
    Input('stored-data', 'data')  # Input: Triggered when the stored data is updated
)
def update_heatmap_faceted(data):
    """
    Updates the faceted heatmap based on the stored data.

    Steps:
    1. Checks if the input data exists; prevents unnecessary updates if not.
    2. Merges the input data with ToxCSM data to prepare for visualization.
    3. Processes the merged data to create a suitable format for the heatmap.
    4. Generates the faceted heatmap figure using the processed data.

    Parameters:
    - data (dict): The data stored in the `stored-data` component.

    Returns:
    - dict: A Plotly figure object representing the faceted heatmap. 
      Returns an empty dictionary if the data is invalid or empty.
    """
    # Step 1: Prevent update if no data is provided
    if not data:
        raise PreventUpdate

    # Step 2: Merge the input data with ToxCSM-related information
    merged_data = get_merged_toxcsm_data(data)
    if merged_data.empty:  # Check if the merged data is empty
        return {}

    # Step 3: Process the merged data to format it for the heatmap
    heatmap_data = process_heatmap_data(merged_data)
    if heatmap_data.empty:  # Check if the processed data is empty
        return {}

    # Step 4: Generate the faceted heatmap using the processed data
    fig = plot_heatmap_faceted(heatmap_data)
    return fig  # Return the generated figure
