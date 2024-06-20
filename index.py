"""
index.py
---------
Este arquivo inicializa a aplicação Dash, define o layout principal e configura a navegação entre as abas.
"""

# -------------------------------
# Importações
# -------------------------------

# Importa os componentes principais do Dash para construção da interface.
from dash import Dash, dcc, html

# Importa o componente de cabeçalho personalizado.
from components.header import Header

# Importa funções para obter layouts das páginas.
from layouts.about import get_about_layout
from layouts.data_analysis import get_dataAnalysis_layout

# Certifique-se de importar os callbacks antes de importar a aplicação
import callbacks.P1_COUNT_KO_callbacks  # Importa os callbacks do novo arquivo
import callbacks.P2_KO_20PATHWAY_callbacks  # Importa os callbacks do novo arquivo
import callbacks.callbacks  # Importa os callbacks existentes
import callbacks.P3_compounds_callbacks
import callbacks.P4_rank_compounds_callbacks

# Importação da aplicação deve vir depois dos callbacks
from app import app

# -------------------------------
# Configuração do Layout Principal
# -------------------------------
# Define o layout da aplicação, incluindo o cabeçalho e as abas para navegação.
app.layout = html.Div(
    className='main-content', 
    children=[
        # Cabeçalho da Aplicação
        Header(),

        # Navegação por Abas
        dcc.Tabs(
            id="tabs", 
            value='tab-about', 
            className='main-tabs',  # Adiciona a classe CSS personalizada
            children=[
                dcc.Tab(label='About', value='tab-about', className='tab', selected_className='tab--selected'),
                dcc.Tab(label='Data Analysis', value='tab-data-analysis', className='tab', selected_className='tab--selected')
            ]
        ),

        # Conteúdo das Abas
        # Atualizado dinamicamente com base na aba selecionada.
        html.Div(id='tabs-content', className='tabs-content'),

        # Armazenamento de Dados no Lado do Cliente
        # Utilizado para compartilhar dados entre callbacks sem afetar o layout.
        dcc.Store(id='stored-data'),

        # Container para Gráficos (Inicialmente Oculto)
        # Pode ser utilizado para exibir gráficos com base em dados processados.
        html.Div(id='output-graphs', style={'display': 'none'})
    ]
)

# -------------------------------
# Inicialização do Servidor
# -------------------------------
# Ponto de entrada para iniciar a aplicação Dash.
if __name__ == '__main__':
    app.run_server(debug=True)
