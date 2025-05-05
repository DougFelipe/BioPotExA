# callbacks/core/merge_feedback_callbacks.py
"""
Handles real-time merge operations with BioRemPP, HADEG, and ToxCSM databases,
records execution time, and controls interface state update.
"""

import time
import pandas as pd
from dash import callback_context, html
from dash.exceptions import PreventUpdate
from dash.dependencies import Input, Output, State
from app import app
from utils.data_processing import (
    merge_input_with_database,
    merge_input_with_database_hadegDB,
    merge_with_toxcsm
)
from callbacks.core.feedback_alerts import create_alert


@app.callback(
    [
        Output('merge-status', 'data'),
        Output('page-state', 'data', allow_duplicate=True),
        Output('alert-container', 'children')
    ],
    [Input('process-data', 'n_clicks')],
    [State('stored-data', 'data')],
    prevent_initial_call=True
)
def handle_merge_and_feedback(n_clicks, stored_data):
    if n_clicks is None or not stored_data:
        raise PreventUpdate

    input_df = pd.DataFrame(stored_data)

    merge_times = {}
    errors = []

    # MERGE 1: BioRemPP (main database)
    try:
        print("[DEBUG] Starting merge with BioRemPP...")
        start = time.time()
        merged_biorempp = merge_input_with_database(input_df.copy())
        merge_times['BioRemPP'] = round(time.time() - start, 2)
        print("[DEBUG] BioRemPP merged columns:", merged_biorempp.columns.tolist())
    except Exception as e:
        errors.append(f"BioRemPP merge failed: {str(e)}")
        merged_biorempp = None

    # MERGE 2: HADEG (independent merge for other analysis)
    try:
        print("[DEBUG] Starting merge with HADEG...")
        start = time.time()
        _ = merge_input_with_database_hadegDB(input_df.copy())
        merge_times['HADEG'] = round(time.time() - start, 2)
        print("[DEBUG] HADEG merge completed.")
    except Exception as e:
        errors.append(f"HADEG merge failed: {str(e)}")

    # MERGE 3: ToxCSM (must use BioRemPP as input)
    if merged_biorempp is not None:
        try:
            print("[DEBUG] Starting merge with ToxCSM...")
            print("[DEBUG] Columns available before ToxCSM merge:", merged_biorempp.columns.tolist())
            start = time.time()
            _ = merge_with_toxcsm(merged_biorempp.copy())
            merge_times['ToxCSM'] = round(time.time() - start, 2)
            print("[DEBUG] ToxCSM merge completed.")
        except Exception as e:
            errors.append(f"ToxCSM merge failed: {str(e)}")
    else:
        errors.append("ToxCSM merge skipped due to BioRemPP merge failure.")

    # Feedback to UI
    if errors:
        alert = create_alert([
            "One or more merges failed:", html.Ul([html.Li(err) for err in errors])
        ], color='danger')
        return {'status': 'failed', 'merge_times': merge_times}, 'initial', alert

    alert_msg = html.Div([
    html.P("✅ All merges completed successfully.", style={'marginBottom': '5px'}),
    html.Ul([
        html.Li(f"BioRemPP: {merge_times.get('BioRemPP', '-')}s"),
        html.Li(f"HADEG: {merge_times.get('HADEG', '-')}s"),
        html.Li(f"ToxCSM: {merge_times.get('ToxCSM', '-')}s")
    ], style={'paddingLeft': '20px', 'margin': 0})
    ])
    alert = create_alert(alert_msg, color='success')

    return {'status': 'done', 'merge_times': merge_times}, 'processed', alert
