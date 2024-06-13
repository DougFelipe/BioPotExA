# my_dash_app/layouts/P3_compounds_layout.py

from dash import html, dcc
import dash_bootstrap_components as dbc

def get_compound_scatter_layout():
    return html.Div([
        html.Div([
            html.Div('Filter by Compound Class', className='menu-text'),
            dcc.Dropdown(
                id='compound-class-dropdown',
                multi=False,  # Permite seleção única
                placeholder='Select Compound Class'
            ),
        ], className='navigation-menu'),
        dcc.Graph(id='compound-scatter-plot')
    ], className='graph-card')
