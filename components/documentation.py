"""
documentation.py 
-----------
This script defines the layout for the "Features" page of the BioRemPP platform. 

The Features page provides an overview of the platform's capabilities, including:
- Platform Overview
- Key Features and Expected Results
- Data Table Integration
- Gene and Pathway Analysis
- Interactions Between Samples, Compounds, and Genes
- Advanced Analytical Tools
- Toxicity Predictions
- Support Section

The layout utilizes Dash components to organize and display information interactively.
Additionally, a left sidebar menu is integrated to allow quick navigation to each topic or subtopic.
The sidebar has been configured as a sticky menu that follows the user's scrolling.
"""

# ----------------------------------------
# Imports
# ----------------------------------------

from dash import html, dcc  # Dash components for creating the UI
import dash_bootstrap_components as dbc  # Bootstrap components for styling
from components.alerts import hadeg_alert, toxcsm_alert  # Alerts for HADEG and ToxCSM integrations

# ----------------------------------------
# Function: get_features_layout
# ----------------------------------------

def get_features_layout():
    """
    Returns the layout for the BioRemPP Features page.

    The layout is structured into multiple sections:
    - Platform Overview
    - Key Features and Expected Results
    - Toxicity Predictions
    - Advanced Tools and Features
    - Support Section
    
    Each section provides an overview of specific functionalities, interactive data visualizations, 
    or support-related links.
    
    A left sidebar menu is included to navigate directly to each topic and subtopic.
    The sidebar is configured to be sticky, so it remains visible as the user scrolls.
    
    Returns:
    - dash.html.Div: A Div containing the entire layout for the Features page.
    """
    # Define the left sidebar menu with navigation links for each topic or subtopic
    sidebar = dbc.Col(
        [
            html.H2("Navigation Menu", className="sidebar-title"),
            html.Hr(),
            dbc.Nav(
                [
                    dbc.NavLink("Platform Overview", href="#platform-overview", className="sidebar-link-highlight", external_link=True),
                    dbc.NavLink("BioRemPP Database", href="#biorempp-database", className="sidebar-link-highlight", external_link=True),
                    dbc.NavLink("Uploading Your Data", href="#upload-data-section", className="sidebar-link-highlight", external_link=True),                  
                    dbc.NavLink("Expected Results", href="#expected-results-section", className="sidebar-link-highlight", external_link=True),
                    dbc.NavLink("1 - Data Tables & Database Integration", href="#main-results-table", className="sidebar-link", external_link=True),
                    dbc.NavLink("2 - Gene & Metabolic Pathway Analysis", href="#gene-metabolic-analysis", className="sidebar-link", external_link=True),
                    dbc.NavLink("3 - Interactions Between Entities", href="#interactions-entities", className="sidebar-link", external_link=True),
                    dbc.NavLink("4 - Interaction-Based Rankings", href="#interaction-rankings", className="sidebar-link", external_link=True),
                    dbc.NavLink("5 - Patterns & Heatmaps", href="#heatmaps", className="sidebar-link", external_link=True),
                    dbc.NavLink("6 -Intersection & Group Exploration", href="#intersection-group", className="sidebar-link", external_link=True),
                    dbc.NavLink("7 - Toxicity Predictions", href="#toxicity-heatmap-faceted", className="sidebar-link", external_link=True),
                ],
                vertical=True,
                pills=True,
            ),
        ],
        width=3,
        className="sidebar sticky-sidebar"
    )

    # Define the main content area with all sections and corresponding anchor IDs for the sidebar links
    content = dbc.Col(
        [
            # Overview Section
            html.Div(
                id="platform-overview",
                children=[
                    html.H2("Platform Overview", className="help-section-title"),
                    html.P(
                        "BioRemPP is a free platform, accessible to all users without requiring a login. Designed to address the global challenge of environmental pollution caused by priority pollutants, BioRemPP leverages advanced data analysis techniques to explore and identify biotechnological potential in bioremediation",
                        className="features-intro"
                    ),
                    html.P(
                        "The platform provides tools for analyzing genomic data to identify microorganisms capable of pollutant degradation, offering a sustainable approach to environmental restoration. By accepting input in .txt format, where each sample is represented by a unique identifier followed by a list of KEGG Orthologs (KOs), BioRemPP delivers comprehensive insights into the bioremediation potential of samples",
                        className="features-intro"
                    ),
                    html.P(
                        [
                            "Results generated by BioRemPP are structured into seven key sections, integrating data from BioRemPP, ",
                            html.A("HADEG", href="https://github.com/jarojasva/HADEG", target="_blank", title="Visit the HADEG database"), 
                            ", and ", 
                            html.A("ToxCSM", href="https://biosig.lab.uq.edu.au/toxcsm/", target="_blank", title="Visit the ToxCSM database"),
                            " databases. These sections include detailed data tables and visualizations that explore relationships between samples, compounds, genes, and metabolic pathways. The platform offers 20 interactive chart types, enabling users to investigate complex relationships and patterns in their datasets, providing a multi-dimensional characterization of bioremediation potential."
                        ],
                        className="features-intro"
                    ),
                    html.P(
                        "Powered by Python-based libraries such as Pandas and NumPy for data preprocessing, and scikit-learn for identifying significant patterns, BioRemPP ensures robust data manipulation and analysis. Visualization capabilities are enhanced by Matplotlib and Plotly, delivering interactive and informative charts. The user interface, built with Dash, provides an intuitive and dynamic environment for data exploration",
                        className="features-intro"
                    ),
                    html.P(
                        "This platform is entirely new, representing an innovative approach to genomic data analysis for bioremediation. No comparable tools were identified during its development, and it does not rely on third-party software with restrictive terms",
                        className="features-intro"
                    ),
                ],
                className="features-section"
            ),

                    html.Div(
                        id="biorempp-database",
                        children=[
                            html.H1("BioRemPP Database", className="section-title"),
                            html.P(
                                "The BioRemPP database encompasses comprehensive annotations across a diverse set of variables, offering detailed insights into the relationships between genes, compounds, and their roles in bioremediation processes"
                            ),
                            html.P("The following outlines the key database fields. A summary of the database's main components is presented below:"),
                            html.Ul([
                                html.Li("Variables: 8"),
                                html.Li("KO Identifiers: 986"),
                                html.Li("Gene Symbols: 978"),
                                html.Li("Gene Names: 912"),
                                html.Li("Compounds (cpd): 324"),
                                html.Li("Compound Classes: 12"),
                                html.Ul([
                                    html.Li("Aliphatic, Aromatic, Chlorinated, Halogenated, Inorganic,Organometallic, Organophosphorus, Organosulfur, Polyaromatic, Sulfur-containing"),
                                ]),
                                html.Li([
                                    "Reference Categories (referenceAG):",
                                    html.Ul([
                                        html.Li("ATSDR"),
                                        html.Li("CONAMA"),
                                        html.Li("EPA"),
                                        html.Li("EPC"),
                                        html.Li("IARC1"),
                                        html.Li("IARC2A"),
                                        html.Li("IARC2B"),
                                        html.Li("PSL"),
                                        html.Li("WFD")
                                    ])
                                ]),
                                html.Li("Compound Names: 324"),
                                html.Li("Enzyme Activities: 149"),
                            ])
                        ]
                    ),


            html.Div(
                id="upload-data-section",
        className="help-page",
        children=[
            # Title and Introduction Section
            html.P(
                "Here, you will find detailed instructions on how to use this application, "
                "as well as descriptions of the key sections and tables within the interface",
                className="help-intro"
            ),
            # Uploading Your Data Section
            html.H2("Uploading Your Data", className="help-section-title"),
            html.P(
                "To analyze your data effectively, follow the step-by-step guide below to upload, process, and explore your results",
                className="help-text"
            ),
                                html.Ul(
                                    children=[
                                    html.Li([
                        html.Strong("Step 1 - Upload: "),
                        "Upload your data file in the specified format (.txt) by dragging and dropping the file, or selecting it directly. ",
                        "Make sure the file follows the expected format to avoid processing issues.",

                        # Imagem que mostra o passo a passo de upload
                        html.Img(
                            src="./assets/images/documentation/upload.png",
                            alt="Upload Steps",
                            className="doc-image"
                        ),

                        # Legenda explicando os elementos numerados na imagem
                        html.Div(
                            className="doc-legend",
                            children=[
                                html.P([
                                    html.Strong("1 - Drag & Drop or Select a File: "),
                                    "Allows you to quickly upload the file from your local machine by dragging and dropping."
                                ]),
                                html.P([
                                    html.Strong("2 - Load Example Data: "),
                                    "Lets you automatically load a pre-formatted example dataset for testing or demonstration."
                                ]),
                                html.P([
                                    html.Strong("3 - Submit: "),
                                    "Triggers the data processing and integration with the BioRemPP database."
                                ]),
                                html.P([
                                    html.Strong("4 - Feedback Message: "),
                                    "Indicates the example dataset was successfully loaded. You can now proceed."
                                ]),
                                html.P([
                                    html.Strong("5 - Progress Feedback: "),
                                    "Indicates that the example dataset was successfully loaded. You can now proceed to the next step."
                                ]),
                                html.P([
                                    html.Strong("6 - View Results: "),
                                    "After processing, click here to explore and analyze the resulting data."
                                ]),
                            ]
                        ),

                        html.Br(),

                        html.P("Note: Several tools are available to obtain K.O. identifiers from various types of data, such as genomic, DNA, or amino acid sequences. Some of these tools include:"),
                        html.Ul([
                            html.Li(html.A("BLASTKOALA", href="https://www.kegg.jp/blastkoala/", target="_blank", title="Visit BLASTKOALA tool")),
                            html.Li(html.A("GhostKOALA", href="https://www.kegg.jp/ghostkoala/", target="_blank", title="Visit GhostKOALA tool")),
                            html.Li(html.A("Prokka", href="https://github.com/tseemann/prokka", target="_blank", title="Visit Prokka on GitHub")),
                            html.Li(html.A("eggNOG-mapper", href="http://eggnog-mapper.embl.de/", target="_blank", title="Visit eggNOG-mapper tool")),
                            html.Li(html.A("KAAS", href="https://www.genome.jp/tools/kaas/", target="_blank", title="Visit KAAS tool")),
                            html.Li(html.A("DRAM", href="https://github.com/WrightonLabCSU/DRAM", target="_blank", title="Visit DRAM tool")),
                            html.Li(html.A("MEGAN", href="https://ab.inf.uni-tuebingen.de/software/megan6/", target="_blank", title="Visit MEGAN tool")),
                            html.Li(html.A("DIAMOND", href="https://github.com/bbuchfink/diamond", target="_blank", title="Visit DIAMOND on GitHub")),
                            html.Li(html.A("KEGG Mapper", href="https://www.genome.jp/kegg/mapper/", target="_blank", title="Visit KEGG Mapper tool")),
                            html.Li(html.A("PanPhlAn", href="https://github.com/SegataLab/panphlan", target="_blank", title="Visit PanPhlAn on GitHub"))
                        ])
                    ]),

                    html.Br(),
                    html.Li([
                        html.Strong("Step 2 - Process: "),
                        "Once the file is uploaded, click the 'Submit' button to process your data. ",
                        "During this step, your input data is merged with the BioRemPP databases to generate results tables and graphs"
                    ]),
                    html.Br(),
                    html.Li([
                        html.Strong("Step 3 - Analyze: "),
                        "After processing, results will be available for analysis. ",
                        "Explore the tables and visualizations to identify patterns, trends, and insights within your dataset"
                    ]),
                ],
                className="step-list"
            ),
            html.P(
                "If needed, you can also load an example dataset to test the analysis functionality. This allows you to familiarize yourself with the tool before uploading your own data",
                className="help-text"
            ),
            # Visualizing Results Section
            html.H2("Visualizing Results", className="help-section-title"),
            html.P(
                "The 'Results' section provides a comprehensive suite of interactive tools and visualizations to help you analyze your data effectively. "
                "You can explore key features, such as pathways, gene activity, compound interactions, and clustering patterns. "
                "Each result is presented in an intuitive format, including interactive charts, heatmaps, scatter plots, and hierarchical dendrograms. "
                "These visualizations allow you to identify trends, correlations, and insights across your dataset, facilitating a deeper understanding of biological relationships",
                className="help-text"
            ),
            html.P(
                "Use filters and dropdowns to focus on specific data points, customize views, and prioritize the most relevant results. "
                "The visual outputs are designed to be user-friendly, enabling you to navigate complex data",
                className="help-text"
            ),
            # Navigation Section
            html.H2("Navigation", className="help-section-title"),
            html.P(
                "Below is a detailed explanation of the main components of the application, corresponding to the numbered areas in the image below",
                className="help-text"
            ),
            html.Div(
                className="image-container",
                children=[
                    html.Img(
                        src="./assets/exemple1.png",
                        alt="Example Layout of Data Analysis Page",
                        className="example-image"
                    ),
                    html.Div(
                        className="doc-legend",  # Classe para manter o padrão das legendas recentes
                        children=[
                            html.P([
                                html.Strong("1 - Navigation Menu: "),
                                "This section displays the navigation menu. It allows users to access different sections quickly."
                            ]),
                            html.P([
                                html.Strong("2 - Results Section: "),
                                "This section serves as the starting point for presenting results. It displays various analyses and visualizations generated by the application."
                            ]),
                            html.P([
                                html.Strong("3 - Analysis Details: "),
                                "Each analysis includes three main parts: the title of the analysis, a brief description of the result, and an explanation of what is expected from that result."
                            ]),
                            html.P([
                                html.Strong("4 - Dropdown Component: "),
                                "Detailed results are displayed within a dropdown component. Clicking it will reveal specific content for viewing."
                            ]),
                        ]
                    ),

                ]
            ),
        ]
    ),

            # Expected Results Section
            html.Div(                
                children=[
                    # BioRemPP Database Subsection

html.Div(
    id="expected-results-section",
    children=[
        # Expected Results Title and Description (após o bloco de banco de dados)
        html.H2("Expected Results", className="features-section-title"),
        html.P(
            "Explore the insights generated by BioRemPP through its various visualization tools. "
            "Each result provides detailed information and actionable data to support your research objectives",
            className="features-text"
        ),
    ]
),


                    # Section 1: Main Results Table
                    html.Div(
                        id="main-results-table",
                        className="section",
                        children=[
                            html.Div(
                                className="section-header",
                                children=[
                                    html.H3("1 - Data Tables and Database Integration", className="section-title"),
                                    html.P("Provide an overview of the data integrated into the databases", className="section-objective"),
                                ]
                            ),
                    html.Div(
                        className="analysis-header",
                        children=[
                            html.H5("BioRemPP Results Table", className="analysis-title"),
                            html.P(
                                "This table presents the processed data merged with the BioRemPP database, offering a comprehensive overview of the input data and its matched records",
                                className="analysis-description"
                            ),
                            html.P(
                                "The merged table reveals how well the input data aligns with the main database, providing insights into the completeness and relevance of the data",
                                className="analysis-insights"
                            ),
                            # Image of the Results Table
                            html.Img(
                                src="./assets/images/documentation/main-results-table.png",
                                alt="Main Results Table",
                                className="doc-image"
                            ),
                            # Short legend explaining numbered elements in the image (title + description)
                            html.Div(
                                className="doc-legend",
                                children=[
                                    html.P([
                                        html.Strong("1 - Table Result: "),
                                        "Represents the result displayed upon clicking a row or expanding a specific record."
                                    ]),
                                    html.P([
                                        html.Strong("2 - Database Features: "),
                                        "Highlights the features (columns) retrieved from the BioRemPP database."
                                    ]),
                                    html.P([
                                        html.Strong("3 - Advanced Filtering: "),
                                        "Indicates advanced filtering options for narrowing down table results."
                                    ]),
                                ]
                            ),
                            html.Div([dbc.Placeholder(color="success", className="me-1 mt-1 w-100", size="xs")]),
                        ]
                    ),
                        ]
                    ),

                    # Section 2: HADEG Results Table
                    html.Div(
                        id="hadeg-results-table",
                        className="section",
                        children=[
                            html.Div(
                                className="analysis-header",
                                children=[
                                    html.H5("HADEG Results Table", className="analysis-title"),
                                    html.P(
                                        "This table contains data merged with the HADEG database, enabling the exploration of additional annotations and insights",
                                        className="analysis-description"
                                    ),
                                    html.P(
                                        "The table helps identify significant matches with HADEG, enhancing the understanding of potential functional and structural associations",
                                        className="analysis-insights"
                                    ),
                                    # Alerta específico (permanece como já definido)
                                    hadeg_alert(),
                                    # Nova imagem do HADEG Results Table
                                    html.Img(
                                        src="./assets/images/documentation/hadeg-results-table.png",
                                        alt="HADEG Results Table",
                                        className="doc-image"
                                    ),
                                    # Mesma legenda utilizada no Main Results Table
                                    html.Div(
                                        className="doc-legend",
                                        children=[
                                            html.P([
                                                html.Strong("1 - Table Result: "),
                                                "Represents the result displayed upon clicking a row or expanding a specific record."
                                            ]),
                                            html.P([
                                                html.Strong("2 - Database Features: "),
                                                "Highlights the features (columns) retrieved from the HADEG database."
                                            ]),
                                            html.P([
                                                html.Strong("3 - Advanced Filtering: "),
                                                "Indicates advanced filtering options for narrowing down table results."
                                            ]),
                                        ]
                                    ),
                                    html.Div([dbc.Placeholder(color="success", className="me-1 mt-1 w-100", size="xs")]),
                                ]
                            ),
                        ]
                    ),

                    # Section 3: ToxCSM Results Table
                    html.Div(
                        id="toxcsm-results-table",
                        className="section",
                        children=[
                            html.Div(
                                className="analysis-header",
                                children=[
                                    html.H5("ToxCSM Results Table", className="analysis-title"),
                                    html.P(
                                        "This table shows data merged with the TOXCSM database, providing toxicity predictions and compound interactions",
                                        className="analysis-description"
                                    ),
                                    html.P(
                                        "By analyzing this table, you can assess the toxicity potential and prioritize compounds for further investigation",
                                        className="analysis-insights"
                                    ),
                                    # Alerta específico (permanece como já definido)
                                    toxcsm_alert(),
                                    # Nova imagem do ToxCSM Results Table
                                    html.Img(
                                        src="./assets/images/documentation/toxcsm-results-table.png",
                                        alt="ToxCSM Results Table",
                                        className="doc-image"
                                    ),
                                    # Mesma legenda utilizada no Main Results Table
                                    html.Div(
                                        className="doc-legend",
                                        children=[
                                            html.P([
                                                html.Strong("1 - Table Result: "),
                                                "Represents the result displayed upon clicking a row or expanding a specific record."
                                            ]),
                                            html.P([
                                                html.Strong("2 - Database Features: "),
                                                "Highlights the features (columns) retrieved from the ToxCSM database."
                                            ]),
                                            html.P([
                                                html.Strong("3 - Advanced Filtering: "),
                                                "Indicates advanced filtering options for narrowing down table results."
                                            ]),
                                        ]
                                    ),
                                    html.Div([dbc.Placeholder(color="success", className="me-1 mt-1 w-100", size="xs")]),
                                ]
                            ),
                        ]
                    ),
                ]
            ),

            # Section 2: Gene and Metabolic Pathway Analysis
            html.Div(
                id="gene-metabolic-analysis",
                className="section-header",
                children=[
                    html.H3("2 - Gene and Metabolic Pathway Analysis", className="section-title"),
                    html.P("Explore genes and metabolic pathways associated with compounds", className="section-objective"),
                ]
            ),

            # Section 4: Gene Count Chart
            html.Div(
                id="gene-count-chart",
                className="section",
                children=[
                    html.Div(
                        className="analysis-header",
                        children=[
                            html.H5("Gene Count Associated with Priority Compounds", className="analysis-title"),
                            html.P(
                                "This bar chart displays the count of unique genes associated with priority compounds for each sample",
                                className="analysis-description"
                            ),
                            html.P(
                                "By analyzing this chart, you can identify which samples have a higher number of unique gene associations, offering insights into potential hotspots of genetic activity",
                                className="analysis-insights"
                            ),
                            # Image illustrating the chart
                            html.Img(
                                src="./assets/images/documentation/gene-count-chart.png",
                                alt="Gene Count Chart",
                                className="doc-image"
                            ),
                            # Legend explaining the numbered elements in the image
                            html.Div(
                                className="doc-legend",
                                children=[
                                    html.P([
                                        html.Strong("1 - Chart Header: "),
                                        "Displays the title and a concise overview of the chart’s purpose."
                                    ]),
                                    html.P([
                                        html.Strong("2 - Range Filter: "),
                                        "Allows filtering of the samples by gene count, focusing the analysis on a specific range."
                                    ]),
                                    html.P([
                                        html.Strong("3 - Interactive Chart Tools: "),
                                        "Provide functionalities for downloading the chart, zooming in/out, resetting axes, and selecting specific data regions."
                                    ]),
                                    html.P([
                                        html.Strong("4 - X-Axis: "),
                                        "Indicates the unique gene counts associated with each sample, facilitating quick comparisons across different samples."
                                    ]),
                                ]
                            ),
                        ]
                    ),
                    html.Div([dbc.Placeholder(color="success", className="me-1 mt-1 w-100", size="xs")]),
                ]
            ),


            # Section 5: Violin Boxplot (Gene Distribution)
            html.Div(
                id="violin-boxplot",
                className="section",
                children=[
                    html.Div(
                        className="analysis-header",
                        children=[
                            html.H5("Gene Distribution", className="analysis-title"),
                            html.P(
                                "This violin boxplot illustrates the distribution of unique genes associated with priority compounds across samples",
                                className="analysis-description"
                            ),
                            html.P(
                                "Identifies trends and outliers in gene distribution, providing a comprehensive view of genetic activity",
                                className="analysis-insights"
                            ),
                            # Image illustrating the Violin Boxplot
                            html.Img(
                                src="./assets/images/documentation/violin-boxplot.png",
                                alt="Violin Boxplot for Gene Distribution",
                                className="doc-image"
                            ),
                            # Legend explaining the numbered elements in the image
                            html.Div(
                                className="doc-legend",
                                children=[
                                    html.P([
                                        html.Strong("1 - Sample Filter: "),
                                        "Enables selection or filtering of specific samples, adjusting which data are displayed in the violin boxplot."
                                    ]),
                                    html.P([
                                        html.Strong("2 - Distribution Statistics: "),
                                        "Represents the violin and boxplot overlay, showing the spread of gene counts, including min, max, median, quartiles, and potential outliers"
                                    ]),
                                ]
                            ),
                        ]
                    ),
                    html.Div([dbc.Placeholder(color="success", className="me-1 mt-1 w-100", size="xs")]),
                ]
            ),


            # Section 6: Pathway KO Bar Chart
            html.Div(
                id="pathway-ko-bar-chart",
                className="section",
                children=[
                    html.Div(
                        className="analysis-header",
                        children=[
                            html.H5("Distribution of Genes in Xenobiotics Biodegradation Pathways", className="analysis-title"),
                            html.P(
                                "This bar chart highlights the distribution of KEGG Ortholog (KO) counts across 20 degradation pathways",
                                className="analysis-description"
                            ),
                            html.P(
                                "By analyzing this chart, you can gain insights into the functional diversity of pathways and identify dominant or underrepresented pathways in the dataset",
                                className="analysis-insights"
                            ),
                            # Image illustrating the Pathway KO Bar Chart
                            html.Img(
                                src="./assets/images/documentation/pathway-ko-bar-chart.png",
                                alt="Pathway KO Bar Chart",
                                className="doc-image"
                            ),
                            # Legend explaining the numbered elements in the image
                            html.Div(
                                className="doc-legend",
                                children=[
                                    html.P([
                                        html.Strong("1 - Sample Filter: "),
                                        "Allows you to select a specific sample (e.g., Acinetobacter Baumannii - acb), refining the chart to show only that sample’s pathway gene counts."
                                    ]),
                                    html.P([
                                        html.Strong("2 - Pathway Gene Counts: "),
                                        "Displays the number of unique genes associated with each degradation pathway for the selected sample, helping to identify the most represented pathways."
                                    ]),
                                ]
                            ),
                        ]
                    ),
                    html.Div([dbc.Placeholder(color="success", className="me-1 mt-1 w-100", size="xs")]),
                ]
            ),


            # Section 7: Sample KO Pathway Chart
            html.Div(
                id="sample-ko-pathway-chart",
                className="section",
                children=[
                    html.Div(
                        className="analysis-header",
                        children=[
                            html.H5("Sample-Specific Pathway Activity", className="analysis-title"),
                            html.P(
                                "This bar chart presents the KEGG Ortholog (KO) distribution across pathways, grouped by sample",
                                className="analysis-description"
                            ),
                            html.P(
                                "This visualization allows you to understand how different pathways are represented within each sample, helping to identify pathway-specific trends",
                                className="analysis-insights"
                            ),
                            # Image illustrating the Sample KO Pathway Chart
                            html.Img(
                                src="./assets/images/documentation/sample-ko-pathway-chart.png",
                                alt="Sample KO Pathway Chart",
                                className="doc-image"
                            ),
                            # Legend explaining the numbered elements in the image
                            html.Div(
                                className="doc-legend",
                                children=[
                                    html.P([
                                        html.Strong("1 - Pathway Filter: "),
                                        "Allows the user to select a specific pathway from a dropdown, focusing the analysis on the chosen pathway."
                                    ]),
                                    html.P([
                                        html.Strong("2 - Selected Pathway: "),
                                        "Displays the pathway currently in focus (e.g., Aminobenzoate), indicating which data is shown."
                                    ]),
                                    html.P([
                                        html.Strong("3 - Sample-Specific Gene Counts: "),
                                        "Shows how many unique genes are present in each sample for the selected pathway."
                                    ]),
                                ]
                            ),
                        ]
                    ),
                    html.Div([dbc.Placeholder(color="success", className="me-1 mt-1 w-100", size="xs")]),
                ]
            ),

            # Section 18: Scatter Plot of KOs by Sample for Pathway
            html.Div(
                id="sample-ko-scatter",
                className="section",
                children=[
                    html.Div(
                        className="analysis-header",
                        children=[
                        html.H5("Sample-Compound Interactions in Xenobiotics Biodegradation Pathways", className="analysis-title"),
                        html.P(
                            "This scatter plot shows the distribution of genes across different samples for a specific pathway",
                            className="analysis-description"
                        ),
                        html.P(
                            "By analyzing this scatter plot, you can identify patterns of genes across samples, helping to pinpoint critical samples for specific pathways",
                            className="analysis-insights"
                        ),
                        # Image illustrating the scatter plot
                        html.Img(
                            src="./assets/images/documentation/sample-ko-scatter.png",
                            alt="Scatter Plot of KOs by Sample",
                            className="doc-image"
                        ),
                        # Legend explaining the numbered elements in the image
                        html.Div(
                            className="doc-legend",
                            children=[
                                html.P([
                                    html.Strong("1 - Chart Title: "),
                                    "Provides a concise description of the scatter plot and what it represents."
                                ]),
                                html.P([
                                    html.Strong("2 - Pathway Filter: "),
                                    "Allows the user to select a specific pathway (e.g., Fluorobenzoate), focusing the plot on the KOs associated with that pathway."
                                ]),
                                html.P([
                                    html.Strong("3 - Genes Distribution by Sample: "),
                                    "Displays individual gene points across different samples, helping to identify which samples harbor genes relevant to the chosen pathway."
                                ]),
                            ]
                        ),
                    ]
                    ),
                    html.Div([dbc.Placeholder(color="success", className="me-1 mt-1 w-100", size="xs")]),
                ]
            ),


            # Section 3: Interactions Between Entities (Samples, Compounds, and Genes)
            html.Div(
                id="interactions-entities",
                className="section-header",
                children=[
                    html.H3("3 - Interactions Between Entities (Samples, Compounds, and Genes)", className="section-title"),
                    html.P("Identify interaction patterns between samples, compounds, and genes", className="section-objective"),
                ]
            ),

            # Section 8: Scatter Plot of Samples vs Compounds
            html.Div(
                id="compound-scatter-chart",
                className="section",
                children=[
                    html.Div(
                        className="analysis-header",
                        children=[
                            html.H5("Sample-Compound Interactions", className="analysis-title"),
                            html.P(
                                "This scatter plot highlights the relationship between samples and compounds, illustrating their interactions and associations",
                                className="analysis-description"
                            ),
                            html.P(
                                "Use this visualization to detect key sample-compound interactions and prioritize samples or compounds of interest",
                                className="analysis-insights"
                            ),
                            # Image illustrating the Sample-Compound Interaction Plot
                            html.Img(
                                src="./assets/images/documentation/compound-scatter-chart.png",
                                alt="Sample-Compound Interaction Plot",
                                className="doc-image"
                            ),
                            # Legend explaining the numbered elements in the image
                            html.Div(
                                className="doc-legend",
                                children=[
                                    html.P([
                                        html.Strong("1 - Plot Title: "),
                                        "Displays the overall name of the chart (e.g., 'Sample-Compound Interaction Plot')."
                                    ]),
                                    html.P([
                                        html.Strong("2 - Compound Class Filter: "),
                                        "Allows selection of a specific compound class (e.g., 'Metal'), focusing the scatter plot on compounds within that category."
                                    ]),
                                    html.P([
                                        html.Strong("3 - Scatter Plot of Samples vs Compounds: "),
                                        "Shows each compound’s presence or interaction across different samples, highlighting potential key relationships or high-priority samples."
                                    ]),
                                ]
                            ),
                        ]
                    ),
                    html.Div([dbc.Placeholder(color="success", className="me-1 mt-1 w-100", size="xs")]),
                ]
            ),


            # Section 12: Scatter Plot of Genes vs Compounds
            html.Div(
                id="gene-compound-scatter-chart",
                className="section",
                children=[
                    html.Div(
                        className="analysis-header",
                        children=[
                            html.H5("Gene-Compound Interactions", className="analysis-title"),
                            html.P(
                                "This scatter plot highlights the relationships between genes and compounds, highlighting associations that may indicate important interactions",
                                className="analysis-description"
                            ),
                            html.P(
                                "By analyzing this chart, you can identify gene-compound pairs with potential biological or chemical significance",
                                className="analysis-insights"
                            ),
                        ]
                    ),
                    html.Div([dbc.Placeholder(color="success", className="me-1 mt-1 w-100", size="xs")]),
                ]
            ),

            # Section 13: Scatter Plot of Samples vs Genes
            html.Div(
                id="sample-gene-scatter-chart",
                className="section",
                children=[
                    html.Div(
                        className="analysis-header",
                        children=[
                            html.H5("Sample-Gene Associations", className="analysis-title"),
                            html.P(
                                "This scatter plot highlights the relationships between samples and genes, providing insights into genetic patterns across various samples",
                                className="analysis-description"
                            ),
                            html.P(
                                "By analyzing this plot, you can identify significant gene associations across different samples, aiding in the discovery of genetic hotspots",
                                className="analysis-insights"
                            ),
                        ]
                    ),
                    html.Div([dbc.Placeholder(color="success", className="me-1 mt-1 w-100", size="xs")]),
                ]
            ),

            # Section 19: Enzyme Activity Counts per Sample
            html.Div(
                id="sample-enzyme-activity",
                className="section",
                children=[
                    html.Div(
                        className="analysis-header",
                        children=[
                            html.H5("Metabolic Enzyme Activity Counts per Sample", className="analysis-title"),
                            html.P(
                                "This bar chart shows the distribution of enzyme activity counts across different samples",
                                className="analysis-description"
                            ),
                            html.P(
                                "Analyzing enzyme activity counts helps identify variations in enzymatic activity across samples, providing insights into metabolic activity",
                                className="analysis-insights"
                            ),
                        ]
                    ),
                    html.Div([dbc.Placeholder(color="success", className="me-1 mt-1 w-100", size="xs")]),
                ]
            ),

            # Section 22: Gene-Compound Interaction Network
            html.Div(
                id="gene-compound-network",
                className="section",
                children=[
                    html.Div(
                        className="analysis-header",
                        children=[
                            html.H5("Gene-Compound Interaction Network", className="analysis-title"),
                            html.P(
                                "This network graph visualizes the interactions between genes and compounds, providing insights into functional relationships",
                                className="analysis-description"
                            ),
                            html.P(
                                "By analyzing this graph, you can explore the connectivity and association strength between genes and compounds, uncovering potential targets or key interactions",
                                className="analysis-insights"
                            ),
                        ]
                    ),
                    html.Div([dbc.Placeholder(color="success", className="me-1 mt-1 w-100", size="xs")]),
                ]
            ),

            # Section 4: Interaction-Based Rankings
            html.Div(
                id="interaction-rankings",
                className="section-header",
                children=[
                    html.H3("4 - Interaction-Based Rankings", className="section-title"),
                    html.P("Prioritize samples, genes or compounds based on specific interactions", className="section-objective"),
                ]
            ),

            # Section 9: Ranking of Samples by Compound Interaction
            html.Div(
                id="sample-rank-compounds-chart",
                className="section",
                children=[
                    html.Div(
                        className="analysis-header",
                        children=[
                            html.H5("Sample-Compound Interaction Rankings", className="analysis-title"),
                            html.P(
                                "This chart ranks samples based on the number and intensity of their interactions with compounds in the dataset",
                                className="analysis-description"
                            ),
                            html.P(
                                "By examining this chart, you can identify samples with the most interactions, providing valuable insights into their significance in the analysis",
                                className="analysis-insights"
                            ),
                        ]
                    ),
                    html.Div([dbc.Placeholder(color="success", className="me-1 mt-1 w-100", size="xs")]),
                ]
            ),

            # Section 10: Ranking of Compounds by Sample Interaction
            html.Div(
                id="compound-rank-chart",
                className="section",
                children=[
                    html.Div(
                        className="analysis-header",
                        children=[
                            html.H5("Compound-Sample Interaction Rankings", className="analysis-title"),
                            html.P(
                                "This chart ranks compounds based on their interactions with samples, showcasing which compounds are most significant",
                                className="analysis-description"
                            ),
                            html.P(
                                "Use this chart to focus on compounds with the most interactions, which can help prioritize targets for further investigation",
                                className="analysis-insights"
                            ),
                        ]
                    ),
                    html.Div([dbc.Placeholder(color="success", className="me-1 mt-1 w-100", size="xs")]),
                ]
            ),

            # Section 11: Ranking of Compounds by Gene Interaction
            html.Div(
                id="compound-rank-gene-chart",
                className="section",
                children=[
                    html.Div(
                        className="analysis-header",
                        children=[
                            html.H5("Compound-Gene Interaction Rankings", className="analysis-title"),
                            html.P(
                                "This ranking chart identifies compounds with associations with genes, revealing key genetic activity",
                                className="analysis-description"
                            ),
                            html.P(
                                "This visualization is useful to prioritize compounds with significant genetic interactions, aiding in targeted research and analysis",
                                className="analysis-insights"
                            ),
                        ]
                    ),
                    html.Div([dbc.Placeholder(color="success", className="me-1 mt-1 w-100", size="xs")]),
                ]
            ),

            # Section 5: Patterns and Interactions with Heatmaps
            html.Div(
                id="heatmaps",
                className="section-header",
                children=[
                    html.H3("5 - Patterns and Interactions with Heatmaps", className="section-title"),
                    html.P("This session highlights associations between biological variables such as samples, genes, and pathways", className="section-objective"),
                ]
            ),

            # Section 14: Heatmap of Samples vs Reference AG
            html.Div(
                id="sample-reference-heatmap",
                className="section",
                children=[
                    html.Div(
                        className="analysis-header",
                        children=[
                            html.H5("Sample-Reference Agency Associations Heatmap", className="analysis-title"),
                            html.P(
                                "This heatmap displays the association between samples and reference agencies, highlighting compound occurrences and interactions",
                                className="analysis-description"
                            ),
                            html.P(
                                "Analyze this heatmap to discover hotspots of compound activity linked to reference agencies",
                                className="analysis-insights"
                            ),
                        ]
                    ),
                    html.Div([dbc.Placeholder(color="success", className="me-1 mt-1 w-100", size="xs")]),
                ]
            ),

            # Section 16: Heatmap of Genes vs Samples
            html.Div(
                id="gene-sample-heatmap",
                className="section",
                children=[
                    html.Div(
                        className="analysis-header",
                        children=[
                            html.H5("Gene-Sample Association Heatmap", className="analysis-title"),
                            html.P(
                                "This heatmap illustrates the relationship between genes, pathways and samples, providing insights into unique relationships",
                                className="analysis-description"
                            ),
                            html.P(
                                "By analyzing this heatmap, you can identify trends and hotspots in the gene-sample-pathways interactions, providing insights into their biological relevance",
                                className="analysis-insights"
                            ),
                            hadeg_alert(),  # Alert maintained as requested
                        ]
                    ),
                    html.Div([dbc.Placeholder(color="success", className="me-1 mt-1 w-100", size="xs")]),
                ]
            ),

            # Section 17: Heatmap of Pathways vs Compound Pathways
            html.Div(
                id="pathway-heatmap",
                className="section",
                children=[
                    html.Div(
                        className="analysis-header",
                        children=[
                            html.H5("Pathway-Compound Heatmap", className="analysis-title"),
                            html.P(
                                "This heatmap visualizes the interaction between metabolic pathways and compound pathways across samples, highlighting gene activity",
                                className="analysis-description"
                            ),
                            html.P(
                                "Use this heatmap to explore how pathways and compound pathways are interconnected for each sample",
                                className="analysis-insights"
                            ),
                            hadeg_alert(),  # Alert maintained as requested
                        ]
                    ),
                    html.Div([dbc.Placeholder(color="success", className="me-1 mt-1 w-100", size="xs")]),
                ]
            ),

            # Section 6: Intersection and Group Exploration
            html.Div(
                id="intersection-group",
                className="section-header",
                children=[
                    html.H3("6 - Intersection and Group Exploration", className="section-title"),
                    html.P("Investigate overlap and grouping patterns among samples", className="section-objective"),
                ]
            ),

            # Section 15: Sample Groups by Compound Class
            html.Div(
                id="sample-groups-chart",
                className="section",
                children=[
                    html.Div(
                        className="analysis-header",
                        children=[
                            html.H5("Compound-Based Sample Grouping", className="analysis-title"),
                            html.P(
                                "Displays how samples are grouped and classified according to their compound content, emphasizing patterns in their composition",
                                className="analysis-description"
                            ),
                            html.P(
                                "Use this visualization to detect clusters of samples with similar compound profiles, supporting targeted compound or sample research",
                                className="analysis-insights"
                            ),
                        ]
                    ),
                    html.Div([dbc.Placeholder(color="success", className="me-1 mt-1 w-100", size="xs")]),
                ]
            ),

            # Section 21: Sample UpSet Plot
            html.Div(
                id="sample-upset-plot",
                className="section",
                children=[
                    html.Div(
                        className="analysis-header",
                        children=[
                            html.H5("Intersection of Genes Across Samples", className="analysis-title"),
                            html.P(
                                "This UpSet plot visualizes intersections of orthologous genes (KOs) across multiple samples, highlighting overlaps and unique associations",
                                className="analysis-description"
                            ),
                            html.P(
                                "By analyzing this plot, you can identify shared and unique orthologs between samples, highlighting potential relationships and prioritize samples with shared or unique genes for further exploration",
                                className="analysis-insights"
                            ),
                        ]
                    ),
                    html.Div([dbc.Placeholder(color="success", className="me-1 mt-1 w-100", size="xs")]),
                ]
            ),

            # Section 20: Sample Clustering Dendrogram
            html.Div(
                id="sample-clustering-dendrogram",
                className="section",
                children=[
                    html.Div(
                        className="analysis-header",
                        children=[
                            html.H5("Hierarchical Clustering of Samples", className="analysis-title"),
                            html.P(
                                "Hierarchically clusters samples based on genes associated with priority compounds, providing a detailed view of their relationships",
                                className="analysis-description"
                            ),
                            html.P(
                                "By analyzing this clustering, you can identify patterns of similarity or divergence between samples",
                                className="analysis-insights"
                            ),
                        ]
                    ),
                    html.Div([dbc.Placeholder(color="success", className="me-1 mt-1 w-100", size="xs")]),
                ]
            ),

                            html.Div([
            html.H3("7 - Toxicity Predictions", className="section-title"),
            html.P(
                "Visualize and understand toxicity predictions",
                className="section-objective"
            ),
        ], className="section-header"),

            # Section 7: Toxicity Predictions
            html.Div(
                id="toxicity-heatmap-faceted",
                className="section",
                children=[
                    html.Div(
                        className="analysis-header",
                        children=[
                            html.H5("Comprehensive Toxicity Heatmap", className="analysis-title"),
                            html.P(
                                "This heatmap provides a visual representation of toxicity predictions across the five main categories of analysis",
                                className="analysis-description"
                            ),
                            html.P(
                                "Explore toxicity predictions to identify high-risk compounds or category, supporting risk assessment and decision-making",
                                className="analysis-insights"
                            ),
                            toxcsm_alert(),  # Alert maintained as requested
                        ]
                    ),
                    html.Div([dbc.Placeholder(color="success", className="me-1 mt-1 w-100", size="xs")]),
                ]
            ),
        ],
        width=9
    )

    # Assemble the overall layout using a container and row for responsiveness.
    layout = dbc.Container(
        dbc.Row([sidebar, content]),
        fluid=True,
        className="features-container"
    )
    return layout

# For local testing
if __name__ == "__main__":
    import dash
    app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
    app.layout = get_features_layout()
    app.run_server(debug=True)
