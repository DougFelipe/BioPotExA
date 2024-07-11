from dash import html, dcc

def get_sample_gene_scatter_layout():
    """
    Constrói o layout para o scatter plot da relação entre samples e genes, incluindo um filtro por quantidade de compostos únicos associados.

    Returns:
        Uma `html.Div` contendo o scatter plot e o filtro.
    """
    return html.Div([
        html.Div([
            html.Div('Filter by Number of Compounds Associated', className='menu-text'),
            dcc.Dropdown(
                id='p8-compound-association-dropdown',
                multi=False,  # Permite seleção única
                placeholder='Select a Number of Compounds'
            )
        ], className='navigation-menu'),
        html.Div(
            dcc.Graph(id='p8-sample-gene-scatter-plot'),
            className='graph-container',
            style={'height': 'auto', 'overflowY': 'auto'}
        )
    ], className='graph-card')
