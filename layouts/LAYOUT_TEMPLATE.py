# my_dash_app/layouts/LAYOUT_TEMPLATE.py
from dash import html, dcc
from utils.components import create_card  # Supondo que você tenha uma função auxiliar para criar cards

def get_ko_20pathway_layout():
    return html.Div([
        html.Div(id='output-merge-table'),  # Local para exibir a tabela resultante do merge
        # Container para o gráfico análise das vias
        html.Div([
            create_card('KO 20 Pathway Analysis', 'Esta seção fornece uma análise detalhada da interação entre KOs e vias de degradação específicas.'),

            html.Div([
                'Filtros:',  # Texto explicativo para o dropdown
                  # Inserir o dropdown aqui
            ], className='navigation-menu'),
            # inserir o gráfico aqui
        ], className='graph-card'),

    ], className='tabs-content')
