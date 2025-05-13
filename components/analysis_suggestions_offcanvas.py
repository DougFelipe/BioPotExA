from dash import html
import dash_bootstrap_components as dbc

def analysis_suggestions_offcanvas(offcanvas_id="offcanvas-analysis-suggestions", is_open=False):
    return dbc.Offcanvas([
        dbc.Tabs([

                                    # Aba 1 - Por Perguntas Orientadoras
            dbc.Tab(label="Guiding Questions", children=[

                html.Div([
                    html.H6("1. Which samples have more genes associated with bioremediation?", className="fw-bold text-muted"),
                    html.Div(html.A("View: Gene Counts Across Samples", href="#gene-count-chart", className="text-primary mb-3"))
                ]),

                html.Div([
                    html.H6("2. Are gene distributions balanced across samples or are there outliers?", className="fw-bold text-muted"),
                    html.Div(html.A("View: Gene Distribution Among Samples", href="#violin-boxplot", className="text-primary mb-3"))
                ]),

                html.Div([
                    html.H6("3. Which pathways are most active across samples?", className="fw-bold text-muted"),
                    html.Div(html.A("View: Distribution of KO in Pathways", href="#pathway-ko-bar-chart", className="text-primary mb-3"))
                ]),

                html.Div([
                    html.H6("4. How do samples differ in pathway activity?", className="fw-bold text-muted"),
                    html.Div(html.A("View: Pathway Activity per Sample", href="#sample-ko-pathway-chart", className="text-primary mb-3"))
                ]),

                html.Div([
                    html.H6("5. Are there any outlier samples in terms of compound profile?", className="fw-bold text-muted"),
                    html.Div(html.A("View: Sample Clustering", href="#sample-clustering-dendrogram", className="text-primary mb-3"))
                ]),

                html.Div([
                    html.H6("6. Which genes are shared or unique across samples?", className="fw-bold text-muted"),
                    html.Div(html.A("View: Intersection Analysis", href="#sample-upset-plot", className="text-primary mb-3"))
                ]),

                html.Div([
                    html.H6("7. Which compounds are predicted to be most toxic?", className="fw-bold text-muted"),
                    html.Div(html.A("View: Toxicity Prediction Heatmap", href="#toxicity-heatmap-faceted", className="text-primary mb-3"))
                ]),

                html.Div([
                    html.H6("8. What are the strongest gene-compound associations?", className="fw-bold text-muted"),
                    html.Div(html.A("View: Gene-Compound Interaction Plot", href="#gene-compound-scatter-chart", className="text-primary mb-3"))
                ]),

                html.Div([
                    html.H6("9. Which samples interact with more compounds?", className="fw-bold text-muted"),
                    html.Div(html.A("View: Sample-Compound Interaction Plot", href="#compound-scatter-chart", className="text-primary mb-3"))
                ]),

                html.Div([
                    html.H6("10. What are the key gene-compound interaction networks?", className="fw-bold text-muted"),
                    html.Div(html.A("View: Gene-Compound Interaction", href="#gene-compound-network", className="text-primary mb-3"))
                ]),

                    html.Div([
                    html.H6("11. Which genes are most associated with each specific sample?", className="fw-bold text-muted"),
                    html.Div(html.A("View: Gene-Sample Heatmap", href="#gene-sample-heatmap", className="text-primary mb-3"))
                ]),

                html.Div([
                    html.H6("12. How do genes and samples interact for a specific pathway?", className="fw-bold text-muted"),
                    html.Div(html.A("View: Scatter Plot of KOs by Sample", href="#sample-ko-scatter", className="text-primary mb-3"))
                ]),

                html.Div([
                    html.H6("13. What are the key patterns in compound-pathway relationships?", className="fw-bold text-muted"),
                    html.Div(html.A("View: Pathway-Compound Interaction Map", href="#pathway-heatmap", className="text-primary mb-3"))
                ]),

                html.Div([
                    html.H6("14. What are the main compound groupings across samples?", className="fw-bold text-muted"),
                    html.Div(html.A("View: Sample Grouping by Compound Class Pattern", href="#sample-groups-chart", className="text-primary mb-3"))
                ]),

                html.Div([
                    html.H6("15. Which samples rank highest in compound interaction?", className="fw-bold text-muted"),
                    html.Div(html.A("View: Ranking of Samples by Compound Interaction", href="#sample-rank-compounds-chart", className="text-primary mb-3"))
                ]),

                html.Div([
                    html.H6("16. Which compounds are most connected to multiple samples?", className="fw-bold text-muted"),
                    html.Div(html.A("View: Ranking of Compounds by Sample Interaction", href="#compound-rank-chart", className="text-primary mb-3"))
                ]),

                html.Div([
                    html.H6("17. Which compounds are most linked to genetic activity?", className="fw-bold text-muted"),
                    html.Div(html.A("View: Ranking of Compounds by Gene Interaction", href="#compound-rank-gene-chart", className="text-primary mb-3"))
                ]),

                html.Div([
                    html.H6("18. Which enzymes or enzymatic activity are most frequently detected across the samples?", className="fw-bold text-muted"),
                    html.Div(html.A("View: Enzyme Activity by Sample", href="#sample-enzyme-activity", className="text-primary mb-3"))
                ]),

                html.Div([
                    html.H6("19. Which compounds are addressed according to the priority lists?", className="fw-bold text-muted"),
                    html.Div(html.A("View: Sample-Reference Agency Heatmap", href="#sample-reference-heatmap", className="text-primary mb-3"))
                ]),

                html.Div([
                    html.H6("20. What are the direct relationships between samples and individual genes?", className="fw-bold text-muted"),
                    html.Div(html.A("View: Sample-Gene Associations Plot", href="#sample-gene-scatter-chart", className="text-primary mb-3"))
                ])


            ]),

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
