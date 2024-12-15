from dash import dcc, html

def get_gene_compound_network_layout():
    """
    Constructs the layout for the Gene-Compound Interaction Network graph.

    Returns:
        A `html.Div` containing the graph for the Gene-Compound Interaction Network.
    """
    return html.Div([
        # Gene-Compound Network Graph
        html.Div(
            dcc.Graph(
                id="gene-compound-network-graph",
                config={"displayModeBar": True, "scrollZoom": True},
                style={"height": "600px", "width": "100%"}  # Define height and full width
            ),
            className="chart-container"
        ),
        # Placeholder visual (if necessary)
        html.Div(
            className="placeholder-container",
            children=[
                html.Div(
                    className="placeholder-card",
                    children=[
                        html.P("No data to display", className="placeholder-text")
                    ]
                )
            ],
        )
    ], className="graph-card")  # Wrapper div for consistent styling
