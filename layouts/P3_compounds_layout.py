# my_dash_app/layouts/P3_compounds_layout.py

from dash import html, dcc
from utils.components import create_card

def get_compound_scatter_layout():
    """
    Constrói o layout para o gráfico de pontos de compostos, incluindo filtros.

    Returns:
        Uma `html.Div` contendo o gráfico de pontos e os filtros.
    """
    compound_class_filter = dcc.Dropdown(
        id='compound-class-dropdown',
        multi=True,
        placeholder='Select Compound Class'
    )

    return html.Div([
        create_card(
            title='Sample vs Compounds',
            content='This section provides a scatter plot analysis of samples versus compounds from the database.'
        ),
        html.Div([
            'Filter by Compound Class',
            compound_class_filter
        ], className='navigation-menu'),
        dcc.Graph(id='compound-scatter-plot')
    ], className='graph-card')
