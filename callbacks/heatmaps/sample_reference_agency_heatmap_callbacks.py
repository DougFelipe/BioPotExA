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
from utils.data_processing import merge_input_with_database
from utils.heatmaps.sample_reference_agency_heatmap_processing import process_sample_reference_heatmap  # Heatmap processing utility
from utils.heatmaps.sample_reference_agency_heatmap_plot import plot_sample_reference_heatmap  
# Callback: Update Sample x ReferenceAG Heatmap
# ----------------------------------------

@app.callback(
    Output('sample-reference-heatmap', 'figure'),  # Output: Heatmap figure
    [Input('process-data', 'n_clicks')],  # Input: Button clicks for triggering data processing
    [State('stored-data', 'data')]  # State: Data stored in memory from user input
)
def update_sample_reference_heatmap(n_clicks, stored_data):
    """
    Updates the "Sample x ReferenceAG Heatmap" based on the processed input data.

    Workflow:
    1. Verifies if the button has been clicked (`n_clicks >= 1`) and if data is available.
    2. Converts the stored data into a pandas DataFrame.
    3. Merges the input data with a database using the `merge_input_with_database` utility.
    4. Processes the merged data into a format suitable for a heatmap using `process_sample_reference_heatmap`.
    5. Generates and returns the heatmap figure using `plot_sample_reference_heatmap`.

    Parameters:
    - n_clicks (int): The number of times the "Process Data" button has been clicked.
    - stored_data (list of dict): The data stored in memory, typically uploaded by the user.

    Returns:
    - plotly.graph_objects.Figure: A Plotly figure object representing the heatmap.

    Raises:
    - PreventUpdate: If the button has not been clicked or no data is available.
    """
    # Prevent updates if the button hasn't been clicked or if no data is provided
    if n_clicks < 1 or not stored_data:
        raise PreventUpdate

    # Convert stored data to a pandas DataFrame
    input_df = pd.DataFrame(stored_data)
    
    # Merge the input data with the database
    merged_df = merge_input_with_database(input_df)
    
    # Process the merged data for heatmap generation
    heatmap_data = process_sample_reference_heatmap(merged_df)
    
    # Generate the heatmap figure
    fig = plot_sample_reference_heatmap(heatmap_data)
    
    return fig  # Return the generated heatmap figure
