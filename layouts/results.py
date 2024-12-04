from dash import html
import dash_bootstrap_components as dbc
from layouts.P1_KO_COUNT import get_ko_count_bar_chart_layout, get_ko_violin_boxplot_layout
from layouts.P2_KO_20PATHWAY import get_pathway_ko_bar_chart_layout, get_sample_ko_pathway_bar_chart_layout
from layouts.P3_compounds_layout import get_compound_scatter_layout
from layouts.P4_rank_compounds_layout import get_rank_compounds_layout as get_sample_rank_compounds_layout
from layouts.P5_rank_compounds_layout import get_rank_compounds_layout as get_compound_rank_layout
from layouts.P6_rank_compounds_layout import get_rank_compounds_gene_layout
from layouts.P7_compound_x_genesymbol_layoyt import get_gene_compound_scatter_layout
from layouts.P8_sample_x_genesymbol_layout import get_sample_gene_scatter_layout
from layouts.P9_sample_x_referenceAG_layout import get_sample_reference_heatmap_layout
from layouts.P10_sample_grouping_profile_layout import get_sample_groups_layout
from layouts.P11_layout import get_gene_sample_heatmap_layout
from layouts.P12_layout import get_pathway_heatmap_layout
from layouts.P13_layout import get_sample_ko_scatter_layout
from layouts.P14_sample_enzyme_activity_layout import get_sample_enzyme_activity_layout

def get_results_layout():
    return html.Div([
        html.H2('Data Analysis Results', className='results-title'),
        html.Hr(className="my-2"),
        html.H4('Results from your submitted data', className='results-subtitle'),
        dbc.Accordion(
            [
                dbc.AccordionItem(
                    html.Div(id='output-merge-table'),
                    title="Results Table"
                ),
                dbc.AccordionItem(
                    html.Div(id='output-merge-hadeg-table'),  # Contêiner para a tabela mesclada com hadegDB
                    title="Results Table (hadegDB)"
                ),
                dbc.AccordionItem(
                    html.Div(id='output-merge-toxcsm-table'),  # Contêiner para a tabela mesclada com ToxCSM
                    title="Results Table (ToxCSM)"
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
                    get_sample_ko_scatter_layout(),
                    title="Scatter Plot of KOs by Sample for Pathway"
                ),
                dbc.AccordionItem(
                    get_compound_scatter_layout(),
                    title="Scatter Plot of Samples vs Compounds"
                ),
                dbc.AccordionItem(
                    get_sample_rank_compounds_layout(),
                    title="Ranking of Samples by Compound Interaction"
                ),
                dbc.AccordionItem(
                    get_compound_rank_layout(),
                    title="Ranking of Compounds by Sample Interaction"
                ),
                dbc.AccordionItem(
                    get_rank_compounds_gene_layout(),
                    title="Ranking of Compounds by Gene Interaction"
                ),
                dbc.AccordionItem(
                    get_gene_compound_scatter_layout(),
                    title="Scatter Plot of Genes vs Compounds"
                ),
                dbc.AccordionItem(
                    get_sample_gene_scatter_layout(),
                    title="Scatter Plot of Samples vs Genes"
                ),
                dbc.AccordionItem(
                    get_sample_reference_heatmap_layout(),
                    title="Heatmap of Samples vs Reference AG"
                ),
                dbc.AccordionItem(
                    get_sample_groups_layout(),
                    title="Sample Groups by Compound Class"
                ),
                dbc.AccordionItem(
                    get_gene_sample_heatmap_layout(),
                    title="Heatmap of Genes vs Samples"
                ),
                dbc.AccordionItem(
                    get_pathway_heatmap_layout(),
                    title="Heatmap of Pathways vs Compound Pathways"
                ),
                dbc.AccordionItem(
                    get_sample_enzyme_activity_layout(),
                    title="Enzyme Activity Counts per Sample"
        ),               
            ],
            start_collapsed=True,
            always_open=True,
        )
    ])