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
from utils.table_utils import create_table_from_dataframe
from components.step_guide import create_step_guide  # Importa a função do componente de passo a passo
from components.features_list import create_list_card, features_list_1  # Importa a função e lista de características

# Função para criar a página de Análise de Dados
def get_dataAnalysis_page():
    """
    Cria e retorna um layout para a página de Análise de Dados.
    
    Esta função cria um bloco de conteúdo estilizado como uma página A4, incluindo
    parágrafos explicativos sobre a ferramenta, um botão de upload, um botão para processar dados 
    e espaços reservados para exibição de alertas e tabelas de dados.
    """
    return html.Div([
        html.H2('Análise de Dados para Biorremediação', className='about-title'),
        html.Div(
            [
                html.Div(
                    [
                        html.P(
                            'Nossa plataforma de análise de dados é projetada para pesquisadores e profissionais que '
                            'precisam avaliar o potencial de biorremediação de genomas e metagenomas. Com uma interface '
                            'intuitiva e recursos avançados, a ferramenta facilita a anotação funcional e a identificação de '
                            'genes-chave envolvidos na degradação de poluentes e outras funções ecológicas relevantes.',
                            className='about-content'
                        ),
                        html.P(
                            'Os resultados das análises são apresentados de forma clara e integrada, permitindo uma interpretação '
                            'detalhada dos dados. Isso inclui associações com vias metabólicas conhecidas, comparações com bancos de '
                            'dados de referência e visualizações interativas que destacam os aspectos mais importantes da sua pesquisa.',
                            className='about-content'
                        ),
                        html.P(
                            'Para começar, faça o upload dos seus dados no formato especificado, utilizando a função de arrastar e soltar '
                            'ou selecionando o arquivo manualmente. Uma vez carregados, nossos algoritmos de processamento de dados entram em ação, '
                            'analisando as sequências e retornando insights valiosos em questão de minutos. Após a análise, você pode facilmente '
                            'exportar os dados para uso em publicações, apresentações ou para análises subsequentes em outras plataformas.',
                            className='about-content'
                        ),
                        create_step_guide()  # Adiciona o componente de guia de passos após o terceiro parágrafo
                    ],
                    className='text-container'
                ),
                html.Div(
                    [
                        create_list_card("Data Analysis Features", features_list_1)
                    ],
                    className='list-container'
                )
            ],
            className='content-container'
        ),
        html.Div(
            id='upload-process-card',
            className='upload-process-card-style',
            children=[
                dcc.Upload(
                    id='upload-data',
                    children=html.Div(['Arraste e Solte ou ', html.A('Selecione um Arquivo')]),
                    className='upload-button-style'
                ),
                html.Div(id='alert-container'),
                html.Button(
                    'Processar Arquivo',
                    id='process-data',
                    n_clicks=0,
                    className='process-button-style'
                )
            ]
        ),
        html.Div(id='output-data-upload'),
        html.Div(id='database-data-table'),
    ], className='pages-content')

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
