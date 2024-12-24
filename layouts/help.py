"""
help.py
-------
This script defines the layout of the "Help & Support" page in a Dash web application. 
The page provides detailed instructions, descriptions of the application's key features, 
step-by-step guidance for uploading data, and troubleshooting common issues.

The "Help & Support" page includes:
- Instructions for data upload, processing, and analysis.
- Common issues and their solutions.
- Details on result visualization features.
- A navigation guide explaining the application's main components.
"""

# ----------------------------------------
# Imports
# ----------------------------------------

from dash import html, dcc  # Dash HTML and DCC components for creating the UI
import dash_bootstrap_components as dbc  # Bootstrap components for styled alerts and buttons

# ----------------------------------------
# Function: get_help_layout
# ----------------------------------------

def get_help_layout():
    """
    Returns the layout for the "Help & Support" page.

    The layout includes:
    - A title and introduction.
    - Step-by-step instructions for data upload and analysis.
    - A troubleshooting guide for common issues.
    - Descriptions of result visualization tools.
    - A navigation guide to the application's interface.

    Returns:
    - dash.html.Div: The full layout of the "Help & Support" page as a Dash HTML component.
    """
    return html.Div(
        className="help-page",
        children=[
            # Title Section
            html.H1("Help & Support", className="help-title"),
            html.P(
                "Here, you will find detailed instructions on how to use this application, "
                "as well as descriptions of the key sections and tables within the interface",
                className="help-intro"
            ),

                        # Additional Help Sections
            html.H2("Uploading Your Data", className="help-section-title"),
            html.P(
                "To analyze your data effectively, follow the step-by-step guide below to upload, process, and explore your results",
                className="help-text"
            ),

            # Step-by-step instructions
            html.Ul(
                children=[
            html.Li([
                html.Strong("Step 1 - Upload: "),
                "Upload your data file in the specified format (.txt) by dragging and dropping the file, or selecting it directly. ",
                "Make sure the file follows the expected format to avoid processing issues.",
                html.Br(),
                html.P("Note: Several tools are available to obtain K.O. identifiers from various types of data, such as genomic, DNA, or amino acid sequences. Some of these tools include:"),
                html.Ul([
                    html.Li([
                        html.A("BLASTKOALA", href="https://www.kegg.jp/blastkoala/", target="_blank", title="Visit BLASTKOALA tool")
                    ]),
                    html.Li([
                        html.A("GhostKOALA", href="https://www.kegg.jp/ghostkoala/", target="_blank", title="Visit GhostKOALA tool")
                    ]),
                    html.Li([
                        html.A("Prokka", href="https://github.com/tseemann/prokka", target="_blank", title="Visit Prokka on GitHub")
                    ]),
                    html.Li([
                        html.A("eggNOG-mapper", href="http://eggnog-mapper.embl.de/", target="_blank", title="Visit eggNOG-mapper tool")
                    ]),
                    html.Li([
                        html.A("KAAS", href="https://www.genome.jp/tools/kaas/", target="_blank", title="Visit KAAS tool")
                    ]),
                    html.Li([
                        html.A("DRAM", href="https://github.com/WrightonLabCSU/DRAM", target="_blank", title="Visit DRAM tool")
                    ]),
                    html.Li([
                        html.A("MEGAN", href="https://ab.inf.uni-tuebingen.de/software/megan6/", target="_blank", title="Visit MEGAN tool")
                    ]),
                    html.Li([
                        html.A("DIAMOND", href="https://github.com/bbuchfink/diamond", target="_blank", title="Visit DIAMOND on GitHub")
                    ]),
                    html.Li([
                        html.A("KEGG Mapper", href="https://www.genome.jp/kegg/mapper/", target="_blank", title="Visit KEGG Mapper tool")
                    ]),
                    html.Li([
                        html.A("PanPhlAn", href="https://github.com/SegataLab/panphlan", target="_blank", title="Visit PanPhlAn on GitHub")
                    ])
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
                className="step-list"  # Classe para estilização via CSS
            ),

            html.P(
                "If needed, you can also load an example dataset to test the analysis functionality. This allows you to familiarize yourself with the tool before uploading your own data",
                className="help-text"
            ),


            



            html.H2("Common Issues", className="help-section-title"),
            html.P(
                "Below are common issues you may encounter while using the application, along with solutions to help you resolve them quickly",
                className="help-text"
            ),
            html.Ul(
                children=[
                    html.Li([
                        html.Strong("1. Dataset Format Issues: "),
                        "Ensure that your uploaded dataset strictly follows the required format (.txt). Each sample should be listed with its corresponding KO identifiers in the expected structure. ",
                        "You can refer to the 'How to Use' section for an example dataset or download a sample file to verify the format"
                    ]),
                    html.Br(),
                    html.Li([
                        html.Strong("2. No Graph or Table Displayed: "),
                        "If no graphs or tables are displayed after submitting your data, double-check the following: ",
                        html.Ul(
                            children=[
                                html.Li("Ensure that all required inputs, such as filters or dropdown selections, are properly set"),
                                html.Li("Confirm that your data file is not empty and contains valid entries"),
                                html.Li("Reload the application and re-upload your dataset if the issue persists")
                            ],
                            className="sub-help-list"
                        )
                    ]),
                    html.Br(),
                    html.Li([
                        html.Strong("3. Invalid or Missing Data: "),
                        "Errors may occur if your dataset contains invalid or incomplete values. ",
                        "Check for missing KO identifiers, incorrect sample labels, or corrupted entries. ",
                        "Always validate your dataset before uploading to ensure a smooth processing experience"
                    ]),
                    html.Br(),
                    html.Li([
                        html.Strong("4. Multiple Samples Uploads: "),
                        "If you encounter issues uploading multiple samples, ensure the file does not exceed the allowed limit of 50 samples"
                        
                    ]),
                    html.Br(),
                    html.Li([
                        html.Strong("5. Processing Delays: "),
                        "If the 'Submit' button does not trigger results or the processing takes too long: ",
                        html.Ul(
                            children=[
                                html.Li("Check your internet connection and ensure the file upload completed successfully"),
                                html.Li("Avoid refreshing the page during processing, as it may interrupt the operation"),
                                html.Li("Try uploading the example dataset to verify if the system is working correctly")
                            ],
                            className="sub-help-list"
                        )
                    ]),
                    html.Br(),
                    html.Li([
                        html.Strong("6. Unexpected Errors: "),
                        "If you encounter an unexpected error message or behavior in the application, note the following steps: ",
                        html.Ul(
                            children=[
                                html.Li("Reload the application and clear your browser cache"),
                                html.Li("Verify that the uploaded file adheres to the correct format and does not contain special characters"),
                                html.Li("Check the server logs for any additional error details (if you have administrative access)")
                            ],
                            className="sub-help-list"
                        ),
                        "If the issue persists, contact our support team for assistance"
                    ]),
                    html.Br(),
                    html.Li([
                        html.Strong("7. Need Further Assistance? "),
                        "For additional help, contact our support team at ",
                        html.A("biorempp@gmail.com", href="mailto:biorempp@gmail.com", className="support-link"),
                    ]),
                ],
                className="help-list"
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
                        src="./assets/exemple1.jpg",  # Ensure the image is saved in the `assets/` folder
                        alt="Example Layout of Data Analysis Page",
                        className="example-image"
                    ),
                    html.Div(
                        className="numbered-descriptions",
                        children=[
                            html.H4("1. Navigation Menu", className="help-section-title-right"),
                            html.P(
                                "This section displays the navigation menu. It allows users to access different sections quickly"
                            ),

                            html.H4("2. Results Section", className="help-section-title-right"),
                            html.P(
                                "This section serves as the starting point for presenting results. It displays various analyses and visualizations generated by the application"
                            ),

                            html.H4("3. Analysis Details", className="help-section-title-right"),
                            html.P(
                                "Each analysis includes three main parts: the title of the analysis, a brief description of the result, and an explanation of what is expected from that result"
                            ),

                            html.H4("4. Dropdown Component", className="help-section-title-right"),
                            html.P(
                                "Detailed results are displayed within a dropdown component. Clicking it will reveal specific content for viewing"
                            ),
                        ]
                    ),
                ]
            ),

    ]
)
