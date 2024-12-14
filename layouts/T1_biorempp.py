from dash import html, dcc

def get_biorempp_results_table_layout():
    """
    Cria o layout para a seção da tabela BioRemPP Results Table.

    Returns:
        html.Div: Layout contendo a mensagem inicial, o botão para renderizar a tabela e o contêiner para exibição da tabela.
    """
    return html.Div([
        # Mensagem inicial
        html.P(
            "Click the button below to view the BioRemPP Results Table.",
            className="placeholder-message",
            id="biorempp-placeholder-message"
        ),

        # Botão para exibir a tabela
        html.Button(
            "View BioRemPP Results Table",
            id="view-biorempp-results-button",
            n_clicks=0,
            className="view-results-button"
        ),

        # Contêiner para a tabela de resultados (inicialmente vazio)
        html.Div(
            id="biorempp-results-table-container",
            className="table-container",
            style={"marginTop": "20px"}  # Espaçamento superior para organização
        )
    ])
