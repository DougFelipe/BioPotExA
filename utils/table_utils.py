import dash_ag_grid as dag

def create_table_from_dataframe(df, table_id, hidden_columns=None):
    # Define column definitions
    column_defs = [{'field': col} for col in df.columns]

    # Hide specific columns if requested
    if hidden_columns:
        for col_def in column_defs:
            if col_def['field'] in hidden_columns:
                col_def['hide'] = True

    # Create and configure the AG Grid component
    table = dag.AgGrid(
        id=table_id,
        rowData=df.to_dict("records"),
        columnDefs=column_defs,
        defaultColDef={
            "resizable": True,
            "sortable": True,
            "filter": True,
            "floatingFilter": True
        },
        # Instead of gridOptions, use dashGridOptions
        dashGridOptions={
            "pagination": True,         # Enables pagination
            "paginationPageSize": 10,   # Number of rows per page
            "enableRangeSelection": True,  # Allows cell-range selection
        },
        # To enable CSV export, you can define csvExportParams
        csvExportParams={
            "fileName": "exported_data.csv"  # The default filename for downloaded CSV
        },
        # Optional: enterprise features
        enableEnterpriseModules=False,  # or True if you have a license/enterprise usage
    )

    return table
