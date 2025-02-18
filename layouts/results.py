from components.alerts import hadeg_alert, toxcsm_alert

from components.navbar import navbar  # Importe o navbar definido acima
from dash import html, dcc
import dash_bootstrap_components as dbc

from layouts.T1_biorempp import get_biorempp_results_table_layout
from layouts.T2_hadeg import get_hadeg_results_table_layout
from layouts.T3_toxcsm import get_toxcsm_results_table_layout
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
from layouts.P11_gene_sample__heatmap_layout import get_gene_sample_heatmap_layout
from layouts.P12_compaund_pathway_layout import get_pathway_heatmap_layout
from layouts.P13_gene_sample_scatter_layout import get_sample_ko_scatter_layout
from layouts.P14_sample_enzyme_activity_layout import get_sample_enzyme_activity_layout
from layouts.P15_sample_clustering_layout import get_sample_clustering_layout
from layouts.P16_sample_upset_layout import get_sample_upset_layout
from layouts.P17_gene_compound_network_layout import get_gene_compound_network_layout
from layouts.p18_heatmap_faceted_layout import get_toxicity_heatmap_layout





def get_results_layout():
    return html.Div([
        # Navbar fixo no topo da página
        navbar,

        # Espaçamento para compensar o menu fixo
        html.Div(style={"height": "50px"}),

        # Título principal
        html.H2('Data Analysis Results', className='results-title'),
        html.H4('Results from your submitted data', className='results-subtitle'),
        html.Hr(className="my-2"),



        html.Div([
                html.H3("1 - Data Tables and Database Integration", className="section-title"),
                html.P(
                    "Provide an overview of the data integrated into the databases",
                    className="section-objective"
                ),
            ], className="section-header"),


        # Seção 1: Main Results Table
 html.Div(id="main-results-table", className="section"),

    html.Div(
        className="analysis-header",
        children=[
            dbc.Row(
                [
                    dbc.Col(
                        html.H5("BioRemPP Results Table", className="analysis-title"),
                        width="auto"
                    ),
                    dbc.Col(
                        html.Button(
                            "Download CSV",
                            id="download-csv-btn",
                            n_clicks=0,
                            className="btn btn-primary"
                        ),
                        width="auto"
                    ),
                ],
                align="center",
                justify="between"
            ),
            html.P(
                "This table presents the processed data merged with the BioRemPP database, "
                "offering a comprehensive overview of the input data and its matched records",
                className="analysis-description"
            ),
            html.P(
                "The merged table reveals how well the input data aligns with the main database, "
                "providing insights into the completeness and relevance of the data",
                className="analysis-insights"
            ),
            dbc.Accordion(
                [
                    dbc.AccordionItem(
                        html.Div(
                            get_biorempp_results_table_layout(),
                            className="chart-container"
                        ),
                        title="Results Table"
                    )
                ],
                start_collapsed=True,
                always_open=False
            ),

            # The dcc.Download component for returning CSV to user
            dcc.Download(id="download-merged-csv"),
        ]
    ),

    html.Div([dbc.Placeholder(color="success", className="me-1 mt-1 w-100", size="xs")]),



        # Seção 2: HADEG Results Table
        html.Div(id="hadeg-results-table", className="section"),  # ID para ancoragem no navbar
        html.Div([
            html.H5("HADEG Results Table", className="analysis-title"),
            html.P(
                "This table contains data merged with the HADEG database, enabling the exploration of additional annotations and insights",
                className="analysis-description"
            ),
            html.P(
                "The table helps identify significant matches with HADEG, enhancing the understanding of potential functional and structural associations",
                className="analysis-insights"
            ),
            hadeg_alert(),
            dbc.Accordion(
                [
                    dbc.AccordionItem(
                        html.Div(get_hadeg_results_table_layout(), className="chart-container"),
                        title="Results Table"
                    )
                ],
                start_collapsed=True,
                always_open=False
            ),
        ], className="analysis-header"),
        html.Div([dbc.Placeholder(color="success", className="me-1 mt-1 w-100", size = "xs"),]),



        # Seção 3: TOXCSM Results Table
        html.Div(id="toxcsm-results-table", className="section"),  # ID para ancoragem no navbar
        html.Div([
            html.H5("ToxCSM Results Table", className="analysis-title"),
            html.P(
                "This table shows data merged with the TOXCSM database, providing toxicity predictions and compound interactions",
                className="analysis-description"
            ),
            html.P(
                "By analyzing this table, you can assess the toxicity potential and prioritize compounds for further investigation",
                className="analysis-insights"
            ),
            toxcsm_alert(),
            dbc.Accordion(
                [
                    dbc.AccordionItem(
                        html.Div(get_toxcsm_results_table_layout(), className="chart-container"),
                        title="Results Table"
                    )
                ],
                start_collapsed=True,
                always_open=False
            ),
        ], className="analysis-header"),
        html.Div([dbc.Placeholder(color="success", className="me-1 mt-1 w-100", size="xs")]),


      
        html.Div([
                html.H3("2 - Gene and Metabolic Pathway Analysis", className="section-title"),
                html.P(
                    "Explore genes and metabolic pathways associated with compounds",
                    className="section-objective"
                ),
            ], className="section-header"),

                    # Seção 4: Gene Count Chart
        html.Div(id="gene-count-chart", className="section"),
        html.Div([
            html.H5("Gene Count Associated with Priority Compounds", className="analysis-title"),
            html.P(
                "This bar chart displays the count of unique genes associated with priority compounds for each sample",
                className="analysis-description"
            ),
            html.P(
                "By analyzing this chart, you can identify which samples have a higher number of unique gene associations, offering insights into potential hotspots of genetic activity",
                className="analysis-insights"
            ),
            dbc.Accordion(
                [
                    dbc.AccordionItem(
                        html.Div(get_ko_count_bar_chart_layout(), className="chart-container"),
                        title="Gene Counts Across Samples"
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
            html.H5("Gene Distribution", className="analysis-title"),
            html.P(
                "This violin boxplot illustrates the distribution of unique genes associated with priority compounds across samples",
                className="analysis-description"
            ),
            html.P(
                "Identifies trends and outliers in gene distribution, providing a comprehensive view of genetic activitys",
                className="analysis-insights"
            ),
            dbc.Accordion(
                [
                    dbc.AccordionItem(
                        html.Div(get_ko_violin_boxplot_layout(), className="chart-container"),
                        title="Gene Distribution Among Samples"
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
            html.H5("Distribution of Genes in Xenobiotics Biodegradation Pathways", className="analysis-title"),
            html.P(
                "This bar chart highlights the distribution of KEGG Ortholog (KO) counts across 20 degradation pathways",
                className="analysis-description"
            ),
            html.P(
                "By analyzing this chart, you can gain insights into the functional diversity of pathways and identify dominant or underrepresented pathways in the dataset",
                className="analysis-insights"
            ),
            dbc.Accordion(
                [
                    dbc.AccordionItem(
                        html.Div(get_pathway_ko_bar_chart_layout(), className="chart-container"),
                        title="Distribution of KO in Pathways"
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
            html.H5("Sample-Specific Pathway Activity", className="analysis-title"),
            html.P(
                "This bar chart presents the KEGG Ortholog (KO) distribution across pathways, grouped by sample",
                className="analysis-description"
            ),
            html.P(
                "This visualization allows you to understand how different pathways are represented within each sample, helping to identify pathway-specific trends",
                className="analysis-insights"
            ),
            dbc.Accordion(
                [
                    dbc.AccordionItem(
                        html.Div(get_sample_ko_pathway_bar_chart_layout(), className="chart-container"),
                        title="Pathway Activity per Sample"
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
            html.H5("Sample-Compound Interactions in Xenobiotics Biodegradation Pathways", className="analysis-title"),
            html.P(
                "This scatter plot shows the distribution of genes across different samples for a specific pathway",
                className="analysis-description"
            ),
            html.P(
                "By analyzing this scatter plot, you can identify patterns of genes across samples, helping to pinpoint critical samples for specific pathways",
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



        html.Div([
        html.H3("3 - Interactions Between Entities (Samples, Compounds, and Genes)", className="section-title"),
        html.P(
            "Identify interaction patterns between samples, compounds, and genes",
            className="section-objective"
        ),
             ], className="section-header"),

              # Seção 8: Scatter Plot of Samples vs Compounds
        html.Div(id="compound-scatter-chart", className="section"),  # ID para link no navbar
        html.Div([
            html.H5("Sample-Compound Interactions", className="analysis-title"),
            html.P(
                "This scatter plot highlights the relationship between samples and compounds, illustrating their interactions and associations",
                className="analysis-description"
            ),
            html.P(
                "Use this visualization to detect key sample-compound interactions and prioritize samples or compounds of interest",
                className="analysis-insights"
            ),
            dbc.Accordion(
                [
                    dbc.AccordionItem(
                        html.Div(get_compound_scatter_layout(), className="chart-container"),
                        title="Sample-Compound Interaction Plot"
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
            html.H5("Gene-Compound Interactions", className="analysis-title"),
            html.P(
                "This scatter plot highlights the relationships between genes and compounds, highlighting associations that may indicate important interactions",
                className="analysis-description"
            ),
            html.P(
                "By analyzing this chart, you can identify gene-compound pairs with potential biological or chemical significance",
                className="analysis-insights"
            ),
            dbc.Accordion(
                [
                    dbc.AccordionItem(
                        html.Div(get_gene_compound_scatter_layout(), className="chart-container"),
                        title="Gene-Compound Interaction Plot"
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
            html.H5("Sample-Gene Associations", className="analysis-title"),
            html.P(
                "This scatter plot highlights the relationships between samples and genes, providing insights into genetic patterns across various samples",
                className="analysis-description"
            ),
            html.P(
                "By analyzing this plot, you can identify significant gene associations across different samples, aiding in the discovery of genetic hotspots",
                className="analysis-insights"
            ),
            dbc.Accordion(
                [
                    dbc.AccordionItem(
                        html.Div(get_sample_gene_scatter_layout(), className="chart-container"),
                        title="Sample-Gene Associations Plot"
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
            html.H5("Metabolic Enzyme Activity Counts per Sample", className="analysis-title"),
            html.P(
                "This bar chart shows the distribution of enzyme activity counts across different samples",
                className="analysis-description"
            ),
            html.P(
                "Analyzing enzyme activity counts helps identify variations in enzymatic activity across samples, providing insights into metabolic activity",
                className="analysis-insights"
            ),
            dbc.Accordion(
                [
                    dbc.AccordionItem(
                        html.Div(get_sample_enzyme_activity_layout(), className="chart-container"),
                        title="Enzyme Activity by Sample"
                    )
                ],
                start_collapsed=True,
                always_open=False,
            ),
        ], className="analysis-header"),
        html.Div([dbc.Placeholder(color="success", className="me-1 mt-1 w-100", size="xs")]),


                        # Seção 22: Gene-Compound Interaction Network
        html.Div(id="gene-compound-network", className="section"),  # ID para link no navbar
        html.Div([
            html.H5("Gene-Compound Interaction Network", className="analysis-title"),
            html.P(
                "This network graph visualizes the interactions between genes and compounds, providing insights into functional relationships",
                className="analysis-description"
            ),
            html.P(
                "By analyzing this graph, you can explore the connectivity and association strength between genes and compounds, uncovering potential targets or key interactions",
                className="analysis-insights"
            ),
            dbc.Accordion(
                [
                    dbc.AccordionItem(
                        html.Div(get_gene_compound_network_layout(), className="chart-container"),
                        title="Gene-Compound Interaction"
                    )
                ],
                start_collapsed=True,
                always_open=False,
            ),
        ], className="analysis-header"),
        html.Div([dbc.Placeholder(color="success", className="me-1 mt-1 w-100", size="xs")]),


        html.Div([
        html.H3("4 - Interaction-Based Rankings", className="section-title"),
        html.P(
            "Prioritize samples, genes or compounds based on specific interactions",
            className="section-objective"
        ),
            ], className="section-header"),

                    # Seção 9: Ranking of Samples by Compound Interaction
        html.Div(id="sample-rank-compounds-chart", className="section"),  # ID para link no navbar
        html.Div([
            html.H5("Sample-Compound Interaction Rankings", className="analysis-title"),
            html.P(
                "This chart ranks samples based on the number and intensity of their interactions with compounds in the dataset",
                className="analysis-description"
            ),
            html.P(
                "By examining this chart, you can identify samples with the most interactions, providing valuable insights into their significance in the analysis",
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
            html.H5("Compound-Sample Interaction Rankings", className="analysis-title"),
            html.P(
                "This chart ranks compounds based on their interactions with samples, showcasing which compounds are most significant",
                className="analysis-description"
            ),
            html.P(
                "Use this chart to focus on compounds with the most interactions, which can help prioritize targets for further investigation",
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
            html.H5("Compound-Gene Interaction Rankings", className="analysis-title"),
            html.P(
                "This ranking chart identifies compounds with associations with genes, revealing key genetic activity",
                className="analysis-description"
            ),
            html.P(
                "This visualization is useful to prioritize compounds with significant genetic interactions, aiding in targeted research and analysis",
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

        html.Div([
        html.H3("5 - Patterns and Interactions with Heatmaps", className="section-title"),
        html.P(
            "This session highlights associations between biological variables such as samples, genes, and pathways",
            className="section-objective"
        ),
             ], className="section-header"),

                             # Seção 14: Heatmap of Samples vs Reference AG
        html.Div(id="sample-reference-heatmap", className="section"),  # ID para link no navbar
        html.Div([
            html.H5("Sample-Reference Agency Associations Heatmap", className="analysis-title"),
            html.P(
                "This heatmap displays the association between samples and reference agencies, highlighting compound occurrences and interactions",
                className="analysis-description"
            ),
            html.P(
                "Analyze this heatmap to discover hotspots of compound activity linked to reference agencies",
                className="analysis-insights"
            ),
            dbc.Accordion(
                [
                    dbc.AccordionItem(
                        html.Div(get_sample_reference_heatmap_layout(), className="chart-container"),
                        title="Sample-Reference Agency Heatmap"
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
            html.H5("Gene-Sample Association Heatmap", className="analysis-title"),
            html.P(
                "This heatmap illustrates the relationship between genes, pathways and samples, providing insights into unique relationships",
                className="analysis-description"
            ),
            html.P(
                "By analyzing this heatmap, you can identify trends and hotspots in the gene-sample-pathways interactions, providing insights into their biological relevance",
                className="analysis-insights"
            ),
            hadeg_alert(),
            dbc.Accordion(
                [
                    dbc.AccordionItem(
                        html.Div(get_gene_sample_heatmap_layout(), className="chart-container"),
                        title="Gene-Sample Heatmap"
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
            html.H5("Pathway-Compound Heatmap", className="analysis-title"),
            html.P(
                "This heatmap visualizes the interaction between metabolic pathways and compound pathways across samples, highlighting gene activity",
                className="analysis-description"
            ),
            html.P(
                "Use this heatmap to explore how pathways and compound pathways are interconnected for each sample",
                className="analysis-insights"
            ),
            hadeg_alert(),
            dbc.Accordion(
                [
                    dbc.AccordionItem(
                        html.Div(get_pathway_heatmap_layout(), className="chart-container"),
                        title="Pathway-Compound Interaction Map"
                    )
                ],
                start_collapsed=True,
                always_open=False,
            ),
        ], className="analysis-header"),
        html.Div([dbc.Placeholder(color="success", className="me-1 mt-1 w-100", size="xs")]),


        html.Div([
        html.H3("6 - Intersection and Group Exploration", className="section-title"),
        html.P(
            "Investigate overlap and grouping patterns among samples",
            className="section-objective"
        ),
            ], className="section-header"),
                                        # Seção 15: Sample Groups by Compound Class
        html.Div(id="sample-groups-chart", className="section"),  # ID para link no navbar
        html.Div([
            html.H5("Compound-Based Sample Grouping", className="analysis-title"),
            html.P(
                "Displays how samples are grouped and classified according to their compound content, emphasizing patterns in their composition",
                className="analysis-description"
            ),
            html.P(
                "Use this visualization to detect clusters of samples with similar compound profiles, supporting targeted compound or sample research",
                className="analysis-insights"
            ),
            dbc.Accordion(
                [
                    dbc.AccordionItem(
                        html.Div(get_sample_groups_layout(), className="chart-container"),
                        title="Sample Grouping by Compound Class Pattern"
                    )
                ],
                start_collapsed=True,
                always_open=False,
            ),
        ], className="analysis-header"),
        html.Div([dbc.Placeholder(color="success", className="me-1 mt-1 w-100", size="xs")]),

               

                # Seção 21: Sample UpSet Plot
        html.Div(id="sample-upset-plot", className="section"),  # ID para link no navbar
        html.Div([
            html.H5("Intersection of Genes Across Samples", className="analysis-title"),
            html.P(
                "This UpSet plot visualizes intersections of orthologous genes (KOs) across multiple samples, highlighting overlaps and unique associations",
                className="analysis-description"
            ),
            html.P(
                "By analyzing this plot, you can identify shared and unique orthologs between samples, highlighting potential relationships and  prioritize samples with shared or unique genes for further exploration",
                className="analysis-insights"
            ),
            dbc.Accordion(
                [
                    dbc.AccordionItem(
                        html.Div(get_sample_upset_layout(), className="chart-container"),
                        title="Intersection Analysis"
                    )
                ],
                start_collapsed=True,
                always_open=False,
            ),
        ], className="analysis-header"),
        html.Div([dbc.Placeholder(color="success", className="me-1 mt-1 w-100", size="xs")]),

                                # Seção 20: Sample Clustering Dendrogram
        html.Div(id="sample-clustering-dendrogram", className="section"),  # ID para link no navbar
        html.Div([
            html.H5("Hierarchical Clustering of Samples", className="analysis-title"),
            html.P(
                "Hierarchically clusters samples based on genes associated with priority compounds, providing a detailed view of their relationships",
                className="analysis-description"
            ),
            html.P(
                "By analyzing this clustering, you can identify patterns of similarity or divergence between samples",
                className="analysis-insights"
            ),
            dbc.Accordion(
                [
                    dbc.AccordionItem(
                        html.Div(get_sample_clustering_layout(), className="chart-container"),
                        title="Clustering Dendrogram"
                    )
                ],
                start_collapsed=True,
                always_open=False,
            ),
        ], className="analysis-header"),
        html.Div([dbc.Placeholder(color="success", className="me-1 mt-1 w-100", size="xs")]), 




        html.Div([
        html.H3("7 - Toxicity Predictions", className="section-title"),
        html.P(
            "Visualize and understand toxicity predictions",
            className="section-objective"
        ),
             ], className="section-header"),     

    
            # Seção 23: Heatmap of Toxicity Predictions
        html.Div(id="toxicity-heatmap-faceted", className="section"),  # ID for navbar linking
        html.Div([
            html.H5("Comprehensive Toxicity Heatmap", className="analysis-title"),
            html.P(
                "This heatmap provides a visual representation of toxicity predictions across the five main categories of analysis",
                className="analysis-description"
            ),
            html.P(
                "Explore toxicity predictions to identify high-risk compounds or category, supporting risk assessment and decision-making",
                className="analysis-insights"
            ),
            toxcsm_alert(), 
            dbc.Accordion(
                [
                    dbc.AccordionItem(
                        html.Div(get_toxicity_heatmap_layout(), className="chart-container"),
                        title="Toxicity Prediction Heatmap"
                    )
                ],
                start_collapsed=True,
                always_open=False,
            ),
        ], className="analysis-header"),
        html.Div([dbc.Placeholder(color="success", className="me-1 mt-1 w-100", size="xs")]),


    



    ])    
           
      



               
