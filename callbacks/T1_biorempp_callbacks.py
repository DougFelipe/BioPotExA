"""
T1_biorempp_callbacks.py
------------------------
This script defines a callback for rendering the BioRemPP results table in a Dash web application.
The table is dynamically created based on user interaction and the stored data.

The callback:
- Processes user-provided data stored in the application.
- Merges the input data with a KEGG database.
- Displays a results table or an appropriate message if no data matches.
"""

# ----------------------------------------
# Imports
# ----------------------------------------

from dash import Input, Output, State, callback, html  # Dash components for callbacks and HTML rendering
import pandas as pd  # Pandas for data manipulation
from utils.table_utils import create_table_from_dataframe  # Utility function to create tables
from utils.data_processing import merge_input_with_database  # Utility function to process and merge data

# ----------------------------------------
# Callback: Render BioRemPP Results Table
# ----------------------------------------

@callback(
    [
        Output("biorempp-results-table-container", "children"),  # Renders the results table
        Output("view-biorempp-results-button", "style"),  # Hides the button after it is clicked
        Output("biorempp-placeholder-message", "style")  # Hides the initial placeholder message
    ],
    [Input("view-biorempp-results-button", "n_clicks")],  # Listens for clicks on the button
    [State("stored-data", "data")],  # Retrieves stored data
    prevent_initial_call=True  # Prevents the callback from triggering initially
)
def render_biorempp_table(n_clicks, stored_data):
    """
    Renders the BioRemPP results table upon user interaction.

    Parameters:
    - n_clicks (int): The number of times the "view results" button has been clicked.
    - stored_data (list[dict]): The user-provided data stored in the application.

    Returns:
    - html.Div: The results table if data is available and valid.
    - dict: CSS style to hide the button after it is clicked.
    - dict: CSS style to hide the initial placeholder message.
    """
    # Condition: Button is clicked, and valid data is available
    if n_clicks > 0 and stored_data:
        input_df = pd.DataFrame(stored_data)  # Convert stored data to a DataFrame
        merged_df = merge_input_with_database(input_df)  # Merge input data with the KEGG database

        # If the resulting table is empty
        if merged_df.empty:
            return (
                html.Div("No matches found with KEGG data", className="no-data-message"),  # Display a no-data message
                {"display": "none"},  # Hide the button
                {"display": "none"}  # Hide the initial placeholder message
            )

        # Create a table with the processed data
        table = create_table_from_dataframe(merged_df, "biorempp-results-table")

        return (
            html.Div(table, className="results-table"),  # Render the results table
            {"display": "none"},  # Hide the button
            {"display": "none"}  # Hide the initial placeholder message
        )

    # If no data is available, prevent any updates
    raise dash.exceptions.PreventUpdate
