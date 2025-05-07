import dash  # Core Dash functionality
import dash_bootstrap_components as dbc  # For UI components like alerts
from dash import html, dcc, callback, callback_context, dash_table  # Core Dash components
from dash.dependencies import Input, Output, State  # Input, Output, and State dependencies for callbacks
from dash.exceptions import PreventUpdate  # To prevent unnecessary updates
import pandas as pd  # For data manipulation

# Application Instance
from app import app

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

def process_and_toggle_elements(n_clicks, stored_data, current_state, merge_status):
    """
    Atualiza os botões após o merge_status indicar sucesso.
    """
    if not n_clicks or not stored_data or not merge_status:
        raise PreventUpdate

    if merge_status.get('status') == 'done':
        return (
            {'display': 'inline-block'},  # Mostrar botão "View Results"
            {'display': 'none'},          # Ocultar botão "Submit"
            'processed'
        )

    return (
        {'display': 'none'},
        {'display': 'inline-block'},
        current_state
    )
