# my_dash_app/layouts/data_analysis.py

# Importações necessárias para a aplicação Dash e manipulação de dados
from dash import dcc, html, dash_table
from dash.dependencies import Input, Output, State
import base64
import io
import pandas as pd
import plotly.express as px

# Importações de utilitários e layouts específicos da aplicação
import lorem
from layouts.P1_KO_COUNT import get_ko_count_layout
from layouts.P2_KO_20PATHWAY import get_ko_20pathway_layout
from utils.data_processing import process_ko_data

# Função para criar a página de Análise de Dados
def get_dataAnalysis_page():
    """
    Cria e retorna um layout para a página de Análise de Dados.
    
    Esta função cria um bloco de conteúdo estilizado como uma página A4, incluindo
    um botão de upload, um botão para processar dados e espaços reservados para exibição
    de alertas e tabelas de dados.
    """
    return html.Div([
        html.H3('Data Analysis'),
        dcc.Upload(
            id='upload-data',
            children=html.Button('Carregar Arquivo'),
            style={'marginBottom': '10px'}
        ),
        html.Button('Processar Arquivo', id='process-data', n_clicks=0, disabled=True),
        html.Div(id='alert-container'),
        html.Div(id='output-data-upload'),
        html.Div(id='database-data-table'),
        html.Div(id='output-merge-table'),
    ], className='tabs-content')

# Função para compilar múltiplas páginas de Análise de Dados
def get_dataAnalysis_layout():
    """
    Compila e retorna o layout completo da Análise de Dados, incluindo a página principal
    de análise e páginas adicionais para contagem KO e análise de pathways KO.
    
    Esta função agrupa três blocos de conteúdo de página A4, cada um correspondendo a uma
    parte específica da análise de dados.
    """
    return html.Div([
        get_dataAnalysis_page(),
        get_ko_count_layout(),
        get_ko_20pathway_layout()
    ])

# Função para criar um card de título e conteúdo
def create_card(title, content):
    """
    Cria e retorna um card HTML com um título e conteúdo.
    
    :param title: Título do card.
    :param content: Conteúdo do card, geralmente um parágrafo de texto.
    :return: Um componente HTML Div contendo o título e conteúdo do card.
    """
    return html.Div([
        html.H3(title, className='card-title'),
        html.P(content, className='card-content')
    ], className='card')
