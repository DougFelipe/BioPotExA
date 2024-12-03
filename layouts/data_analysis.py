# Importações necessárias para a aplicação Dash e manipulação de dados
from dash import dcc, html
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
import pandas as pd  # Importar para carregar o sample_data.txt

# Importações de utilitários e layouts específicos da aplicação
from components.step_guide import create_step_card  # Importa a função do componente de passo a passo
from layouts.results import get_results_layout  # Importa o novo layout de resultados

# Função para criar a página de Análise de Dados
def get_dataAnalysis_page():
    return html.Div([
        dcc.Store(id='page-state', data='initial'),  # Armazena o estado da página

        # Conteúdo Inicial
        html.Div(id='initial-content', children=[

            # Título "How to Use"
            html.Div([
                html.H2('How to Use', className='how-to-use'),
                html.Hr(className="my-2"),
            ], className='title-container'),

            # Cards de Passo a Passo
            html.Div(
                className='step-cards-column',  # Classe para os cards alinhados verticalmente
                children=[
                    # Step 1: Upload
                    html.Div(
                        className='step-row',  # Linha que contém o card e o texto
                        children=[
                            create_step_card(
                                step_number="Step 1",
                                title="Upload",
                                description="Upload your data files in the specified format for analysis"
                            ),
                            html.P(
                                "Start by uploading your dataset. Ensure the file is in the specified format to avoid processing issues. "
                                "This step allows the application to read and validate the structure of your data, ensuring it meets the requirements for analysis.",
                                className='step-text'
                            )
                        ]
                    ),
                    # Step 2: Process
                    html.Div(
                        className='step-row',
                        children=[
                            create_step_card(
                                step_number="Step 2",
                                title="Process",
                                description="Submit your data for processing and analysis"
                            ),
                            html.P(
                                "Once your data is uploaded, click the button to process it. During this step, the system will validate the dataset, "
                                "checking for completeness, correct formatting, and potential errors. This ensures the data is ready for in-depth analysis.",
                                className='step-text'
                            )
                        ]
                    ),
                    # Step 3: Analyze
                    html.Div(
                        className='step-row',
                        children=[
                            create_step_card(
                                step_number="Step 3",
                                title="Analyze",
                                description="Analyze results and visualize insights"
                            ),
                            html.P(
                                "After processing, move on to analyzing your data. In this step, you can explore detailed results presented in tables and interactive visualizations. "
                                "These insights are designed to help you understand trends, patterns, and key information within your dataset.",
                                className='step-text'
                            )
                        ]
                    )
                ]
            ),

            # Título "Upload and Analyze Your Data"
            html.Div([
                html.H2('Upload and Analyze Your Data', className='how-to-use'),
                html.Hr(className="my-2"),
            ], className='title-container'),

            # Seção de Upload e Botões
            html.Div(
                id='upload-process-card',
                className='upload-process-card-style',
                children=[
                    dcc.Upload(
                        id='upload-data',
                        children=html.Div(['Drag and Drop or ', html.A('Select a File')]),
                        className='upload-button-style'
                    ),
                    html.Div(id='alert-container'),
                    html.Button(
                        'Upload Your File (or sample data) and Click to Submit',
                        id='process-data',
                        n_clicks=0,
                        className='process-button-style'
                    ),
                    html.Button(
                        'Click to Upload Sample Data',
                        id='see-example-data',
                        n_clicks=0,
                        className='process-sample-button-style'
                    ),
                    html.Button(
                        'View Results',
                        id='view-results',
                        n_clicks=0,
                        className='view-results-style',
                        style={'display': 'none'}  # Inicialmente oculto
                    )
                ]
            ),

            # Título "Related Publications"
            html.Div([
                html.H2('Related Publications', className='how-to-use'),
                html.Hr(className="my-2"),
            ], className='title-container'),

            # Seção de Publicações Relacionadas
            html.Div(
                id='related-publications-card',
                className='upload-process-card-style',
                children=[
                    html.Div([
                        html.H4('Disclaimer for Citation', className='publication-subtitle'),
                        html.P(
                            "If you use BioPExA in your research, please cite the following publication:",
                            className='publication-text'
                        ),
                        html.Blockquote(
                            """
                            Author(s). "BioPExA: A Bioinformatics Tool for Exploring Bioremediation Potential". 
                            Journal of Environmental Research and Biotechnology, Year. DOI:xxxx/xxxxxx
                            """,
                            className='citation-text'
                        )
                    ], className='citation-container'),

                    html.Div([
                        html.H4('Related Articles', className='publication-subtitle'),
                        html.Ul([
                            html.Li(
                                "Author(s). 'Integration of Functional Genomics for Pollutant Degradation Analysis'. "
                                "Environmental Bioinformatics Journal, Year."
                            ),
                            html.Li(
                                "Author(s). 'Advances in Metagenomic Analysis for Bioremediation'. "
                                "Biotechnology Progress Journal, Year."
                            ),
                            html.Li(
                                "Author(s). 'Functional Genomics and Bioremediation Potential Assessment'. "
                                "Proceedings of the Biotechnology Conference, Year. *Winner of Best Oral Presentation Award*"
                            )
                        ], className='related-articles-list')
                    ])
                ]
            ),
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
