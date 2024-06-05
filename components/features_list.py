# my_dash_app/components/features_list.py

from dash import html

# Lista de características para análise de dados
features_list_1 = [
"Analysis of the total gene count associated with prioritized compounds",
"Analysis of the distribution of total genes associated with prioritized compounds",
"Analysis of genes in xenobiotic metabolism and degradation pathways in KEGG",
"Analysis of sample degradation profile by compound class",
"Analysis of the relationship between genes and compounds",
"Analysis of the relationship between genes and degradation pathways",
"Analysis of the relationship between compounds and degradation pathways",
"Analysis of the relationship between compounds and compound classes",
"Analysis of the relationship between compounds and genes" 
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
