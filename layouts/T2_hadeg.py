from dash import html
import dash_bootstrap_components as dbc
from components.alerts import hadeg_alert  # Importando o alerta modularizado

def get_hadeg_results_table_layout():
    """
    Cria o layout para a seção da tabela HADEG Results Table.

    Returns:
        html.Div: Layout contendo a mensagem inicial, o botão para renderizar a tabela e o contêiner para exibição da tabela.
    """
    return html.Div([
        # Mensagem inicial
        html.P(
            "Click the button below to view the HADEG Results Table",
            className="placeholder-message",
            id="hadeg-placeholder-message"
        ),

        # Botão para exibir a tabela (estilizado com dbc.Button)
        dbc.Button(
            "View HADEG Results Table",
            id="view-hadeg-results-button",
            color="success",  # Botão estilizado em vermelho (indicando integração com HADEG)
            className="me-1 mt-2",  # Margens para espaçamento
            n_clicks=0
        ),

        # Contêiner para a tabela de resultados (inicialmente vazio)
        html.Div(
            id="hadeg-results-table-container",
            className="table-container",
            style={"marginTop": "20px"}  # Espaçamento superior para organização
        )
    ])
