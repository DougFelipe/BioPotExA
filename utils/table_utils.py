# my_dash_app/utils/table_utils.py

import pandas as pd
import dash_ag_grid as dag

def create_table_from_dataframe(df: pd.DataFrame, table_id: str) -> dag.AgGrid:
    """
    Cria um componente de tabela Dash AG Grid a partir de um DataFrame do pandas.

    :param df: DataFrame do pandas a ser renderizado como uma tabela.
    :param table_id: ID único para o componente da tabela.
    :return: Componente AgGrid para ser utilizado em um layout do Dash.
    """
    column_defs = [{'field': col} for col in df.columns]

    table = dag.AgGrid(
        id=table_id,
        rowData=df.to_dict("records"),
        columnDefs=column_defs,
        defaultColDef={"resizable": True, "sortable": True, "filter": True, "floatingFilter": True},
    )
    return table
