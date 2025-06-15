"""
P10_sample_grouping_profile_callbacks.py
----------------------------------------
This script defines callbacks for the "Sample Grouping by Compound Class Pattern" feature in a Dash web application. 

Key functionalities:
- Populates a dropdown with unique compound classes derived from the processed data.
- Updates and displays grouped sample data based on the selected compound class.
- Handles data grouping and visualization dynamically using utility functions.

Callbacks:
1. `initialize_compound_class_dropdown`: Initializes the compound class dropdown with options.
2. `update_sample_groups_plot`: Updates the sample grouping plot based on the selected compound class.
"""

# ----------------------------------------
# Imports
# ----------------------------------------

# Dash components and dependencies for interactivity
from dash import callback, html, dcc
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate

# Data manipulation
import pandas as pd

# Application instance
from app import app

# Utility functions for data processing and visualization
from utils.data_processing import merge_input_with_database, group_by_class, minimize_groups
from utils.plot_processing import plot_sample_groups

# ----------------------------------------
# Callback 1: Initialize Dropdown Options
# ----------------------------------------

@app.callback(
    [Output('compound-class-dropdown-p10', 'options'),  # Dropdown options
     Output('compound-class-dropdown-p10', 'value')],   # Selected value (initially None)
    [Input('process-data', 'n_clicks')],                # Triggered when data processing is requested
    [State('stored-data', 'data')]                      # Access stored data
)
def initialize_compound_class_dropdown(n_clicks, stored_data):
    """
    Initializes the compound class dropdown with unique values from the processed data.

    Parameters:
    - n_clicks (int): Number of times the "process-data" button has been clicked.
    - stored_data (list[dict]): Stored data passed from the application state.

    Returns:
    - list[dict]: Options for the dropdown menu, each with 'label' and 'value'.
    - None: Initial dropdown value (no pre-selection).

    Raises:
    - PreventUpdate: If the function is triggered before any data processing (n_clicks < 1).
    """
    if n_clicks < 1 or not stored_data:
        raise PreventUpdate

    input_df = pd.DataFrame(stored_data)  # Convert stored data to DataFrame
    merged_df = merge_input_with_database(input_df)  # Merge input with database
    compound_classes = sorted(merged_df['compoundclass'].unique())  # Get unique compound classes

    # Prepare dropdown options
    dropdown_options = [{'label': cls, 'value': cls} for cls in compound_classes]

    return dropdown_options, None  # No initial selection

# ----------------------------------------
# Callback 2: Update Sample Group Plot
# ----------------------------------------

@app.callback(
    Output('sample-groups-container', 'children'),  # Updates the sample group plot container
    [Input('compound-class-dropdown-p10', 'value')],  # Selected compound class
    [State('stored-data', 'data')]                   # Access stored data
)
def update_sample_groups_plot(compound_class, stored_data):
    """
    Updates the sample grouping plot based on the selected compound class.

    Parameters:
    - compound_class (str): Selected compound class from the dropdown.
    - stored_data (list[dict]): Stored data passed from the application state.

    Returns:
    - dash.html.P: A message if no data is available.
    - dash.dcc.Graph: A plot displaying sample groupings if data is available.
    """
    if not compound_class or not stored_data:
        return html.P(
            "No data available. Please select a compound class",  # Message for no data
            id="no-sample-groups-message",
            style={"textAlign": "center", "color": "gray"}
        )

    input_df = pd.DataFrame(stored_data)  # Convert stored data to DataFrame
    merged_df = merge_input_with_database(input_df)  # Merge input with database

    # Group data by the selected compound class
    grouped_df = group_by_class(compound_class, merged_df)

    # Minimize groups to handle excessive data
    minimized_groups = minimize_groups(grouped_df)

    # Filter grouped data to only include minimized groups
    minimized_df = grouped_df[grouped_df['grupo'].isin(minimized_groups)]

    # Handle empty results after processing
    if minimized_df.empty:
        return html.P(
            "No data available for the selected compound class",  # Message for no data after processing
            id="no-sample-groups-message",
            style={"textAlign": "center", "color": "gray"}
        )

    # Generate the plot using the processed data
    fig = plot_sample_groups(minimized_df)
    return dcc.Graph(figure=fig, style={"height": "auto", "overflowY": "auto"})  # Return the plot as a Dash Graph
