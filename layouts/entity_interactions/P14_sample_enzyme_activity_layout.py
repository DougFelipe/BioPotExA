"""
P14_sample_enzyme_activity_layout.py
------------------------------------
This script defines the layout for the sample enzyme activity bar chart in a Dash web application.
The layout includes a dropdown menu for sample selection and a container for the bar chart display.

The layout is designed to allow users to filter and view enzyme activity data based on the selected sample.
"""

# ----------------------------------------
# Imports
# ----------------------------------------

from dash import html, dcc  # Dash HTML and core components for building UI
import dash_bootstrap_components as dbc
# ----------------------------------------
# Function: get_sample_enzyme_activity_layout
# ----------------------------------------
def get_sample_enzyme_activity_layout():
    """
    Returns a Bootstrap-styled layout for the enzyme activity bar chart per sample,
    including a dropdown filter and a placeholder for empty data.
    """

    return dbc.Card([
        dbc.CardHeader("Filter by Sample", class_name="fw-semibold text-muted"),

        dbc.CardBody([
            dbc.Row([
                dbc.Col(
                    dcc.Dropdown(
                        id='sample-enzyme-dropdown',
                        placeholder="Select a Sample",
                        className="mb-3"
                    ),
                    width=12
                )
            ]),
            dbc.Row([
                dbc.Col(
                    html.Div(
                        id='enzyme-bar-chart-container',
                        children=[
                            html.P(
                                "No data available. Please select a sample",
                                id="no-enzyme-bar-chart-message",
                                className="text-center text-muted"
                            )
                        ]
                    ),
                    width=12
                )
            ])
        ])
    ],
    class_name="shadow-sm border-0 my-3")
