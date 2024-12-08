from dash import html

# Navbar ajustado com título, subtítulo e links organizados
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
                # Links para os gráficos
                html.Div(
                    [
                        html.A("Main Results Table", href="#main-results-table", className="nav-link"),
                        html.A("Results Table (hadegDB)", href="#hadeg-results-table", className="nav-link"),
                        html.A("Results Table (ToxCSM)", href="#toxcsm-results-table", className="nav-link"),
                        html.A("Gene Count Chart", href="#gene-count-chart", className="nav-link"),
                        html.A("Violin Boxplot", href="#violin-boxplot", className="nav-link"),
                        html.A("Pathway KO Bar Chart", href="#pathway-ko-bar-chart", className="nav-link"),
                        html.A("Sample KO Pathway Chart", href="#sample-ko-pathway-chart", className="nav-link"),
                        html.A("Samples vs Compounds", href="#compound-scatter-chart", className="nav-link"),
                        html.A("Sample Ranking by Compounds", href="#sample-rank-compounds-chart", className="nav-link"),
                        html.A("Compound Ranking by Samples", href="#compound-rank-chart", className="nav-link"),
                        html.A("Compound Ranking by Genes", href="#compound-rank-gene-chart", className="nav-link"),
                        html.A("Genes vs Compounds", href="#gene-compound-scatter-chart", className="nav-link"),
                        html.A("Samples vs Genes", href="#sample-gene-scatter-chart", className="nav-link"),
                        html.A("Samples vs Reference AG", href="#sample-reference-heatmap", className="nav-link"),
                        html.A("Sample Groups by Compound Class", href="#sample-groups-chart", className="nav-link"),
                        html.A("Genes vs Samples Heatmap", href="#gene-sample-heatmap", className="nav-link"),
                        html.A("Pathways vs Compound Pathways", href="#pathway-heatmap", className="nav-link"),
                        html.A("Scatter Plot of KOs by Sample", href="#sample-ko-scatter", className="nav-link"),
                        html.A("Enzyme Activity per Sample", href="#sample-enzyme-activity", className="nav-link"),
                        html.A("Sample Clustering Dendrogram", href="#sample-clustering-dendrogram", className="nav-link"),
                        html.A("Sample UpSet Plot", href="#sample-upset-plot", className="nav-link"),
                        html.A("Gene-Compound Network", href="#gene-compound-network", className="nav-link"),
                    ],
                    className="nav-links",  # Classe CSS para organizar os links
                ),
            ],
            className="navbar-menu-container",  # Contêiner para hover
        ),
    ],
    className="navbar-container",  # Classe principal para o navbar
)
