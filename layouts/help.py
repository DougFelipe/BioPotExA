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
