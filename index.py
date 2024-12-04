"""
index.py
---------
Este arquivo inicializa a aplicação Dash, define o layout principal e configura a navegação entre as abas.
"""

# -------------------------------
# Importações
# -------------------------------

# Importa os componentes principais do Dash para construção da interface.
from dash import Dash, dcc, html,Input, Output

# Importa o componente de cabeçalho personalizado.
from components.header import Header

# Importa funções para obter layouts das páginas.
from layouts.about import get_about_layout
from layouts.data_analysis import get_dataAnalysis_page
from layouts.results import get_results_layout  # Importa o layout dos resultados

# Certifique-se de importar os callbacks antes de importar a aplicação
import callbacks.P1_COUNT_KO_callbacks  # Importa os callbacks do novo arquivo
import callbacks.P2_KO_20PATHWAY_callbacks  # Importa os callbacks do novo arquivo
import callbacks.callbacks  # Importa os callbacks existentes
import callbacks.P3_compounds_callbacks
import callbacks.P4_rank_compounds_callbacks
import callbacks.P5_rank_compounds_callbacks
import callbacks.P6_rank_compounds_callbacks
import callbacks.P7_compound_x_genesymbol_callbacks
import callbacks.P8_sample_x_genesymbol_callbacks
import callbacks.P9_sample_x_referenceAG_callbacks
import callbacks.P10_sample_grouping_profile_callbacks
import callbacks.P11_callbacks
import callbacks.P12_callbacks
import callbacks.P13_callbacks
import callbacks.P14_sample_enzyme_activity_callbacks
import callbacks.P15_sample_clustering_callbacks
import callbacks.P16_sample_upset_callbacks


# Importação da aplicação deve vir depois dos callbacks
from app import app


# -------------------------------
# Configuração do Layout Principal
# -------------------------------
# Define o layout inicial da aplicação com suporte à navegação entre páginas
app.layout = html.Div(
    className='main-content',
    children=[
        # Localização da URL para navegação entre páginas
        dcc.Location(id='url', refresh=False),

        # Cabeçalho da Aplicação
        Header(),

        # Conteúdo Dinâmico Atualizado com base na URL
        html.Div(id='page-content'),

        # Armazenamento de Dados no Lado do Cliente
        dcc.Store(id='stored-data'),

        # Container para Gráficos (Inicialmente Oculto)
        html.Div(id='output-graphs', style={'display': 'none'})
    ]
)
# -------------------------------
# Callback para Navegação entre Páginas
# -------------------------------
@app.callback(
    Output('page-content', 'children'),
    Input('url', 'pathname')
)
def display_page(pathname):
    """
    Callback para renderizar o layout correspondente com base na URL do aplicativo.

    :param pathname: Caminho atual da URL.
    :return: Layout correspondente para o caminho especificado.
    """
    if pathname == '/data-analysis':  # Rota para análise de dados
        return get_dataAnalysis_page()
    elif pathname == '/results':  # Rota para página de resultados
        return get_results_layout()
    elif pathname == '/see-example':  # Rota para página "See Example"
        return get_see_example_layout()
    else:  # Página padrão é "About"
        return get_about_layout()



# -------------------------------
# Inicialização do Servidor
# -------------------------------
# Ponto de entrada para iniciar a aplicação Dash.
if __name__ == '__main__':
    app.run_server(debug=True)