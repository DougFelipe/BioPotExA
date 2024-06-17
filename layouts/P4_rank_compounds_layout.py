# layouts/P4_rank_compounds_layout.py

from dash import html, dcc
import dash_bootstrap_components as dbc

def get_rank_compounds_layout():
    """
    Constrói o layout para o gráfico de ranking das amostras com base na interação com compostos.

    Returns:
        Uma `html.Div` contendo o gráfico de ranking.
    """
    return html.Div([
        dbc.Card(
            dbc.CardBody([
               # html.H4('Ranking of Samples by Compound Interaction', className='card-title'),
                dcc.Graph(id='rank-compounds-scatter-plot')
            ])
        )
    ])
