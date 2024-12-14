from dash import Input, Output, State, callback, html
import pandas as pd
from utils.table_utils import create_table_from_dataframe  # Função para criar a tabela
from utils.data_processing import merge_input_with_database_hadegDB  # Função para processar os dados

@callback(
    [
        Output("hadeg-results-table-container", "children"),  # Exibe a tabela
        Output("view-hadeg-results-button", "style"),  # Oculta o botão após o clique
        Output("hadeg-placeholder-message", "style")  # Oculta a mensagem inicial
    ],
    [Input("view-hadeg-results-button", "n_clicks")],
    [State("stored-data", "data")],
    prevent_initial_call=True
)
def render_hadeg_table(n_clicks, stored_data):
    # Condição: Clique no botão e dados válidos disponíveis
    if n_clicks > 0 and stored_data:
        input_df = pd.DataFrame(stored_data)
        merged_df = merge_input_with_database_hadegDB(input_df)

        # Se a tabela resultante estiver vazia
        if merged_df.empty:
            return (
                html.Div("No matches found with the HADEG database", className="no-data-message"),
                {"display": "none"},  # Oculta o botão
                {"display": "none"}  # Oculta a mensagem inicial
            )

        # Criação da tabela com os dados processados
        table = create_table_from_dataframe(merged_df, "hadeg-results-table")

        return (
            html.Div(table, className="results-table"),  # Renderiza a tabela
            {"display": "none"},  # Oculta o botão
            {"display": "none"}  # Oculta a mensagem inicial
        )

    # Se não houver dados, previne qualquer atualização
    raise dash.exceptions.PreventUpdate
