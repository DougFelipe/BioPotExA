"""
callbacks/download_tables.py

This module defines Dash callbacks for exporting processed data as downloadable CSV files.
User input is stored temporarily in the Dash layout and is then merged with different 
databases (BioRemPP, HADEG, ToxCSM) to generate downloadable output.

Callbacks:
    - download_merged_csv: Merges data with the main BioRemPP database and exports to CSV.
    - download_hadeg_csv: Merges data with the HADEG database and exports to CSV.
    - download_toxcsm_csv: Merges data with the main database and then with ToxCSM, and exports to CSV.

Requirements:
    - dash
    - dash-bootstrap-components
    - pandas
    - utils.data_processing (custom merging functions)

Author:
    Your Name (your.email@example.com)

Version:
    1.0.0

Date:
    2025-04-22

License:
    MIT
"""

from dash import callback, Input, Output, State, dcc
from dash.exceptions import PreventUpdate
import pandas as pd
import dash_bootstrap_components as dbc

from utils.core.data_processing import merge_input_with_database, merge_input_with_database_hadegDB, merge_with_toxcsm


@callback(
    Output("download-merged-csv", "data"),
    Input("download-csv-btn", "n_clicks"),
    State("stored-data", "data"),
    prevent_initial_call=True
)
def download_merged_csv(n_clicks, user_data):
    """
    Callback to process and export user-provided data as a CSV after merging it 
    with the main BioRemPP database.

    Parameters:
        n_clicks (int): Number of clicks on the download button.
        user_data (list[dict]): User data stored in the Dash Store component.

    Returns:
        dash.dcc.Download: Object that triggers a CSV file download with the merged data.

    Raises:
        dash.exceptions.PreventUpdate: Raised if no user data is available.
        ValueError: May occur if the user data is malformed.

    Example:
        >>> download_merged_csv(1, [{"compound": "benzene", "value": 3.4}])

    Notes:
        The input data must contain columns compatible with the merge_input_with_database
        function from utils.data_processing.
    """
    if not user_data:
        raise PreventUpdate

    df_input = pd.DataFrame(user_data)
    merged_df = merge_input_with_database(df_input)

    return dcc.send_data_frame(
        merged_df.to_csv,
        filename="biorempp_merged_data.csv",
        index=False
    )


@callback(
    Output("download-hadeg-csv", "data"),
    Input("download-hadeg-csv-btn", "n_clicks"),
    State("stored-data", "data"),
    prevent_initial_call=True
)
def download_hadeg_csv(n_clicks, user_data):
    """
    Callback to merge user-provided data with the HADEG database and export it as a CSV.

    Parameters:
        n_clicks (int): Number of clicks on the download button.
        user_data (list[dict]): User data stored in the Dash Store component.

    Returns:
        dash.dcc.Download: Object that triggers a CSV file download with the HADEG-merged data.

    Raises:
        dash.exceptions.PreventUpdate: Raised if no user data is available.
        ValueError: May occur if the user data is malformed.

    Example:
        >>> download_hadeg_csv(1, [{"compound": "benzene", "value": 3.4}])

    Notes:
        The input data must contain columns compatible with the merge_input_with_database_hadegDB
        function from utils.data_processing.
    """
    if not user_data:
        raise PreventUpdate

    df_input = pd.DataFrame(user_data)
    hadeg_merged_df = merge_input_with_database_hadegDB(df_input)

    return dcc.send_data_frame(
        hadeg_merged_df.to_csv,
        filename="hadeg_results.csv",
        index=False
    )


@callback(
    Output("download-toxcsm-csv", "data"),
    Input("download-toxcsm-csv-btn", "n_clicks"),
    State("stored-data", "data"),
    prevent_initial_call=True
)
def download_toxcsm_csv(n_clicks, user_data):
    """
    Callback to merge user data first with the main BioRemPP database and then with ToxCSM,
    returning the combined result as a downloadable CSV.

    Parameters:
        n_clicks (int): Number of clicks on the download button.
        user_data (list[dict]): User data stored in the Dash Store component.

    Returns:
        dash.dcc.Download: Object that triggers a CSV file download with the ToxCSM-merged data.

    Raises:
        dash.exceptions.PreventUpdate: Raised if no user data is available.
        ValueError: May occur if the user data is malformed.

    Example:
        >>> download_toxcsm_csv(1, [{"compound": "benzene", "value": 3.4}])

    Notes:
        The input data must include fields compatible with both the merge_input_with_database
        and merge_with_toxcsm functions from utils.data_processing.
    """
    if not user_data:
        raise PreventUpdate

    df_input = pd.DataFrame(user_data)
    main_merged = merge_input_with_database(df_input)
    final_merged = merge_with_toxcsm(main_merged)

    return dcc.send_data_frame(
        final_merged.to_csv,
        filename="toxcsm_results.csv",
        index=False
    )
