"""
callbacks.py
------------
This script defines callbacks for a Dash web application. Callbacks manage interactivity by 
updating UI components based on user actions, such as uploading data, loading example datasets, 
or submitting data for processing.

Features include:
- Handling file uploads and example datasets.
- Processing and validating input data.
- Displaying results in tables.
"""

# ----------------------------------------
# Imports
# ----------------------------------------

import dash  # Core Dash functionality
import dash_bootstrap_components as dbc  # For UI components like alerts
from dash import html, dcc, callback, callback_context, dash_table  # Core Dash components
from dash.dependencies import Input, Output, State  # Input, Output, and State dependencies for callbacks
from dash.exceptions import PreventUpdate  # To prevent unnecessary updates
import pandas as pd  # For data manipulation

# Application Instance
from app import app

# Layouts
from layouts.about import get_about_layout
from layouts.data_analysis import get_dataAnalysis_layout
from layouts.results import get_results_layout

# Utilities
from utils.data_validator import validate_and_process_input
from utils.data_loader import load_database
from utils.data_processing import (
    merge_input_with_database,
    merge_with_kegg,
    count_ko_per_pathway,
    count_ko_per_sample_for_pathway,
    merge_input_with_database_hadegDB,
    merge_with_toxcsm
)
from utils.table_utils import create_table_from_dataframe
from utils.plot_processing import plot_pathway_ko_counts, plot_sample_ko_counts

# ----------------------------------------
# Callbacks
# ----------------------------------------

@callback(
    [
        Output('stored-data', 'data'),  # Stores validated and processed data
        Output('process-data', 'disabled'),  # Enables or disables the "Submit" button
        Output('alert-container', 'children'),  # Displays alerts to the user
        Output('page-state', 'data', allow_duplicate=True)  # Tracks the page state
    ],
    [
        Input('upload-data', 'contents'),  # Content of the uploaded file
        Input('see-example-data', 'n_clicks')  # Button click to load example data
    ],
    [State('upload-data', 'filename')],  # Name of the uploaded file
    prevent_initial_call=True
)
def handle_upload_or_example(contents, n_clicks_example, filename):
    """
    Handles file uploads or example dataset loading, processes the input, and updates the UI.

    Parameters:
    - contents (str): File contents (uploaded by the user).
    - n_clicks_example (int): Number of times the "See Example Data" button is clicked.
    - filename (str): Name of the uploaded file.

    Returns:
    - dict: Processed data to be stored.
    - bool: Whether to disable the "Submit" button.
    - dbc.Alert: Alert message indicating success or error.
    - str: Updated page state ('initial' or 'loaded').
    """
    ctx = dash.callback_context  # Tracks which input triggered the callback

    if not ctx.triggered:
        raise PreventUpdate

    triggered_id = ctx.triggered[0]['prop_id'].split('.')[0]

    # Handle example data loading
    if triggered_id == 'see-example-data':
        try:
            example_data_path = 'data/sample_data.txt'
            with open(example_data_path, 'r') as file:
                example_contents = file.read()

            df, error = validate_and_process_input(example_contents, 'sample_data.txt')
            if error:
                return None, True, dbc.Alert(
                    f'Error processing example dataset: {error}',
                    color='danger',
                    is_open=True,
                    duration=4000
                ), 'initial'

            return (
                df.to_dict('records'),
                False,
                dbc.Alert(
                    [
                        "Example dataset loaded successfully",
                        html.Br(),
                        'Click "Submit" to process the data',
                        html.Br(),
                        "Please wait until the progress is complete to view the results"
                    ],
                    color='success',
                    is_open=True,
                    dismissable=True
                ),
                'loaded'
            )
        except Exception as e:
            return None, True, dbc.Alert(
                f'Error loading example dataset: {str(e)}',
                color='danger',
                is_open=True,
                duration=4000
            ), 'initial'

    # Handle file upload
    if triggered_id == 'upload-data' and contents:
        df, error = validate_and_process_input(contents, filename)
        if error:
            return None, True, dbc.Alert(
                error,
                color='danger',
                is_open=True,
                duration=4000
            ), 'initial'

        return (
            df.to_dict('records'),
            False,
            dbc.Alert(
                [
                    "File uploaded and validated successfully",
                    html.Br(),
                    'Click "Submit" to process the data',
                    html.Br(),
                    "Please wait until the progress is complete to view the results"
                ],
                color='success',
                is_open=True,
                dismissable=True
            ),
            'loaded'
        )

    raise PreventUpdate


