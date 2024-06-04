# my_dash_app/components/features_list.py

from dash import html

# Lista de características para análise de dados
features_list_1 = [
    "Análise da contabilização do total de genes associados a compostos prioritários",
    "Análise da distribuição do total de genes associados a compostos prioritários",
    "Análise de genes em vias de metabolismo e degradação de xenobióticos no KEGG",
    "Análise do perfil de degradação das amostras por classe de compostos",
    "Análise da relação entre genes e compostos"
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
