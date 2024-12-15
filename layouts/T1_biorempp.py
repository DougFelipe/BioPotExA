from dash import html
import dash_bootstrap_components as dbc

def get_biorempp_results_table_layout():
    """
    Cria o layout para a seção da tabela BioRemPP Results Table.

    Returns:
        html.Div: Layout contendo a mensagem inicial, o botão para renderizar a tabela e o contêiner para exibição da tabela.
    """
    return html.Div([
        # Mensagem inicial
        html.P(
            "Click the button below to view the BioRemPP Results Table",
            className="placeholder-message",
            id="biorempp-placeholder-message"
        ),

        # Botão para exibir a tabela (estilizado com dbc.Button)
        dbc.Button(
            "View BioRemPP Results Table",
            id="view-biorempp-results-button",
            color="success",  # Define a cor do botão como verde
            className="me-1 mt-2",  # Margens para espaçamento
            n_clicks=0
        ),

        # Contêiner para a tabela de resultados (inicialmente vazio)
        html.Div(
            id="biorempp-results-table-container",
            className="table-container",
            style={"marginTop": "20px"}  # Espaçamento superior para organização
        )
    ])
