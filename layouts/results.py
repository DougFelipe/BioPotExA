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
from layouts.P15_sample_clustering_layout import get_sample_clustering_layout
from layouts.P16_sample_upset_layout import get_sample_upset_layout
from layouts.P17_gene_compound_network_layout import get_gene_compound_network_layout
def get_results_layout():
    return html.Div([
        html.H2('Data Analysis Results', className='results-title'),
        html.Hr(className="my-2"),
        html.H4('Results from your submitted data', className='results-subtitle'),
        
        # Resultado 1: Merge com o banco de 
                html.Div(
            [
                dbc.Placeholder(color="success", className="me-1 mt-1 w-100", size="xs"), 
            ]
        ),

        html.Div([
            html.H5("Main Results Table", className="analysis-title"),
            html.P(
                "This table presents the processed data merged with the main database, offering a comprehensive overview of the input data and its matched records.",
                className="analysis-description"
            ),
            html.P(
                "The merged table reveals how well the input data aligns with the main database, providing insights into the completeness and relevance of the data.",
                className="analysis-insights"
            ),
        ], className="analysis-header"),
        dbc.Accordion(
            [
                dbc.AccordionItem(
                    html.Div(id='output-merge-table'),
                    title="Results Table"
                ),
            ],
            start_collapsed=True,
            always_open=True,
        ),
        html.Div(
            [
                dbc.Placeholder(color="success", className="me-1 mt-1 w-100", size="xs"), 
            ]
        ),

        # Resultado 2: Merge com hadegDB
        html.Div([
            html.H5("Results Table (hadegDB)", className="analysis-title"),
            html.P(
                "This table contains data merged with the hadegDB database, enabling the exploration of additional annotations and insights.",
                className="analysis-description"
            ),
            html.P(
                "The table helps identify significant matches with hadegDB, enhancing the understanding of potential functional and structural associations.",
                className="analysis-insights"
            ),
        ], className="analysis-header"),
        dbc.Accordion(
            [
                dbc.AccordionItem(
                    html.Div(id='output-merge-hadeg-table'),
                    title="Results Table (hadegDB)"
                ),
            ],
            start_collapsed=True,
            always_open=True,
        ),
        html.Div(
            [
                dbc.Placeholder(color="success", className="me-1 mt-1 w-100", size="xs"), 
            ]
        ),

        # Resultado 3: Merge com ToxCSM
        html.Div([
            html.H5("Results Table (ToxCSM)", className="analysis-title"),
            html.P(
                "This table shows data merged with the ToxCSM database, providing toxicity predictions and compound interactions.",
                className="analysis-description"
            ),
            html.P(
                "By analyzing the merged table, you can assess the toxicity potential and prioritize compounds for further investigation.",
                className="analysis-insights"
            ),
        ], className="analysis-header"),
        dbc.Accordion(
            [
                dbc.AccordionItem(
                    html.Div(id='output-merge-toxcsm-table'),
                    title="Results Table (ToxCSM)"
                ),
            ],
            start_collapsed=True,
            always_open=True,
        ),
        html.Div(
            [
                dbc.Placeholder(color="success", className="me-1 mt-1 w-100", size="xs"), 
            ]
        ),

        # Grande accordion para os outros resultados
        dbc.Accordion(
            [
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
                dbc.AccordionItem(
                    get_sample_clustering_layout(),
                    title="Sample Clustering Dendrogram"
                ),
                dbc.AccordionItem(
                    get_sample_upset_layout(),
                    title="UpSet Plot: Amostras e KOs"
                ),
                dbc.AccordionItem(
                    get_gene_compound_network_layout(),
                    title="Gene-Compound Interaction Network",
                ),             
            ],
            start_collapsed=True,
            always_open=True,
        )
    ])
