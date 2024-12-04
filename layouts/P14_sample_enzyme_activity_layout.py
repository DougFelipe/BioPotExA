# my_dash_app/layouts/P14_sample_enzyme_activity_layout.py
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
            ),
        ], className='navigation-menu'),  # Estilização do menu de navegação
        dcc.Graph(
            id='sample-enzyme-bar-chart',  # ID do gráfico de barras
            className='bar-chart-style'
        ),
    ], className='graph-card')
