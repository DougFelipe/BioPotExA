from dash import html, dcc

def get_sample_groups_layout():
    """
    Constrói o layout para o scatter plot dos grupos de samples.

    Returns:
        Uma `html.Div` contendo o scatter plot e o filtro.
    """
    return html.Div([
        html.Div([
            html.Div('Filter by Compound Class', className='menu-text'),
            dcc.Dropdown(
                id='compound-class-dropdown-p10',
                multi=False,  # Permite seleção única
                placeholder='Select a Compound Class'
            )
        ], className='navigation-menu'),
        html.Div(
            dcc.Graph(id='sample-groups-plot'),
            className='graph-container',
            style={'height': 'auto', 'overflowY': 'auto'}
        )
    ], className='graph-card')
