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
                placeholder='Select a Pathway',  # Mensagem de placeholder
                style={'margin-bottom': '20px'}  # Espaçamento inferior
            )
        ], className='navigation-menu'),
        html.Div(
            id='scatter-plot-container',  # Container para mensagens ou o gráfico
            children=[
                html.P(
                    "No data available. Please select a pathway.",  # Mensagem padrão
                    id="no-data-message-p13",
                    style={"textAlign": "center", "color": "gray"}
                )
            ],
            className='graph-container',
            style={'height': 'auto', 'overflowY': 'auto'}
        )
    ], className='graph-card')
