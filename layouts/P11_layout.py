from dash import html, dcc

def get_gene_sample_heatmap_layout():
    """
    Constrói o layout para o heatmap de genes e samples com mensagens dinâmicas e renderização condicional.

    Returns:
        Uma `html.Div` contendo o heatmap e os filtros.
    """
    return html.Div([
        html.Div([
            html.Div('Filter by Compound Pathway', className='menu-text'),
            dcc.Dropdown(
                id='compound-pathway-dropdown-p11',
                multi=False,  # Permite seleção única
                placeholder='Select a Compound Pathway'
            ),
            html.Div('Filter by Pathway', className='menu-text'),
            dcc.Dropdown(
                id='pathway-dropdown-p11',
                multi=False,  # Permite seleção única
                placeholder='Select a Pathway'
            )
        ], className='navigation-menu'),
        html.Div(
            id='gene-sample-heatmap-container',
            children=[
                html.P(
                    "No data available. Please select a compound pathway and pathway.",
                    id="no-gene-sample-heatmap-message",
                    style={"textAlign": "center", "color": "gray"}
                )
            ],
            className='graph-container',
            style={'height': 'auto', 'overflowY': 'auto'}
        )
    ], className='graph-card')
