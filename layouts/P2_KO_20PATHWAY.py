# my_dash_app/layouts/P2_KO_20PATHWAY.py
from dash import html, dcc
from utils.components import create_card  # Supondo que você tenha uma função auxiliar para criar cards

def get_ko_20pathway_layout():
    return html.Div([
        # Container para o gráfico de análise das vias
        html.Div([
            create_card('KO 202 Pathway Analysis', 'Esta seção fornece uma análise detalhada da interação entre KOs e vias de degradação específicas.'),
            html.Div([
                html.Div('Select Sample', className='menu-text'),  # Título do menu de navegação
                dcc.Dropdown(
                    id='pathway-sample-dropdown',  # O ID deve combinar com o ID usado no callback
                ),
            ], className='navigation-menu'),  # Estilização do menu de navegação
            # Gráfico de barras
            dcc.Graph(
                id='pathway-ko-bar-chart',  # O ID aqui deve combinar com o ID usado no callback
                className='bar-chart-style'
            ),
        ], className='graph-card'),
        
        html.Div([
            create_card('Sample KO Pathway Analysis', 'Esta seção fornece uma análise detalhada dos KOs em samples para a via selecionada.'),
            html.Div([
                html.Div('Select Sample', className='menu-text'),  # Título do menu de navegação
                dcc.Dropdown(
                    id='via-dropdown',  # O ID deve combinar com o ID usado no callback
                ),
            ], className='navigation-menu'),  # Estilização do menu de navegação
            dcc.Graph(
                id='via-ko-bar-chart',  # Novo ID para o gráfico de barras das samples
                className='bar-chart-style'
            ),
        ], className='graph-card'),
    ], className='pages-content')
