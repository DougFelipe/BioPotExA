from dash import html, dcc

def get_pathway_heatmap_layout():
    """
    Constrói o layout para o heatmap de Pathways e compound_pathways com mensagem inicial de placeholder.

    Returns:
        Uma `html.Div` contendo o heatmap e os filtros.
    """
    return html.Div([
        html.Div([
            html.Div('Filter by Sample', className='menu-text'),
            dcc.Dropdown(
                id='sample-dropdown-p12',
                multi=False,
                placeholder='Select a Sample'  # Placeholder para guiar o usuário
            )
        ], className='navigation-menu'),
        html.Div(
            id='pathway-heatmap-container',
            children=[
                html.P(
                    "No data available. Please select a sample.",
                    id="placeholder-pathway-heatmap",
                    style={"textAlign": "center", "color": "gray"}
                )
            ],
            className='graph-container',
            style={'height': 'auto', 'overflowY': 'auto'}
        )
    ], className='graph-card')
