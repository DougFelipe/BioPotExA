from dash import html
import dash_bootstrap_components as dbc

def analysis_suggestions_modal(modal_id="modal-analysis-suggestions", is_open=False):
    return dbc.Modal([
        dbc.ModalHeader(dbc.ModalTitle("Suggestions to Explore Your Results")),
        dbc.ModalBody([
            dbc.Tabs([
                dbc.Tab(label="Basic Exploration", children=[
                    html.H6("Recommended Sections:", className="text-success fw-semibold"),
                    html.Ul([
                        html.Li(html.A("Gene Count Chart", href="#gene-count-chart", className="text-primary")),
                        html.Li(html.A("BioRemPP Table", href="#main-results-table", className="text-primary")),
                        html.Li(html.A("Toxicity Heatmap", href="#toxicity-heatmap-faceted", className="text-primary"))
                    ]),
                    html.H6("Guiding Questions:", className="mt-3 text-muted"),
                    html.Ul([
                        html.Li("Which samples have more associated genes?"),
                        html.Li("Are any compounds flagged as toxic?")
                    ])
                ]),
                # Tabs para outras categorias...
            ])
        ]),
        dbc.ModalFooter(
            dbc.Button("Close", id="close-suggestions-modal", className="ms-auto", color="secondary")
        )
    ], id=modal_id, is_open=is_open, size="lg", centered=True)
