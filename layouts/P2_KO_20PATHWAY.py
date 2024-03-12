# my_dash_app/layouts/P2_KO_20PATHWAY.py
from dash import html, dcc
from utils.components import create_card  # Supondo que você tenha uma função auxiliar para criar cards

def get_ko_20pathway_layout():
    return html.Div([
        # Container para o gráfico de análise das vias
        html.Div([
            create_card('KO 20 Pathway Analysis', 'Esta seção fornece uma análise detalhada da interação entre KOs e vias de degradação específicas.'),

            # Dropdown para seleção da amostra
            dcc.Dropdown(
                id='pathway-sample-dropdown',  # O ID aqui deve combinar com o ID usado no callback
                className='dropdown-style'
            ),

            # Gráfico de barras
            dcc.Graph(
                id='pathway-ko-bar-chart',  # O ID aqui deve combinar com o ID usado no callback
                className='bar-chart-style'
            ),
        ], className='graph-card'),
    ], className='tabs-content')