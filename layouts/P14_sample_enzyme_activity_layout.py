from dash import html, dcc

def get_sample_enzyme_activity_layout():
    """
    Constrói o layout para o gráfico de barras da contagem de atividades enzimáticas por amostra.

    Returns:
        Uma `html.Div` contendo o gráfico de barras e o dropdown para seleção de amostras.
    """
    return html.Div([
        html.Div([
            html.Div('Filter by Sample', className='menu-text'),  # Título do dropdown
            dcc.Dropdown(
                id='sample-enzyme-dropdown',  # ID associado ao dropdown
                placeholder="Select a Sample",  # Placeholder para instruir o usuário
            ),
        ], className='navigation-menu'),  # Estilização do menu de navegação
        html.Div(
            id='enzyme-bar-chart-container',  # ID do container do gráfico
            children=[
                html.P(
                    "No data available. Please select a sample.",
                    id="no-enzyme-bar-chart-message",
                    style={"textAlign": "center", "color": "gray"}
                )
            ],
            className='graph-container',  # Classe de estilização do container
        )
    ], className='graph-card')
