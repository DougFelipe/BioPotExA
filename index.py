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
from components.features import get_features_layout  # Import the new layout
from components.bioremediation import get_bioremediation_layout
from components.regulatory_agencies import get_regulatory_agencies_layout

# Importa funções para obter layouts das páginas.
from layouts.about import get_about_layout
from layouts.data_analysis import get_dataAnalysis_page
from layouts.results import get_results_layout  # Importa o layout dos resultados
from layouts.help import get_help_layout

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
import callbacks.P17_gene_compound_network_callbacks
import callbacks.p18_heatmap_faceted_callbacks
import callbacks.T1_biorempp_callbacks

from callbacks.callbacks import  handle_progress

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
# Ajustar o callback de navegação
@app.callback(
    Output('page-content', 'children'),
    Input('url', 'pathname')
)
def display_page(pathname):
    if pathname == '/data-analysis':
        return get_dataAnalysis_page()
    elif pathname == '/results':
        return get_results_layout()
    elif pathname == '/help':  # Nova rota para a página de ajuda
        return get_help_layout()
    elif pathname == '/features':  # Add the route for the Features page
        return get_features_layout()
    elif pathname == '/bioremediation':  # New Bioremediation Page
        return get_bioremediation_layout()
    elif pathname == '/regulatory':
        return get_regulatory_agencies_layout()
    else:
        return get_about_layout()




# -------------------------------
# Inicialização do Servidor
# -------------------------------
# Ponto de entrada para iniciar a aplicação Dash.
if __name__ == '__main__':
    app.run_server(debug=True)