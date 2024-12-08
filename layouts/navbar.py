from dash import html
import dash_bootstrap_components as dbc

# Navbar ajustado com botão para abrir o offcanvas
navbar = html.Div(
    [
        # Título da aplicação "BioRemPP"
        html.A(
            "BioRemPP",
            href="/",
            className="navbar-title",  # Classe CSS para customizar o estilo
        ),
        # Botão para abrir o menu (offcanvas)
        dbc.Button(
            "Open Navigation Menu",  # Texto do botão
            id="open-navigation-menu",  # ID para callback
            color="primary",
            className="open-menu-button",  # Classe CSS para customização
        ),
        # Offcanvas para os links
        dbc.Offcanvas(
            [
                # Título no topo do offcanvas
                html.H5("Navigation Menu", className="offcanvas-title"),
                # Links do menu
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
                    className="offcanvas-links-container",  # Classe CSS para personalizar os links
                ),
            ],
            id="navigation-offcanvas",  # ID para o offcanvas
            placement="top",
            scrollable=True,
            backdrop=False,
            is_open=False,  # Controlado pelo callback
        ),
    ],
    className="navbar-container",
)
