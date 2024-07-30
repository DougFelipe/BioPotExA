from dash import html, dcc

def get_pathway_heatmap_layout():
    """
    Constrói o layout para o heatmap de Pathways e compound_pathways.

    Returns:
        Uma `html.Div` contendo o heatmap e os filtros.
    """
    return html.Div([
        html.Div([
            html.Div('Filter by Sample', className='menu-text'),
            dcc.Dropdown(
                id='sample-dropdown-p12',
                multi=False,  # Permite seleção única
                placeholder='Select a Sample'
            )
        ], className='navigation-menu'),
        html.Div(
            dcc.Graph(id='pathway-heatmap'),
            className='graph-container',
            style={'height': 'auto', 'overflowY': 'auto'}
        )
    ], className='graph-card')
