from dash import html, dcc

def get_toxicity_heatmap_layout():
    """
    Constructs the layout for the Toxicity Heatmap with facets.

    Returns:
        A `html.Div` containing the graph of the Toxicity Heatmap.
    """
    return html.Div([
        # Heatmap Graph
        html.Div(
            dcc.Graph(
                id="toxicity-heatmap-faceted",
                className="chart-container",
                style={"overflow": "auto"}  # Adiciona rolagem ao container do gráfico
            ),
            className="graph-card"
        )
    ])
