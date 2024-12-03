from dash import html, dcc

def get_sample_ko_scatter_layout():
    """
    Constrói o layout para o scatter plot de KOs em samples para a via selecionada.

    Returns:
        Uma `html.Div` contendo o scatter plot e o filtro.
    """
    return html.Div([
        html.Div([
            html.Div('Filter by Pathway', className='menu-text'),  # Título do menu de navegação
            dcc.Dropdown(
                id='pathway-dropdown-p13',  # ID do dropdown para o filtro por pathway
                multi=False,
                placeholder='Select a Pathway'
            )
        ], className='navigation-menu'),
        html.Div(
            dcc.Graph(id='scatter-plot-ko-sample'),  # ID do gráfico scatter plot
            className='graph-container',
            style={'height': 'auto', 'overflowY': 'auto'}
        )
    ], className='graph-card')
