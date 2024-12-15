from dash import Input, Output, State, callback, html
import pandas as pd
from utils.table_utils import create_table_from_dataframe  # Função para criar a tabela
from utils.data_processing import merge_input_with_database, merge_with_toxcsm  # Funções para processar os dados

@callback(
    [
        Output("toxcsm-results-table-container", "children"),  # Exibe a tabela
        Output("view-toxcsm-results-button", "style"),  # Oculta o botão após o clique
        Output("toxcsm-placeholder-message", "style")  # Oculta a mensagem inicial
    ],
    [Input("view-toxcsm-results-button", "n_clicks")],
    [State("stored-data", "data")],
    prevent_initial_call=True
)
def render_toxcsm_table(n_clicks, stored_data):
    # Condição: Clique no botão e dados válidos disponíveis
    if n_clicks > 0 and stored_data:
        input_df = pd.DataFrame(stored_data)
        merged_df = merge_input_with_database(input_df)
        final_merged_df = merge_with_toxcsm(merged_df)

        # Se a tabela resultante estiver vazia
        if final_merged_df.empty:
            return (
                html.Div("No matches found with the TOXCSM database.", className="no-data-message"),
                {"display": "none"},  # Oculta o botão
                {"display": "none"}  # Oculta a mensagem inicial
            )

        # Criação da tabela com os dados processados
        hidden_columns = ['ko', 'compoundclass']  # Esconde as colunas definidas
        table = create_table_from_dataframe(final_merged_df, "toxcsm-results-table", hidden_columns=hidden_columns)

        return (
            html.Div(table, className="results-table"),  # Renderiza a tabela
            {"display": "none"},  # Oculta o botão
            {"display": "none"}  # Oculta a mensagem inicial
        )

    # Se não houver dados, previne qualquer atualização
    raise dash.exceptions.PreventUpdate
