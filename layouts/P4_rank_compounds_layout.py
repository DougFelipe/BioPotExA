# layouts/P4_rank_compounds_layout.py

from dash import html, dcc
from utils.filters import create_range_slider

def get_rank_compounds_layout():
    """
    Constrói o layout para o gráfico de ranking das amostras com base na interação com compostos.

    Returns:
        Uma `html.Div` contendo o gráfico de ranking e o filtro.
    """
    range_slider = create_range_slider(slider_id='compound-count-range-slider')

    return html.Div([
        html.Div([
            html.Div('Filter by Compound Count Range', className='menu-text'),
            range_slider
        ], className='navigation-menu'),
        html.Div(
            dcc.Graph(id='rank-compounds-scatter-plot'),
            className='graph-container',  # Adiciona classe para estilização
            style={'height': 'auto', 'overflowY': 'auto'}  # Define a altura como auto para permitir ajuste dinâmico
        )
    ], className='graph-card')
