"""
P9_sample_x_referenceAG_callbacks.py
-------------------------------------
This script defines the callback function for updating the "Sample x ReferenceAG Heatmap" in a Dash web application.
It processes user-uploaded data, integrates it with a database, and generates a heatmap visualization.

The main components include:
- A callback function triggered by a button click (`process-data`).
- Data processing and merging steps.
- Heatmap generation using processed data.
"""

# ----------------------------------------
# Imports
# ----------------------------------------

from dash import callback  # Dash decorator for defining callbacks
from dash.dependencies import Input, Output, State  # Dash components for interactivity
from dash.exceptions import PreventUpdate  # Exception to prevent unnecessary updates
import pandas as pd  # Pandas for data manipulation

from app import app  # Application instance
from utils.core.data_processing import merge_input_with_database
from utils.heatmaps.sample_reference_agency_heatmap_processing import process_sample_reference_heatmap  # Heatmap processing utility
from utils.heatmaps.sample_reference_agency_heatmap_plot import plot_sample_reference_heatmap  
# Callback: Update Sample x ReferenceAG Heatmap
# ----------------------------------------

@app.callback(  
    Output('sample-reference-heatmap', 'figure'),  # Output: Heatmap figure  
    [Input('biorempp-merged-data', 'data')]  # MUDANÇA: usar store específico  
)  
def update_sample_reference_heatmap(biorempp_data):  
    """  
    Updates the "Sample x ReferenceAG Heatmap" based on pre-processed data.  
  
    Workflow:  
    1. Verifies if processed data is available.  
    2. Converts the stored processed data into a pandas DataFrame.  
    3. Processes the merged data into a format suitable for a heatmap using `process_sample_reference_heatmap`.  
    4. Generates and returns the heatmap figure using `plot_sample_reference_heatmap`.  
  
    Parameters:  
    - biorempp_data (list of dict): Pre-processed data from BioRemPP store.  
  
    Returns:  
    - plotly.graph_objects.Figure: A Plotly figure object representing the heatmap.  
  
    Raises:  
    - PreventUpdate: If no processed data is available.  
    """  
    # Prevent updates if no processed data is provided  
    if not biorempp_data:  
        raise PreventUpdate  
  
    # Convert stored processed data into a DataFrame (dados já processados)  
    merged_df = pd.DataFrame(biorempp_data)  
      
    # Process the merged data for heatmap generation  
    heatmap_data = process_sample_reference_heatmap(merged_df)  
      
    # Generate the heatmap figure  
    fig = plot_sample_reference_heatmap(heatmap_data)  
      
    return fig  # Return the generated heatmap figure
