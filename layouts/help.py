from dash import html, dcc
import dash_bootstrap_components as dbc

def get_help_layout():
    """
    Returns the layout of the Help & Support page with the detailed descriptions of the numbered components.
    """
    return html.Div(
        className="help-page",
        children=[
            # Title Section
            html.H1("Help & Support", className="help-title"),
            html.P(
                "Welcome to the Help & Support page! Here, you will find detailed instructions on how to use this application, "
                "as well as descriptions of the key sections and tables within the interface.",
                className="help-intro"
            ),

            # Navigation Section
            html.H2("Navigation", className="help-section-title"),
            html.P(
                "Below is a detailed explanation of the main components of the application, corresponding to the numbered areas in the image below.",
                className="help-text"
            ),
            html.Div(
                className="image-container",
                children=[
                    html.Img(
                        src="./assets/exemple1.jpg",  # Certifique-se de salvar a imagem em `assets/`
                        alt="Example Layout of Data Analysis Page",
                        className="example-image"
                    ),
                    html.Div(
                        className="numbered-descriptions",
                        children=[
                            html.H4("1. Title and Navigation Menu", className="help-section-title-right"),
                            html.P(
                                "This section displays the application title ('BioRemPP') and a navigation menu. It allows users to access different sections quickly."
                            ),

                            html.H4("2. Section: Data Tables and Database Integration", className="help-section-title-right"),
                            html.P(
                                "Provides an overview of the data integrated into the databases. This section includes the primary analysis of input data combined with various databases such as `hadegDB` and `ToxCSM`."
                            ),

                            html.H4("3. Main Results Table", className="help-section-title-right"),
                            html.P(
                                "This table displays the processed data merged with the main database. It offers a detailed overview of input data and matched records, "
                                "allowing users to evaluate the completeness and relevance of the dataset."
                            ),

                            html.H4("4. Results Table (hadegDB) and Results Table (ToxCSM)", className="help-section-title-right"),
                            html.Ul(
                                children=[
                                    html.Li([
                                        html.Strong("Results Table (hadegDB): "),
                                        "Displays data merged with the `hadegDB` database. This table provides insights into functional and structural annotations."
                                    ]),
                                    html.Li([
                                        html.Strong("Results Table (ToxCSM): "),
                                        "Contains data related to `ToxCSM`, offering toxicity predictions and insights into compound interactions."
                                    ]),
                                ],
                                className="help-list"
                            ),
                        ]
                    ),
                ]
            ),

            # Additional Help Sections
            html.H2("Uploading Your Data", className="help-section-title"),
            html.P(
                "To start analyzing your data, go to the 'Data Analysis' section. Upload your dataset in a supported format "
                "(e.g., CSV or Excel). Ensure the data adheres to the expected structure, as outlined in the user guide.",
                className="help-text"
            ),

            html.H2("Visualizing Results", className="help-section-title"),
            html.P(
                "Results can be visualized in the 'Results' section. Interactive graphs and charts provide insights "
                "into your data, allowing you to explore pathways, gene activity, and more.",
                className="help-text"
            ),

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
        ]
    )
