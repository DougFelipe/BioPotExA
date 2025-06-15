import dash  # Core Dash functionality
import dash_bootstrap_components as dbc  # For UI components like alerts
from dash import html, dcc, callback, callback_context, dash_table  # Core Dash components
from dash.dependencies import Input, Output, State  # Input, Output, and State dependencies for callbacks
from dash.exceptions import PreventUpdate  # To prevent unnecessary updates
from utils.core.table_utils import create_table_from_dataframe  # Utility function for table creation

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

    df_database = load_database('data/database.xlsx')  # Load database content
    table = create_table_from_dataframe(df_database, 'database-data-table')
    return html.Div(table)

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
