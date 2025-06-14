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
from components.tooltip_sample import input_format_tooltip

# Import layouts for results display
from components.pages.results import get_results_layout

# ----------------------------------------
# Function: get_dataAnalysis_page
# ----------------------------------------
def get_dataAnalysis_page():
    return html.Div([
        dcc.Store(id='page-state', data='initial'),



        html.Div(id='initial-content', children=[
            dbc.Container([
                        html.Div([
                        html.H2('Upload and Analyze Your Data', className='how-to-use'),
                                                        # Call to Action
                        dbc.Row([
                            dbc.Col([
                                html.H5("Try It Yourself", className="text-success fw-bold text-center"),
                                html.P("Follow the steps below to start your own bioremediation data analysis",
                                    className="text-center small text-muted")
                            ])
                        ], className="mb-4"),
                        html.Hr(className="my-2")
                    ], className='title-container'),


                # Step 1
                dbc.Row([
                    dbc.Col([
                        html.P('Step 1', className='text-success fw-bold text-center fs-4'),                                    

                        html.H3('Understand the Process', className='text-success text-center fs-3'),
                        html.P(
                            "Start your analysis by integrating your dataset with curated bioremediation databases, specifically designed for environmental priority pollutants, including BioRemPP, HADEG, and ToxCSM",
                            className='help-message text-center small mt-2'
                        ),
                        html.P(
                            "Simply upload a file or use the sample data provided",
                            className='help-message text-center small mt-1'
                        ),
                        html.P(
                            [
                                "If you are encountering difficulties with any of these steps, refer to the ",
                                html.A("Help page", href="/help", className="help-link", target="_self"),
                                " and ",
                                html.A("Documentation", href="/documentation", className="help-link", target="_self"),
                                " for guidance"
                            ],
                            className="help-message text-center small mt-2"
                        ),
                        html.Hr()
                    ])
                ]),

                html.Hr(className="my-2"),     

                # Step 2
                dbc.Row([
                    dbc.Col([
                        html.P('Step 2', className='text-success fw-bold text-center fs-4'),
                        html.H3('Upload Your Data', className='text-success text-center fs-3'),
                        html.P(
                            [
                                "A dataset can be submitted by either selecting or dragging and dropping a file in the prescribed format (as in this ",
                                input_format_tooltip(),
                                "), or alternatively, by downloading the complete dataset below or loading a predefined sample using the demonstration button"
                            ],
                            className='help-message text-center small mt-2'
                        )


                    ])
                ]),

                # Download Example Data
                dbc.Row([
                    dbc.Col([
                        html.Div(
                            get_sample_data_button(),
                            className="text-center my-3"
                        )
                    ])
                ]),

                # Upload Area
                dbc.Row([
                    dbc.Col([
                        html.Div(
                            id='upload-process-card',
                            className='upload-process-card-style p-4 rounded shadow-sm',
                            style={'backgroundColor': '#f8fdf8'},
                            children=[
                                html.H5("Upload Area", className='text-center text-success fw-bold fs-2'),
                                html.P("Choose one of the options below to provide your data",
                                       className='help-message text-center small mt-2'),

                                html.Div(
                                    className='upload-buttons-container d-flex justify-content-center align-items-center',
                                    style={'gap': '20px', 'flexWrap': 'wrap'},
                                    children=[
                                        dcc.Upload(
                                            id='upload-data',
                                            children=html.Div([
                                                "📁 ", html.Span("Drag and Drop", style={'color': '#28a745'}), " or ",
                                                html.A("Select a File", style={'color': '#28a745'})
                                            ]),
                                            className='upload-button-style p-3 border border-success rounded',
                                            style={
                                                'cursor': 'pointer',
                                                'textAlign': 'center',
                                                'backgroundColor': '#fff',
                                                'borderStyle': 'dashed',
                                                'minWidth': '280px'
                                            }
                                        ),
                                        html.Span('Or', className='upload-or-text fw-bold text-muted'),
                                        html.Button(
                                            'Click to Automatically Upload Exemple Data',
                                            id='see-example-data',
                                            n_clicks=0,
                                            className='process-sample-button-style btn btn-success'
                                        )
                                    ]
                                ),

                                
                                html.Div(id='alert-container', className='alert-container my-3'),
    
                                html.Div(
                                    className='button-progress-container text-center mt-4',
                                    children=[
                                        html.H3("Process and Analyze", className='text-center text-success fw-bold fs-2'),
                                        html.P(
                                            [
                                                "Once your data is ready, click ",
                                                html.Span("Submit", className="fw-bold text-success"),
                                                " to begin analysis",
                                                html.Br(),
                                                "After processing, the ",
                                                html.Span("View Results", className="fw-bold text-danger"),
                                                " button will become available"
                                            ],
                                            className='help-message text-center small mt-2'
                                        ),


                                        html.Button(
                                            'Submit',
                                            id='process-data',
                                            n_clicks=0,
                                            className='process-button-style btn btn-success me-2'
                                        ),
                                        html.Button(
                                            'View Results',
                                            id='view-results',
                                            n_clicks=0,
                                            className='view-results-style btn btn-outline-warning btn-lg',
                                            style={
                                                'display': 'none'
                                            }
                                        ),
                                    ]
                                ),
                            ]
                        )
                    ])
                ])
            ])
        ]),

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
