# my_dash_app/layouts/about.py
from dash import html
import lorem

# Define the layout for the "About" tab
def get_about_layout():
    return html.Div([
        html.H3('About'),
        html.P(lorem.paragraph())
    ], style={'padding': '20px'})
