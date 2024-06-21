# layouts/P4_rank_compounds_layout.py

from dash import html, dcc

def get_rank_compounds_layout():
    """
    Constrói o layout para o gráfico de ranking das amostras com base na interação com compostos.

    Returns:
        Uma `html.Div` contendo o gráfico de ranking.
    """
    return html.Div([
        html.Div(
            dcc.Graph(id='rank-compounds-scatter-plot'),
            className='graph-container',  # Adiciona classe para estilização
            style={'height': 'auto', 'overflowY': 'auto'}  # Define a altura como auto para permitir ajuste dinâmico
        )
    ], className='graph-card')
