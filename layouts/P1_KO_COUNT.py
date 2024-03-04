# my_dash_app/layouts/P1_KO_COUNT.py

from dash import html, dcc
from utils.components import create_card
from utils.filters import create_range_slider

def get_ko_count_layout():
    """
    Constrói o layout para a seção de contagem de KO, incluindo gráficos e um slider de filtragem.

    Esta função cria o layout da página para a contagem de KO, que inclui:
    - Um cartão com uma introdução à análise de contagem de KO.
    - Um slider para filtrar os dados exibidos nos gráficos.
    - Um gráfico de barras mostrando a contagem de KO por amostra.
    - Um gráfico de violino e boxplot para a distribuição da contagem de KO.

    Returns:
        Uma `html.Div` contendo todos os componentes do layout.
    """

    # Criação do RangeSlider usando a função auxiliar modularizada
    koSlider = create_range_slider(slider_id='ko-count-range-slider')

    # Construção do layout
    return html.Div([
        # Introdução à análise de contagem de KO
        create_card(
            title='Gene Count and Distribution',
            content='Esta seção fornece uma análise detalhada da contagem de KOs.'
        ),

        # Container para o gráfico de barras da contagem de KO e o menu de navegação
        html.Div([
            # Menu de navegação incluindo o RangeSlider para filtragem de dados
            html.Div([
                html.Div('Filters Options', className='menu-text'),  # Texto do menu de navegação
                koSlider  # Inclusão do RangeSlider no menu de navegação
            ], className='navigation-menu'),  # Estilização do menu de navegação
            
            # Gráfico de barras da contagem de KO
            dcc.Graph(id='ko-count-bar-chart')
        ], className='graph-card'),  # Estilização do card do gráfico de barras

        # Repetição do cartão de introdução (pode ser removido ou substituído conforme necessário)
        create_card(
            title='Gene Count and Distribution',
            content='Esta seção fornece uma análise detalhada da contagem de KOs.'
        ),

        # Container para o gráfico de violino e boxplot
        html.Div([
            html.Div('Teste de menu de navegação', className='navigation-menu'),  # Texto do menu de navegação (pode ser ajustado)
            dcc.Graph(id='ko-violin-boxplot-chart')  # Gráfico de violino e boxplot
        ], className='graph-card'),  # Estilização do card do gráfico de violino e boxplot

    ], className='tabs-content')  # Estilização do conteúdo da aba
