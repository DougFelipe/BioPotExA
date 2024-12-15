# my_dash_app/layouts/P15_sample_clustering_layout.py
from dash import html, dcc

def get_sample_clustering_layout():
    """
    Constrói o layout para o dendrograma das amostras com opções de distância e agrupamento.

    Returns:
        Uma `html.Div` contendo os dropdowns e o gráfico do dendrograma.
    """
    return html.Div([
        html.Div([
            html.Div('Select Distance Metric', className='menu-text'),
            dcc.Dropdown(
                id='clustering-distance-dropdown',
                options=[
                    {'label': 'Euclidean', 'value': 'euclidean'},
                    {'label': 'Manhattan', 'value': 'cityblock'},
                    {'label': 'Cosine', 'value': 'cosine'}
                ],
                value=None,  # Começa vazio
                placeholder='Select a distance metric',  # Texto do placeholder
            ),
        ], className='navigation-menu'),
        html.Div([
            html.Div('Select Clustering Method', className='menu-text'),
            dcc.Dropdown(
                id='clustering-method-dropdown',
                options=[
                    {'label': 'Single Linkage', 'value': 'single'},
                    {'label': 'Complete Linkage', 'value': 'complete'},
                    {'label': 'Average Linkage', 'value': 'average'},
                    {'label': 'Ward', 'value': 'ward'}
                ],
                value=None,  # Começa vazio
                placeholder='Select a clustering method',  # Texto do placeholder
            ),
        ], className='navigation-menu'),
        html.Div(
            id='sample-clustering-graph-container',
            children=[],
            className='graph-card'
        ),
    ])
