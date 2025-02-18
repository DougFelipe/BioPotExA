# Import the pandas library for handling tabular data.
import pandas as pd

# Import the Dash AG Grid component for rendering interactive tables in Dash applications.
import dash_ag_grid as dag

# -------------------------------
# Function: create_table_from_dataframe
# -------------------------------
import dash_bootstrap_components as dbc
import dash_ag_grid as dag
def create_table_from_dataframe(df, table_id, hidden_columns=None):
    column_defs = [{"field": col} for col in df.columns]

    # Hide columns if needed
    if hidden_columns:
        for c in column_defs:
            if c["field"] in hidden_columns:
                c["hide"] = True

    return dag.AgGrid(
        id=table_id,
        rowData=df.to_dict("records"),
        columnDefs=column_defs,
        defaultColDef={
            "resizable": True,
            "sortable": True,
            "filter": True,
            "floatingFilter": True
        },
        dashGridOptions={
            "pagination": True,
            "paginationPageSize": 10,
            "enableRangeSelection": True
        },
        csvExportParams={
            "fileName": "biorempp_export.csv"
        },
        style={"height": "400px", "width": "100%"}
    )
