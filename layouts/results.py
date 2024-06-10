# my_dash_app/layouts/results.py
import dash_bootstrap_components as dbc
from dash import dcc, html
from layouts.P1_KO_COUNT import get_ko_count_layout
from layouts.P2_KO_20PATHWAY import get_ko_20pathway_layout

def get_results_layout():
    """
    Cria e retorna um layout para a página de Resultados.
    
    Esta função cria um bloco de conteúdo estilizado como uma página A4, incluindo
    um título, subtítulo e um container para o accordion com os gráficos.
    """
    return html.Div([
        html.H2('Resultados da Análise de Dados', className='results-title'),
        html.H3('Aqui estão os resultados das suas análises.', className='results-subtitle'),
        dcc.Accordion([
            dcc.AccordionItem(
                title='Gráfico de Contagem KO',
                children=get_ko_count_layout(),
                start_collapsed=True,
                always_open=True,
            ),
            dcc.AccordionItem(
                title='Gráfico de Análise de Pathways KO',
                children=get_ko_20pathway_layout(),
                start_collapsed=True,
                always_open=True,
            )
        ], id='results-accordion', className='results-accordion')
    ], className='results-container')
