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
    """
    Returns the layout for the "Help & Support" page, focusing on Common Issues.
    Additional potential issues have been included for a more comprehensive list.

    Returns:
    - dash.html.Div: The full layout of the "Help & Support" page with expanded Common Issues.
    """
    return html.Div(
        className="help-page",
        children=[
            # Common Issues Section
            html.H2("Common Issues", className="help-section-title"),
            html.P(
                "Below are common issues you may encounter while using the application, along with solutions to help you resolve them quickly",
                className="help-text"
            ),
            html.Ul(
                children=[
                    # 1. Dataset Format Issues
                    html.Li([
                        html.Strong("1. Dataset Format Issues: "),
                        "Ensure that your uploaded dataset strictly follows the required format (.txt). Each sample should be listed with its corresponding KO identifiers in the expected structure. ",
                        "You can refer to the 'How to Use' section for an example dataset or download a sample file to verify the format."
                    ]),
                    html.Br(),

                    # 2. No Graph or Table Displayed
                    html.Li([
                        html.Strong("2. No Graph or Table Displayed: "),
                        "If no graphs or tables are displayed after submitting your data, double-check the following: ",
                        html.Ul(
                            children=[
                                html.Li("Ensure that all required inputs, such as filters or dropdown selections, are properly set."),
                                html.Li("Confirm that your data file is not empty and contains valid entries."),
                                html.Li("Reload the application and re-upload your dataset if the issue persists.")
                            ],
                            className="sub-help-list"
                        )
                    ]),
                    html.Br(),

                    # 3. Invalid or Missing Data
                    html.Li([
                        html.Strong("3. Invalid or Missing Data: "),
                        "Errors may occur if your dataset contains invalid or incomplete values. ",
                        "Check for missing KO identifiers, incorrect sample labels, or corrupted entries. ",
                        "Always validate your dataset before uploading to ensure a smooth processing experience."
                    ]),
                    html.Br(),

                    # 4. Multiple Samples Uploads
                    html.Li([
                        html.Strong("4. Multiple Samples Uploads: "),
                        "If you encounter issues uploading multiple samples, ensure the file does not exceed the allowed limit of 50 samples."
                    ]),
                    html.Br(),

                    # 5. Processing Delays
                    html.Li([
                        html.Strong("5. Processing Delays: "),
                        "If the 'Submit' button does not trigger results or the processing takes too long: ",
                        html.Ul(
                            children=[
                                html.Li("Check your internet connection and ensure the file upload completed successfully."),
                                html.Li("Avoid refreshing the page during processing, as it may interrupt the operation."),
                                html.Li("Try uploading the example dataset to verify if the system is working correctly.")
                            ],
                            className="sub-help-list"
                        )
                    ]),
                    html.Br(),

                    # 6. Unexpected Errors
                    html.Li([
                        html.Strong("6. Unexpected Errors: "),
                        "If you encounter an unexpected error message or behavior in the application, note the following steps: ",
                        html.Ul(
                            children=[
                                html.Li("Reload the application and clear your browser cache."),
                                html.Li("Verify that the uploaded file adheres to the correct format and does not contain special characters."),
                                html.Li("Check the server logs for any additional error details (if you have administrative access).")
                            ],
                            className="sub-help-list"
                        ),
                        "If the issue persists, contact our support team for assistance."
                    ]),
                    html.Br(),

                    # 7. File Name or Special Characters
                    html.Li([
                        html.Strong("7. File Name or Special Characters: "),
                        "If your file name contains spaces or special characters, the upload may fail or cause unexpected errors. ",
                        "Rename your file to remove special characters (e.g., use underscores instead of spaces) and try again."
                    ]),
                    html.Br(),

                    # 8. Browser Compatibility
                    html.Li([
                        html.Strong("8. Browser Compatibility: "),
                        "Some browsers may not fully support certain features of the application. ",
                        "Ensure you are using a modern browser (Chrome, Firefox, Edge, or Safari) to avoid compatibility issues."
                    ]),
                    html.Br(),

                    # 9. Results Partially Loading
                    html.Li([
                        html.Strong("9. Results Partially Loading: "),
                        "If only some charts or tables appear, it might indicate an issue with specific data fields or incomplete data. ",
                        "Check the data integrity and ensure all samples have valid KO entries. ",
                        "Try reprocessing the data or using the example dataset to confirm if the issue is dataset-specific."
                    ]),
                    html.Br(),

                    # 11. Proxy or Firewall Restrictions
                    html.Li([
                        html.Strong("10. Proxy or Firewall Restrictions: "),
                        "If you are behind a corporate firewall or proxy, certain requests may be blocked. ",
                        "Contact your IT department to whitelist the application’s domain or try accessing from a different network."
                    ]),
                    html.Br(),

                    # 12. Need Further Assistance (moved to the last position)
                    html.Li([
                        html.Strong("Need Further Assistance? "),
                        "For additional help, contact our support team at ",
                        html.A("biorempp@gmail.com", href="mailto:biorempp@gmail.com", className="support-link"),
                    ]),
                    html.Br(),
                ],
                className="help-list"
            ),
        ]
    )
