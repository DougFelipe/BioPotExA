# my_dash_app/callbacks/callbacks.py
from dash.dependencies import Input, Output
from app import app
from layouts.about import get_about_layout
from layouts.data_analysis import get_dataAnalysis_layout

@app.callback(Output('tabs-content', 'children'),
              [Input('tabs', 'value')])
def render_tab_content(tab):
    if tab == 'tab-about':
        return get_about_layout()
    elif tab == 'tab-data-analysis':
        return get_dataAnalysis_layout()
    # Você pode adicionar mais condições elif para outras abas aqui.
