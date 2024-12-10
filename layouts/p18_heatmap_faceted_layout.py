from dash import html, dcc

def get_toxicity_heatmap_layout():
    """
    Retorna o layout do heatmap de toxicidade.
    """
    return html.Div(
        className="toxicity-heatmap-section",
        children=[
            html.H5("Toxicity Heatmap", className="analysis-title"),
            html.P(
                "This heatmap shows the toxicity predictions grouped into key categories, "
                "such as Nuclear Response, Stress Response, Genomic, Environmental, and Organic.",
                className="analysis-description"
            ),
            html.P(
                "By analyzing this heatmap, you can identify patterns and relationships "
                "between compounds and their toxicity profiles.",
                className="analysis-insights"
            ),
            dcc.Graph(id="toxicity-heatmap-faceted", className="chart-container"),
        ]
    )
