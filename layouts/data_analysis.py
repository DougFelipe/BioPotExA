# my_dash_app/layouts/data_analysis.py
from dash import html
import lorem

def get_dataAnalysis_page():
    # Esta função cria um único bloco de conteúdo estilizado como uma página A4
    return html.Div([
        html.H3('Data Analysis'),
        html.P(lorem.paragraph()),
        # Adicione aqui outros componentes Dash, como dcc.Graph, dcc.Table, etc.
    ], className='tabs-content')

def get_dataAnalysis_layout():
    # Esta função compila três blocos de conteúdo de página A4
    return html.Div([
        get_dataAnalysis_page(),
        get_dataAnalysis_page()
    ])
