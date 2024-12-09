from dash import html, dcc
import dash_bootstrap_components as dbc

def get_help_layout():
    """
    Returns the layout of the Help & Support page with an additional Expected Results section.
    """
    return html.Div(
        className="help-page",
        children=[
            # Title Section
            html.H1("Help & Support", className="help-title"),
            html.P(
                "Welcome to the Help & Support page! Here, you will find detailed instructions on how to use this application, "
                "as well as descriptions of the expected results and how to interpret them.",
                className="help-intro"
            ),

            # Help Information Section
            html.Div(
                children=[
                    # Navigation Section
                    html.H2("Navigation", className="help-section-title"),
                    html.P(
                        "Use the navigation menu at the top of the page to access different sections of the application, "
                        "including data upload, result analysis, and interactive visualizations.",
                        className="help-text"
                    ),

                    # Data Upload Section
                    html.H2("Uploading Your Data", className="help-section-title"),
                    html.P(
                        "To start analyzing your data, go to the 'Data Analysis' section. Upload your dataset in a supported format "
                        "(e.g., CSV or Excel). Ensure the data adheres to the expected structure, as outlined in the user guide.",
                        className="help-text"
                    ),

                    # Expected Results Section
                    html.H2("Expected Results", className="help-section-title"),
                    html.Div(id="expected-results-section", className="section"),
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
                    html.Div([dbc.Placeholder(color="success", className="me-1 mt-1 w-100", size="xs")]),

                                        # Section: Results Table (hadegDB)
                    html.Div(id="expected-hadeg-results-table", className="section"),
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
                    html.Div([dbc.Placeholder(color="success", className="me-1 mt-1 w-100", size="xs")]),

                                        # Section: Results Table (ToxCSM)
                    html.Div(id="expected-toxcsm-results-table", className="section"),
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
                    ], className="analysis-header"),
                    html.Div([dbc.Placeholder(color="success", className="me-1 mt-1 w-100", size="xs")]),


                    # Section 4: Gene Count Chart
                    html.Div(id="expected-gene-count-chart", className="section"),
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
                    ], className="analysis-header"),
                    html.Div([dbc.Placeholder(color="success", className="me-1 mt-1 w-100", size="xs")]),

                    # Section 5: Violin Boxplot
                    html.Div(id="expected-violin-boxplot", className="section"),
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
                    ], className="analysis-header"),
                    html.Div([dbc.Placeholder(color="success", className="me-1 mt-1 w-100", size="xs")]),

                    # Section 6: Pathway KO Bar Chart
                    html.Div(id="expected-pathway-ko-bar-chart", className="section"),  # Updated ID for Help page
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
                    ], className="analysis-header"),
                    html.Div([dbc.Placeholder(color="success", className="me-1 mt-1 w-100", size="xs")]),

                    # Section 7: Sample KO Pathway Chart
                    html.Div(id="expected-sample-ko-pathway-chart", className="section"),  # Updated ID for Help page
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
                    ], className="analysis-header"),
                    html.Div([dbc.Placeholder(color="success", className="me-1 mt-1 w-100", size="xs")]),

                    # Section 8: Scatter Plot of Samples vs Compounds
                    html.Div(id="expected-compound-scatter-chart", className="section"),  # Updated ID for Help page
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
                    ], className="analysis-header"),
                    html.Div([dbc.Placeholder(color="success", className="me-1 mt-1 w-100", size="xs")]),

                    # Section 9: Ranking of Samples by Compound Interaction
                    html.Div(id="expected-sample-rank-compounds-chart", className="section"),  # Updated ID for Help page
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
                    ], className="analysis-header"),
                    html.Div([dbc.Placeholder(color="success", className="me-1 mt-1 w-100", size="xs")]),

                    # Section 10: Ranking of Compounds by Sample Interaction
                    html.Div(id="expected-compound-rank-chart", className="section"),  # Updated ID for Help page
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
                    ], className="analysis-header"),
                    html.Div([dbc.Placeholder(color="success", className="me-1 mt-1 w-100", size="xs")]),

                    # Section 11: Ranking of Compounds by Gene Interaction
                    html.Div(id="expected-compound-rank-gene-chart", className="section"),  # Updated ID for Help page
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
                    ], className="analysis-header"),
                    html.Div([dbc.Placeholder(color="success", className="me-1 mt-1 w-100", size="xs")]),

                    # Section 12: Scatter Plot of Genes vs Compounds
                    html.Div(id="expected-gene-compound-scatter-chart", className="section"),  # Updated ID for Help page
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
                    ], className="analysis-header"),
                    html.Div([dbc.Placeholder(color="success", className="me-1 mt-1 w-100", size="xs")]),

                    # Section 13: Scatter Plot of Samples vs Genes
                    html.Div(id="expected-sample-gene-scatter-chart", className="section"),  # Updated ID for Help page
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
                    ], className="analysis-header"),
                    html.Div([dbc.Placeholder(color="success", className="me-1 mt-1 w-100", size="xs")]),

                    # Section 14: Heatmap of Samples vs Reference AG
                    html.Div(id="expected-sample-reference-heatmap", className="section"),  # Updated ID for Help page
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
                    ], className="analysis-header"),
                    html.Div([dbc.Placeholder(color="success", className="me-1 mt-1 w-100", size="xs")]),

                    # Section 15: Sample Groups by Compound Class
                    html.Div(id="expected-sample-groups-chart", className="section"),  # Updated ID for Help page
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
                    ], className="analysis-header"),
                    html.Div([dbc.Placeholder(color="success", className="me-1 mt-1 w-100", size="xs")]),

                    # Section 16: Heatmap of Genes vs Samples
                    html.Div(id="expected-gene-sample-heatmap", className="section"),  # Updated ID for Help page
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
                    ], className="analysis-header"),
                    html.Div([dbc.Placeholder(color="success", className="me-1 mt-1 w-100", size="xs")]),


                    # Section 17: Heatmap of Pathways vs Compound Pathways
                    html.Div(id="expected-pathway-heatmap", className="section"),  # Updated ID for Help page
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
                    ], className="analysis-header"),
                    html.Div([dbc.Placeholder(color="success", className="me-1 mt-1 w-100", size="xs")]),

                    
                    # Section 18: Scatter Plot of KOs by Sample for Pathway
                    html.Div(id="expected-sample-ko-scatter", className="section"),  # Updated ID for Help page
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
                    ], className="analysis-header"),
                    html.Div([dbc.Placeholder(color="success", className="me-1 mt-1 w-100", size="xs")]),


                    # Section 19: Enzyme Activity Counts per Sample
                    html.Div(id="expected-sample-enzyme-activity", className="section"),  # Updated ID for Help page
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
                    ], className="analysis-header"),
                    html.Div([dbc.Placeholder(color="success", className="me-1 mt-1 w-100", size="xs")]),


                    # Section 20: Sample Clustering Dendrogram
                    html.Div(id="expected-sample-clustering-dendrogram", className="section"),  # Updated ID for Help page
                    html.Div([
                        html.H5("Sample Clustering Dendrogram", className="analysis-title"),
                        html.P(
                            "This dendrogram visualizes the hierarchical clustering of samples based on their genetic or metabolic profiles.",
                            className="analysis-description"
                        ),
                        html.P(
                            "By analyzing this clustering, you can identify patterns of similarity or divergence between samples, aiding in deeper insights into their relationships.",
                            className="analysis-insights"
                        ),
                    ], className="analysis-header"),
                    html.Div([dbc.Placeholder(color="success", className="me-1 mt-1 w-100", size="xs")]),


                    # Section 21: UpSet Plot: Samples and KOs
                    html.Div(id="expected-sample-upset-plot", className="section"),  # Updated ID for Help page
                    html.Div([
                        html.H5("UpSet Plot: Samples and KOs", className="analysis-title"),
                        html.P(
                            "This UpSet plot visualizes intersections of KOs (Orthologous Genes) across multiple samples.",
                            className="analysis-description"
                        ),
                        html.P(
                            "By analyzing this plot, you can identify shared and unique orthologs between samples, highlighting potential relationships and diversity.",
                            className="analysis-insights"
                        ),
                    ], className="analysis-header"),
                    html.Div([dbc.Placeholder(color="success", className="me-1 mt-1 w-100", size="xs")]),

                    # Section 22: Gene-Compound Interaction Network
                    html.Div(id="expected-gene-compound-network", className="section"),  # Updated ID for Help page
                    html.Div([
                        html.H5("Gene-Compound Interaction Network", className="analysis-title"),
                        html.P(
                            "This network graph visualizes the interactions between genes and compounds, providing insights into functional relationships.",
                            className="analysis-description"
                        ),
                        html.P(
                            "By analyzing this graph, you can explore the connectivity and association strength between genes and compounds, uncovering potential targets or key interactions.",
                            className="analysis-insights"
                        ),
                    ], className="analysis-header"),
                    html.Div([dbc.Placeholder(color="success", className="me-1 mt-1 w-100", size="xs")]),

                    # Results Visualization Section
                    html.H2("Visualizing Results", className="help-section-title"),
                    html.P(
                        "Results can be visualized in the 'Results' section. Interactive graphs and charts provide insights "
                        "into your data, allowing you to explore pathways, gene activity, and more.",
                        className="help-text"
                    ),

                    # Common Issues Section
                    html.H2("Common Issues", className="help-section-title"),
                    html.Ul(
                        children=[
                            html.Li("Ensure that your dataset follows the required format."),
                            html.Li("If no graph is displayed, check if the filters (dropdown selections) are properly set."),
                            html.Li("If you encounter errors, confirm that the uploaded file does not contain invalid values."),
                            html.Li("For further assistance, contact our support team via the provided email."),
                        ],
                        className="help-list"
                    ),

                    # Resources Section
                    html.H2("Additional Resources", className="help-section-title"),
                    html.P(
                        "For further reading on the biological databases used in this application (e.g., KEGG, PubChem), visit their official websites. "
                        "The user guide and tutorials are also available from the application's main page.",
                        className="help-text"
                    ),
                ]
            ),
        ]
    )