@app.callback(
    Output('output-data-upload', 'children'),  # Updates the table with uploaded data
    Input('stored-data', 'data')  # Triggered when 'stored-data' is updated
)
def update_table(stored_data):
    """
    Updates the displayed table with the stored data.

    Parameters:
    - stored_data (dict): Data stored after processing.

    Returns:
    - html.Div: A table displaying the stored data.
    """
    if stored_data is None:
        return html.Div('Nenhum dado para exibir.')  # No data message

    df = pd.DataFrame(stored_data)
    table = create_table_from_dataframe(df, 'data-upload-table')  # Creates a Dash table
    return html.Div(table)


@app.callback(
    Output('database-data-table', 'children'),  # Updates the table with database content
    [Input('process-data', 'n_clicks')],  # Triggered when "Submit" button is clicked
    prevent_initial_call=True
)
def update_database_table(n_clicks):
    """
    Updates the table to display the database content.

    Parameters:
    - n_clicks (int): Number of times the "Submit" button is clicked.

    Returns:
    - html.Div: A table displaying the database content.
    """
    if n_clicks is None or n_clicks < 1:
        raise PreventUpdate

    df_database = load_database('data/database.csv')  # Load database content
    table = create_table_from_dataframe(df_database, 'database-data-table')
    return html.Div(table)


@app.callback(
    Output('ko-count-table-container', 'children'),  # Updates the KO count table
    [Input('process-data', 'n_clicks')],  # Triggered when "Submit" button is clicked
    [State('stored-data', 'data')]  # Reads stored data
)
def update_ko_count_table(n_clicks, stored_data):
    """
    Processes data to compute KO counts and updates the displayed table.

    Parameters:
    - n_clicks (int): Number of times the "Submit" button is clicked.
    - stored_data (dict): Data stored after processing.

    Returns:
    - html.Div: A table displaying KO counts.
    """
    if n_clicks is None or n_clicks < 1:
        raise PreventUpdate

    if stored_data is None:
        return html.Div('Nenhum dado para exibir.')  # No data message

    input_df = pd.DataFrame(stored_data)
    merged_df = merge_input_with_database(input_df)  # Merge input with database
    table = dash_table.DataTable(
        data=merged_df.to_dict('records'),
        columns=[{'name': i, 'id': i} for i in merged_df.columns],
        page_size=10,
        style_table={'overflowX': 'auto'}
    )

    return html.Div(table, id='ko-count-table-container')

# ----------------------------------------
# Callback: Toggle Additional Analysis Visibility
# ----------------------------------------

@app.callback(
    Output('additional-analysis-container', 'style'),
    [Input('process-data', 'n_clicks')]
)
def toggle_additional_analysis_visibility(n_clicks):
    """
    Toggles the visibility of the additional analysis container based on button clicks.

    Parameters:
    - n_clicks (int): Number of clicks on the "process-data" button.

    Returns:
    - dict: CSS style to set the container's display property.
    """
    if n_clicks and n_clicks > 0:
        return {'display': 'block'}  # Show the container
    else:
        raise PreventUpdate  # Prevent unnecessary UI updates


# ----------------------------------------
# Callback: Toggle Graph Visibility
# ----------------------------------------

