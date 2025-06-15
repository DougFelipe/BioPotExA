"""
P12_compound_pathway_callbacks.py
---------------------------------
This script defines callbacks for handling dropdown initialization and updating the heatmap visualization
for pathway-compound interactions in a Dash web application.

Key Components:
- Dropdown menu for selecting a sample.
- Heatmap displaying pathway-compound interactions for the selected sample.

Callbacks:
1. `initialize_sample_dropdown`: Populates the dropdown with sample options from stored data.
2. `update_pathway_heatmap`: Updates the heatmap based on the selected sample and stored data.
"""

# ----------------------------------------
# Imports
# ----------------------------------------

from dash import callback, html, dcc  # Core Dash components
from dash.dependencies import Input, Output, State  # Input, Output, and State for callbacks
from dash.exceptions import PreventUpdate  # Exception to stop callback updates
import pandas as pd  # Data manipulation

from app import app  # Dash app instance
from utils.core.data_processing import merge_input_with_database_hadegDB
from utils.heatmaps.pathway_compound_interaction_processing import process_pathway_data  # Import pathway data processing function
from utils.heatmaps.pathway_compound_interaction_plot import plot_pathway_heatmap  # Import heatmap plotting function

# ----------------------------------------
# Callback 1: Initialize Dropdown
# ----------------------------------------

@app.callback(
    [Output('sample-dropdown-p12', 'options'),  # Dropdown options
     Output('sample-dropdown-p12', 'value')],   # Selected value in the dropdown
    [Input('process-data', 'n_clicks')],        # Triggered by the "process-data" button clicks
    [State('stored-data', 'data')]              # Stored data used for processing
)
def initialize_sample_dropdown(n_clicks, stored_data):
    """
    Initializes the sample dropdown menu with available sample options from the stored data.

    Parameters:
    - n_clicks (int): Number of times the "process-data" button has been clicked.
    - stored_data (dict): Data stored in the application, representing user-uploaded or preloaded input.

    Returns:
    - dropdown_options (list): A list of dictionaries representing dropdown options (label and value pairs).
    - None: No initial selection in the dropdown.

    Raises:
    - PreventUpdate: If stored data is not available or the button hasn't been clicked.
    """
    if not stored_data or n_clicks < 1:
        raise PreventUpdate

    input_df = pd.DataFrame(stored_data)  # Convert stored data into a DataFrame
    merged_df = merge_input_with_database_hadegDB(input_df)  # Merge data with HADEG database

    # Retrieve unique samples and prepare dropdown options
    samples = sorted(merged_df['sample'].unique())
    dropdown_options = [{'label': sample, 'value': sample} for sample in samples]

    return dropdown_options, None  # No initial selection

# ----------------------------------------
# Callback 2: Update Pathway Heatmap
# ----------------------------------------

@app.callback(
    Output('pathway-heatmap-container', 'children'),  # Container for the heatmap
    [Input('sample-dropdown-p12', 'value')],          # Triggered by changes in the selected dropdown value
    [State('stored-data', 'data')]                    # Stored data used for generating the heatmap
)
def update_pathway_heatmap(selected_sample, stored_data):
    """
    Updates the heatmap visualization for pathway-compound interactions based on the selected sample.

    Parameters:
    - selected_sample (str): The currently selected sample from the dropdown menu.
    - stored_data (dict): Data stored in the application, representing user-uploaded or preloaded input.

    Returns:
    - dcc.Graph: A Dash graph component containing the heatmap figure.
    - html.P: A placeholder message if no data is available or the sample has no associated data.
    """
    if not selected_sample or not stored_data:
        # Display a placeholder message if no data is available
        return html.P(
            "No data available. Please select a sample",  # User message
            id="placeholder-pathway-heatmap",             # HTML ID for styling or testing
            style={"textAlign": "center", "color": "gray"}  # Centered gray text for clarity
        )

    input_df = pd.DataFrame(stored_data)  # Convert stored data into a DataFrame
    merged_df = merge_input_with_database_hadegDB(input_df)  # Merge data with HADEG database

    # Process data for heatmap generation
    grouped_df = process_pathway_data(merged_df)
    if grouped_df.empty or selected_sample not in grouped_df['sample'].unique():
        # Display a message if the selected sample has no associated data
        return html.P(
            "No data available for the selected sample",  # User message
            id="no-data-pathway-heatmap",                 # HTML ID for styling or testing
            style={"textAlign": "center", "color": "gray"}  # Centered gray text for clarity
        )

    # Generate the heatmap figure
    fig = plot_pathway_heatmap(grouped_df, selected_sample)
    return dcc.Graph(figure=fig, style={'height': 'auto'})  # Return the heatmap as a Dash graph component
