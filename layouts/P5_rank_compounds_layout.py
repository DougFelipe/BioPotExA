from dash import html, dcc

def get_rank_compounds_layout():
    """
    Constrói o layout para o gráfico de ranking dos compostos com base no número de amostras atuando neles, incluindo um filtro por classe de composto.

    Returns:
        Uma `html.Div` contendo o gráfico de ranking e o filtro.
    """
    return html.Div([
        html.Div([
            html.Div('Filter by Compound Class', className='menu-text'),
            dcc.Dropdown(
                id='p5-compound-class-dropdown',
                multi=False,  # Permite seleção única
                placeholder='Select a Compound Class'
            )
        ], className='navigation-menu'),
        html.Div(
            id='p5-compound-ranking-container',  # Container dinâmico para a mensagem ou gráfico
            children=[
                html.P(
                    "No data available. Please select a compound class.",
                    id="p5-placeholder-message",
                    style={"textAlign": "center", "color": "gray"}
                )
            ],
            className='graph-container',
            style={'height': 'auto', 'overflowY': 'auto'}
        )
    ], className='graph-card')
