from dash import html
import dash_bootstrap_components as dbc

def analysis_suggestions_offcanvas(offcanvas_id="offcanvas-analysis-suggestions", is_open=False):
    return dbc.Offcanvas([
        dbc.Tabs([
            dbc.Tab(label="Basic Exploration", children=[
                html.H6("Recommended Sections:", className="text-success fw-semibold"),
                html.Ul([
                    html.Li(html.A("Gene Count Chart", href="#gene-count-chart", className="text-primary")),
                    html.Li(html.A("BioRemPP Table", href="#main-results-table", className="text-primary")),
                    html.Li(html.A("Toxicity Heatmap", href="#toxicity-heatmap-faceted", className="text-primary"))
                ]),
                html.H6("Guiding Questions:", className="mt-4 text-muted"),
                html.Ul([
                    html.Li("Which samples have more associated genes?"),
                    html.Li("Are any compounds flagged as toxic?"),
                    html.Li("Do most genes fall within expected metabolic pathways?")
                ]),
                html.H6("Suggested Interpretation:", className="mt-4 text-muted"),
                html.Ul([
                    html.Li("Higher gene counts may suggest greater metabolic potential or contaminant diversity."),
                    html.Li("Toxic compounds flagged by ToxCSM can guide sample prioritization."),
                    html.Li("Initial observations can help filter samples for deeper pathway analysis.")
                ])
            ])
        ])
    ],
    id=offcanvas_id,
    title="Suggestions to Explore Your Results",
    is_open=is_open,
    placement="top",
    scrollable=True,
    backdrop=True,
    class_name="p-3",
    style={"maxWidth": "100%", "zIndex": 1051}
)
