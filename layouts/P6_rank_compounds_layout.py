from dash import html, dcc

def get_rank_compounds_gene_layout():
    """
    Constrói o layout para o gráfico de ranking dos compostos com base no número de genes únicos atuantes,
    incluindo um filtro por classe de composto.

    Returns:
        Uma `html.Div` contendo o gráfico de ranking e o filtro.
    """
    return html.Div([
        html.Div([
            html.Div('Filter by Compound Class', className='menu-text'),
            dcc.Dropdown(
                id='p6-compound-class-dropdown',
                multi=False,  # Permite seleção única
                placeholder='Select a Compound Class',
                style={"margin-bottom": "20px"}  # Adiciona espaçamento inferior
            )
        ], className='navigation-menu'),
        html.Div(
            id='p6-compound-ranking-container',  # Container dinâmico para gráfico ou mensagem
            children=[
                html.P(
                    "No data available. Please select a compound class.",
                    id="p6-placeholder-message",
                    style={"textAlign": "center", "color": "gray", "marginTop": "20px"}
                )
            ],
            className='graph-container',
            style={'height': 'auto', 'overflowY': 'auto'}
        )
    ], className='graph-card')
