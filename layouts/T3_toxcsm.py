from dash import html
import dash_bootstrap_components as dbc
from components.alerts import toxcsm_alert  # Importando o alerta modularizado

def get_toxcsm_results_table_layout():
    """
    Cria o layout para a seção da tabela ToxCSM Results Table.

    Returns:
        html.Div: Layout contendo a mensagem inicial, o botão para renderizar a tabela e o contêiner para exibição da tabela.
    """
    return html.Div([
        # Mensagem inicial
        html.P(
            "Click the button below to view the ToxCSM Results Table",
            className="placeholder-message",
            id="toxcsm-placeholder-message"
        ),

        # Botão para exibir a tabela (estilizado com dbc.Button)
        dbc.Button(
            "View ToxCSM Results Table",
            id="view-toxcsm-results-button",
            color="success",  # Botão estilizado em vermelho para manter consistência
            className="me-1 mt-2",  # Margens para espaçamento
            n_clicks=0
        ),
        # Contêiner para a tabela de resultados (inicialmente vazio)
        html.Div(
            id="toxcsm-results-table-container",
            className="table-container",
            style={"marginTop": "20px"}  # Espaçamento superior para organização
        )
    ])
