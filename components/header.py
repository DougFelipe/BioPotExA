# components/header.py
from dash import dcc, html

def Header():
    return html.Header(className='main-header', children=[
        html.H1(children='Biorremediation Potential Explorer & Analyzer BioPotExA', className='main-title')
    ])
