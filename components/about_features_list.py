# my_dash_app/components/about_features_list.py

from dash import html

# Lista de características da página About
about_features_list = [
    html.Li([html.Strong("Identificação"), html.Br(), " do potencial biotecnológico para biorremediação"]),
    html.Li("Análise de dados de anotação funcional de genomas de bactérias, fungos e plantas"),
    html.Li("Caracterização de organismos com potencial para degradação de poluentes"),
    html.Li("Integração de dados sobre poluentes prioritários de agências reguladoras, PubChem e KEGG"),
    html.Li("Análise de dados de anotação funcional de genomas de bactérias, fungos e plantas"),
    html.Li("Caracterização de organismos com potencial para degradação de poluentes"),
    html.Li("Integração de dados sobre poluentes prioritários de agências reguladoras, PubChem e KEGG"),
    html.Li("Análise de dados de anotação funcional de genomas de bactérias, fungos e plantas"),
    html.Li("Caracterização de organismos com potencial para degradação de poluentes"),
    html.Li("Integração de dados sobre poluentes prioritários de agências reguladoras, PubChem e KEGG"),
]


# Função para criar a lista estilizada
def create_about_features_list(features):
    return html.Div(
        html.Ol(
            [html.Li(feature) for feature in features],
            className='gradient-list'
        ),
        className='scrollable-list-container'
    )
