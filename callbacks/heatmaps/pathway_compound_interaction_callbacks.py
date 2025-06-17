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

# Utilitários da aplicação (ajustados para a nova estrutura)
from utils import setup_logger
from utils.heatmaps import process_pathway_data, plot_pathway_heatmap


# ----------------------------------------
# Callback 1: Initialize Dropdown
# ----------------------------------------

@app.callback(  
    [Output('sample-dropdown-p12', 'options'),  # Dropdown options  
     Output('sample-dropdown-p12', 'value')],   # Selected value in the dropdown  
    [Input('hadeg-merged-data', 'data')]        # MUDANÇA: usar store específico do HADEG  
)  
def initialize_sample_dropdown(hadeg_data):  
    """  
    Initializes the sample dropdown menu with available sample options from pre-processed HADEG data.  
  
    Parameters:  
    - hadeg_data (list of dict): Pre-processed data from HADEG store.  
  
    Returns:  
    - dropdown_options (list): A list of dictionaries representing dropdown options (label and value pairs).  
    - None: No initial selection in the dropdown.  
    """  
    if not hadeg_data:  
        return [], None  
  
    # Convert stored processed data into a DataFrame (dados já processados)  
    merged_df = pd.DataFrame(hadeg_data)  
  
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
    [State('hadeg-merged-data', 'data')]              # MUDANÇA: usar store específico do HADEG  
)  
def update_pathway_heatmap(selected_sample, hadeg_data):  
    """  
    Updates the heatmap visualization for pathway-compound interactions based on the selected sample using pre-processed HADEG data.  
  
    Parameters:  
    - selected_sample (str): The currently selected sample from the dropdown menu.  
    - hadeg_data (list of dict): Pre-processed data from HADEG store.  
  
    Returns:  
    - dcc.Graph: A Dash graph component containing the heatmap figure.  
    - html.P: A placeholder message if no data is available or the sample has no associated data.  
    """  
    if not selected_sample or not hadeg_data:  
        # Display a placeholder message if no data is available  
        return html.P(  
            "No data available. Please select a sample",  # User message  
            id="placeholder-pathway-heatmap",             # HTML ID for styling or testing  
            style={"textAlign": "center", "color": "gray"}  # Centered gray text for clarity  
        )  
  
    # Convert stored processed data into a DataFrame (dados já processados)  
    merged_df = pd.DataFrame(hadeg_data)  
  
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
