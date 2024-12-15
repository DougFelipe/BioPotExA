from dash import html
import dash_bootstrap_components as dbc

def hadeg_alert():
    """
    Generates an alert for HADEG database integration with a reference link.
    """
    return dbc.Alert(
        [
            "The results displayed are derived from the integration with the HADEG database. ",
            "For more information about genes and pathways, please refer to the original source: ",
            html.A(
                "HADEG GitHub Repository",
                href="https://github.com/jarojasva/HADEG",
                target="_blank",
                style={"color": "#007bff", "font-weight": "bold", "text-decoration": "underline"}  # Custom link style
            ),
        ],
        color="danger",
        className="mt-3"
    )

def toxcsm_alert():
    """
    Generates an alert for ToxCSM tool integration with a reference link.
    """
    return dbc.Alert(
        [
            "The results displayed are derived from the integration with the ToxCSM tool. ",
            "For more information about toxicity predictions and categories, please refer to the official source: ", 
            html.A(
                "ToxCSM Website",
                href="https://biosig.lab.uq.edu.au/toxcsm/",
                target="_blank",
                style={"color": "#007bff", "font-weight": "bold", "text-decoration": "underline"}  # Custom link style
            ),
        ],
        color="danger",
        className="mt-3"
    )
