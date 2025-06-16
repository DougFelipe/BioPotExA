"""
upload_handlers.py
-------------------
Handles file uploads and example dataset loading for the application.

Functions:
- validate_upload_size: Check if uploaded file size is within allowed limit.
- load_example_data: Load an example dataset.
- process_uploaded_file: Validate and process an uploaded file.
"""

import dash  # Core Dash functionality
import dash_bootstrap_components as dbc  # For UI components like alerts
from dash import html, dcc, callback, callback_context, dash_table  # Core Dash components
from dash.dependencies import Input, Output, State  # Input, Output, and State dependencies for callbacks
from dash.exceptions import PreventUpdate  # To prevent unnecessary updates
import pandas as pd  # For data manipulation

# Application Instance
from app import app

import os
from utils.core.data_validator import validate_and_process_input

MAX_UPLOAD_SIZE_MB = 5  # 5 MB limit

def validate_upload_size(contents):
    """
    Validates if the uploaded content size is within the allowed maximum.

    Parameters:
    - contents (str): Content of the uploaded file.

    Returns:
    - (bool, str): Tuple of (is_valid, error_message)
    """
    if contents and len(contents) > MAX_UPLOAD_SIZE_MB * 1024 * 1024:
        return False, f"O arquivo enviado ultrapassa {MAX_UPLOAD_SIZE_MB} MB."
    return True, None

def load_example_data():
    """
    Loads and processes the example dataset stored in 'data/sample_data.txt'.

    Returns:
    - (pd.DataFrame, str): Tuple of (dataframe, error_message)
    """
    try:
        example_path = os.path.join('data', 'sample_data.txt')
        with open(example_path, 'r') as file:
            example_contents = file.read()

        df, error = validate_and_process_input(example_contents, 'sample_data.txt')
        if error:
            return None, error
        return df, None
    except Exception as e:
        return None, str(e)

def process_uploaded_file(contents, filename):
    """
    Processes a user-uploaded file.

    Parameters:
    - contents (str): File contents.
    - filename (str): Name of the uploaded file.

    Returns:
    - (pd.DataFrame, str): Tuple of (dataframe, error_message)
    """
    is_valid_size, size_error = validate_upload_size(contents)
    if not is_valid_size:
        return None, size_error

    df, error = validate_and_process_input(contents, filename)
    if error:
        return None, error
    return df, None


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
                        "Example dataset loaded successfully!",
                        html.Br(),
                        'Click ',
                        html.Strong('"Submit"'),
                        ' below to process the data'
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
                    'Click "Submit" to process the data'
                ],
                color='success',
                is_open=True,
                dismissable=True
            ),
            'loaded'
        )

    raise PreventUpdate
