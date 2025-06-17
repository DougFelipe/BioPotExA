"""
P14_sample_enzyme_activity_callbacks.py
---------------------------------------
This script defines callbacks for the enzyme activity analysis section in a Dash web application. 

Features include:
- Initializing a dropdown with available samples.
- Generating a bar chart displaying unique enzyme activity counts based on the selected sample.

Callbacks:
1. `initialize_sample_dropdown`: Populates the dropdown menu with sample options.
2. `update_enzyme_activity_chart`: Updates the bar chart based on the selected sample.
"""

# ----------------------------------------
# Imports
# ----------------------------------------

from dash import callback, html, dcc  # Dash components for UI and callbacks
from dash.dependencies import Input, Output, State  # Input/Output/State for callback handling
from dash.exceptions import PreventUpdate  # Exception to stop unnecessary updates
import pandas as pd  # Data manipulation

from app import app  # Dash app instance

# Modular imports via public API exposed by utils
from utils.entity_interactions import (
    plot_enzyme_activity_counts,
    count_unique_enzyme_activities
)

# ----------------------------------------
# Callback: Initialize Dropdown with Samples
# ----------------------------------------

@app.callback(  
    [Output('sample-enzyme-dropdown', 'options'),  # Dropdown options  
     Output('sample-enzyme-dropdown', 'value')],  # Default selected value  
    [Input('biorempp-merged-data', 'data')]  # MUDANÇA: usar store específico  
)  
def initialize_sample_dropdown(biorempp_data):  
    """  
    Populates the dropdown menu with unique sample names using pre-processed data.  
  
    Parameters:  
    - biorempp_data (list of dict): Pre-processed data from BioRemPP store.  
  
    Returns:  
    - list[dict]: A list of dictionaries for dropdown options (label and value).  
    - None: No default value is set initially.  
    """  
    if not biorempp_data:  # Prevent updates if no processed data is available  
        return [], None  
  
    # Convert stored processed data into a DataFrame (dados já processados)  
    merged_df = pd.DataFrame(biorempp_data)  
  
    # Retrieve unique sample names and prepare dropdown options  
    samples = sorted(merged_df['sample'].unique())  
    dropdown_options = [{'label': sample, 'value': sample} for sample in samples]  
  
    return dropdown_options, None  # No default selection for the dropdown

# ----------------------------------------
# Callback: Update Bar Chart Based on Selected Sample
# ----------------------------------------

@app.callback(  
    Output('enzyme-bar-chart-container', 'children'),  # Container for the bar chart  
    [Input('sample-enzyme-dropdown', 'value')],  # Triggered when a sample is selected  
    [State('biorempp-merged-data', 'data')]  # MUDANÇA: usar store específico  
)  
def update_enzyme_activity_chart(selected_sample, biorempp_data):  
    """  
    Updates the bar chart to show unique enzyme activity counts using pre-processed data.  
  
    Parameters:  
    - selected_sample (str): The sample selected from the dropdown menu.  
    - biorempp_data (list of dict): Pre-processed data from BioRemPP store.  
  
    Returns:  
    - dash.html.P: A message if no data is available or found for the selected sample.  
    - dash.dcc.Graph: A bar chart showing unique enzyme activity counts for the selected sample.  
    """  
    if not selected_sample or not biorempp_data:  # Check if a sample is selected and data is available  
        return html.P(  
            "No data available. Please select a sample",  # Message displayed if no data is found  
            id="no-enzyme-bar-chart-message",  # Unique ID for styling and testing  
            style={"textAlign": "center", "color": "gray"}  # Styling for the message  
        )  
  
    # Convert stored processed data into a DataFrame (dados já processados)  
    merged_df = pd.DataFrame(biorempp_data)  
  
    # Count unique enzyme activities for the selected sample  
    enzyme_count_df = count_unique_enzyme_activities(merged_df, selected_sample)  
  
    if enzyme_count_df.empty:  # Check if the DataFrame is empty  
        return html.P(  
            "No data found for the selected sample",  # Message displayed if no enzyme data is found  
            id="no-enzyme-bar-chart-message",  # Unique ID for styling and testing  
            style={"textAlign": "center", "color": "gray"}  # Styling for the message  
        )  
  
    # Generate the bar chart using the processed data  
    fig = plot_enzyme_activity_counts(enzyme_count_df, selected_sample)  
  
    # Return the bar chart as a Dash Graph component  
    return dcc.Graph(figure=fig, className='bar-chart-style')  # CSS class for additional styling