@app.callback(
    Output('output-graphs', 'style'),
    Input('tabs', 'value')
)
def toggle_graph_visibility(tab):
    """
    Toggles the visibility of graphs based on the selected tab.

    Parameters:
    - tab (str): The selected tab value.

    Returns:
    - dict: CSS style to control graph visibility.
    """
    if tab == 'tab-data-analysis':
        return {'display': 'block'}  # Show the graphs


# ----------------------------------------
# Callback: Handle Progress Bar Updates
# ----------------------------------------

@callback(
    [
        Output('progress-bar', 'value'),  # Progress bar percentage value
        Output('progress-bar', 'label'),  # Progress bar label text
        Output('progress-interval', 'disabled'),  # Interval enable/disable state
        Output('progress-container', 'style')  # Progress bar container visibility
    ],
    [
        Input('upload-data', 'contents'),
        Input('see-example-data', 'n_clicks'),
        Input('process-data', 'n_clicks'),
        Input('progress-interval', 'n_intervals')
    ],
    prevent_initial_call=True
)
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
    triggered_id = ctx.triggered_id  # Identifies the triggered input

    if triggered_id in ['upload-data', 'see-example-data']:
        return 0, "", True, {"display": "block", "textAlign": "center"}  # Show the progress bar but do not start

    if triggered_id == 'process-data':
        return 0, "", False, {"display": "block", "textAlign": "center"}  # Reset and start the progress bar

    if triggered_id == 'progress-interval':
        progress = min(n_intervals * 10, 100)  # Increment progress by 10% per interval
        if progress == 100:
            return progress, "Processing Complete!", True, {"display": "block", "textAlign": "center"}  # Complete
        return progress, f"{progress}%", False, {"display": "block", "textAlign": "center"}  # Update progress

    raise PreventUpdate  # No updates if no valid input is triggered


# ----------------------------------------
# Callback: Display Results Section
# ----------------------------------------

@app.callback(
    [Output('initial-content', 'style'), 
     Output('results-content', 'style')],
    [Input('view-results', 'n_clicks'), 
     State('page-state', 'data')],
    prevent_initial_call=True
)
def display_results(n_clicks, current_state):
    """
    Controls the visibility of the results section based on the "View Results" button click.

    Parameters:
    - n_clicks (int): Number of clicks on the "view-results" button.
    - current_state (str): Current state of the page (e.g., 'processed').

    Returns:
    - Tuple: CSS styles to toggle the visibility of the initial and results sections.
    """
    if n_clicks > 0 and current_state == 'processed':
        return {'display': 'none'}, {'display': 'block'}  # Show results and hide initial content
    return {'display': 'block'}, {'display': 'none'}  # Default state


# ----------------------------------------
# Callback: Process and Toggle Elements
# ----------------------------------------

@callback(
    [
        Output('view-results', 'style'),  # "View Results" button visibility
        Output('process-data', 'style'),  # "Click to Submit" button visibility
        Output('page-state', 'data')  # Page state (e.g., 'processed', 'loaded')
    ],
    [Input('process-data', 'n_clicks')],
    [State('stored-data', 'data'), State('page-state', 'data')],
    prevent_initial_call=True
)
def process_and_toggle_elements(n_clicks, stored_data, current_state):
    """
    Toggles visibility of "View Results" and "Click to Submit" buttons based on the page state.

    Parameters:
    - n_clicks (int): Number of clicks on the "process-data" button.
    - stored_data (dict): Data stored for processing.
    - current_state (str): Current state of the page.

    Returns:
    - Tuple: CSS styles for button visibility and updated page state.
    """
    if n_clicks > 0 and stored_data and current_state == 'loaded':
        return (
            {'display': 'inline-block'},  # Show "View Results" button
            {'display': 'none'},  # Hide "Click to Submit" button
            'processed'  # Update state to 'processed'
        )
    return (
        {'display': 'none'},  # Hide "View Results" button
        {'display': 'inline-block'},  # Show "Click to Submit" button
        current_state  # Keep the current state
    )
