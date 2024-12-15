from dash import html, dcc

def get_sample_reference_heatmap_layout():
    """
    Constrói o layout para o heatmap da relação entre samples e referenceAG.

    Returns:
        Uma `html.Div` contendo o heatmap.
    """
    return html.Div([
        html.Div(
            dcc.Graph(id='sample-reference-heatmap'),
            className='graph-container',
            style={'height': 'auto', 'overflowY': 'auto'}
        )
    ], className='graph-card')
