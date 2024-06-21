#my_dash_app/layouts/P5_rank_compounds_layout.py
from dash import html, dcc

def get_rank_compounds_layout():
    """
    Constrói o layout para o gráfico de ranking dos compostos com base no número de amostras atuando neles, incluindo um filtro por classe de composto.

    Returns:
        Uma `html.Div` contendo o gráfico de ranking e o filtro.
    """
    return html.Div([
        html.Div([
            html.Div('Filter by Compound Class', className='menu-text'),
            dcc.Dropdown(
                id='p5-compound-class-dropdown',
                multi=False,  # Permite seleção única
                placeholder='Select a Compound Class'
            )
        ], className='navigation-menu'),
        html.Div(
            dcc.Graph(id='p5-rank-compounds-bar-plot'),
            className='graph-container',
            style={'height': 'auto', 'overflowY': 'auto'}
        )
    ], className='graph-card')
