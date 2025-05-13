# callbacks/dashboard/eda_report_callbacks.py

import pandas as pd
from dash import callback, Output, Input, State, dcc
from dash.exceptions import PreventUpdate
from ydata_profiling import ProfileReport

from utils.data_processing import merge_input_with_database  # <- IMPORTANTE

@callback(
    Output("download-eda-report", "data"),
    Input("download-eda-btn", "n_clicks"),
    State("stored-data", "data"),
    prevent_initial_call=True
)
def generate_eda_report(n_clicks, stored_data):
    if not stored_data:
        raise PreventUpdate

    try:
        # Converte o input para DataFrame
        df_input = pd.DataFrame(stored_data)

        # Realiza o merge com o database.csv
        df_merged = merge_input_with_database(df_input)

        # Gera o relatório do profiling com base no merged
        profile = ProfileReport(df_merged, minimal=False, explorative=True)
        html_str = profile.to_html()

        return dcc.send_string(html_str, filename="EDA_Report_BioRemPP_.html")

    except Exception as e:
        print(f"[ERROR] Failed to generate merged EDA report: {str(e)}")
        raise PreventUpdate
