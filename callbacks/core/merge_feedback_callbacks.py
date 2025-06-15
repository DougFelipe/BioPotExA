# callbacks/core/merge_feedback_callbacks.py
"""
Handles real-time merge operations with BioRemPP, HADEG, and ToxCSM databases,
records execution time, and controls interface state update.
"""

import time
import logging
import pandas as pd
import dash_bootstrap_components as dbc
from dash import callback_context, html
from dash.exceptions import PreventUpdate
from dash.dependencies import Input, Output, State

from app import app
from utils.core.data_processing import (
    merge_input_with_database,
    merge_input_with_database_hadegDB,
    merge_with_toxcsm
)
from callbacks.core.feedback_alerts import create_alert

# Setup logging
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


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
    """
    Handles the sequential merging of input data with multiple databases,
    measuring execution time and returning feedback to the user interface.

    Parameters
    ----------
    n_clicks : int
        Number of times the process-data button was clicked.
    stored_data : dict
        Input data stored in dictionary format (from Dash Store).

    Returns
    -------
    tuple
        - dict: Merge status and timings.
        - str: New page state ("processed" or "initial").
        - dash.html.Div: Alert component for user feedback.
    """
    if n_clicks is None or not stored_data:
        raise PreventUpdate

    input_df = pd.DataFrame(stored_data)
    merge_times = {}
    errors = []

    # MERGE 1: BioRemPP
    try:
        logger.info("Starting merge with BioRemPP...")
        start = time.time()
        merged_biorempp = merge_input_with_database(input_df.copy())
        merge_times['BioRemPP'] = round(time.time() - start, 2)
        logger.info("BioRemPP merge completed in %.2fs", merge_times['BioRemPP'])
    except Exception as e:
        error_msg = f"BioRemPP merge failed: {str(e)}"
        logger.error(error_msg)
        errors.append(error_msg)
        merged_biorempp = None

    # MERGE 2: HADEG
    try:
        logger.info("Starting merge with HADEG...")
        start = time.time()
        _ = merge_input_with_database_hadegDB(input_df.copy())
        merge_times['HADEG'] = round(time.time() - start, 2)
        logger.info("HADEG merge completed in %.2fs", merge_times['HADEG'])
    except Exception as e:
        error_msg = f"HADEG merge failed: {str(e)}"
        logger.error(error_msg)
        errors.append(error_msg)

    # MERGE 3: ToxCSM (depends on BioRemPP)
    if merged_biorempp is not None:
        try:
            logger.info("Starting merge with ToxCSM...")
            start = time.time()
            _ = merge_with_toxcsm(merged_biorempp.copy())
            merge_times['ToxCSM'] = round(time.time() - start, 2)
            logger.info("ToxCSM merge completed in %.2fs", merge_times['ToxCSM'])
        except Exception as e:
            error_msg = f"ToxCSM merge failed: {str(e)}"
            logger.error(error_msg)
            errors.append(error_msg)
    else:
        msg = "ToxCSM merge skipped due to BioRemPP merge failure."
        logger.warning(msg)
        errors.append(msg)

    # UI Feedback
    if errors:
        alert = create_alert([
            "❌ One or more merges failed:",
            html.Ul([html.Li(err) for err in errors])
        ], color='danger')
        return {'status': 'failed', 'merge_times': merge_times}, 'initial', alert

    alert_msg = html.Div([
        html.P("✅ All merges completed successfully.", style={'marginBottom': '5px'}),
        html.Ul([
            html.Li(f"BioRemPP: {merge_times.get('BioRemPP', '-'):.2f}s"),
            html.Li(f"HADEG: {merge_times.get('HADEG', '-'):.2f}s"),
            html.Li([
                f"ToxCSM: {merge_times.get('ToxCSM', '-'):.2f}s",
                html.Br(),
                dbc.Spinner(size="sm", color="success", type="border", spinner_style={"marginRight": "6px"}),
                html.Span("Generating output"),
                html.Br(),
                html.Span("Click the "),
                html.Strong("View Results", style={"color": "red", "fontWeight": "bold"}),
                html.Span(" button when it becomes available.")
            ])
        ], style={'paddingLeft': '20px', 'margin': 0})
    ])

    alert = create_alert(alert_msg, color='success')
    return {'status': 'done', 'merge_times': merge_times}, 'processed', alert
