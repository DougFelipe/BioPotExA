from dash import html
import dash_bootstrap_components as dbc

# Navbar ajustado com todas as sessões como dbc.Cards
navbar = html.Div(
    [
        # Título da aplicação
        html.A(
            "BioRemPP",
            href="/",
            className="navbar-title",  # Classe CSS para o título
        ),
        # Contêiner para subtítulo e links
        html.Div(
            [
                # Subtítulo da aplicação
                html.P(
                    "Navigation Menu",
                    className="navbar-subtitle",  # Classe CSS para o subtítulo
                ),

                # Links organizados em dbc.Cards para 7 sessões
                html.Div(
                    [
                        # Sessão 1: Data Tables and Database Integration
                        dbc.Card(
                            dbc.CardBody(
                                [
                                    html.H5("Data Tables and Database Integration", className="card-title"),
                                    html.A("BioRemPP Results Table", href="#main-results-table", className="nav-link"),
                                    html.A("HADEG Results Table", href="#hadeg-results-table", className="nav-link"),
                                    html.A("ToxCSM Results Table", href="#toxcsm-results-table", className="nav-link"),
                                ]
                            ),
                            className="nav-card",
                        ),

                        # Sessão 2: Gene and Metabolic Pathway Analysis
                        dbc.Card(
                            dbc.CardBody(
                                [
                                    html.H5("Gene and Metabolic Pathway Analysis", className="card-title"),
                                    html.A("Gene Counts Across Samples", href="#gene-count-chart", className="nav-link"),
                                    html.A("Gene Distribution Among Samples", href="#violin-boxplot", className="nav-link"),
                                    html.A("Distribution of KO in Pathways", href="#pathway-ko-bar-chart", className="nav-link"),
                                    html.A("Pathway Activity per Sample", href="#sample-ko-pathway-chart", className="nav-link"),
                                    html.A("Scatter Plot of KOs by Sample", href="#sample-ko-scatter", className="nav-link"),
                                ]
                            ),
                            className="nav-card",
                        ),

                        # Sessão 3: Interactions Between Entities
                        dbc.Card(
                            dbc.CardBody(
                                [
                                    html.H5("Interactions Between Entities", className="card-title"),
                                    html.A("Sample-Compound Interaction", href="#compound-scatter-chart", className="nav-link"),
                                    html.A("Gene-Compound Interaction", href="#gene-compound-scatter-chart", className="nav-link"),
                                    html.A("Sample-Gene Associations", href="#sample-gene-scatter-chart", className="nav-link"),
                                    html.A("Enzyme Activity by Sample", href="#sample-enzyme-activity", className="nav-link"),
                                    html.A("Gene-Compound Network", href="#gene-compound-network", className="nav-link"),
                                ]
                            ),
                            className="nav-card",
                        ),

                        # Sessão 4: Ranking and Prioritization
                        dbc.Card(
                            dbc.CardBody(
                                [
                                    html.H5("Ranking and Prioritization", className="card-title"),
                                    html.A("Ranking of Samples by Compound Interaction", href="#sample-rank-compounds-chart", className="nav-link"),
                                    html.A("Ranking of Compounds by Sample Interaction", href="#compound-rank-chart", className="nav-link"),
                                    html.A("Ranking of Compounds by Gene Interaction", href="#compound-rank-gene-chart", className="nav-link"),
                                ]
                            ),
                            className="nav-card",
                        ),

                        # Sessão 5: Patterns and Interactions with Heatmaps
                        dbc.Card(
                            dbc.CardBody(
                                [
                                    html.H5("Patterns and Interactions with Heatmaps", className="card-title"),
                                    html.A("Sample-Reference Agency Heatmap", href="#sample-reference-heatmap", className="nav-link"),
                                    html.A("Gene-Sample Heatmap", href="#gene-sample-heatmap", className="nav-link"),
                                    html.A("Pathway-Compound Interaction Map", href="#pathway-heatmap", className="nav-link"),
                                ]
                            ),
                            className="nav-card",
                        ),

                        # Sessão 6: Intersection and Group Exploration
                        dbc.Card(
                            dbc.CardBody(
                                [
                                    html.H5("Intersection and Group Exploration", className="card-title"),
                                    html.A("Sample Grouping by Compound Class Pattern", href="#sample-groups-chart", className="nav-link"),
                                    html.A("Intersection Analysis", href="#sample-upset-plot", className="nav-link"),
                                    html.A("Clustering Dendrogram", href="#sample-clustering-dendrogram", className="nav-link"),
                                ]
                            ),
                            className="nav-card",
                        ),

                        # Sessão 7: Toxicity Predictions
                        dbc.Card(
                            dbc.CardBody(
                                [
                                    html.H5("Toxicity Predictions", className="card-title"),
                                    html.A("Comprehensive Toxicity Prediction Heatmap", href="#toxicity-heatmap-faceted", className="nav-link"),
                                ]
                            ),
                            className="nav-card",
                        ),
                    ],
                    className="nav-links",  # Contêiner geral com todos os cards
                ),
            ],
            className="navbar-menu-container",  # Contêiner geral do menu
        ),
    ],
    className="navbar-container",  # Classe principal para o navbar
)
