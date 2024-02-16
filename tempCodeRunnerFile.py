app.layout = html.Div(className='main-content', children=[
    html.Header(className='main-header', children=[
        html.H1(children='Biorremediation Potential Explorer & Analyzer', className='main-title'),
        html.A("View on GitHub", href="https://github.com/yourrepo/yourproject", target="_blank",
               className='github-link')
    ]),
    dcc.Tabs(id="tabs", value='tab-about', children=[
        dcc.Tab(label='About', value='tab-about'),
        dcc.Tab(label='Data Analysis', value='tab-data-analysis')
    ], className='main-tabs'),
    html.Div(id='tabs-content', className='tabs-content')
])