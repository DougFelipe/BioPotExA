from dash import html, dcc

def get_pathway_ko_bar_chart_layout():
    """
    Constructs the layout for the KO pathway analysis bar chart, including filters.
    """
    return html.Div([
        html.Div([
            html.Div('Filter by Sample', className='menu-text'),
            dcc.Dropdown(
                id='pathway-sample-dropdown',
                placeholder="Select a sample",  # Instructional text
                style={"margin-bottom": "20px"}  # Bottom spacing
            ),
        ], className='navigation-menu'),
        html.Div(
            id='pathway-ko-chart-container',  # Chart container
            children=[
                html.P(
                    "No chart available. Please select a sample.",
                    id="no-pathway-ko-chart-message",
                    style={"textAlign": "center", "color": "gray"}
                )
            ],
            className='graph-card'
        )
    ])

def get_sample_ko_pathway_bar_chart_layout():
    """
    Constructs the layout for the bar chart analyzing KOs in samples for the selected pathway.
    """
    return html.Div([
        html.Div([
            html.Div('Filter by Pathway', className='menu-text'),
            dcc.Dropdown(
                id='via-dropdown',
                placeholder="Select a pathway",  # Instructional text
                style={"margin-bottom": "20px"}  # Bottom spacing
            ),
        ], className='navigation-menu'),
        html.Div(
            id='via-ko-chart-container',  # Chart container
            children=[
                html.P(
                    "No chart available. Please select a pathway.",
                    id="no-via-ko-chart-message",
                    style={"textAlign": "center", "color": "gray"}
                )
            ],
            className='graph-card'
        )
    ])
