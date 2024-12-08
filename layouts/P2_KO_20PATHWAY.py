from dash import html, dcc

def get_pathway_ko_bar_chart_layout():
    """
    Constrói o layout para o gráfico de barras da análise das vias KO, incluindo filtros.
    """
    return html.Div([
        html.Div([
            html.Div('Filter by Sample', className='menu-text'),
            dcc.Dropdown(
                id='pathway-sample-dropdown',
                placeholder="Selecione uma amostra",  # Texto de instrução
                style={"margin-bottom": "20px"}  # Espaçamento inferior
            ),
        ], className='navigation-menu'),
        html.Div(
            id='pathway-ko-chart-container',  # Container do gráfico
            children=[
                html.P(
                    "Nenhum gráfico disponível. Por favor, selecione uma amostra.",
                    id="no-pathway-ko-chart-message",
                    style={"textAlign": "center", "color": "gray"}
                )
            ],
            className='graph-card'
        )
    ])

def get_sample_ko_pathway_bar_chart_layout():
    """
    Constrói o layout para o gráfico de barras da análise dos KOs em samples para a via selecionada.
    """
    return html.Div([
        html.Div([
            html.Div('Filter by Pathway', className='menu-text'),
            dcc.Dropdown(
                id='via-dropdown',
                placeholder="Selecione uma via",  # Texto de instrução
                style={"margin-bottom": "20px"}  # Espaçamento inferior
            ),
        ], className='navigation-menu'),
        html.Div(
            id='via-ko-chart-container',  # Container do gráfico
            children=[
                html.P(
                    "Nenhum gráfico disponível. Por favor, selecione uma via.",
                    id="no-via-ko-chart-message",
                    style={"textAlign": "center", "color": "gray"}
                )
            ],
            className='graph-card'
        )
    ])
