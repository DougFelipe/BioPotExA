# components/header.py
from dash import dcc
from dash import html

def Header():
    return html.Header(className='main-header', children=[
        html.H1(children='Biorremediation Potential Explorer & Analyzer BioPotExA', className='main-title'),
        html.A("View on GitHub", href="https://github.com/yourrepo/yourproject", target="_blank",
               className='github-link')
    ])
