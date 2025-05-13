from dash import html
import dash_bootstrap_components as dbc

def analysis_suggestions_offcanvas(offcanvas_id="offcanvas-analysis-suggestions", is_open=False):
    return dbc.Offcanvas([
        dbc.Tabs([

            # Aba 1 - Exploração Básica
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
                        ], className="h-100 shadow-sm"), width=6
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
                        ], className="h-100 shadow-sm"), width=6
                    )
                ], className="g-3 mt-2")
            ]),

            # Aba 2 - Por Tipo de Dado ou Entidade
            dbc.Tab(label="By Data Type / Entity", children=[
                html.H6("Genes", className="text-success fw-semibold"),
                html.Ul([
                    html.Li(html.A("Gene Counts Across Samples", href="#gene-count-chart", className="text-primary")),
                    html.Li(html.A("Gene Distribution Among Samples", href="#violin-boxplot", className="text-primary")),
                    html.Li(html.A("Intersection Analysis", href="#sample-upset-plot", className="text-primary")),
                ]),
                html.H6("Metabolic Pathways", className="text-success fw-semibold mt-3"),
                html.Ul([
                    html.Li(html.A("Distribution of KO in Pathways", href="#pathway-ko-bar-chart", className="text-primary")),
                    html.Li(html.A("Pathway Activity per Sample", href="#sample-ko-pathway-chart", className="text-primary")),
                    html.Li(html.A("Pathway-Compound Interaction Map", href="#pathway-heatmap", className="text-primary"))
                ]),
                html.H6("Compounds", className="text-success fw-semibold mt-3"),
                html.Ul([
                    html.Li(html.A("Toxicity Prediction Heatmap", href="#toxicity-heatmap-faceted", className="text-primary")),
                    html.Li(html.A("Gene-Compound Interaction Plot", href="#gene-compound-scatter-chart", className="text-primary")),
                    html.Li(html.A("Ranking of Compounds by Gene Interaction", href="#compound-rank-gene-chart", className="text-primary"))
                ]),
                html.H6("Samples", className="text-success fw-semibold mt-3"),
                html.Ul([
                    html.Li(html.A("BioRemPP Results Table", href="#main-results-table", className="text-primary")),
                    html.Li(html.A("Sample-Pathway Specific  Activity", href="#sample-ko-pathway-chart", className="text-primary")),
                    html.Li(html.A("Sample Clustering", href="#sample-clustering-dendrogram", className="text-primary"))
                ]),
                html.H6("Associations & Interactions", className="text-success fw-semibold mt-3"),
                html.Ul([
                    html.Li(html.A("Sample-Compound Interaction Plot", href="#compound-scatter-chart", className="text-primary")),
                    html.Li(html.A("Gene-Compound Interaction", href="#gene-compound-network", className="text-primary")),
                    html.Li(html.A("Gene-Sample Heatmap", href="#gene-sample-heatmap", className="text-primary"))
                ]),

                html.Hr(className="my-3"),

                dbc.Row([
                    dbc.Col(
                        dbc.Card([
                            dbc.CardHeader("🧭 Guiding Questions", className="fw-bold text-muted"),
                            dbc.CardBody([
                                html.Ul([
                                    html.Li("Which genes appear most frequently across samples?"),
                                    html.Li("Are there dominant pathways in specific samples?"),
                                    html.Li("Do any samples cluster based on gene presence?"),
                                    html.Li("Which compounds have stronger gene associations?"),
                                    html.Li("Which pathways show the highest enzymatic activity?"),
                                    html.Li("How do compound toxicities vary across samples?"),
                                    html.Li("Do certain genes appear only in specific groups?"),
                                    html.Li("Which interactions are most central in the networks?"),
                                    html.Li("What patterns emerge from gene-sample heatmaps?"),
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
                                    html.Li("Frequent genes may indicate conserved metabolic potential."),
                                    html.Li("Dominant pathways might signal sample specialization."),
                                    html.Li("Gene-based clusters suggest functional groupings among samples."),
                                    html.Li("Stronger associations may imply compound reactivity or biodegradability."),
                                    html.Li("Pathway activity levels can highlight metabolic efficiency."),
                                    html.Li("High toxicity variance may suggest selectivity in bioremediation targets."),
                                    html.Li("Gene exclusivity may reveal niche adaptation or novel traits."),
                                    html.Li("Highly connected nodes in interaction networks can represent key players."),
                                    html.Li("Heatmaps reveal co-occurrence patterns."),
                                ], className="mb-0")
                            ])
                        ], className="h-100 shadow-sm"),
                        width=6
                    )
                ], className="g-3 mt-2")
            ]),

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
