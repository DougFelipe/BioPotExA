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

                                        # Expected Results Section
                    html.H2("Expected Results", className="help-section-title"),
                    html.Div(id="expected-results-section", className="section"),
                        html.A(
                        "Visit the BioPExA Features page for more information.",
                        href="/features",
                        className="features-link"
                    ),

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
