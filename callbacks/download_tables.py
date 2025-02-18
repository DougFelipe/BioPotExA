# callbacks/download_tables.py

from dash import callback, Input, Output, State, dcc
from dash.exceptions import PreventUpdate
import pandas as pd
import dash_bootstrap_components as dbc

from utils.data_processing import merge_input_with_database,merge_input_with_database_hadegDB, merge_with_toxcsm

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



@callback(
    Output("download-hadeg-csv", "data"),
    Input("download-hadeg-csv-btn", "n_clicks"),
    State("stored-data", "data"),  # Or whichever store holds your user data
    prevent_initial_call=True
)
def download_hadeg_csv(n_clicks, user_data):
    """
    Merge the user's input data with the HADEG DB, then provide a CSV download.
    """
    if not user_data:
        raise PreventUpdate

    # Convert stored data (list of dicts) to DataFrame
    df_input = pd.DataFrame(user_data)

    # Merge with the HADEG DB
    hadeg_merged_df = merge_input_with_database_hadegDB(df_input)

    return dcc.send_data_frame(
        hadeg_merged_df.to_csv,
        filename="hadeg_results.csv",
        index=False
    )

@callback(
    Output("download-toxcsm-csv", "data"),
    Input("download-toxcsm-csv-btn", "n_clicks"),
    State("stored-data", "data"),  # or whichever store holds your user data
    prevent_initial_call=True
)
def download_toxcsm_csv(n_clicks, user_data):
    """
    Merge the user's input data with the main BioRemPP DB (to get 'cpd', 'compoundclass', etc.),
    then merge that result with ToxCSM, returning a CSV download.
    """
    if not user_data:
        raise PreventUpdate

    # Convert stored data (list of dicts) to DataFrame
    df_input = pd.DataFrame(user_data)

    # 1) Merge user input with the main BioRemPP DB
    #    This step ensures columns like 'cpd', 'compoundclass', 'ko' exist.
    main_merged = merge_input_with_database(df_input)

    # 2) Now merge the main_merged DataFrame with ToxCSM
    final_merged = merge_with_toxcsm(main_merged)

    # Return a CSV file for download
    return dcc.send_data_frame(
        final_merged.to_csv,
        filename="toxcsm_results.csv",
        index=False
    )
