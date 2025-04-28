# callbacks/dashboard/progress_callbacks.py

from dash.exceptions import PreventUpdate
import dash

def handle_progress(contents, n_clicks_example, n_clicks_submit, n_intervals):
    """
    Handles progress bar updates during data upload, submission, and processing.

    Parameters:
    - contents (str): Uploaded data content in base64 format.
    - n_clicks_example (int): Number of clicks on the "see-example-data" button.
    - n_clicks_submit (int): Number of clicks on the "process-data" button.
    - n_intervals (int): Number of interval updates.

    Returns:
    - Tuple: Updated values for progress bar percentage, label, interval state, and container style.
    """
    ctx = dash.callback_context
    triggered_id = ctx.triggered_id

    if triggered_id in ['upload-data', 'see-example-data']:
        return 0, "", True, {"display": "block", "textAlign": "center"}

    if triggered_id == 'process-data':
        return 0, "", False, {"display": "block", "textAlign": "center"}

    if triggered_id == 'progress-interval':
        progress = min(n_intervals * 10, 100)
        if progress == 100:
            return progress, "Processing Complete!", True, {"display": "block", "textAlign": "center"}
        return progress, f"{progress}%", False, {"display": "block", "textAlign": "center"}

    raise PreventUpdate
