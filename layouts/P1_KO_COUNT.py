# my_dash_app/layouts/P1_KO_COUNT.py

from dash import html, dcc
from utils.components import create_card
from utils.filters import create_range_slider

def get_ko_count_bar_chart_layout():
    """
    Constrói o layout para o gráfico de barras da contagem de KO, incluindo filtros.

    Returns:
        Uma `html.Div` contendo o gráfico de barras e os filtros.
    """
    ko_slider = create_range_slider(slider_id='ko-count-range-slider')

    return html.Div([
        #create_card(
        #    title='',
         #   content='Esta seção fornece uma análise detalhada da contagem de KOs.'
        #),  
        html.Div([
            html.Div('Filter by Range', className='menu-text'),
            ko_slider
        ], className='navigation-menu'),
        dcc.Graph(id='ko-count-bar-chart')
    ], className='graph-card')

def get_ko_violin_boxplot_layout():
    """
    Constrói o layout para o gráfico de violino e boxplot da contagem de KO, incluindo filtros.

    Returns:
        Uma `html.Div` contendo o gráfico de violino e boxplot e os filtros.
    """
    ko_violin_filter = dcc.Dropdown(
        id='sample-dropdown',
        multi=True,  # Permite seleções múltiplas
        placeholder='Sample'
    )

    return html.Div([
       # create_card(
        #    title='',
         #   content='Esta seção fornece uma análise detalhada da contagem de KOs.'
        #),
        html.Div([
            'Filter by Sample',
            ko_violin_filter
        ], className='navigation-menu'),
        dcc.Graph(id='ko-violin-boxplot-chart')
    ], className='graph-card')
