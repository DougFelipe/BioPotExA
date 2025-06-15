from components.alerts import hadeg_alert, toxcsm_alert

from components.navbar import navbar  # Importe o navbar definido acima
from components.analytical_highlight import analytical_highlight
from components.analysis_suggestions_offcanvas import analysis_suggestions_offcanvas
from components.divider import NeonDivider  


from dash import html, dcc
import dash_bootstrap_components as dbc

from layouts.results_overview.biorempp_results_table_layout import get_biorempp_results_table_layout
from layouts.results_overview.hadeg_results_table_layout import get_hadeg_results_table_layout
from layouts.results_overview.toxcsm_results_table_layout import get_toxcsm_results_table_layout
from layouts.gene_pathway_analysis.gene_counts_across_samples_layout import get_ko_count_bar_chart_layout, get_ko_violin_boxplot_layout
from layouts.gene_pathway_analysis.distribution_of_ko_in_pathways_layout import get_pathway_ko_bar_chart_layout, get_sample_ko_pathway_bar_chart_layout
from layouts.entity_interactions.sample_compound_interaction_layout import get_compound_scatter_layout
from layouts.rankings.ranking_samples_by_compound_interaction_layout import get_rank_compounds_layout as get_sample_rank_compounds_layout
from layouts.rankings.ranking_compounds_by_sample_interaction_layout import get_rank_compounds_layout as get_compound_rank_layout
from layouts.rankings.ranking_compounds_by_gene_interaction_layout import get_rank_compounds_gene_layout
from layouts.entity_interactions.gene_compound_interaction_layout import get_gene_compound_scatter_layout
from layouts.entity_interactions.sample_gene_associations_layout import get_sample_gene_scatter_layout
from layouts.heatmaps.sample_reference_agency_heatmap_layout import get_sample_reference_heatmap_layout
from layouts.intersections_and_groups.sample_grouping_by_compound_class_pattern_layout import get_sample_groups_layout
from layouts.heatmaps.gene_sample_heatmap_layout import get_gene_sample_heatmap_layout
from layouts.heatmaps.pathway_compound_interaction_layout import get_pathway_heatmap_layout
from layouts.gene_pathway_analysis.gene_distribution_among_samples_layout import get_sample_ko_scatter_layout
from layouts.entity_interactions.enzyme_activity_by_sample_layout import get_sample_enzyme_activity_layout
from layouts.intersections_and_groups.clustering_dendrogram_layout import get_sample_clustering_layout
from layouts.intersections_and_groups.intersection_analysis_layout import get_sample_upset_layout
from layouts.entity_interactions.gene_compound_interaction_network_layout import get_gene_compound_network_layout
from layouts.toxicity.toxicity_prediction_heatmap_layout import get_toxicity_heatmap_layout





