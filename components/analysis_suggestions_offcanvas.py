from dash import html
import dash_bootstrap_components as dbc

def analysis_suggestions_offcanvas(offcanvas_id="offcanvas-analysis-suggestions", is_open=False):
    return dbc.Offcanvas([
        dbc.Tabs([
            dbc.Tab(label="Basic Exploration", children=[
                html.H6("Sections:", className="text-success fw-semibold"),
                html.Ul([
                    html.Li(html.A("BioRemPP Results Table", href="#main-results-table", className="text-primary")),
                    html.Li(html.A("HADEG Results Table", href="#hadeg-results-table", className="text-primary")),
                    html.Li(html.A("ToxCSM Results Table", href="#toxcsm-results-table", className="text-primary")),
                    html.Li(html.A("Gene Counts Across Samples", href="#gene-count-chart", className="text-primary")),
                    html.Li(html.A("Toxicity Prediction Heatmap", href="#toxicity-heatmap-faceted", className="text-primary"))
                ]),

                html.Hr(className="my-3"),

                dbc.Row([
                    dbc.Col(
                        dbc.Card([
                            dbc.CardHeader("🧭 Guiding Questions", className="fw-bold text-muted"),
                            dbc.CardBody([
                                html.Ul([
                                    html.Li("Which samples show more genes associated with biodegradation?"),
                                    html.Li("Are there any compounds predicted as toxic?"),
                                    html.Li("How many entries were matched in the BioRemPP and HADEG databases?"),
                                    html.Li("Do compounds with more gene associations also show higher toxicity?"),
                                    html.Li("Are there samples with little or no database matches?")
                                ], className="mb-0")
                            ])
                        ], className="h-100 shadow-sm"),
                        width=6
                    ),
                    dbc.Col(
                        dbc.Card([
                            dbc.CardHeader("🔍 Suggested Interpretation", className="fw-bold text-muted"),
                            dbc.CardBody([
                                html.Ul([
                                    html.Li("Higher gene counts may indicate richer metabolic potential in specific samples."),
                                    html.Li("Toxicity predictions can help prioritize compounds for closer inspection."),
                                    html.Li("Initial table matches provide a general sense of sample relevance in bioremediation contexts."),
                                    html.Li("Co-occurrence of gene richness and toxicity may indicate complex biodegradation scenarios."),
                                    html.Li("Samples with low matches may require improved annotation or could represent novel profiles.")
                                ], className="mb-0")
                            ])
                        ], className="h-100 shadow-sm"),
                        width=6
                    )
                ], className="g-3 mt-2")

            ])
        ])
    ],
    id=offcanvas_id,
    title="Suggestions to Explore Your Results",
    is_open=is_open,
    placement="bottom",
    scrollable=True,
    backdrop=True,
    class_name="p-3",
    style={"maxWidth": "100%", "zIndex": 1051}
)
