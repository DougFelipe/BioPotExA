# my_dash_app/layouts/P1_KO_COUNT.py
from dash import html
import lorem

def get_ko_count_layout():
    # Esta função cria um layout de conteúdo estilizado como uma página A4
    return html.Div([
        html.H3('KO Count Analysis'),
        html.P(lorem.paragraph()),
        # O container onde a tabela de contagem de KO será exibida
       
        html.Div(id='ko-count-output')
    ], className='tabs-content')


