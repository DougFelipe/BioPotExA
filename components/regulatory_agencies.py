"""
regulatory_agencies.py
----------------------
This script defines the layout for the Regulatory Agencies page in a Dash web application. 

The page provides:
- An overview of priority environmental pollutants.
- Descriptions of global regulatory agencies and their roles in identifying and managing hazardous substances.
- Structured content with headings, sections, and descriptive text.
"""

# ----------------------------------------
# Imports
# ----------------------------------------

from dash import html
import dash_bootstrap_components as dbc

# ----------------------------------------
# Function: get_regulatory_agencies_layout
# ----------------------------------------

def get_regulatory_agencies_layout():
    return html.Div(
        dbc.Container([

            # Título da Página
            dbc.Row([
                dbc.Col([
                    html.H1(
                        "Regulatory Agencies and Environmental Directives",
                        className="text-success fw-bold text-center mb-4",
                        style={"fontFamily": "'Times New Roman', serif"}
                    ),
                    html.P(
                        "BioRemPP provides a comprehensive database that includes compounds identified as priority environmental pollutants. "
                        "These compounds are recognized by global regulatory agencies or entities due to their environmental and human health impacts.",
                        className="text-center text-dark fs-5",
                        style={"fontFamily": "Arial, sans-serif"}
                    )
                ])
            ]),

            # Seção: Priority Pollutants
            dbc.Row([
                dbc.Col([
                    html.H4("Priority Environmental Pollutants", className="text-success fw-bold mt-5 mb-3", style={"fontFamily": "'Times New Roman', serif"}),
                    html.P(
                        "Priority pollutants are compounds that pose significant risks to environmental and human health. "
                        "These substances often include organic compounds, heavy metals, pesticides, and industrial chemicals. "
                        "They are targeted for monitoring and remediation efforts due to their persistence, toxicity, and bioaccumulation potential.",
                        className="text-dark fs-6",
                        style={"fontFamily": "Arial, sans-serif"}
                    ),
                    html.P(
                        "By focusing on these compounds, BioRemPP aims to support global initiatives for environmental sustainability "
                        "and the development of innovative bioremediation strategies.",
                        className="text-dark fs-6",
                        style={"fontFamily": "Arial, sans-serif"}
                    )
                ])
            ]),

            # Seção: Regulatory Agencies
            dbc.Row([
                dbc.Col([
                    html.H4("Key Environmental Regulatory Agencies", className="text-success fw-bold mt-5 mb-3", style={"fontFamily": "'Times New Roman', serif"}),

                    dbc.Row([
                        dbc.Col([
                            html.H5("Agency for Toxic Substances and Disease Registry (ATSDR, USA)", className="fw-semibold mb-1", style={"fontFamily": "'Times New Roman', serif"}),
                            html.P(
                                "The ATSDR identifies hazardous substances and assesses their health effects. Its priority substance list "
                                "guides environmental cleanup and regulatory actions in the USA.",
                                style={"fontFamily": "Arial, sans-serif"}
                            )
                        ])
                    ]),

                    dbc.Row([
                        dbc.Col([
                            html.H5("National Environmental Council (CONAMA, Brazil)", className="fw-semibold mb-1", style={"fontFamily": "'Times New Roman', serif"}),
                            html.P(
                                "CONAMA establishes guidelines for pollution control, water quality, and the regulation of hazardous substances in Brazil. "
                                "It prioritizes pollutants based on their environmental impact and risks to public health.",
                                style={"fontFamily": "Arial, sans-serif"}
                            )
                        ])
                    ]),

                    dbc.Row([
                        dbc.Col([
                            html.H5("Environmental Protection Agency (EPA, USA)", className="fw-semibold mb-1", style={"fontFamily": "'Times New Roman', serif"}),
                            html.P(
                                "The EPA regulates pollutants through programs like the National Priority List and CERCLA (Superfund), focusing on "
                                "mitigating environmental contamination and promoting sustainability.",
                                style={"fontFamily": "Arial, sans-serif"}
                            )
                        ])
                    ]),

                    dbc.Row([
                        dbc.Col([
                            html.H5("European Parliament (EP)", className="fw-semibold mb-1", style={"fontFamily": "'Times New Roman', serif"}),
                            html.P(
                                "The EP enforces directives like the REACH regulation and the Water Framework Directive, which aim to protect "
                                "the environment and human health by monitoring and regulating pollutants across Europe.",
                                style={"fontFamily": "Arial, sans-serif"}
                            )
                        ])
                    ]),

                    dbc.Row([
                        dbc.Col([
                            html.H5("International Agency for Research on Cancer (IARC)", className="fw-semibold mb-1", style={"fontFamily": "'Times New Roman', serif"}),
                            html.P(
                                "The IARC classifies compounds based on their carcinogenic potential (Groups 1, 2A, and 2B). "
                                "This classification informs regulatory actions and prioritization for monitoring.",
                                style={"fontFamily": "Arial, sans-serif"}
                            )
                        ])
                    ]),

                    dbc.Row([
                        dbc.Col([
                            html.H5("Canadian Environmental Protection Act (CEPA) - Priority Substances Lists (PSL1 and PSL2)", className="fw-semibold mb-1", style={"fontFamily": "'Times New Roman', serif"}),
                            html.P(
                                "The CEPA prioritizes substances based on their toxicity, persistence, and bioaccumulation. "
                                "PSL1 and PSL2 guide environmental management actions in Canada.",
                                style={"fontFamily": "Arial, sans-serif"}
                            )
                        ])
                    ]),

                    dbc.Row([
                        dbc.Col([
                            html.H5("Water Framework Directive (WFD)", className="fw-semibold mb-1", style={"fontFamily": "'Times New Roman', serif"}),
                            html.P(
                                "The WFD aims to achieve good water quality in Europe by targeting priority pollutants in surface and groundwater. "
                                "It provides a framework for monitoring and remediation efforts.",
                                style={"fontFamily": "Arial, sans-serif"}
                            )
                        ])
                    ])
                ])
            ])

        ]),
        className="py-4"
    )
