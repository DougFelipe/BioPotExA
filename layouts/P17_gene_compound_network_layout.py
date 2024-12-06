from dash import dcc, html
import dash_bootstrap_components as dbc

def get_gene_compound_network_layout():
    """
    Retorna o layout para o gráfico de rede Gene-Compound.
    """
    return html.Div(
        className="gene-compound-network-container",
        children=[
            # Título da análise
            html.Div(
                className="analysis-header",
                children=[
                    html.H5("Gene-Compound Interaction Network", className="analysis-title"),
                    html.P(
                        "This visualization shows interactions between genes and compounds, highlighting relationships that are key for understanding biodegradation pathways.",
                        className="analysis-description",
                    ),
                    html.P(
                        "By analyzing this network, you can identify compounds influenced by multiple genes or genes associated with various compounds, which may indicate functional hotspots or essential genes.",
                        className="analysis-insights",
                    ),
                ],
            ),
            # Gráfico de rede (dcc.Graph)
            dbc.Accordion(
                [
                    dbc.AccordionItem(
                        title="Gene-Compound Interaction Network",
                        children=[
                            dcc.Graph(
                                id="gene-compound-network-graph",
                                config={"displayModeBar": True, "scrollZoom": True},
                                style={"height": "600px", "width": "100%"},
                            )
                        ],
                    )
                ],
                start_collapsed=False,
                always_open=True,
            ),
            # Placeholder visual
            html.Div(
                [
                    dbc.Placeholder(size="xs", className="me-1 mt-1 w-100", color="success"),
                ],
            ),
        ],
    )
