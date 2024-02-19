# my_dash_app/layouts/P2_KO_20PATHWAY.py
from dash import html, dcc
from utils.components import create_card  # Supondo que você tenha uma função auxiliar para criar cards

def get_ko_20pathway_layout():
    return html.Div([
        create_card('KO 20 Pathway Analysis', 'Esta seção fornece uma análise detalhada da interação entre KOs e vias de degradação específicas.'),
        html.Div(id='output-merge-table'),  # Local para exibir a tabela resultante do merge
        # Outros componentes conforme necessário
    ], className='tabs-content')
