from layouts.navbar import navbar  # Importe o navbar definido acima
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
        # Navbar fixo no topo da página
        navbar,

        # Espaçamento para compensar o menu fixo
        html.Div(style={"height": "100px"}),

        # Título principal
        html.H2('Data Analysis Results', className='results-title'),
        html.Hr(className="my-2"),
        html.H4('Results from your submitted data', className='results-subtitle'),

        # Seção 1: Main Results Table
        html.Div(id="main-results-table", className="section"),
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
            dbc.Accordion(
                [
                    dbc.AccordionItem(
                        html.Div(id='output-merge-table'),
                        title="Results Table"
                    )
                ],
                start_collapsed=True,
                always_open=True,
            ),
        ], className="analysis-header"),
        html.Div([dbc.Placeholder(color="success", className="me-1 mt-1 w-100", size = "xs"),]),

        # Seção 2: Results Table (hadegDB)
        html.Div(id="hadeg-results-table", className="section"),
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
            dbc.Accordion(
                [
                    dbc.AccordionItem(
                        html.Div(id='output-merge-hadeg-table'),
                        title="Results Table (hadegDB)"
                    )
                ],
                start_collapsed=True,
                always_open=True,
            ),
        ], className="analysis-header"),
        html.Div([dbc.Placeholder(color="success", className="me-1 mt-1 w-100", size = "xs"),]),

        # Seção 3: Results Table (ToxCSM)
        html.Div(id="toxcsm-results-table", className="section"),
        html.Div([
            html.H5("Results Table (ToxCSM)", className="analysis-title"),
            html.P(
                "This table shows data merged with the ToxCSM database, providing toxicity predictions and compound interactions.",
                className="analysis-description"
            ),
            html.P(
                "By analyzing this table, you can assess the toxicity potential and prioritize compounds for further investigation.",
                className="analysis-insights"
            ),
            dbc.Accordion(
                [
                    dbc.AccordionItem(
                        html.Div(id='output-merge-toxcsm-table'),
                        title="Results Table (ToxCSM)"
                    )
                ],
                start_collapsed=True,
                always_open=True,
            ),
        ], className="analysis-header"),
        html.Div([dbc.Placeholder(color="success", className="me-1 mt-1 w-100", size = "xs"),]),

        # Seção 4: Gene Count Chart
        html.Div(id="gene-count-chart", className="section"),
        html.Div([
            html.H5("Gene Count Associated with Priority Compounds", className="analysis-title"),
            html.P(
                "This bar chart displays the count of unique genes associated with priority compounds for each sample.",
                className="analysis-description"
            ),
            html.P(
                "By analyzing this chart, you can identify which samples have a higher number of unique gene associations, offering insights into potential hotspots of genetic activity.",
                className="analysis-insights"
            ),
            dbc.Accordion(
                [
                    dbc.AccordionItem(
                        html.Div(get_ko_count_bar_chart_layout(), className="chart-container"),
                        title="Gene Count Bar Chart"
                    )
                ],
                start_collapsed=True,
                always_open=False,
            ),
        ], className="analysis-header"),
        html.Div([dbc.Placeholder(color="success", className="me-1 mt-1 w-100", size = "xs"),]),

        # Seção 5: Violin Boxplot
        html.Div(id="violin-boxplot", className="section"),
        html.Div([
            html.H5("Violin Boxplot for Gene Distribution", className="analysis-title"),
            html.P(
                "This violin boxplot illustrates the distribution of unique genes associated with priority compounds across samples.",
                className="analysis-description"
            ),
            html.P(
                "This visualization helps identify patterns and variability in gene distribution, highlighting sample-specific trends.",
                className="analysis-insights"
            ),
            dbc.Accordion(
                [
                    dbc.AccordionItem(
                        html.Div(get_ko_violin_boxplot_layout(), className="chart-container"),
                        title="Violin Boxplot"
                    )
                ],
                start_collapsed=True,
                always_open=False,
            ),
        ], className="analysis-header"),
        html.Div([dbc.Placeholder(color="success", className="me-1 mt-1 w-100", size = "xs"),]),
        
        
        # Seção 6: Pathway KO Bar Chart
        html.Div(id="pathway-ko-bar-chart", className="section"),  # ID para link no navbar
        html.Div([
            html.H5("Pathway KO Bar Chart", className="analysis-title"),
            html.P(
                "This bar chart highlights the distribution of KEGG Ortholog (KO) counts across various pathways.",
                className="analysis-description"
            ),
            html.P(
                "By analyzing this chart, you can gain insights into the functional diversity of pathways influenced by the data.",
                className="analysis-insights"
            ),
            dbc.Accordion(
                [
                    dbc.AccordionItem(
                        html.Div(get_pathway_ko_bar_chart_layout(), className="chart-container"),
                        title="Pathway KO Bar Chart"
                    )
                ],
                start_collapsed=True,
                always_open=False,
            ),
        ], className="analysis-header"),
        html.Div([dbc.Placeholder(color="success", className="me-1 mt-1 w-100", size="xs")]),

                # Seção 7: Sample KO Pathway Chart
        html.Div(id="sample-ko-pathway-chart", className="section"),  # ID para link no navbar
        html.Div([
            html.H5("Sample KO Pathway Chart", className="analysis-title"),
            html.P(
                "This bar chart presents the KEGG Ortholog (KO) distribution across pathways, grouped by sample.",
                className="analysis-description"
            ),
            html.P(
                "This visualization allows you to understand how different pathways are represented within each sample, helping to identify pathway-specific trends.",
                className="analysis-insights"
            ),
            dbc.Accordion(
                [
                    dbc.AccordionItem(
                        html.Div(get_sample_ko_pathway_bar_chart_layout(), className="chart-container"),
                        title="Sample KO Pathway Bar Chart"
                    )
                ],
                start_collapsed=True,
                always_open=False,
            ),
        ], className="analysis-header"),
        html.Div([dbc.Placeholder(color="success", className="me-1 mt-1 w-100", size="xs")]),
        

                # Seção 8: Scatter Plot of Samples vs Compounds
        html.Div(id="compound-scatter-chart", className="section"),  # ID para link no navbar
        html.Div([
            html.H5("Scatter Plot of Samples vs Compounds", className="analysis-title"),
            html.P(
                "This scatter plot visualizes the relationship between samples and compounds, highlighting the interactions between these entities.",
                className="analysis-description"
            ),
            html.P(
                "By exploring this chart, you can identify key interactions and trends, helping to focus on samples or compounds of interest.",
                className="analysis-insights"
            ),
            dbc.Accordion(
                [
                    dbc.AccordionItem(
                        html.Div(get_compound_scatter_layout(), className="chart-container"),
                        title="Scatter Plot of Samples vs Compounds"
                    )
                ],
                start_collapsed=True,
                always_open=False,
            ),
        ], className="analysis-header"),
        html.Div([dbc.Placeholder(color="success", className="me-1 mt-1 w-100", size="xs")]),
        
        
        # Seção 9: Ranking of Samples by Compound Interaction
        html.Div(id="sample-rank-compounds-chart", className="section"),  # ID para link no navbar
        html.Div([
            html.H5("Ranking of Samples by Compound Interaction", className="analysis-title"),
            html.P(
                "This ranking chart highlights the interaction of samples with compounds, showcasing which samples are more active or relevant in the dataset.",
                className="analysis-description"
            ),
            html.P(
                "By examining this chart, you can identify samples with the most interactions, providing valuable insights into their significance in the analysis.",
                className="analysis-insights"
            ),
            dbc.Accordion(
                [
                    dbc.AccordionItem(
                        html.Div(get_sample_rank_compounds_layout(), className="chart-container"),
                        title="Ranking of Samples by Compound Interaction"
                    )
                ],
                start_collapsed=True,
                always_open=False,
            ),
        ], className="analysis-header"),
        html.Div([dbc.Placeholder(color="success", className="me-1 mt-1 w-100", size="xs")]),


                # Seção 10: Ranking of Compounds by Sample Interaction
        html.Div(id="compound-rank-chart", className="section"),  # ID para link no navbar
        html.Div([
            html.H5("Ranking of Compounds by Sample Interaction", className="analysis-title"),
            html.P(
                "This ranking chart identifies compounds based on their interactions with samples, revealing compounds with higher significance.",
                className="analysis-description"
            ),
            html.P(
                "Use this chart to focus on compounds with the most interactions, which can help prioritize targets for further investigation.",
                className="analysis-insights"
            ),
            dbc.Accordion(
                [
                    dbc.AccordionItem(
                        html.Div(get_compound_rank_layout(), className="chart-container"),
                        title="Ranking of Compounds by Sample Interaction"
                    )
                ],
                start_collapsed=True,
                always_open=False,
            ),
        ], className="analysis-header"),
        html.Div([dbc.Placeholder(color="success", className="me-1 mt-1 w-100", size="xs")]),


                # Seção 11: Ranking of Compounds by Gene Interaction
        html.Div(id="compound-rank-gene-chart", className="section"),  # ID para link no navbar
        html.Div([
            html.H5("Ranking of Compounds by Gene Interaction", className="analysis-title"),
            html.P(
                "This ranking chart identifies compounds based on their interactions with genes, revealing compounds associated with higher genetic activity.",
                className="analysis-description"
            ),
            html.P(
                "This visualization is useful to prioritize compounds with significant genetic interactions, aiding in targeted research and analysis.",
                className="analysis-insights"
            ),
            dbc.Accordion(
                [
                    dbc.AccordionItem(
                        html.Div(get_rank_compounds_gene_layout(), className="chart-container"),
                        title="Ranking of Compounds by Gene Interaction"
                    )
                ],
                start_collapsed=True,
                always_open=False,
            ),
        ], className="analysis-header"),
        html.Div([dbc.Placeholder(color="success", className="me-1 mt-1 w-100", size="xs")]),


                # Seção 12: Scatter Plot of Genes vs Compounds
        html.Div(id="gene-compound-scatter-chart", className="section"),  # ID para link no navbar
        html.Div([
            html.H5("Scatter Plot of Genes vs Compounds", className="analysis-title"),
            html.P(
                "This scatter plot visualizes the relationships between genes and compounds, highlighting associations that may indicate important interactions.",
                className="analysis-description"
            ),
            html.P(
                "By analyzing this chart, researchers can identify gene-compound pairs with potential biological or chemical significance.",
                className="analysis-insights"
            ),
            dbc.Accordion(
                [
                    dbc.AccordionItem(
                        html.Div(get_gene_compound_scatter_layout(), className="chart-container"),
                        title="Scatter Plot of Genes vs Compounds"
                    )
                ],
                start_collapsed=True,
                always_open=False,
            ),
        ], className="analysis-header"),
        html.Div([dbc.Placeholder(color="success", className="me-1 mt-1 w-100", size="xs")]),

                # Seção 13: Scatter Plot of Samples vs Genes
        html.Div(id="sample-gene-scatter-chart", className="section"),  # ID para link no navbar
        html.Div([
            html.H5("Scatter Plot of Samples vs Genes", className="analysis-title"),
            html.P(
                "This scatter plot visualizes the relationships between samples and genes, providing insights into genetic patterns across various samples.",
                className="analysis-description"
            ),
            html.P(
                "By analyzing this plot, users can identify significant gene associations across different samples, aiding in the discovery of genetic hotspots.",
                className="analysis-insights"
            ),
            dbc.Accordion(
                [
                    dbc.AccordionItem(
                        html.Div(get_sample_gene_scatter_layout(), className="chart-container"),
                        title="Scatter Plot of Samples vs Genes"
                    )
                ],
                start_collapsed=True,
                always_open=False,
            ),
        ], className="analysis-header"),
        html.Div([dbc.Placeholder(color="success", className="me-1 mt-1 w-100", size="xs")]),


                # Seção 14: Heatmap of Samples vs Reference AG
        html.Div(id="sample-reference-heatmap", className="section"),  # ID para link no navbar
        html.Div([
            html.H5("Heatmap of Samples vs Reference AG", className="analysis-title"),
            html.P(
                "This heatmap displays the association between samples and reference AGs, highlighting compound occurrences and interactions.",
                className="analysis-description"
            ),
            html.P(
                "By analyzing this heatmap, you can identify patterns and relationships between the samples and reference AGs, supporting further exploration of compound interactions.",
                className="analysis-insights"
            ),
            dbc.Accordion(
                [
                    dbc.AccordionItem(
                        html.Div(get_sample_reference_heatmap_layout(), className="chart-container"),
                        title="Heatmap of Samples vs Reference AG"
                    )
                ],
                start_collapsed=True,
                always_open=False,
            ),
        ], className="analysis-header"),
        html.Div([dbc.Placeholder(color="success", className="me-1 mt-1 w-100", size="xs")]),

                # Seção 15: Sample Groups by Compound Class
        html.Div(id="sample-groups-chart", className="section"),  # ID para link no navbar
        html.Div([
            html.H5("Sample Groups by Compound Class", className="analysis-title"),
            html.P(
                "This visualization presents the grouping of samples based on compound classes, providing an overview of their classification.",
                className="analysis-description"
            ),
            html.P(
                "By analyzing these groups, you can identify patterns and relationships among samples and their associated compound classes.",
                className="analysis-insights"
            ),
            dbc.Accordion(
                [
                    dbc.AccordionItem(
                        html.Div(get_sample_groups_layout(), className="chart-container"),
                        title="Sample Groups by Compound Class"
                    )
                ],
                start_collapsed=True,
                always_open=False,
            ),
        ], className="analysis-header"),
        html.Div([dbc.Placeholder(color="success", className="me-1 mt-1 w-100", size="xs")]),


                # Seção 16: Heatmap of Genes vs Samples
        html.Div(id="gene-sample-heatmap", className="section"),  # ID para link no navbar
        html.Div([
            html.H5("Heatmap of Genes vs Samples", className="analysis-title"),
            html.P(
                "This heatmap illustrates the relationship between genes and samples, showing unique associations through a color gradient.",
                className="analysis-description"
            ),
            html.P(
                "By analyzing this heatmap, you can identify trends and hotspots in the gene-sample interactions, providing insights into their biological relevance.",
                className="analysis-insights"
            ),
            dbc.Accordion(
                [
                    dbc.AccordionItem(
                        html.Div(get_gene_sample_heatmap_layout(), className="chart-container"),
                        title="Genes vs Samples Heatmap"
                    )
                ],
                start_collapsed=True,
                always_open=False,
            ),
        ], className="analysis-header"),
        html.Div([dbc.Placeholder(color="success", className="me-1 mt-1 w-100", size="xs")]),

                # Seção 17: Heatmap of Pathways vs Compound Pathways
        html.Div(id="pathway-heatmap", className="section"),  # ID para link no navbar
        html.Div([
            html.H5("Heatmap of Pathways vs Compound Pathways", className="analysis-title"),
            html.P(
                "This heatmap visualizes the interaction between metabolic pathways and compound pathways, showing unique KO counts for each interaction.",
                className="analysis-description"
            ),
            html.P(
                "Use this heatmap to explore how pathways and compound pathways are interconnected, identifying areas of higher KO activity.",
                className="analysis-insights"
            ),
            dbc.Accordion(
                [
                    dbc.AccordionItem(
                        html.Div(get_pathway_heatmap_layout(), className="chart-container"),
                        title="Pathways vs Compound Pathways Heatmap"
                    )
                ],
                start_collapsed=True,
                always_open=False,
            ),
        ], className="analysis-header"),
        html.Div([dbc.Placeholder(color="success", className="me-1 mt-1 w-100", size="xs")]),

                # Seção 18: Scatter Plot of KOs by Sample for Pathway
        html.Div(id="sample-ko-scatter", className="section"),  # ID para link no navbar
        html.Div([
            html.H5("Scatter Plot of KOs by Sample for Pathway", className="analysis-title"),
            html.P(
                "This scatter plot visualizes the distribution of KOs across different samples for a specific pathway.",
                className="analysis-description"
            ),
            html.P(
                "By analyzing this scatter plot, you can identify patterns of KO distribution across samples, helping to pinpoint critical samples for specific pathways.",
                className="analysis-insights"
            ),
            dbc.Accordion(
                [
                    dbc.AccordionItem(
                        html.Div(get_sample_ko_scatter_layout(), className="chart-container"),
                        title="Scatter Plot of KOs by Sample"
                    )
                ],
                start_collapsed=True,
                always_open=False,
            ),
        ], className="analysis-header"),
        html.Div([dbc.Placeholder(color="success", className="me-1 mt-1 w-100", size="xs")]),

                # Seção 19: Enzyme Activity Counts per Sample
        html.Div(id="sample-enzyme-activity", className="section"),  # ID para link no navbar
        html.Div([
            html.H5("Enzyme Activity Counts per Sample", className="analysis-title"),
            html.P(
                "This bar chart shows the distribution of enzyme activity counts across different samples.",
                className="analysis-description"
            ),
            html.P(
                "Analyzing enzyme activity counts helps identify variations in enzymatic activity across samples, providing insights into metabolic activity.",
                className="analysis-insights"
            ),
            dbc.Accordion(
                [
                    dbc.AccordionItem(
                        html.Div(get_sample_enzyme_activity_layout(), className="chart-container"),
                        title="Enzyme Activity Bar Chart"
                    )
                ],
                start_collapsed=True,
                always_open=False,
            ),
        ], className="analysis-header"),
        html.Div([dbc.Placeholder(color="success", className="me-1 mt-1 w-100", size="xs")]),



    ])