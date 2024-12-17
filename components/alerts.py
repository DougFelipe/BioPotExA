"""
alerts.py
---------
This script defines reusable alert components for a Dash web application using Dash Bootstrap Components (DBC).
The alerts provide information about the integration of external tools/databases such as HADEG and ToxCSM.

Each alert contains:
- A descriptive message.
- A hyperlink referencing the original source for more details.
- A distinct visual style using Bootstrap's "danger" color scheme.

Functions:
- `hadeg_alert`: Generates an alert for HADEG database integration.
- `toxcsm_alert`: Generates an alert for ToxCSM tool integration.
"""

# ----------------------------------------
# Imports
# ----------------------------------------

from dash import html  # Dash HTML components for hyperlink integration
import dash_bootstrap_components as dbc  # DBC components for alerts

# ----------------------------------------
# Function: hadeg_alert
# ----------------------------------------

def hadeg_alert():
    """
    Generates an alert for the HADEG database integration.

    The alert displays a message indicating that the displayed results are derived from the HADEG database.
    It also includes a hyperlink to the HADEG GitHub repository for further information.

    Returns:
    - dbc.Alert: A Bootstrap-styled alert component with a message and reference link.
    """
    return dbc.Alert(
        [
            # Alert message describing the HADEG database
            "The results displayed are derived from the integration with the HADEG database. ",
            "For more information about genes and pathways, please refer to the original source: ",
            
            # Hyperlink to the HADEG GitHub repository
            html.A(
                "HADEG GitHub Repository",  # Link text
                href="https://github.com/jarojasva/HADEG",  # External link URL
                target="_blank",  # Opens the link in a new browser tab
                style={
                    "color": "#007bff",  # Bootstrap primary link color
                    "font-weight": "bold",  # Bold font for emphasis
                    "text-decoration": "underline"  # Underline for link visibility
                }
            ),
        ],
        color="danger",  # Bootstrap "danger" color for visual distinction (red)
        className="mt-3"  # Adds a top margin for spacing (Bootstrap utility class)
    )

# ----------------------------------------
# Function: toxcsm_alert
# ----------------------------------------

def toxcsm_alert():
    """
    Generates an alert for the ToxCSM tool integration.

    The alert displays a message indicating that the displayed results are derived from the ToxCSM tool.
    It also includes a hyperlink to the ToxCSM website for further information.

    Returns:
    - dbc.Alert: A Bootstrap-styled alert component with a message and reference link.
    """
    return dbc.Alert(
        [
            # Alert message describing the ToxCSM tool
            "The results displayed are derived from the integration with the ToxCSM tool. ",
            "For more information about toxicity predictions and categories, please refer to the official source: ",
            
            # Hyperlink to the ToxCSM website
            html.A(
                "ToxCSM Website",  # Link text
                href="https://biosig.lab.uq.edu.au/toxcsm/",  # External link URL
                target="_blank",  # Opens the link in a new browser tab
                style={
                    "color": "#007bff",  # Bootstrap primary link color
                    "font-weight": "bold",  # Bold font for emphasis
                    "text-decoration": "underline"  # Underline for link visibility
                }
            ),
        ],
        color="danger",  # Bootstrap "danger" color for visual distinction (red)
        className="mt-3"  # Adds a top margin for spacing (Bootstrap utility class)
    )
