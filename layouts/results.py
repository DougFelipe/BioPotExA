# my_dash_app/layouts/results.py

from dash import html
import dash_bootstrap_components as dbc
from layouts.P1_KO_COUNT import get_ko_count_layout
from layouts.P2_KO_20PATHWAY import get_ko_20pathway_layout

def get_results_layout():
    return html.Div([
        html.H2('Analysis Results', className='results-title'),
        html.Hr(className="my-2"),
        html.H4('Below are the analysis results from your submitted data.', className='results-subtitle'),
        dbc.Accordion(
            [
                dbc.AccordionItem(
                    get_ko_count_layout(),
                    title="KO Count Analysis"
                ),
                dbc.AccordionItem(
                    get_ko_20pathway_layout(),
                    title="KO Pathway Analysis"
                ),
            ],
            start_collapsed=True,
        )
    ])
