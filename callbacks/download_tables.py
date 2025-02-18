# callbacks/download_tables.py

from dash import callback, Input, Output, State, dcc
from dash.exceptions import PreventUpdate
import pandas as pd
import dash_bootstrap_components as dbc

from utils.data_processing import merge_input_with_database

@callback(
    Output("download-merged-csv", "data"),
    Input("download-csv-btn", "n_clicks"),
    State("stored-data", "data"),  # Updated to match the existing store ID in your layout
    prevent_initial_call=True
)
def download_merged_csv(n_clicks, user_data):
    """
    Callback to merge the user's data with the database, then return a CSV download.
    """
    if not user_data:
        # If there's no data to merge, do nothing.
        raise PreventUpdate

    # Convert the stored data (list of dicts) to a DataFrame
    df_input = pd.DataFrame(user_data)

    # Merge with your database
    merged_df = merge_input_with_database(df_input)  # from your custom function

    # Return a CSV file for download
    return dcc.send_data_frame(
        merged_df.to_csv,
        filename="biorempp_merged_data.csv",
        index=False
    )
