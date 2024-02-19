# my_dash_app/components/components.py
from dash import html,dcc

##MODULAZIRA A CRIAÇÃO DE TITULOS E DESCRIÇÃO DOS RESULTADOS
def create_card(title, content):
    return html.Div([
        html.H3(title, className='analysis-title'),
        html.P(content, className='analysis-description')
    ], className='analysis-card')
