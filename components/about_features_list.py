# my_dash_app/components/about_features_list.py

from dash import html

# Lista de características da página About
about_features_list = [
    html.Li([html.Strong("List of Compounds Compiled"), html.Br(), "by 11 environmental regulatory agencies"]),
    html.Li([html.Strong("253 Priority Compounds"), html.Br(), "reported by regulatory agencies"]),
    html.Li([html.Strong("12 Classes of Compounds"), html.Br(), "reported as environmental contaminants"]),
    html.Li([html.Strong("20 KEGG Pathways"), html.Br(), "for xenobiotic biodegradation "]),
    html.Li([html.Strong("75 Pathways"), html.Br(), "related to biodegradation "]),
    html.Li([html.Strong("367 Enzymes"), html.Br(), "involved in biodegradation "]),

   
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