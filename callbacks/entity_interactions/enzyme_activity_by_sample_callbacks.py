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
from utils.data_processing import merge_input_with_database
from utils.entity_interactions.enzyme_activity_by_sample_plot import plot_enzyme_activity_counts  # Importing the plotting function
from utils.entity_interactions.enzyme_activity_by_sample_processing import count_unique_enzyme_activities  # Importing the processing function

# ----------------------------------------
# Callback: Initialize Dropdown with Samples
# ----------------------------------------

@app.callback(
    [Output('sample-enzyme-dropdown', 'options'),  # Dropdown options
     Output('sample-enzyme-dropdown', 'value')],  # Default selected value
    [Input('process-data', 'n_clicks')],  # Trigger when the "process data" button is clicked
    [State('stored-data', 'data')]  # Access stored data in the application state
)
def initialize_sample_dropdown(n_clicks, stored_data):
    """
    Populates the dropdown menu with unique sample names after data processing.

    Parameters:
    - n_clicks (int): Number of clicks on the "process data" button.
    - stored_data (dict): Data stored in the app's state, typically uploaded by the user.

    Returns:
    - list[dict]: A list of dictionaries for dropdown options (label and value).
    - None: No default value is set initially.

    Raises:
    - PreventUpdate: If no data is available or the button has not been clicked.
    """
    if n_clicks < 1 or not stored_data:  # Prevent updates if conditions are not met
        raise PreventUpdate

    # Convert stored data into a DataFrame and merge with the database
    input_df = pd.DataFrame(stored_data)
    merged_df = merge_input_with_database(input_df)

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
    [State('stored-data', 'data')]  # Access stored data in the application state
)
def update_enzyme_activity_chart(selected_sample, stored_data):
    """
    Updates the bar chart to show unique enzyme activity counts for the selected sample.

    Parameters:
    - selected_sample (str): The sample selected from the dropdown menu.
    - stored_data (dict): Data stored in the app's state, typically uploaded by the user.

    Returns:
    - dash.html.P: A message if no data is available or found for the selected sample.
    - dash.dcc.Graph: A bar chart showing unique enzyme activity counts for the selected sample.
    """
    if not selected_sample or not stored_data:  # Check if a sample is selected and data is available
        return html.P(
            "No data available. Please select a sample",  # Message displayed if no data is found
            id="no-enzyme-bar-chart-message",  # Unique ID for styling and testing
            style={"textAlign": "center", "color": "gray"}  # Styling for the message
        )

    # Convert stored data into a DataFrame and merge with the database
    input_df = pd.DataFrame(stored_data)
    merged_df = merge_input_with_database(input_df)

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
