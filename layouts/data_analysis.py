# my_dash_app/layouts/data_analysis.py
from dash import html
import lorem


def get_dataAnalysis_layout():
    return html.Div([
        html.H3('Data Analysis'),
        html.P(lorem.paragraph()),
        # Adicione aqui outros componentes Dash, como dcc.Graph, dcc.Table, etc.
    ], style={'padding': '20px'})
