"""
about.py
--------
This script defines the layout for the "About" page of the Dash web application. 
The "About" page provides an introduction to the Bioremediation Potential Profile (BioRemPP), 
including its purpose, features, and integration with external databases.

The page includes:
- A stylized card with a logo and system description.
- An explanation of the tool's biotechnological potential in bioremediation.
- A call-to-action section to initiate analysis.
- Integration of the data analysis layout.
"""

# ----------------------------------------
# Imports
# ----------------------------------------

from dash import html
import dash_bootstrap_components as dbc
from components.pages.data_analysis import get_dataAnalysis_layout
from components.ui.analysis_suggestions import analysis_suggestions_offcanvas

# ----------------------------------------
# Function: get_about_layout
# ----------------------------------------

def get_about_layout():
    return html.Div(
        dbc.Container([

            # Card de Apresentação
            dbc.Card(
                [
                    dbc.Row(
                        [
                            dbc.Col(
                                dbc.CardImg(
                                    src="assets/images/BIOREMPP_LOGO.png",
                                    className="img-fluid rounded-start",
                                ),
                                className="col-md-3",
                            ),
                            dbc.Col(
                                dbc.CardBody(
                                    [
                                        html.P(
                                            "The Bioremediation Potential Profile (BioRemPP) is a scientific web application designed to explore the biotechnological potential of microbial, fungal, and plant genomes for bioremediation purposes",
                                            className="card-text text-dark fs-5",
                                            style={"fontFamily": "Arial, sans-serif"}
                                        ),
                                        html.P(
                                            "BioRemPP enables functional analysis of annotated genomes through integration with multiple curated bioremediation-related databases and supports the understanding of degradation mechanisms, metabolic pathways, enzymatic functions, and relationships between samples, genes, compounds, toxic compound associations, and other significant biological results.",
                                            className="card-text text-dark fs-5",
                                            style={"fontFamily": "Arial, sans-serif"}
                                        ),
                                    ]
                                ),
                                className="col-md-8",
                            ),
                        ],
                        className="g-0 d-flex align-items-center",
                    )
                ],
                className="mb-5 shadow-sm",
                style={"maxWidth": "100%", "borderRadius": "1rem"}
            ),

            # Importação do Layout da Análise de Dados
            dbc.Row([
                dbc.Col([
                    html.Div(
                        get_dataAnalysis_layout(),
                        className='data-analysis-content'
                    )
                ])
            ]),

            # Botão flutuante fixo
            # Botão flutuante fixo com estilo corrigido
            html.Div([
                dbc.Button(
                    [html.Span("Analytical", style={"display": "block"}), html.Span("Suggestions", style={"display": "block"})],
                    id="open-suggestions-offcanvas",
                    n_clicks=0,
                    className="btn btn-outline-success btn-sm",
                    style={
                        "backgroundColor": "white",
                        "borderColor": "#198754",
                        "color": "#198754",
                        "fontWeight": "500",
                        "lineHeight": "1.2",
                        "whiteSpace": "normal",
                        "textAlign": "center"
                    }
                )
            ], style={
                "position": "fixed",
                "bottom": "25px",
                "right": "25px",
                "zIndex": "1051"
            }),


        ]),
        className='about-container py-4'
    )
