# Importações necessárias para a aplicação Dash e manipulação de dados
from dash import Input, Output, callback, dash,dcc, html
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
import pandas as pd  # Importar para carregar o sample_data.txt

# Importações de utilitários e layouts específicos da aplicação
from components.step_guide import create_step_card  # Importa a função do componente de passo a passo
from components.tooltip_sample import input_format_tooltip
from components.download_button import get_sample_data_button
from layouts.results import get_results_layout  # Importa o novo layout de resultados



# Função para criar a página de Análise de Dados
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
                            html.Div(
                                [
                                    html.P(
                                        [
                                            "Start by uploading ",
                                            input_format_tooltip(),
                                            ". Ensure the file is in the specified format to avoid processing issues. "
                                            "This step allows the application to read and validate the structure of your data, ensuring it meets the requirements for analysis."
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
                                        "Once your data is uploaded, click the button to process it. During this step, the system will validate the dataset, "
                                        "checking for completeness, correct formatting, and potential errors. This ensures the data is ready for in-depth analysis.",
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

            html.Div(
                id='upload-process-card',
                className='upload-process-card-style',
                children=[
                    html.Div(  # Texto explicativo do passo 1
                        className='upload-explanatory-text',
                        children=[
                            html.P(
                                "Submit your file or click the button to load the example dataset.",
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
                                'Upload Sample Data',
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
                        className='process-explanatory-text',
                        children=[
                            html.P(
                                "Click to submit your data for processing and results presentation.",
                                className='step-explanation'
                            )
                        ]
                    ),
                    html.Div(
                        className='button-progress-container',  # Classe que organiza os elementos
                        children=[
                            # Botão "Click to Submit"
                            html.Button(
                                'Click to Submit',
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
                    html.Div(  # Disclaimer para citação
                        className='citation-disclaimer-container',
                        children=[
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
                        ]
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
                    ], className='citation-container'),

            html.Div([
                html.Ul([
                    html.Li([
                        html.Span("Freitas, Júlia Firme; Lima Silva, Douglas Felipe de; Castro, Jenielly Noronha Ferreira; Agnez-Lima, Lucymara Fassarella. "),
                        html.Span("Genomic and phenotypic characterization of novel Ochrobactrum species isolated from Brazilian oil reservoirs: Genomic diversity and bioremediation potential. ", className="article-title"),
                        html.Span("Process Biochemistry, Volume 149, Pages 74-84, 2025. "),
                        html.A("Read more",
                            href="https://www.sciencedirect.com/science/article/pii/S1359511324003970",
                            target="_blank", className="related-article-link")
                    ]),
                                html.Hr(className="my-2"),

                    html.Li([
                        html.Span("Freitas, Júlia Firme; Silva, Douglas Felipe de Lima; Silva, Beatriz Soares; Castro, Jenielly Noronha Ferreira; Felipe, Marcus Bruno Mendonça Chaves; Silva-Portela, Renata Cláudia Brito; Minnicelli, Carolina Farah; Agnez-Lima, Lucymara Fassarella. "),
                        html.Span("Genomic and phenotypic features of Acinetobacter baumannii isolated from oil reservoirs reveal a novel subspecies specialized in degrading hazardous hydrocarbons. ", className="article-title"),
                        html.Span("Microbiological Research, Volume 273, 127420, August 2023. "),
                        html.A("Read more",
                            href="https://doi.org/10.1016/j.micres.2023.127420",
                            target="_blank", className="related-article-link")
                    ]),
                                html.Hr(className="my-2"),

                    html.Li([
                        html.Span("Silva, Douglas Felipe de Lima; Agnez-Lima, Lucymara Fassarella. "),
                        html.Span("MicroBioReToxiC (MicroBRTC) - A bioinformatics pipeline for analyzing the bioremediation potential of environmental pollutants in microorganisms. ", className="article-title"),
                        html.Span("Presented at the XXIV Encontro de Genética do Nordeste (XXIV ENGENE), 2023. *Winner of Oral Presentation Award*. "),
                    ]),
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
