from dash import html, dcc

def get_pathway_heatmap_layout():
    """
    Constrói o layout para o heatmap de Pathway vs Compound Pathway, incluindo filtros.

    Returns:
        Uma `html.Div` contendo o heatmap e os filtros.
    """
    return html.Div([
        html.Div([
            html.Div('Filter by Sample', className='menu-text'),
            dcc.Dropdown(
                id='sample-dropdown',
                multi=False,
                placeholder='Select a Sample'
            )
        ], className='navigation-menu'),
        dcc.Graph(id='pathway-heatmap', className='heatmap-style')
    ], className='graph-card')
