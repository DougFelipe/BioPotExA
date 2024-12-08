from dash import html

# Navbar fixo no topo da página com o título e links
navbar = html.Div(
    [
        # Nome "BioRemPP" como link para a homepage
        html.A(
            "BioRemPP",  # Nome da aplicação
            href="/",  # Link para a homepage
            className="navbar-brand",  # Classe para customizar o estilo
            style={
                "fontSize": "24px",
                "fontWeight": "bold",
                "textDecoration": "none",
                "color": "#007BFF",  # Azul (ou qualquer cor que desejar)
                "marginRight": "20px",  # Espaçamento para separação dos links
            },
        ),
        # Links para as seções
        html.A("Main Results Table", href="#main-results-table", className="nav-link"),
        html.A("Results Table (hadegDB)", href="#hadeg-results-table", className="nav-link"),
        html.A("Results Table (ToxCSM)", href="#toxcsm-results-table", className="nav-link"),
        html.A("Gene Count Chart", href="#gene-count-chart", className="nav-link"),
    ],
    className="navbar",
    style={
        "position": "fixed",
        "top": "0",
        "width": "100%",
        "backgroundColor": "#F8F9FA",  # Cor de fundo do menu
        "padding": "10px 20px",  # Espaçamento interno
        "zIndex": "1000",  # Garantir que fique acima de outros elementos
        "boxShadow": "0px 4px 8px rgba(0, 0, 0, 0.1)",  # Sombra para destaque
        "display": "flex",
        "alignItems": "center",
    },
)
