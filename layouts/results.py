# layouts/results.py

from dash import html
import dash_bootstrap_components as dbc
from layouts.P1_KO_COUNT import get_ko_count_bar_chart_layout, get_ko_violin_boxplot_layout
from layouts.P2_KO_20PATHWAY import get_pathway_ko_bar_chart_layout, get_sample_ko_pathway_bar_chart_layout
from layouts.P3_compounds_layout import get_compound_scatter_layout
from layouts.P4_rank_compounds_layout import get_rank_compounds_layout

def get_results_layout():
    return html.Div([
        html.H2('Data Analysis Results', className='results-title'),
        html.Hr(className="my-2"),
        html.H4('Results from your submitted data', className='results-subtitle'),
        dbc.Accordion(
            [
                dbc.AccordionItem(
                    html.Div(id='output-merge-table'),  # Contêiner para a tabela mesclada
                    title="Results Table"
                ),
                dbc.AccordionItem(
                    get_ko_count_bar_chart_layout(),
                    title="Gene count associated with priority compounds",
                ),
                dbc.AccordionItem(
                    get_ko_violin_boxplot_layout(),
                    title="Distribution of genes associated with priority compounds"
                ),
                dbc.AccordionItem(
                    get_pathway_ko_bar_chart_layout(),
                    title="KEGG Xenobiotics Biodegradation and Metabolism (Grouped by Sample)"
                ),
                dbc.AccordionItem(
                    get_sample_ko_pathway_bar_chart_layout(),
                    title="KEGG Xenobiotics Biodegradation and Metabolism (Grouped by Pathway)"
                ),
                dbc.AccordionItem(
                    get_compound_scatter_layout(),
                    title="Scatter Plot of Samples vs Compounds"
                ),
                dbc.AccordionItem(
                    get_rank_compounds_layout(),
                    title="Ranking of Samples by Compound Interaction"
                ),
                # Adicionar mais análises conforme necessário
            ],
            start_collapsed=True,
            always_open=True,
        )
    ])
