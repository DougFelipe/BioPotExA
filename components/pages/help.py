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

from dash import html  # Dash HTML components for creating the UI
import dash_bootstrap_components as dbc  # Bootstrap components for styled alerts and buttons

# ----------------------------------------
# Function: get_help_layout
# ----------------------------------------
def get_help_layout():
    return html.Div(
        dbc.Container([

            # Título e introdução
            dbc.Row([
                dbc.Col([
                    html.H1(
                        "Help & Support",
                        className="text-success fw-bold text-center mb-4",
                        style={"fontFamily": "'Times New Roman', serif"}
                    ),
                    html.P(
                        "Below are common issues you may encounter while using the application, along with solutions to help you resolve them quickly.",
                        className="text-center text-dark fs-5",
                        style={"fontFamily": "Arial, sans-serif"}
                    )
                ])
            ]),

            # Seção de problemas comuns
            dbc.Row([
                dbc.Col([
                    html.H4(
                        "Common Issues",
                        className="text-success fw-bold mt-5 mb-4",
                        style={"fontFamily": "'Times New Roman', serif"}
                    ),
                    html.Ul([
                        html.Li([
                            html.Strong("1. Dataset Format Issues: "),
                            "Ensure that your uploaded dataset strictly follows the required format (.txt). Each sample should be listed with its corresponding KO identifiers in the expected structure. ",
                            "You can refer to the 'How to Use' section for an example dataset or download a sample file to verify the format."
                        ], className="mb-4"),

                        html.Li([
                            html.Strong("2. No Graph or Table Displayed: "),
                            "If no graphs or tables are displayed after submitting your data, double-check the following: ",
                            html.Ul([
                                html.Li("Ensure that all required inputs, such as filters or dropdown selections, are properly set."),
                                html.Li("Confirm that your data file is not empty and contains valid entries."),
                                html.Li("Reload the application and re-upload your dataset if the issue persists.")
                            ], className="mb-2")
                        ], className="mb-4"),

                        html.Li([
                            html.Strong("3. Invalid or Missing Data: "),
                            "Errors may occur if your dataset contains invalid or incomplete values. ",
                            "Check for missing KO identifiers, incorrect sample labels, or corrupted entries. ",
                            "Always validate your dataset before uploading to ensure a smooth processing experience."
                        ], className="mb-4"),

                        html.Li([
                            html.Strong("4. Multiple Samples Uploads: "),
                            "If you encounter issues uploading multiple samples, ensure the file does not exceed the allowed limit of 50 samples."
                        ], className="mb-4"),

                        html.Li([
                            html.Strong("5. Processing Delays: "),
                            "If the 'Submit' button does not trigger results or the processing takes too long: ",
                            html.Ul([
                                html.Li("Check your internet connection and ensure the file upload completed successfully."),
                                html.Li("Avoid refreshing the page during processing, as it may interrupt the operation."),
                                html.Li("Try uploading the example dataset to verify if the system is working correctly.")
                            ], className="mb-2")
                        ], className="mb-4"),

                        html.Li([
                            html.Strong("6. Unexpected Errors: "),
                            "If you encounter an unexpected error message or behavior in the application, note the following steps: ",
                            html.Ul([
                                html.Li("Reload the application and clear your browser cache."),
                                html.Li("Verify that the uploaded file adheres to the correct format and does not contain special characters."),
                                html.Li("Check the server logs for any additional error details (if you have administrative access).")
                            ], className="mb-2"),
                            " If the issue persists, contact our support team for assistance."
                        ], className="mb-4"),

                        html.Li([
                            html.Strong("7. File Name or Special Characters: "),
                            "If your file name contains spaces or special characters, the upload may fail or cause unexpected errors. ",
                            "Rename your file to remove special characters (e.g., use underscores instead of spaces) and try again."
                        ], className="mb-4"),

                        html.Li([
                            html.Strong("8. Browser Compatibility: "),
                            "Some browsers may not fully support certain features of the application. ",
                            "Ensure you are using a modern browser (Chrome, Firefox, Edge, or Safari) to avoid compatibility issues."
                        ], className="mb-4"),

                        html.Li([
                            html.Strong("9. Results Partially Loading: "),
                            "If only some charts or tables appear, it might indicate an issue with specific data fields or incomplete data. ",
                            "Check the data integrity and ensure all samples have valid KO entries. ",
                            "Try reprocessing the data or using the example dataset to confirm if the issue is dataset-specific."
                        ], className="mb-4"),

                        html.Li([
                            html.Strong("10. Proxy or Firewall Restrictions: "),
                            "If you are behind a corporate firewall or proxy, certain requests may be blocked. ",
                            "Contact your IT department to whitelist the application’s domain or try accessing from a different network."
                        ], className="mb-4"),

                        html.Li([
                            html.Strong("Need Further Assistance? "),
                            "For additional help, contact our support team at ",
                            html.A("biorempp@gmail.com", href="mailto:biorempp@gmail.com", className="text-primary fw-semibold")
                        ], className="mb-4")

                    ], style={"fontFamily": "Arial, sans-serif", "fontSize": "15px", "paddingLeft": "0"})
                ])
            ])

        ]),
        className="py-4"
    )
