# components/publications.py
from dash import html

def get_publications_layout():
    return html.Div([
        # Título
        html.Div([
            html.H2('Previous Publications', className='how-to-use'),
            html.Hr(className="my-2"),
        ], className='title-container'),

        # Lista de publicações
        html.Div(
            id='related-publications-card',
            className='upload-process-card-style',
            children=[
                html.Div([
                    html.Ul([
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
        )
    ])
