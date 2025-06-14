"""
T2_hadeg_callbacks.py
---------------------
This script defines a Dash callback for processing and displaying results from the HADEG database.
The callback:
- Renders a table with matched results.
- Hides the "View Results" button and initial placeholder message once results are displayed.
- Displays a message if no matches are found.

The script uses utility functions to process input data and generate the results table.
"""

# ----------------------------------------
# Imports
# ----------------------------------------

from dash import Input, Output, State, callback, html  # Dash components and callback utilities
import pandas as pd  # For data manipulation with DataFrame
from utils.table_utils import create_table_from_dataframe  # Function to create a Dash table
from utils.data_processing import merge_input_with_database_hadegDB  # Function to merge input data with the HADEG database

# ----------------------------------------
# Callback: render_hadeg_table
# ----------------------------------------

@callback(
    [
        Output("hadeg-results-table-container", "children"),  # Displays the results table
        Output("view-hadeg-results-button", "style"),  # Hides the "View Results" button after clicking
        Output("hadeg-placeholder-message", "style")  # Hides the initial placeholder message
    ],
    [Input("view-hadeg-results-button", "n_clicks")],  # Triggered when the button is clicked
    [State("stored-data", "data")],  # Retrieves the stored input data
    prevent_initial_call=True  # Prevents the callback from firing initially
)
def render_hadeg_table(n_clicks, stored_data):
    """
    Processes input data and displays the results from the HADEG database in a table format.

    Parameters:
    - n_clicks (int): Number of clicks on the "View Results" button.
    - stored_data (dict or None): Input data stored in the application state.

    Returns:
    - tuple:
        - html.Div: A container with the results table or a "No matches found" message.
        - dict: A style dictionary to hide the "View Results" button.
        - dict: A style dictionary to hide the placeholder message.

    Raises:
    - dash.exceptions.PreventUpdate: Prevents the callback from updating if no data is available or no clicks are made.
    """
    # Condition: Button is clicked and valid data is available
    if n_clicks > 0 and stored_data:
        # Convert stored data to a pandas DataFrame
        input_df = pd.DataFrame(stored_data)
        
        # Merge the input data with the HADEG database
        merged_df = merge_input_with_database_hadegDB(input_df)

        # If the resulting table is empty
        if merged_df.empty:
            return (
                html.Div(
                    "No matches found with the HADEG database",  # Message displayed when no matches are found
                    className="no-data-message"  # CSS class for styling
                ),
                {"display": "none"},  # Hides the "View Results" button
                {"display": "none"}  # Hides the initial placeholder message
            )

        # Create a table with the processed data
        table = create_table_from_dataframe(merged_df, "hadeg-results-table")

        return (
            html.Div(table, className="results-table"),  # Renders the table inside a container
            {"display": "none"},  # Hides the "View Results" button
            {"display": "none"}  # Hides the initial placeholder message
        )

    # If no data is available, prevent any update
    raise dash.exceptions.PreventUpdate
