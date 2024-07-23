from dash import html, dcc

def get_gene_sample_heatmap_layout():
    """
    Constrói o layout para o heatmap de genes e samples.

    Returns:
        Uma `html.Div` contendo o heatmap e os filtros.
    """
    return html.Div([
        html.Div([
            html.Div('Filter by Compound Pathway', className='menu-text'),
            dcc.Dropdown(
                id='compound-pathway-dropdown-p11',
                multi=False,  # Permite seleção única
                placeholder='Select a Compound Pathway'
            ),
            html.Div('Filter by Pathway', className='menu-text'),
            dcc.Dropdown(
                id='pathway-dropdown-p11',
                multi=False,  # Permite seleção única
                placeholder='Select a Pathway'
            )
        ], className='navigation-menu'),
        html.Div(
            dcc.Graph(id='gene-sample-heatmap'),
            className='graph-container',
            style={'height': 'auto', 'overflowY': 'auto'}
        )
    ], className='graph-card')
