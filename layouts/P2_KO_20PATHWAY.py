# my_dash_app/layouts/P2_KO_20PATHWAY.py
from dash import html, dcc
from utils.components import create_card

def get_pathway_ko_bar_chart_layout():
    """
    Constrói o layout para o gráfico de barras da análise das vias KO, incluindo filtros.

    Returns:
        Uma `html.Div` contendo o gráfico de barras e os filtros.
    """
    return html.Div([
       # create_card('', 'Esta seção fornece uma análise detalhada da interação entre KOs e vias de degradação específicas.'),
        html.Div([
            html.Div('Filter by Sample', className='menu-text'),  # Título do menu de navegação
            dcc.Dropdown(
                id='pathway-sample-dropdown',  # O ID deve combinar com o ID usado no callback
            ),
        ], className='navigation-menu'),  # Estilização do menu de navegação
        dcc.Graph(
            id='pathway-ko-bar-chart',  # O ID aqui deve combinar com o ID usado no callback
            className='bar-chart-style'
        ),
    ], className='graph-card')

def get_sample_ko_pathway_bar_chart_layout():
    """
    Constrói o layout para o gráfico de barras da análise dos KOs em samples para a via selecionada, incluindo filtros.

    Returns:
        Uma `html.Div` contendo o gráfico de barras e os filtros.
    """
    return html.Div([
        #create_card('', content =  'Esta seção fornece uma análise detalhada dos KOs em samples para a via selecionada.'),
        html.Div([
            html.Div('Filter by Sample', className='menu-text'),  # Título do menu de navegação
            dcc.Dropdown(
                id='via-dropdown',  # O ID deve combinar com o ID usado no callback
            ),
        ], className='navigation-menu'),  # Estilização do menu de navegação
        dcc.Graph(
            id='via-ko-bar-chart',  # Novo ID para o gráfico de barras das samples
            className='bar-chart-style'
        ),
    ], className='graph-card')
