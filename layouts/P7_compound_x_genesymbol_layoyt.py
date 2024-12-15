from dash import html, dcc

def get_gene_compound_scatter_layout():
    """
    Constrói o layout para o scatter plot da relação entre genes e compostos,
    exibindo uma mensagem inicial até que os filtros sejam aplicados.

    Returns:
        Uma `html.Div` contendo os filtros e a área do gráfico.
    """
    return html.Div([
        html.Div([
            html.Div('Filter by Compound Name', className='menu-text'),
            dcc.Dropdown(
                id='p7-compound-dropdown',
                multi=True,  # Permite multiseleção
                placeholder='Select Compound(s)'
            ),
            html.Div('Filter by Gene Symbol', className='menu-text'),
            dcc.Dropdown(
                id='p7-gene-dropdown',
                multi=True,  # Permite multiseleção
                placeholder='Select Gene(s)'
            )
        ], className='navigation-menu'),
        html.Div(
            id='p7-gene-compound-scatter-container',  # Container para o gráfico ou mensagem inicial
            className='graph-container',
            style={'height': 'auto', 'overflowY': 'auto'},
            children=html.P(  # Mensagem inicial
                "Select compound or gene to view results",
                style={'textAlign': 'center', 'color': 'gray', 'fontSize': '16px'}
            )
        )
    ], className='graph-card')