def get_results_layout():
    return html.Div([
        # Navbar fixo no topo da página
        navbar,

        # Espaçamento para compensar o menu fixo
        html.Div(style={"height": "50px"}),

# Título da página
html.Div(id="results-top"),
dbc.Row([
    dbc.Col([
        html.H1("Data Analysis Results", className="text-success fw-bold text-center"),
        html.H5("Results from your submitted data", className="text-muted text-center"),
        html.Div([
            html.Button(
                "📊 Download EDA Report (BioRemPP)",
                id="download-eda-btn",
                n_clicks=0,
                className="btn btn-success btn-lg mb-3"
            ),
            dcc.Download(id="download-eda-report"),

            # Alerta
            html.Div(id="eda-alert", style={"display": "none"}),

            # Intervalo de tempo para esconder alerta
            dcc.Interval(id="eda-alert-interval", interval=15000, n_intervals=0, disabled=True)
        ]),





        # Botão flutuante fixo + componente offcanvas
        html.Div([
            dbc.Button(
                [html.Span("Analytical", style={"display": "block"}), html.Span("Suggestions", style={"display": "block"})],
                id="open-suggestions-offcanvas",
                n_clicks=0,
                className="btn btn-outline-success btn-sm",
                title="Explore analysis suggestions",
                style={
                    "backgroundColor": "white",
                    "borderColor": "#198754",
                    "color": "#198754",
                    "fontWeight": "500",
                    "lineHeight": "1.2",
                    "whiteSpace": "normal",
                    "textAlign": "center"
                }
            ),
            dbc.Button("×", id="close-suggestions-offcanvas", className="d-none"),
            analysis_suggestions_offcanvas()
        ], style={
            "position": "fixed",
            "bottom": "25px",
            "right": "25px",
            "zIndex": "1051"
        }),
        html.Hr(className="my-4")
    ])
]),


# Seção BioRemPP
html.Div([
    html.H3("Data Tables and Database Integration", className="section-title text-center fw-bold text-primary"),
    html.P(
        "Provide an overview of the data integrated into the databases",
        className="section-objective text-center text-muted"
    )
], className="section-header"),

html.Hr(className="my-2"),


# Subsection: BioRemPP Results
html.Div(id="main-results-table", className="section"),
html.Div([
    html.H5("BioRemPP Results Table", className="analysis-title text-center fw-bold"),
    dbc.Row([
        dbc.Col(
            dbc.Button("Download CSV", id="download-csv-btn", n_clicks=0, color="primary"),
            width="auto",
            className="d-flex justify-content-center"
        )
    ], justify="center", className="mb-2"),
    html.P(
        "This table presents the processed data merged with the BioRemPP database, offering a comprehensive overview of the input data and its matched records.",
        className="analysis-description text-center"
    ),
    analytical_highlight(),
    html.P(
        "The merged table reveals how well the input data aligns with the main database, providing insights into the completeness and relevance of the data.",
        className="analysis-insights text-center"
    ),
    dbc.Accordion([
        dbc.AccordionItem(
            html.Div(get_biorempp_results_table_layout(), className="chart-container"),
            title=("Results Table")
        )
    ], start_collapsed=True),
    dcc.Download(id="download-merged-csv"),
    NeonDivider(className="my-2"),
], className="analysis-header"),

# Seção HADEG
html.Div(id="hadeg-results-table", className="section"),
html.Div([
    html.H5("HADEG Results Table", className="analysis-title text-center fw-bold mt-5"),
    dbc.Row([
        dbc.Col(
            dbc.Button("Download CSV", id="download-hadeg-csv-btn", n_clicks=0, color="primary"),
            width="auto",
            className="d-flex justify-content-center"
        )
    ], justify="center", className="mb-2"),
    html.P(
        "This table contains data merged with the HADEG database, enabling the exploration of additional annotations and insights.",
        className="analysis-description text-center"
    ),
    analytical_highlight(),
    html.P(
        "The table helps identify significant matches with HADEG, enhancing the understanding of potential functional and structural associations.",
        className="analysis-insights text-center"
    ),
    hadeg_alert(),
    dbc.Accordion([
        dbc.AccordionItem(
            html.Div(get_hadeg_results_table_layout(), className="chart-container"),
            title=("Results Table")
        )
    ], start_collapsed=True),
    dcc.Download(id="download-hadeg-csv"),
    NeonDivider(className="my-2"),
], className="analysis-header"),

# Seção TOXCSM
html.Div(id="toxcsm-results-table", className="section"),
html.Div([
    html.H5("ToxCSM Results Table", className="analysis-title text-center fw-bold mt-5"),
    dbc.Row([
        dbc.Col(
            dbc.Button("Download CSV", id="download-toxcsm-csv-btn", n_clicks=0, color="primary"),
            width="auto",
            className="d-flex justify-content-center"
        )
    ], justify="center", className="mb-2"),
    html.P(
        "This table shows data merged with the TOXCSM database, providing toxicity predictions and compound interactions.",
        className="analysis-description text-center"
    ),
    analytical_highlight(),
    html.P(
        "By analyzing this table, you can assess the toxicity potential and prioritize compounds for further investigation.",
        className="analysis-insights text-center"
    ),
    toxcsm_alert(),
    dbc.Accordion([
        dbc.AccordionItem(
            html.Div(get_toxcsm_results_table_layout(), className="chart-container"),
            title=("Results Table")
        )
    ], start_collapsed=True),
    dcc.Download(id="download-toxcsm-csv"),
    NeonDivider(className="my-2"),
], className="analysis-header"),




      
# Seção: Gene and Metabolic Pathway Analysis
html.Div([
    html.H3("Gene and Metabolic Pathway Analysis", className="section-title text-center fw-bold text-primary"),
    html.P(
        "Explore genes and metabolic pathways associated with compounds",
        className="section-objective text-center"
    ),
], className="section-header"),

html.Hr(className="my-2"),

# Seção 4: Gene Count Chart
html.Div(id="gene-count-chart", className="section"),
html.Div([
    html.H5("Gene Count Associated with Priority Compounds", className="analysis-title text-center fw-bold"),
    html.P(
        "This bar chart displays the count of unique genes associated with priority compounds for each sample",
        className="analysis-description text-center"
    ),
    analytical_highlight(),
    html.P(
        "By analyzing this chart, you can identify which samples have a higher number of unique gene associations, offering insights into potential hotspots of genetic activity",
        className="analysis-insights text-center"
    ),
    dbc.Accordion([
        dbc.AccordionItem(
            html.Div(get_ko_count_bar_chart_layout(), className="chart-container"),
            title=("Gene Counts Across Samples")
        )
    ], start_collapsed=True)
], className="analysis-header"),
NeonDivider(className="my-2"),

# Seção 5: Violin Boxplot
html.Div(id="violin-boxplot", className="section"),
html.Div([
    html.H5("Gene Distribution", className="analysis-title text-center fw-bold"),
    html.P(
        "This violin boxplot illustrates the distribution of unique genes associated with priority compounds across samples",
        className="analysis-description text-center"
    ),
    analytical_highlight(),
    html.P(
        "Identifies trends and outliers in gene distribution, providing a comprehensive view of genetic activitys",
        className="analysis-insights text-center"
    ),
    dbc.Accordion([
        dbc.AccordionItem(
            html.Div(get_ko_violin_boxplot_layout(), className="chart-container"),
            title=("Gene Distribution Among Samples")
        )
    ], start_collapsed=True)
], className="analysis-header"),
NeonDivider(className="my-2"),

# Seção 6: Pathway KO Bar Chart
html.Div(id="pathway-ko-bar-chart", className="section"),
html.Div([
    html.H5("Distribution of Genes in Xenobiotics Biodegradation Pathways", className="analysis-title text-center fw-bold"),
    html.P(
        "This bar chart highlights the distribution of KEGG Ortholog (KO) counts across 20 degradation pathways",
        className="analysis-description text-center"
    ),
        analytical_highlight(),
    html.P(
        "By analyzing this chart, you can gain insights into the functional diversity of pathways and identify dominant or underrepresented pathways in the dataset",
        className="analysis-insights text-center"
    ),
    dbc.Accordion([
        dbc.AccordionItem(
            html.Div(get_pathway_ko_bar_chart_layout(), className="chart-container"),
            title=("Distribution of KO in Pathways")
        )
    ], start_collapsed=True)
], className="analysis-header"),
NeonDivider(className="my-2"),

# Seção 7: Sample KO Pathway Chart
html.Div(id="sample-ko-pathway-chart", className="section"),
html.Div([
    html.H5("Sample-Pathway Specific  Activity", className="analysis-title text-center fw-bold"),
    html.P(
        "This bar chart presents the KEGG Ortholog (KO) distribution across pathways, grouped by sample",
        className="analysis-description text-center"
    ),
    analytical_highlight(),
    html.P(
        "This visualization allows you to understand how different pathways are represented within each sample, helping to identify pathway-specific trends",
        className="analysis-insights text-center"
    ),
    dbc.Accordion([
        dbc.AccordionItem(
            html.Div(get_sample_ko_pathway_bar_chart_layout(), className="chart-container"),
            title=("Pathway Activity per Sample")
        )
    ], start_collapsed=True)
], className="analysis-header"),
NeonDivider(className="my-2"),

# Seção 8: Scatter Plot of KOs by Sample
html.Div(id="sample-ko-scatter", className="section"),
html.Div([
    html.H5("Sample-Compound Interactions in Xenobiotics Biodegradation Pathways", className="analysis-title text-center fw-bold"),
    html.P(
        "This scatter plot shows the distribution of genes across different samples for a specific pathway",
        className="analysis-description text-center"
    ),
        analytical_highlight(),
    html.P(
        "By analyzing this scatter plot, you can identify patterns of genes across samples, helping to pinpoint critical samples for specific pathways",
        className="analysis-insights text-center"
    ),
    dbc.Accordion([
        dbc.AccordionItem(
            html.Div(get_sample_ko_scatter_layout(), className="chart-container"),
            title=("Scatter Plot of KOs by Sample")
        )
    ], start_collapsed=True)
], className="analysis-header"),
NeonDivider(className="my-2"),


# Seção: Interactions Between Entities
html.Div([
    html.H3("Interactions Between Entities", className="section-title text-center fw-bold text-primary"),
    html.P(
        "Identify interaction patterns between samples, compounds, and genes",
        className="section-objective text-center"
    ),
], className="section-header"),

html.Hr(className="my-2"),

# Sample-Compound Scatter
html.Div(id="compound-scatter-chart", className="section"),
html.Div([
    html.H5("Sample-Compound Interactions", className="analysis-title text-center fw-bold"),
    html.P(
        "This scatter plot highlights the relationship between samples and compounds, illustrating their interactions and associations",
        className="analysis-description text-center"
    ),
    analytical_highlight(),
    html.P(
        "Use this visualization to detect key sample-compound interactions and prioritize samples or compounds of interest",
        className="analysis-insights text-center"
    ),
    dbc.Accordion([
        dbc.AccordionItem(
            html.Div(get_compound_scatter_layout(), className="chart-container"),
            title=("Sample-Compound Interaction Plot")
        )
    ], start_collapsed=True)
], className="analysis-header"),
NeonDivider(className="my-2"),

# Gene-Compound Scatter
html.Div(id="gene-compound-scatter-chart", className="section"),
html.Div([
    html.H5("Gene-Compound Interactions", className="analysis-title text-center fw-bold"),
    html.P(
        "This scatter plot highlights the relationships between genes and compounds, highlighting associations that may indicate important interactions",
        className="analysis-description text-center"
    ),
    analytical_highlight(),
    html.P(
        "By analyzing this chart, you can identify gene-compound pairs with potential biological or chemical significance",
        className="analysis-insights text-center"
    ),
    dbc.Accordion([
        dbc.AccordionItem(
            html.Div(get_gene_compound_scatter_layout(), className="chart-container"),
            title=("Gene-Compound Interaction Plot")
        )
    ], start_collapsed=True)
], className="analysis-header"),
NeonDivider(className="my-2"),

# Sample-Gene Scatter
html.Div(id="sample-gene-scatter-chart", className="section"),
html.Div([
    html.H5("Sample-Gene Associations", className="analysis-title text-center fw-bold"),
    html.P(
        "This scatter plot highlights the relationships between samples and genes, providing insights into genetic patterns across various samples",
        className="analysis-description text-center"
    ),
    analytical_highlight(),
    html.P(
        "By analyzing this plot, you can identify significant gene associations across different samples, aiding in the discovery of genetic hotspots",
        className="analysis-insights text-center"
    ),
    dbc.Accordion([
        dbc.AccordionItem(
            html.Div(get_sample_gene_scatter_layout(), className="chart-container"),
            title=("Sample-Gene Associations Plot")
        )
    ], start_collapsed=True)
], className="analysis-header"),
NeonDivider(className="my-2"),

# Enzyme Activity
html.Div(id="sample-enzyme-activity", className="section"),
html.Div([
    html.H5("Metabolic Enzyme Activity Counts per Sample", className="analysis-title text-center fw-bold"),
    html.P(
        "This bar chart shows the distribution of enzyme activity counts across different samples",
        className="analysis-description text-center"
    ),
    analytical_highlight(),
    html.P(
        "Analyzing enzyme activity counts helps identify variations in enzymatic activity across samples, providing insights into metabolic activity",
        className="analysis-insights text-center"
    ),
    dbc.Accordion([
        dbc.AccordionItem(
            html.Div(get_sample_enzyme_activity_layout(), className="chart-container"),
            title=("Enzyme Activity by Sample")
        )
    ], start_collapsed=True)
], className="analysis-header"),
NeonDivider(className="my-2"),

# Gene-Compound Network
html.Div(id="gene-compound-network", className="section"),
html.Div([
    html.H5("Gene-Compound Interaction Network", className="analysis-title text-center fw-bold"),
    html.P(
        "This network graph visualizes the interactions between genes and compounds, providing insights into functional relationships",
        className="analysis-description text-center"
    ),
    analytical_highlight(),
    html.P(
        "By analyzing this graph, you can explore the connectivity and association strength between genes and compounds, uncovering potential targets or key interactions",
        className="analysis-insights text-center"
    ),
    dbc.Accordion([
        dbc.AccordionItem(
            html.Div(get_gene_compound_network_layout(), className="chart-container"),
            title=("Gene-Compound Interaction")
        )
    ], start_collapsed=True)
], className="analysis-header"),
NeonDivider(className="my-2"),



# Seção: Interaction-Based Rankings
html.Div([
    html.H3("Interaction-Based Rankings", className="section-title text-center fw-bold text-primary"),
    html.P(
        "Prioritize samples, genes or compounds based on specific interactions",
        className="section-objective text-center"
    ),
], className="section-header"),

html.Hr(className="my-2"),

# Seção 9: Ranking of Samples by Compound Interaction
html.Div(id="sample-rank-compounds-chart", className="section"),
html.Div([
    html.H5("Sample-Compound Interaction Rankings", className="analysis-title text-center fw-bold"),
    html.P(
        "This chart ranks samples based on the number and intensity of their interactions with compounds in the dataset",
        className="analysis-description text-center"
    ),
    analytical_highlight(),
    html.P(
        "By examining this chart, you can identify samples with the most interactions, providing valuable insights into their significance in the analysis",
        className="analysis-insights text-center"
    ),
    dbc.Accordion([
        dbc.AccordionItem(
            html.Div(get_sample_rank_compounds_layout(), className="chart-container"),
            title=("Ranking of Samples by Compound Interaction")
        )
    ], start_collapsed=True)
], className="analysis-header"),
NeonDivider(className="my-2"),

# Seção 10: Ranking of Compounds by Sample Interaction
html.Div(id="compound-rank-chart", className="section"),
html.Div([
    html.H5("Compound-Sample Interaction Rankings", className="analysis-title text-center fw-bold"),
    html.P(
        "This chart ranks compounds based on their interactions with samples, showcasing which compounds are most significant",
        className="analysis-description text-center"
    ),
    analytical_highlight(),
    html.P(
        "Use this chart to focus on compounds with the most interactions, which can help prioritize targets for further investigation",
        className="analysis-insights text-center"
    ),
    dbc.Accordion([
        dbc.AccordionItem(
            html.Div(get_compound_rank_layout(), className="chart-container"),
            title=("Ranking of Compounds by Sample Interaction")
        )
    ], start_collapsed=True)
], className="analysis-header"),
NeonDivider(className="my-2"),

# Seção 11: Ranking of Compounds by Gene Interaction
html.Div(id="compound-rank-gene-chart", className="section"),
html.Div([
    html.H5("Compound-Gene Interaction Rankings", className="analysis-title text-center fw-bold"),
    html.P(
        "This ranking chart identifies compounds with associations with genes, revealing key genetic activity",
        className="analysis-description text-center"
    ),
    analytical_highlight(),
    html.P(
        "This visualization is useful to prioritize compounds with significant genetic interactions, aiding in targeted research and analysis",
        className="analysis-insights text-center"
    ),
    dbc.Accordion([
        dbc.AccordionItem(
            html.Div(get_rank_compounds_gene_layout(), className="chart-container"),
            title=("Ranking of Compounds by Gene Interaction")
        )
    ], start_collapsed=True)
], className="analysis-header"),
NeonDivider(className="my-2"),


# Seção: Patterns and Interactions with Heatmaps
html.Div([
    html.H3("Patterns and Interactions with Heatmaps", className="section-title text-center fw-bold text-primary"),
    html.P(
        "This session highlights associations between biological variables such as samples, genes, and pathways",
        className="section-objective text-center"
    ),
], className="section-header"),

html.Hr(className="my-2"),

# Seção 14: Sample vs Reference Agency Heatmap
html.Div(id="sample-reference-heatmap", className="section"),
html.Div([
    html.H5("Sample-Reference Agency Associations Heatmap", className="analysis-title text-center fw-bold"),
    html.P(
        "This heatmap displays the association between samples and reference agencies, highlighting compound occurrences and interactions",
        className="analysis-description text-center"
    ),
    analytical_highlight(),
    html.P(
        "Analyze this heatmap to discover hotspots of compound activity linked to reference agencies",
        className="analysis-insights text-center"
    ),
    dbc.Accordion([
        dbc.AccordionItem(
            html.Div(get_sample_reference_heatmap_layout(), className="chart-container"),
            title=("Sample-Reference Agency Heatmap")
        )
    ], start_collapsed=True)
], className="analysis-header"),
NeonDivider(className="my-2"),

# Seção 16: Gene vs Sample Heatmap
html.Div(id="gene-sample-heatmap", className="section"),
html.Div([
    html.H5("Gene-Sample Association Heatmap", className="analysis-title text-center fw-bold"),
    html.P(
        "This heatmap illustrates the relationship between genes, pathways and samples, providing insights into unique relationships",
        className="analysis-description text-center"
    ),
    analytical_highlight(),
    html.P(
        "By analyzing this heatmap, you can identify trends and hotspots in the gene-sample-pathways interactions, providing insights into their biological relevance",
        className="analysis-insights text-center"
    ),
    hadeg_alert(),
    dbc.Accordion([
        dbc.AccordionItem(
            html.Div(get_gene_sample_heatmap_layout(), className="chart-container"),
            title=("Gene-Sample Heatmap")
        )
    ], start_collapsed=True)
], className="analysis-header"),
NeonDivider(className="my-2"),

# Seção 17: Pathway vs Compound Pathway Heatmap
html.Div(id="pathway-heatmap", className="section"),
html.Div([
    html.H5("Pathway-Compound Heatmap", className="analysis-title text-center fw-bold"),
    html.P(
        "This heatmap visualizes the interaction between metabolic pathways and compound pathways across samples, highlighting gene activity",
        className="analysis-description text-center"
    ),
    analytical_highlight(),
    html.P(
        "Use this heatmap to explore how pathways and compound pathways are interconnected for each sample",
        className="analysis-insights text-center"
    ),
    hadeg_alert(),
    dbc.Accordion([
        dbc.AccordionItem(
            html.Div(get_pathway_heatmap_layout(), className="chart-container"),
            title=("Pathway-Compound Interaction Map")
        )
    ], start_collapsed=True)
], className="analysis-header"),
NeonDivider(className="my-2"),



# Seção: Intersection and Group Exploration
html.Div([
    html.H3("Intersection and Group Exploration", className="section-title text-center fw-bold text-primary"),
    html.P(
        "Investigate overlap and grouping patterns among samples",
        className="section-objective text-center"
    ),
], className="section-header"),

html.Hr(className="my-2"),

# Seção 15: Sample Groups by Compound Class
html.Div(id="sample-groups-chart", className="section"),
html.Div([
    html.H5("Compound-Based Sample Grouping", className="analysis-title text-center fw-bold"),
    html.P(
        "Displays how samples are grouped and classified according to their compound content, emphasizing patterns in their composition",
        className="analysis-description text-center"
    ),
    analytical_highlight(),
    html.P(
        "Use this visualization to detect clusters of samples with similar compound profiles, supporting targeted compound or sample research",
        className="analysis-insights text-center"
    ),
    dbc.Accordion([
        dbc.AccordionItem(
            html.Div(get_sample_groups_layout(), className="chart-container"),
            title=("Sample Grouping by Compound Class Pattern")
        )
    ], start_collapsed=True)
], className="analysis-header"),
NeonDivider(className="my-2"),

# Seção 21: Sample UpSet Plot
html.Div(id="sample-upset-plot", className="section"),
html.Div([
    html.H5("Intersection of Genes Across Samples", className="analysis-title text-center fw-bold"),
    html.P(
        "This UpSet plot visualizes intersections of orthologous genes (KOs) across multiple samples, highlighting overlaps and unique associations",
        className="analysis-description text-center"
    ),
    analytical_highlight(),
    html.P(
        "By analyzing this plot, you can identify shared and unique orthologs between samples, highlighting potential relationships and prioritize samples with shared or unique genes for further exploration",
        className="analysis-insights text-center"
    ),
    dbc.Accordion([
        dbc.AccordionItem(
            html.Div(get_sample_upset_layout(), className="chart-container"),
            title=("Intersection Analysis")
        )
    ], start_collapsed=True)
], className="analysis-header"),
NeonDivider(className="my-2"),

# Seção 20: Sample Clustering Dendrogram
html.Div(id="sample-clustering-dendrogram", className="section"),
html.Div([
    html.H5("Hierarchical Clustering of Samples", className="analysis-title text-center fw-bold"),
    html.P(
        "Hierarchically clusters samples based on genes associated with priority compounds, providing a detailed view of their relationships",
        className="analysis-description text-center"
    ),
    analytical_highlight(),
    html.P(
        "By analyzing this clustering, you can identify patterns of similarity or divergence between samples",
        className="analysis-insights text-center"
    ),
    dbc.Accordion([
        dbc.AccordionItem(
            html.Div(get_sample_clustering_layout(), className="chart-container"),
            title=("Clustering Dendrogram")
        )
    ], start_collapsed=True)
], className="analysis-header"),
NeonDivider(className="my-2"),

# Seção: Toxicity Predictions
html.Div([
    html.H3("Toxicity Predictions", className="section-title text-center fw-bold text-primary"),
    html.P(
        "Visualize and understand toxicity predictions",
        className="section-objective text-center"
    ),
], className="section-header"),

html.Hr(className="my-2"),

# Seção 23: Heatmap of Toxicity Predictions
html.Div(id="toxicity-heatmap-faceted", className="section"),
html.Div([
    html.H5("Comprehensive Toxicity Heatmap", className="analysis-title text-center fw-bold"),
    html.P(
        "This heatmap provides a visual representation of toxicity predictions across the five main categories of analysis",
        className="analysis-description text-center"
    ),
    analytical_highlight(),
    html.P(
        "Explore toxicity predictions to identify high-risk compounds or category, supporting risk assessment and decision-making",
        className="analysis-insights text-center"
    ),
    toxcsm_alert(),
    dbc.Accordion([
        dbc.AccordionItem(
            html.Div(get_toxicity_heatmap_layout(), className="chart-container"),
            title=("Toxicity Prediction Heatmap")
        )
    ], start_collapsed=True)
], className="analysis-header"),
NeonDivider(className="my-2"),
 
html.Div(id="dummy-scroll", style={"display": "none"}),


    ])    
           
      



               
