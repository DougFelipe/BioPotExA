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
from utils.toxicity.toxicity_prediction_heatmap_processing import process_heatmap_data
from utils.toxicity.toxicity_prediction_heatmap_plot import plot_heatmap_faceted  # Utility function for generating the heatmap plot

# ----------------------------------------
# Callback for Faceted Heatmap Update
# ----------------------------------------

@app.callback(  
    Output('toxicity-heatmap-faceted', 'figure'),  # Output: Figure for the heatmap component  
    Input('toxcsm-merged-data', 'data')  # MUDANÇA: usar store específico do ToxCSM  
)  
def update_heatmap_faceted(toxcsm_data):  
    """  
    Updates the faceted heatmap based on pre-processed ToxCSM data.  
  
    Steps:  
    1. Checks if the ToxCSM processed data exists; prevents unnecessary updates if not.  
    2. Processes the merged data to create a suitable format for the heatmap.  
    3. Generates the faceted heatmap figure using the processed data.  
  
    Parameters:  
    - toxcsm_data (list of dict): Pre-processed data from ToxCSM store.  
  
    Returns:  
    - dict: A Plotly figure object representing the faceted heatmap.   
      Returns an empty dictionary if the data is invalid or empty.  
    """  
    # Step 1: Prevent update if no processed data is provided  
    if not toxcsm_data:  
        raise PreventUpdate  
  
    # Step 2: Convert stored processed data into a DataFrame (dados já processados)  
    merged_data = pd.DataFrame(toxcsm_data)  
    if merged_data.empty:  # Check if the merged data is empty  
        return {}  
  
    # Step 3: Process the merged data to format it for the heatmap  
    heatmap_data = process_heatmap_data(merged_data)  
    if heatmap_data.empty:  # Check if the processed data is empty  
        return {}  
  
    # Step 4: Generate the faceted heatmap using the processed data  
    fig = plot_heatmap_faceted(heatmap_data)  
    return fig  # Return the generated figure
