# my_dash_app/layouts/P1_KO_COUNT.py
from dash import html, dcc

def get_ko_count_layout():
    return html.Div([
        html.H3('KO Count Analysis'),
        html.P('Esta seção fornece uma análise detalhada da contagem de KOs.'),
        # Container para a tabela de dados unidos
        html.Div(id='ko-count-table-p1', className='ko-table'),
        # Container para o gráfico de barras da contagem de KO
        dcc.Graph(id='ko-count-bar-chart')
    ], className='tabs-content')
