# my_dash_app/components/components.py

# Importa os componentes HTML e DCC do Dash.
from dash import html, dcc

# Função para criar um card com título e descrição.
def create_card(title, content):
    """
    Cria e retorna um card HTML com um título e uma descrição.

    :param title: O título a ser exibido no card.
    :param content: A descrição ou conteúdo a ser exibido no card.
    :return: Um componente html.Div contendo o título e a descrição.
    """
    return html.Div([
        html.H3(title, className='analysis-title'),  # Título do card com classe CSS personalizada.
        html.P(content, className='analysis-description')  # Descrição do card com classe CSS personalizada.
    ], className='analysis-card')  # Div principal com classe CSS personalizada.
