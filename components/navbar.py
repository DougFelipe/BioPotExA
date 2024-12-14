from dash import html

# Navbar ajustado com todas as sessões dentro de nav-links
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

                # Links organizados em uma única div "nav-links"
                html.Div(
                    [
                        # Sessão 1: Data Tables and Database Integration
                        html.P("1 - Data Tables and Database Integration", className="navbar-section-title"),
                        html.A("Main Results Table", href="#main-results-table", className="nav-link"),
                        html.A("Results Table (hadegDB)", href="#hadeg-results-table", className="nav-link"),
                        html.A("Results Table (ToxCSM)", href="#toxcsm-results-table", className="nav-link"),

                        # Sessão 2: Gene and Metabolic Pathway Analysis
                        html.P("2 - Gene and Metabolic Pathway Analysis", className="navbar-section-title"),
                        html.A("Gene Count Chart", href="#gene-count-chart", className="nav-link"),
                        html.A("Violin Boxplot", href="#violin-boxplot", className="nav-link"),
                        html.A("Pathway KO Bar Chart", href="#pathway-ko-bar-chart", className="nav-link"),
                        html.A("Sample KO Pathway Chart", href="#sample-ko-pathway-chart", className="nav-link"),
                        html.A("Scatter Plot of KOs by Sample", href="#sample-ko-scatter", className="nav-link"),

                        # Sessão 3: Interactions Between Entities
                        html.P("3 - Interactions Between Entities", className="navbar-section-title"),
                        html.A("Samples vs Compounds", href="#compound-scatter-chart", className="nav-link"),
                        html.A("Genes vs Compounds", href="#gene-compound-scatter-chart", className="nav-link"),
                        html.A("Samples vs Genes", href="#sample-gene-scatter-chart", className="nav-link"),
                        html.A("Enzyme Activity per Sample", href="#sample-enzyme-activity", className="nav-link"),
                        html.A("Gene-Compound Network", href="#gene-compound-network", className="nav-link"),

                        # Sessão 5: Patterns and Interactions with Heatmaps
                        html.P("5 - Patterns and Interactions with Heatmaps", className="navbar-section-title"),
                        html.A("Samples vs Reference AG", href="#sample-reference-heatmap", className="nav-link"),
                        html.A("Genes vs Samples Heatmap", href="#gene-sample-heatmap", className="nav-link"),
                        html.A("Pathways vs Compound Pathways", href="#pathway-heatmap", className="nav-link"),

                        # Sessão 6: Intersection and Group Exploration
                        html.P("6 - Intersection and Group Exploration", className="navbar-section-title"),
                        html.A("Sample Groups by Compound Class", href="#sample-groups-chart", className="nav-link"),
                        html.A("Sample UpSet Plot", href="#sample-upset-plot", className="nav-link"),
                        html.A("Sample Clustering Dendrogram", href="#sample-clustering-dendrogram", className="nav-link"),

                        # Sessão 7: Toxicity Predictions
                        html.P("7 - Toxicity Predictions", className="navbar-section-title"),
                        html.A("Comprehensive Toxicity Heatmap", href="#toxicity-heatmap-faceted", className="nav-link"),
                    ],
                    className="nav-links",  # Todos os links e títulos dentro de um único contêiner
                ),
            ],
            className="navbar-menu-container",  # Contêiner geral do menu
        ),
    ],
    className="navbar-container",  # Classe principal para o navbar
)
