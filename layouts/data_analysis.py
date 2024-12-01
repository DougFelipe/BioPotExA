# Importações necessárias para a aplicação Dash e manipulação de dados
from dash import dcc, html
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
import pandas as pd  # Importar para carregar o sample_data.txt

# Importações de utilitários e layouts específicos da aplicação
from components.step_guide import create_step_guide  # Importa a função do componente de passo a passo
from layouts.results import get_results_layout  # Importa o novo layout de resultados

# Função para criar a página de Análise de Dados
def get_dataAnalysis_page():
    return html.Div([
        dcc.Store(id='page-state', data='initial'),  # Armazena o estado da página

        # Conteúdo Inicial
        html.Div(id='initial-content', children=[
            html.Div([
                html.Div([
                    html.H2('How to Use', className='how-to-use'),
                    html.Hr(className="my-2"),
                    create_step_guide(),
                    html.Div(id='upload-process-card', className='upload-process-card-style', children=[
                        dcc.Upload(
                            id='upload-data',
                            children=html.Div(['Drag and Drop or ', html.A('Select a File')]),
                            className='upload-button-style'
                        ),
                        html.Div(id='alert-container'),
                        html.Button(
                            'Click to Submit and Process Data',
                            id='process-data',
                            n_clicks=0,
                            className='process-button-style'
                        ),
                        # Botão "See Example"
                        html.Button(
                            'See Example',
                            id='see-example-data',
                            n_clicks=0,
                            className='process-button-style'
                        ),
                        html.Button(
                            'View Results',
                            id='view-results',
                            n_clicks=0,
                            className='view-results-style',
                            style={'display': 'none'}  # Inicialmente oculto
                        )
                    ])
                ], className='text-container'),
            ], className='content-container')
        ]),

        # Conteúdo dos Resultados
        html.Div(id='results-content', style={'display': 'none'}, children=[
            get_results_layout()
        ])
    ], className='pages-content')

# Função para compilar múltiplas páginas de Análise de Dados
def get_dataAnalysis_layout():
    return html.Div([
        get_dataAnalysis_page()
    ])
