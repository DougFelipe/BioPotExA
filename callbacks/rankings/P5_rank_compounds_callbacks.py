"""
P5_rank_compounds_callbacks.py
------------------------------
This script defines the callbacks for the "Rank Compounds by Sample Interaction" section in a Dash web application.

Features:
1. Initializes a dropdown with compound classes derived from user-uploaded data.
2. Updates a bar chart displaying the ranking of compounds based on their interaction with samples.

The script uses Dash callbacks to manage interactivity and relies on utility functions for data processing and plotting.
"""

# ----------------------------------------
# Imports
# ----------------------------------------

from dash import callback, html, dcc  # Dash components for layout and interactivity
from dash.dependencies import Input, Output, State  # Dash dependencies for callbacks
from dash.exceptions import PreventUpdate  # Prevents unnecessary callback execution
import pandas as pd  # Data manipulation

# Importing the main app instance and utility functions
from app import app
from utils.data_processing import merge_input_with_database, process_compound_ranking
from utils.plot_processing import plot_compound_ranking

# ----------------------------------------
# Callback: Initialize Dropdown for Compound Classes
# ----------------------------------------

@app.callback(
    [Output('p5-compound-class-dropdown', 'options'),
     Output('p5-compound-class-dropdown', 'value')],
    [Input('process-data', 'n_clicks')],  # Triggered by clicking the "Process Data" button
    [State('stored-data', 'data')]  # Accesses stored data
)
def initialize_compound_class_dropdown(n_clicks, stored_data):
    """
    Initializes the dropdown options with available compound classes.

    Parameters:
    - n_clicks (int): Number of clicks on the "Process Data" button.
    - stored_data (list of dict): Uploaded data stored in the Dash app.

    Returns:
    - list of dict: Dropdown options with available compound classes.
    - None: No initial value selected for the dropdown.
    """
    # Prevent callback execution if no data is available or button has not been clicked
    if not stored_data or n_clicks < 1:
        raise PreventUpdate

    # Convert stored data into a DataFrame
    input_df = pd.DataFrame(stored_data)

    # Merge the input data with the database
    merged_df = merge_input_with_database(input_df)

    # Extract unique compound classes and sort them alphabetically
    compound_classes = sorted(merged_df['compoundclass'].unique())

    # Format dropdown options
    dropdown_options = [{'label': cls, 'value': cls} for cls in compound_classes]

    # Return dropdown options with no pre-selected value
    return dropdown_options, None

# ----------------------------------------
# Callback: Update Compound Ranking Plot
# ----------------------------------------

@app.callback(
    Output('p5-compound-ranking-container', 'children'),
    [Input('p5-compound-class-dropdown', 'value')],  # Triggered when a dropdown value is selected
    [State('stored-data', 'data')]  # Accesses stored data
)
def update_compound_ranking_plot(selected_class, stored_data):
    """
    Updates the compound ranking bar chart based on the selected compound class.

    Parameters:
    - selected_class (str): The compound class selected from the dropdown.
    - stored_data (list of dict): Uploaded data stored in the Dash app.

    Returns:
    - dash.html.P or dash.dcc.Graph: A placeholder message or the updated bar chart.
    """
    # If no data or compound class is selected, display a placeholder message
    if not selected_class or not stored_data:
        return html.P(
            "No data available. Please select a compound class",  # Message for missing data
            id="p5-placeholder-message",  # ID for CSS styling or testing
            style={"textAlign": "center", "color": "gray"}  # Centered and gray text
        )

    # Convert stored data into a DataFrame
    input_df = pd.DataFrame(stored_data)

    # Merge the input data with the database
    merged_df = merge_input_with_database(input_df)

    # Filter data by the selected compound class
    filtered_df = merged_df[merged_df['compoundclass'] == selected_class]

    # If no data is available for the selected class, display a warning message
    if filtered_df.empty:
        return html.P(
            "No data available for the selected compound class",  # Warning message
            id="p5-no-data-message",  # ID for CSS styling or testing
            style={"textAlign": "center", "color": "gray"}  # Centered and gray text
        )

    # Process the filtered data to create the compound ranking
    compound_ranking_df = process_compound_ranking(filtered_df)

    # Generate a bar chart with the processed data
    fig = plot_compound_ranking(compound_ranking_df)

    # Return the bar chart as a Dash Graph component
    return dcc.Graph(figure=fig, id="p5-rank-compounds-bar-plot")
