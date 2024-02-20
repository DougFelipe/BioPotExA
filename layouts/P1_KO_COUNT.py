# my_dash_app/layouts/P1_KO_COUNT.py
from dash import html, dcc
from utils.components import create_card

def get_ko_count_layout():
    return html.Div([
        create_card('Gene Count and Distribution', 'Esta seção fornece uma análise detalhada da contagem de KOs.'),

        # Container para a tabela de dados unidos
        html.Div(id='ko-count-table-p1', className='ko-table'),

        # Container para o card do gráfico de barras da contagem de KO com menu de navegação
        html.Div([
            html.Div('Teste de menu de navegação', className='navigation-menu'),  # Adicionado menu de navegação
            dcc.Graph(id='ko-count-bar-chart')
        ], className='graph-card'),

        create_card('Gene Count and Distribution', 'Esta seção fornece uma análise detalhada da contagem de KOs.'),
        
        # Container para o card do gráfico de violino e boxplot
        html.Div([
            html.Div('Teste de menu de navegação', className='navigation-menu'),  # Adicionado menu de navegação
            dcc.Graph(id='ko-violin-boxplot-chart')
        ], className='graph-card'),

    ], className='tabs-content')
