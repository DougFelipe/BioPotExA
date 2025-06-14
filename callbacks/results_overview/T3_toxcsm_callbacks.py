"""
T3_toxcsm_callbacks.py
----------------------
This script defines a Dash callback for rendering the TOXCSM results table. It integrates stored user data with 
the TOXCSM database to display matching results in a dynamically generated table.

Key Features:
- Validates user data stored in the application.
- Processes the data by merging it with the TOXCSM database.
- Dynamically generates a table to display the results.
- Handles cases where no matches are found, showing appropriate messages and styling.
"""

# ----------------------------------------
# Imports
# ----------------------------------------

from dash import Input, Output, State, callback, html  # Dash components for interactivity and UI updates
import pandas as pd  # For data manipulation
from utils.table_utils import create_table_from_dataframe  # Utility function for creating tables
from utils.data_processing import merge_input_with_database, merge_with_toxcsm  # Data processing utilities

# ----------------------------------------
# Callback: Render TOXCSM Results Table
# ----------------------------------------

@callback(
    [
        Output("toxcsm-results-table-container", "children"),  # Displays the table
        Output("view-toxcsm-results-button", "style"),  # Hides the button after it's clicked
        Output("toxcsm-placeholder-message", "style")  # Hides the initial placeholder message
    ],
    [Input("view-toxcsm-results-button", "n_clicks")],  # Trigger: Button click
    [State("stored-data", "data")],  # Reads stored data from the application
    prevent_initial_call=True  # Prevents callback execution on initial load
)
def render_toxcsm_table(n_clicks, stored_data):
    """
    Handles the rendering of the TOXCSM results table when the button is clicked.

    Steps:
    1. Validates the button click and the presence of stored data.
    2. Merges the input data with the TOXCSM database.
    3. Generates a table if matches are found; otherwise, shows a "No matches" message.
    4. Updates UI elements by hiding the button and placeholder message.

    Parameters:
    - n_clicks (int): Number of times the "View TOXCSM Results" button is clicked.
    - stored_data (dict): Data stored in the application, typically user-uploaded content.

    Returns:
    - children (html.Div or html.Div): A Div containing the results table or a "No matches" message.
    - button_style (dict): A style dictionary to hide the button.
    - placeholder_style (dict): A style dictionary to hide the placeholder message.
    """
    # Condition: Button clicked and valid data available
    if n_clicks > 0 and stored_data:
        input_df = pd.DataFrame(stored_data)  # Converts stored data to a DataFrame
        merged_df = merge_input_with_database(input_df)  # Merges input data with the database
        final_merged_df = merge_with_toxcsm(merged_df)  # Merges results with the TOXCSM database

        # If the resulting table is empty
        if final_merged_df.empty:
            return (
                html.Div(
                    "No matches found with the TOXCSM database",  # Message for no matches
                    className="no-data-message"  # CSS class for styling the message
                ),
                {"display": "none"},  # Hides the button
                {"display": "none"}  # Hides the initial placeholder message
            )

        # Creates a table with the processed data
        hidden_columns = ['ko', 'compoundclass']  # Defines columns to hide
        table = create_table_from_dataframe(
            final_merged_df, 
            "toxcsm-results-table", 
            hidden_columns=hidden_columns  # Passes the hidden columns
        )

        return (
            html.Div(table, className="results-table"),  # Renders the table
            {"display": "none"},  # Hides the button
            {"display": "none"}  # Hides the initial placeholder message
        )

    # If no data is available, prevent any updates
    raise dash.exceptions.PreventUpdate
