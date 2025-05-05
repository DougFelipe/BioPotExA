# callbacks/dashboard/progress_callbacks.py

from dash.exceptions import PreventUpdate
import dash

def handle_progress(contents, n_clicks_example, n_clicks_submit, n_intervals, merge_status):
    ctx = dash.callback_context
    triggered_id = ctx.triggered_id

    if triggered_id in ['upload-data', 'see-example-data']:
        return 0, "", True, {"display": "block", "textAlign": "center"}

    if triggered_id == 'process-data':
        return 0, "", False, {"display": "block", "textAlign": "center"}

    if triggered_id == 'progress-interval':
        if merge_status and merge_status.get('status') == 'done':
            total_time = sum(merge_status.get('merge_times', {}).values())
            total_time = max(total_time, 1.0)  # mínimo 1s
            step = 100 / (total_time * 2)  # Simula duas atualizações por segundo

            progress = min(round(n_intervals * step), 100)

            if progress >= 100:
                return 100, "Processing Complete!", True, {"display": "block", "textAlign": "center"}

            return progress, f"{progress}%", False, {"display": "block", "textAlign": "center"}

    raise PreventUpdate
