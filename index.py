# my_dash_app/index.py
from dash import Dash
from dash import dcc
from dash import html
from components.header import Header
from layouts.about import get_about_layout
from layouts.data_analysis import get_dataAnalysis_layout

from callbacks.callbacks import render_tab_content

from app import app



app.layout = html.Div(className='main-content', children=[
    Header(),
    dcc.Tabs(id="tabs", value='tab-about', children=[
        dcc.Tab(label='About', value='tab-about', className='tab'),
        dcc.Tab(label='Data Analysis', value='tab-data-analysis', className='tab')
    ], className='main-tabs'),
    html.Div(id='tabs-content', className='tabs-content'),
    dcc.Store(id='stored-data'),
    html.Div(id='output-graphs', style={'display': 'none'})  # Gráficos inicialmente ocultos
])



if __name__ == '__main__':
    app.run_server(debug=True)
