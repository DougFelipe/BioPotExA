# layouts/P3_compounds_layout.py

from dash import html, dcc

def get_compound_scatter_layout():
    """
    Constrói o layout para o gráfico de dispersão dos compostos, incluindo um filtro por classe de composto.

    Returns:
        Uma `html.Div` contendo o gráfico de dispersão e o filtro.
    """
    return html.Div([
        html.Div([
            html.Div('Filter by Compound Class', className='menu-text'),
            dcc.Dropdown(
                id='compound-class-dropdown',
                multi=False,  # Permite seleção única
                placeholder='Select a Compound Class'
            )
        ], className='navigation-menu'),
        html.Div(
            dcc.Graph(id='compound-scatter-plot'),
            className='graph-container',  # Adiciona classe para estilização
            style={'height': 'auto', 'overflowY': 'auto'}  # Define a altura como auto para permitir ajuste dinâmico
        )
    ], className='graph-card')
