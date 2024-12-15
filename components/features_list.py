# my_dash_app/components/features_list.py

from dash import html

# Lista de características para análise de dados
features_list_1 = [
"Total gene count associated with prioritized compounds",
"Distribution of total genes associated with prioritized compounds",
"Analysis of genes in xenobiotic metabolism and degradation pathways in KEGG",
"Sample degradation profile by compound class",
"Biosurfactant production genes and pathways",
"Plastic degradation genes and pathways",
"Relationship between genes and compounds",
"Relationship between genes and degradation pathways",
"Relationship between compounds and degradation pathways",
"Relationship between compounds and compound classes",
"Relationship between compounds and genes" 
]

# Função para criar cards de lista
def create_list_card(title, features):
    """
    Cria e retorna um card HTML com um título e uma lista de características.

    :param title: Título do card.
    :param features: Lista de características a serem incluídas no card.
    :return: Um componente HTML Div representando o card.
    """
    return html.Div(
        [
            html.H4(title, className='list-title'),
            html.Ul([html.Li(feature) for feature in features], className='list-group')
        ],
        className='list-card'
    )
