from dash import html, dcc

def get_sample_gene_scatter_layout():
    """
    Cria o layout para o scatter plot que relaciona samples e genesymbols para uma via metabólica selecionada.

    Returns:
        html.Div: Componente Div contendo o dropdown e o scatter plot.
    """
    return html.Div([
        html.Div([
            html.Div('Filter by Pathway', className='menu-text'),
            dcc.Dropdown(
                id='via-dropdown-p13',  # ID único para evitar conflitos
                placeholder='Select a Pathway',
                multi=False  # Seleção única
            )
        ], className='navigation-menu'),
        dcc.Graph(
            id='sample-gene-scatter-plot',  # Gráfico de dispersão
            className='scatter-plot-style'
        )
    ], className='graph-card')
