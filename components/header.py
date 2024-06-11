# components/header.py
from dash import dcc, html

def Header():
    return html.Header(className='main-header', children=[
        html.Div(className='header-left', children=[
            html.A('BioPExA', href='/about', className='main-title')
        ]),
        html.Div(className='header-right', children=[
            html.A('BioPExa Features', href='/features', className='header-link'),
            html.A('Bioremediation', href='/bioremediation', className='header-link'),
            html.A('Regulatory Agencies', href='/regulatory', className='header-link'),
            html.A('Changelog', href='/changelog', className='header-link'),
            html.A('Contact', href='/contact', className='header-link')
        ])
    ])
