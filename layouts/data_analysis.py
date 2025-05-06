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
            html.Div([
                html.H2('Upload and Analyze Your Data', className='how-to-use'),
                html.Hr(className="my-2"),
            ], className='title-container'),

            html.Div(
                [
                    html.P(
                        [
                            "If you are encountering difficulties with any of these steps, please refer to the ",
                            html.A("Help page", href="/help", className="help-link", target="_self"),
                            " and the ",
                            html.A("Documentation", href="/documentation", className="help-link", target="_self"),
                            " section, for detailed instructions and troubleshooting tips"
                        ],
                        className="help-message"
                    ),
                ],
                className="help-message-container"
            ),

            html.Div(
                get_sample_data_button(),
                className="button-container"
            ),

            html.Div(
                id='upload-process-card',
                className='upload-process-card-style',
                children=[
                    html.Div(
                        className='upload-explanatory-text',
                        children=[
                            html.P(
                                "Submit your file or click the button to load the example dataset",
                                className='step-explanation'
                            )
                        ]
                    ),
                    html.Div(
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
                    html.Div(
                        id='alert-container',
                        className='alert-container'
                    ),
                    html.Div(
                        html.Hr(className="my-2"),
                    ),
                    html.Div(
                        className='button-progress-container',
                        children=[
                            html.Button(
                                'Submit',
                                id='process-data',
                                n_clicks=0,
                                className='process-button-style'
                            ),
                            html.Button(
                                'View Results',
                                id='view-results',
                                n_clicks=0,
                                className='view-results-style',
                                style={'display': 'none'}
                            ),
                            html.Div(
                                id="progress-container",
                                children=[
                                    dcc.Interval(
                                        id="progress-interval",
                                        n_intervals=0,
                                        interval=1000,
                                        disabled=True
                                    ),
                                    dbc.Progress(
                                        id="progress-bar",
                                        value=0,
                                        striped=True,
                                        animated=True,
                                    )
                                ],
                                style={"display": "none"}
                            ),
                        ]
                    ),
                ]
            ),
        ]),

        # Resultados
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
