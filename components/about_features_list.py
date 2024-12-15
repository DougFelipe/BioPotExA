# my_dash_app/components/about_features_list.py

from dash import html

# Lista de características da página About
about_features_list = [
    html.Li([html.Strong("11 Compounds Lists"), html.Br(), "by 11 environmental regulatory agencies"]),
    html.Li([html.Strong("253 Priority Compounds"), html.Br(), "reported by regulatory agencies"]),
    html.Li([html.Strong("12 Classes of Compounds"), html.Br(), "reported as environmental contaminants"]),
    html.Li([html.Strong("20 KEGG Pathways"), html.Br(), "for xenobiotic biodegradation "]),
    html.Li([html.Strong("75 Pathways"), html.Br(), "related to biodegradation "]),
    html.Li([html.Strong("457 genes"), html.Br(), "involved in biodegradation "]),
    html.Li([html.Strong("411 Enzymes"), html.Br(), "associated with priority compounds "]),
    html.Li([html.Strong("69 Enzymatic Activity"), html.Br(), "promoting biodegradation "]),
    html.Li([html.Strong("35 genes"), html.Br(), "involved in biosurfactant production "]),
    html.Li([html.Strong("12 pathways"), html.Br(), "involved in biosurfactant production "]),


   
]


# Função para criar a lista de características
def create_about_features_list():
    return html.Div(
        className='scrollable-list-container',
        children=[
            html.Ol(
                className='gradient-list',
                children=[html.Li(feature) for feature in about_features_list]
            )
        ]
    )