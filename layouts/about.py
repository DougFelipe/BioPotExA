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
from layouts.data_analysis import get_dataAnalysis_layout

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
                            # Coluna com logo (substituir o src pela logo real depois)
                            dbc.Col(
                                dbc.CardImg(
                                    src="assets/images/HAZARD_LOGO.png",
                                    className="img-fluid rounded-start",
                                ),
                                className="col-md-3",
                            ),

                            # Coluna com conteúdo textual
                            dbc.Col(
                                dbc.CardBody(
                                    [
                                        html.H1(
                                            "Bioremediation Potential Profile",
                                            className="text-success fw-bold mb-2",
                                            style={"fontFamily": "'Times New Roman', serif"}
                                        ),
                                        html.P(
                                            "Bioremediation Potential Profile (BioRemPP) is a scientific web application designed to explore the biotechnological potential of microbial, fungal, and plant genomes for bioremediation purposes",
                                            className="card-text text-dark fs-5",
                                            style={"fontFamily": "Arial, sans-serif"}
                                        ),
                                        html.P(
                                            "BioRemPP enables functional analysis of annotated genomes through integration with multiple curated bioremediation-related databases and supports the understanding of degradation mechanisms, metabolic pathways, enzymatic functions, and relationships between samples, genes, compounds, toxic compound associations, and othersignificant biological results ",
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
            ])

        ]),
        className='about-container py-4'
    )
