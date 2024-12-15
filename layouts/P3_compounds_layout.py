from dash import html, dcc

def get_compound_scatter_layout():
    """
    Constrói o layout para o gráfico de dispersão dos compostos, incluindo um filtro por classe de composto.

    Returns:
        Uma `html.Div` contendo o dropdown e o espaço para o gráfico de dispersão.
    """
    return html.Div([
        html.Div([
            html.Div('Filter by Compound Class', className='menu-text'),
            dcc.Dropdown(
                id='compound-class-dropdown',
                multi=False,  # Permite seleção única
                placeholder='Select a Compound Class',  # Placeholder no dropdown
                style={"marginBottom": "20px"}  # Espaçamento abaixo do dropdown
            )
        ], className='navigation-menu'),
        html.Div(
            id='compound-scatter-container',  # Container dinâmico para o gráfico ou mensagem
            children=[
                html.P(
                    "No graph available. Please select a compound class.",
                    style={"textAlign": "center", "color": "gray", "fontSize": "16px", "marginTop": "20px"}
                )
            ],
            className='graph-container',  # Classe para estilização
            style={"height": "auto", "overflowY": "auto"}  # Ajuste dinâmico de altura
        )
    ], className='graph-card')
