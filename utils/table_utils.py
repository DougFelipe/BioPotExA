# my_dash_app/utils/table_utils.py

import pandas as pd
import dash_ag_grid as dag

def create_table_from_dataframe(df: pd.DataFrame, table_id: str, hidden_columns: list = None) -> dag.AgGrid:
    """
    Cria um componente de tabela Dash AG Grid a partir de um DataFrame do pandas, 
    com a opção de ocultar colunas específicas.

    :param df: DataFrame do pandas a ser renderizado como uma tabela.
    :param table_id: ID único para o componente da tabela.
    :param hidden_columns: Lista de colunas a serem ocultadas na tabela.
    :return: Componente AgGrid para ser utilizado em um layout do Dash.
    """
    column_defs = [{'field': col} for col in df.columns]

    # Ocultar colunas específicas
    if hidden_columns:
        for col_def in column_defs:
            if col_def['field'] in hidden_columns:
                col_def['hide'] = True

    table = dag.AgGrid(
        id=table_id,
        rowData=df.to_dict("records"),
        columnDefs=column_defs,
        defaultColDef={"resizable": True, "sortable": True, "filter": True, "floatingFilter": True},
    )
    return table
