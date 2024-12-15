from dash import html, dcc

def get_sample_gene_scatter_layout():
    """
    Constrói o layout para o scatter plot da relação entre samples e genes, incluindo filtros para ambos.

    Returns:
        Uma `html.Div` contendo os dropdowns e o scatter plot.
    """
    return html.Div([
        html.Div([
            html.Div('Filter by Sample', className='menu-text'),
            dcc.Dropdown(
                id='p8-sample-dropdown',
                multi=True,  # Permite múltiplas seleções
                placeholder='Select samples'
            ),
            html.Div('Filter by Gene', className='menu-text', style={'margin-top': '20px'}),
            dcc.Dropdown(
                id='p8-gene-dropdown',
                multi=True,  # Permite múltiplas seleções
                placeholder='Select genes'
            )
        ], className='navigation-menu'),
        html.Div(
            id='p8-sample-gene-scatter-container',  # Container para exibir gráfico ou mensagens
            children=html.P(
                "Select sample or gene to view results",
                style={'textAlign': 'center', 'color': 'gray', 'fontSize': '16px'}
            ),
            className='graph-container',
            style={'height': 'auto', 'overflowY': 'auto'}
        )
    ], className='graph-card')
