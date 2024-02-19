# my_dash_app/layouts/data_analysis.py
from dash import dcc, html, dash_table
from dash.dependencies import Input, Output, State
import base64
import io
import pandas as pd
import plotly.express as px


import lorem
from layouts.P1_KO_COUNT import get_ko_count_layout
from layouts.P2_KO_20PATHWAY import get_ko_20pathway_layout
from utils.data_processing import process_ko_data


def get_dataAnalysis_page():
    # Esta função cria um único bloco de conteúdo estilizado como uma página A4
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


## MOSTRAR AS MULTIPLAS PÁGINAS DAS
def get_dataAnalysis_layout():
    # Esta função compila três blocos de conteúdo de página A4
    return html.Div([
        get_dataAnalysis_page(),
        get_ko_count_layout(),
        get_ko_20pathway_layout()
    ])


##MODULAZIRA A CRIAÇÃO DE TITULOS E DESCRIÇÃO DOS RESULTADOS
def create_card(title, content):
    return html.Div([
        html.H3(title, className='card-title'),
        html.P(content, className='card-content')
    ], className='card')