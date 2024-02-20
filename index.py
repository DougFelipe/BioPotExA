# my_dash_app/index.py

# -------------------------------
# Importações
# -------------------------------
from dash import Dash, dcc, html
from components.header import Header
from layouts.about import get_about_layout
from layouts.data_analysis import get_dataAnalysis_layout
from callbacks.callbacks import render_tab_content
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
            children=[
                dcc.Tab(label='About', value='tab-about', className='tab'),
                dcc.Tab(label='Data Analysis', value='tab-data-analysis', className='tab')
            ], 
            className='main-tabs'
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

