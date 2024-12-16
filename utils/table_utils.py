"""
table_utils.py
--------------
This script contains utility functions for working with Dash AG Grid tables, including generating tables from pandas DataFrames.
"""

# -------------------------------
# Imports
# -------------------------------

# Import the pandas library for handling tabular data.
import pandas as pd

# Import the Dash AG Grid component for rendering interactive tables in Dash applications.
import dash_ag_grid as dag

# -------------------------------
# Function: create_table_from_dataframe
# -------------------------------

def create_table_from_dataframe(df: pd.DataFrame, table_id: str, hidden_columns: list = None) -> dag.AgGrid:
    """
    Creates a Dash AG Grid table component from a pandas DataFrame, 
    with an option to hide specific columns.

    Parameters:
    - df (pd.DataFrame): The pandas DataFrame to be rendered as a table.
    - table_id (str): A unique ID for the table component.
    - hidden_columns (list, optional): A list of column names to hide in the table. Defaults to None.

    Returns:
    - dag.AgGrid: The Dash AG Grid component configured with the specified data and settings.
    """

    # Define column configurations for AG Grid based on the DataFrame's columns.
    # Each column will initially have the same settings.
    column_defs = [{'field': col} for col in df.columns]

    # Hide specific columns if `hidden_columns` is provided.
    if hidden_columns:
        for col_def in column_defs:
            if col_def['field'] in hidden_columns:
                col_def['hide'] = True  # Add the `hide` property to the column definition.

    # Create and configure the AG Grid component.
    table = dag.AgGrid(
        id=table_id,  # Set the unique ID for the table.
        rowData=df.to_dict("records"),  # Convert the DataFrame rows into a list of dictionaries for rendering.
        columnDefs=column_defs,  # Set the column definitions, including hidden columns if applicable.
        defaultColDef={  # Default properties for all columns.
            "resizable": True,  # Allow resizing of columns.
            "sortable": True,  # Enable sorting for all columns.
            "filter": True,  # Add basic filtering options to columns.
            "floatingFilter": True  # Include floating filters for quick filtering inputs.
        },
    )

    # Return the configured AG Grid component to be used in a Dash layout.
    return table
