"""
callbacks.py
------------
Central hub for orchestrating high-level callbacks in the Dash web application.

Complex logic has been modularized into:

- core/upload_handlers.py: Handling file uploads and validations.
- dashboard/display_tables.py: Data table rendering.
- dashboard/toggle_visibility.py: Controlling visibility of sections and buttons.
- dashboard/progress_callbacks.py: Progress bar management.
"""

# ----------------------------------------
# Imports
# ----------------------------------------

import dash
import dash_bootstrap_components as dbc
from dash import html, dcc, callback
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
import pandas as pd

# Application Instance
from app import app

# Layouts
from layouts.about import get_about_layout
from layouts.data_analysis import get_dataAnalysis_layout
from layouts.results import get_results_layout

# ✅ Novos Módulos
from callbacks.core.upload_handlers import handle_upload_or_example as handle_upload_or_example_logic
from callbacks.dashboard.display_tables import update_table as update_table_logic, update_database_table as update_database_table_logic, update_ko_count_table as update_ko_count_table_logic
from callbacks.dashboard.toggle_visibility import toggle_additional_analysis_visibility as toggle_additional_analysis_visibility_logic, toggle_graph_visibility as toggle_graph_visibility_logic, display_results as display_results_logic, process_and_toggle_elements as process_and_toggle_elements_logic
from callbacks.dashboard.progress_callbacks import handle_progress as handle_progress_logic
from callbacks.core.merge_feedback_callbacks import handle_merge_and_feedback
import callbacks.core.merge_feedback_callbacks



# ----------------------------------------
# Callbacks
# ----------------------------------------

@callback(
    [
        Output('stored-data', 'data'),
        Output('process-data', 'disabled'),
        Output('alert-container', 'children', allow_duplicate=True),  # <- Adicione isto
        Output('page-state', 'data', allow_duplicate=True)
    ],
    [
        Input('upload-data', 'contents'),
        Input('see-example-data', 'n_clicks')
    ],
    [State('upload-data', 'filename')],
    prevent_initial_call=True
)
def handle_upload_or_example(contents, n_clicks_example, filename):
    return handle_upload_or_example_logic(contents, n_clicks_example, filename)


@callback(
    Output('output-data-upload', 'children'),
    Input('stored-data', 'data')
)
def update_table(stored_data):
    return update_table_logic(stored_data)


@callback(
    Output('database-data-table', 'children'),
    [Input('process-data', 'n_clicks')],
    prevent_initial_call=True
)
def update_database_table(n_clicks):
    return update_database_table_logic(n_clicks)


@callback(
    Output('ko-count-table-container', 'children'),
    [Input('process-data', 'n_clicks')],
    [State('stored-data', 'data')],
    prevent_initial_call=True
)
def update_ko_count_table(n_clicks, stored_data):
    return update_ko_count_table_logic(n_clicks, stored_data)


@callback(
    Output('additional-analysis-container', 'style'),
    [Input('process-data', 'n_clicks')]
)
def toggle_additional_analysis_visibility(n_clicks):
    return toggle_additional_analysis_visibility_logic(n_clicks)


@callback(
    Output('output-graphs', 'style'),
    Input('tabs', 'value')
)
def toggle_graph_visibility(tab):
    return toggle_graph_visibility_logic(tab)


@callback(
    [
        Output('progress-bar', 'value'),
        Output('progress-bar', 'label'),
        Output('progress-interval', 'disabled'),
        Output('progress-container', 'style')
    ],
    [
        Input('upload-data', 'contents'),
        Input('see-example-data', 'n_clicks'),
        Input('process-data', 'n_clicks'),
        Input('progress-interval', 'n_intervals')
    ],
    [State('merge-status', 'data')],
    prevent_initial_call=True
)
def handle_progress(contents, n_clicks_example, n_clicks_submit, n_intervals, merge_status):
    return handle_progress_logic(contents, n_clicks_example, n_clicks_submit, n_intervals, merge_status)



@callback(
    [
        Output('initial-content', 'style'),
        Output('results-content', 'style')
    ],
    [Input('view-results', 'n_clicks')],
    [State('page-state', 'data')],
    prevent_initial_call=True
)
def display_results(n_clicks, current_state):
    return display_results_logic(n_clicks, current_state)


@callback(
    [
        Output('view-results', 'style'),
        Output('process-data', 'style'),
        Output('page-state', 'data')
    ],
    [Input('process-data', 'n_clicks')],
    [
        State('stored-data', 'data'),
        State('page-state', 'data'),
        State('merge-status', 'data')  # ← novo state
    ],
    prevent_initial_call=True
)
def process_and_toggle_elements(n_clicks, stored_data, current_state, merge_status):
    return process_and_toggle_elements_logic(n_clicks, stored_data, current_state, merge_status)
