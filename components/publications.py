from dash import html
import dash_bootstrap_components as dbc

def get_publications_layout():
    return html.Div(
        dbc.Container([

            # Título da Página
            dbc.Row([
                dbc.Col([
                    html.H1(
                        "Previous Publications",
                        className="text-success fw-bold text-center mb-3",
                        style={"fontFamily": "'Times New Roman', serif"}
                    ),
                    html.Hr()
                ])
            ]),

            # Lista de Publicações
            dbc.Row([
                dbc.Col([
                    html.Ul([

                        html.Li([
                            html.H5(
                                "Unlocking the transcriptional profiles of an oily waste-degrading bacterial consortium",
                                className="fw-bold text-dark",
                                style={"fontFamily": "'Times New Roman', serif"}
                            ),
                            html.P(
                                "Silva-Portela, Rita de Cássia Barreto; Minnicelli, Carolina Fonseca; Freitas, Júlia Firme; Fonseca, Marbella Maria Bernardes; Lima Silva, Douglas Felipe de; Silva-Barbalho, Kamila Karla; Falcão, Raul Maia; Bruce, Thiago; Cavalcante, João Vitor Ferreira; Dalmolin, Rodrigo Juliani Siqueira; Agnez-Lima, Lucymara Fassarella",
                                className="mb-1",
                                style={"fontFamily": "Arial, sans-serif"}
                            ),
                            html.P(
                                "Journal of Hazardous Materials, 2024, Pages 136866",
                                className="mb-1",
                                style={"fontFamily": "Arial, sans-serif"}
                            ),
                            html.A(
                                "DOI: https://doi.org/10.1016/j.jhazmat.2024.136866",
                                href="https://doi.org/10.1016/j.jhazmat.2024.136866",
                                target="_blank",
                                className="text-decoration-none text-primary fw-semibold"
                            ),
                            html.Hr()
                        ]),

                        html.Li([
                            html.H5(
                                "Genomic and phenotypic characterization of novel Ochrobactrum species isolated from Brazilian oil reservoirs: Genomic diversity and bioremediation potential",
                                className="fw-bold text-dark",
                                style={"fontFamily": "'Times New Roman', serif"}
                            ),
                            html.P(
                                "Freitas, Júlia Firme; Lima Silva, Douglas Felipe de; Castro, Jenielly Noronha Ferreira; Agnez-Lima, Lucymara Fassarella",
                                className="mb-1",
                                style={"fontFamily": "Arial, sans-serif"}
                            ),
                            html.P(
                                "Process Biochemistry, Volume 149, Pages 74-84, 2025",
                                className="mb-1",
                                style={"fontFamily": "Arial, sans-serif"}
                            ),
                            html.A(
                                "DOI: https://www.sciencedirect.com/science/article/pii/S1359511324003970",
                                href="https://www.sciencedirect.com/science/article/pii/S1359511324003970",
                                target="_blank",
                                className="text-decoration-none text-primary fw-semibold"
                            ),
                            html.Hr()
                        ]),

                        html.Li([
                            html.H5(
                                "Genomic and phenotypic features of Acinetobacter baumannii isolated from oil reservoirs reveal a novel subspecies specialized in degrading hazardous hydrocarbons",
                                className="fw-bold text-dark",
                                style={"fontFamily": "'Times New Roman', serif"}
                            ),
                            html.P(
                                "Freitas, Júlia Firme; Silva, Douglas Felipe de Lima; Silva, Beatriz Soares; Castro, Jenielly Noronha Ferreira; Felipe, Marcus Bruno Mendonça Chaves; Silva-Portela, Renata Cláudia Brito; Minnicelli, Carolina Farah; Agnez-Lima, Lucymara Fassarella",
                                className="mb-1",
                                style={"fontFamily": "Arial, sans-serif"}
                            ),
                            html.P(
                                "Microbiological Research, Volume 273, 127420, August 2023",
                                className="mb-1",
                                style={"fontFamily": "Arial, sans-serif"}
                            ),
                            html.A(
                                "DOI: https://doi.org/10.1016/j.micres.2023.127420",
                                href="https://doi.org/10.1016/j.micres.2023.127420",
                                target="_blank",
                                className="text-decoration-none text-primary fw-semibold"
                            ),
                            html.Hr()
                        ]),

                        html.Li([
                            html.H5(
                                "MicroBioReToxiC (MicroBRTC) - A bioinformatics pipeline for analyzing the bioremediation potential of environmental pollutants in microorganisms",
                                className="fw-bold text-dark",
                                style={"fontFamily": "'Times New Roman', serif"}
                            ),
                            html.P(
                                "Silva, Douglas Felipe de Lima; Agnez-Lima, Lucymara Fassarella",
                                className="mb-1",
                                style={"fontFamily": "Arial, sans-serif"}
                            ),
                            html.P(
                                "Presented at the XXIV Encontro de Genética do Nordeste (XXIV ENGENE), 2023. *Winner of Oral Presentation Award*",
                                className="mb-1",
                                style={"fontFamily": "Arial, sans-serif"}
                            ),
                            html.Hr()
                        ])

                    ], style={"listStyleType": "none", "paddingLeft": 0})
                ])
            ])

        ]),
        className="py-4"
    )
