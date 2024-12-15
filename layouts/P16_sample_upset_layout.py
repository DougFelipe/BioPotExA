# my_dash_app/layouts/P16_sample_upset_layout.py
from dash import html, dcc

def get_sample_upset_layout():
    """
    Constrói o layout para o gráfico UpSet Plot das amostras e identificadores KO.

    Returns:
        Uma `html.Div` contendo o dropdown multi-seleção e o gráfico UpSet.
    """
    return html.Div([
        html.Div([
            html.Div('Select Samples', className='menu-text'),
            dcc.Dropdown(
                id='upsetplot-sample-dropdown',
                multi=True,
                placeholder="Selecione as amostras",  # Texto de instrução no dropdown
                style={"margin-bottom": "20px"}
            )
        ], className='navigation-menu'),
        html.Div(
            id='upset-plot-container',
            children=[
                html.P(
                    "Nenhum gráfico disponível. Por favor, selecione as amostras.",
                    id="no-upset-plot-message",
                    style={"textAlign": "center", "color": "gray"}
                )
            ],
            className='graph-card'
        )
    ])
