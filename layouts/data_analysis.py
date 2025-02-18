"""
data_analysis.py
-----------------
This script defines the "Data Analysis" page of the Dash web application, including:
- Step-by-step instructions for users on how to upload, process, and analyze their data.
- Components for uploading files, downloading sample data, and displaying results.
- Links to related publications and citation guidelines.

Functions:
- `get_dataAnalysis_page`: Generates the main layout for the data analysis page, including all steps and instructions.
- `get_dataAnalysis_layout`: Compiles the data analysis layout into a reusable format.
"""

# ----------------------------------------
# Imports
# ----------------------------------------

# Core Dash components for interactivity and layout design
from dash import Input, Output, callback, dcc, html
from dash.dependencies import Input, Output, State

# Bootstrap components for styling
import dash_bootstrap_components as dbc

# Pandas for data manipulation
import pandas as pd

# Import reusable components
from components.step_guide import create_step_card  # Step-by-step cards
from components.tooltip_sample import input_format_tooltip  # Tooltip for input format
from components.download_button import get_sample_data_button  # Button for downloading sample data

# Import layouts for results display
from layouts.results import get_results_layout

# ----------------------------------------
# Function: get_dataAnalysis_page
# ----------------------------------------
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
                                description="Upload your data file in the specified .txt format for analysis"
                            ),
                            html.Div(
                                [
                                    html.P(
                                        [
                                            "Start by ",
                                            input_format_tooltip(),
                                            html.Br(),
                                            html.Br(),
                                            "Ensure the file and input data are in the specified format to avoid processing issues",
                                            html.Br(),
                                            html.Br(),
                                            "This step allows the application to read and validate the structure of your data, ensuring it meets the requirements for analysis"
                                        ],
                                        className='step-text'
                                    ),
                                    html.Div(
                                        get_sample_data_button(),  # Botão de download incluído no Step 1
                                        className="button-container"  # Classe para centralizar o botão
                                    )
                                ],
                                className="card-content"  # Classe para estilizar o conteúdo do card
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
                            html.Div(
                                [
                                    html.P(
                                        [
                                            "Once your data or example data is uploaded, click the 'Submit' button and await to see the results",
                                            html.Br(),
                                            html.Br(),
                                            "This is where the provided data is merged with the BioRemPP databases to render the results tables and graphs"
                                        ],
                                        className='step-text'
                                    )
                                ],
                                className="card-content"  # Classe para estilizar o conteúdo do card
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
                                [
                                    "After processing, move on to analyzing your data",
                                    html.Br(),
                                    html.Br(),
                                    "In this step, you can explore detailed results presented in tables and interactive visualizations",
                                    html.Br(),
                                    html.Br(),
                                    "These insights are designed to help you understand trends, patterns, and key information within your dataset"
                                ],
                                className='step-text'
                            )
                        ]
                    ),

                    html.Div(
                        [
                            html.P(
                                [
                                    "If you are encountering difficulties with any of these steps, please refer to the ",
                                    html.A("Help page", href="/help", className="help-link", target="_self"),
                                    ", particularly the ",
                                    html.A("Common Issues",className="help-link2", target="_self"),
                                    " section, for detailed instructions and troubleshooting tips"
                                ],
                                className="help-message"
                            )
                        ],
                        className="help-message-container"  # Classe para estilização
                    )

                ]
            ),


            # Título "Upload and Analyze Your Data"
            html.Div([
                html.H2('Upload and Analyze Your Data', className='how-to-use'),
                html.Hr(className="my-2"),
            ], className='title-container'),

            html.Div(
                id='upload-process-card',
                className='upload-process-card-style',
                children=[
                    html.Div(  # Texto explicativo do passo 1
                        className='upload-explanatory-text',
                        children=[
                            html.P(
                                "Submit your file or click the button to load the example dataset",
                                className='step-explanation'
                            )
                        ]
                    ),
                    html.Div(  # Container para alinhar os botões lado a lado
                        className='upload-buttons-container',
                        children=[
                            dcc.Upload(
                                id='upload-data',
                                children=html.Div(['Drag and Drop or ', html.A('Select a File')]),
                                className='upload-button-style'
                            ),
                            html.Span('Or', className='upload-or-text'),
                            html.Button(
                                'Click to Automatically Upload Exemple Data',
                                id='see-example-data',
                                n_clicks=0,
                                className='process-sample-button-style'
                            )
                        ]
                    ),
                    html.Div(  # Alerta para o botão "Upload"
                        id='alert-container',
                        className='alert-container'
                    ),
                    html.Div(  # Texto explicativo do passo 2
                        html.Hr(className="my-2"),
                    ),
                    html.Div(
                        className='button-progress-container',  # Classe que organiza os elementos
                        children=[
                            # Botão "Click to Submit"
                            html.Button(
                                'Submit',
                                id='process-data',
                                n_clicks=0,
                                className='process-button-style'
                            ),
                            
                            # Botão "View Results" (Inicialmente oculto)
                            html.Button(
                                'View Results',
                                id='view-results',
                                n_clicks=0,
                                className='view-results-style',
                                style={'display': 'none'}  # Inicialmente oculto
                            ),

                            # Barra de Progresso (Sempre abaixo dos botões)
                            html.Div(
                                id="progress-container",
                                children=[
                                    dcc.Interval(
                                        id="progress-interval",
                                        n_intervals=0,
                                        interval=1000,  # Intervalo de 1 segundo
                                        disabled=True  # Começa desabilitado
                                    ),
                                    dbc.Progress(
                                        id="progress-bar",
                                        value=0,
                                        striped=True,
                                        animated=True,
                                    )
                                ],
                                style={"display": "none"}  # Inicialmente oculto
                            ),
                        ]
                    ),


                    html.Button(
                        'View Results',
                        id='view-results',
                        n_clicks=0,
                        className='view-results-style',
                        style={'display': 'none'}  # Inicialmente oculto
                    ),
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
            html.Ul([
            # Novo Artigo 1
            html.Li([
                html.Span(
                    "Silva-Portela, Rita de Cássia Barreto; Minnicelli, Carolina Fonseca; Freitas, Júlia Firme; Fonseca, Marbella Maria Bernardes; Lima Silva, Douglas Felipe de; Silva-Barbalho, Kamila Karla; Falcão, Raul Maia; Bruce, Thiago; Cavalcante, João Vitor Ferreira; Dalmolin, Rodrigo Juliani Siqueira; Agnez-Lima, Lucymara Fassarella",
                    className="authors-line"
                ),
                html.Span(
                    "Unlocking the transcriptional profiles of an oily waste-degrading bacterial consortium",
                    className="article-title"
                ),
                html.Span(
                    "Journal of Hazardous Materials, 2024, Pages 136866",
                    className="journal-info"
                ),
                html.A(
                    "DOI: https://doi.org/10.1016/j.jhazmat.2024.136866",
                    href="https://doi.org/10.1016/j.jhazmat.2024.136866",
                    target="_blank",
                    className="related-article-link"
                )
            ]),
            html.Hr(className="my-2"),

            # Artigo 2
            html.Li([
                html.Span(
                    "Freitas, Júlia Firme; Lima Silva, Douglas Felipe de; Castro, Jenielly Noronha Ferreira; Agnez-Lima, Lucymara Fassarella",
                    className="authors-line"
                ),
                html.Span(
                    "Genomic and phenotypic characterization of novel Ochrobactrum species isolated from Brazilian oil reservoirs: Genomic diversity and bioremediation potential",
                    className="article-title"
                ),
                html.Span(
                    "Process Biochemistry, Volume 149, Pages 74-84, 2025",
                    className="journal-info"
                ),
                html.A(
                    "DOI: https://www.sciencedirect.com/science/article/pii/S1359511324003970",
                    href="https://www.sciencedirect.com/science/article/pii/S1359511324003970",
                    target="_blank",
                    className="related-article-link"
                )
            ]),
            html.Hr(className="my-2"),

            # Artigo 3
            html.Li([
                html.Span(
                    "Freitas, Júlia Firme; Silva, Douglas Felipe de Lima; Silva, Beatriz Soares; Castro, Jenielly Noronha Ferreira; Felipe, Marcus Bruno Mendonça Chaves; Silva-Portela, Renata Cláudia Brito; Minnicelli, Carolina Farah; Agnez-Lima, Lucymara Fassarella",
                    className="authors-line"
                ),
                html.Span(
                    "Genomic and phenotypic features of Acinetobacter baumannii isolated from oil reservoirs reveal a novel subspecies specialized in degrading hazardous hydrocarbons",
                    className="article-title"
                ),
                html.Span(
                    "Microbiological Research, Volume 273, 127420, August 2023",
                    className="journal-info"
                ),
                html.A(
                    "DOI: https://doi.org/10.1016/j.micres.2023.127420",
                    href="https://doi.org/10.1016/j.micres.2023.127420",
                    target="_blank",
                    className="related-article-link"
                )
            ]),
            html.Hr(className="my-2"),

            # Artigo 4
            html.Li([
                html.Span(
                    "Silva, Douglas Felipe de Lima; Agnez-Lima, Lucymara Fassarella",
                    className="authors-line"
                ),
                html.Span(
                    "MicroBioReToxiC (MicroBRTC) - A bioinformatics pipeline for analyzing the bioremediation potential of environmental pollutants in microorganisms",
                    className="article-title"
                ),
                html.Span(
                    "Presented at the XXIV Encontro de Genética do Nordeste (XXIV ENGENE), 2023. *Winner of Oral Presentation Award*",
                    className="journal-info"
                )
            ])
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


# ----------------------------------------
# Function: get_dataAnalysis_layout
# ----------------------------------------

# Função para compilar múltiplas páginas de Análise de Dados
def get_dataAnalysis_layout():
    """
    Compiles the data analysis page into a reusable layout.

    Returns:
    - dash.html.Div: A Dash HTML Div containing the compiled layout.
    """
        
    return html.Div([
        get_dataAnalysis_page()
    ])
