"""
P16_sample_upset_layout.py
--------------------------
This script defines the layout for the UpSet Plot feature in a Dash web application.
The UpSet Plot visualizes the intersections of selected samples and their associated KO identifiers.

The layout includes:
- A dropdown for multi-selection of samples.
- A container for displaying the UpSet Plot or a placeholder message if no samples are selected.

Functions:
- `get_sample_upset_layout`: Constructs and returns the layout for the UpSet Plot.
"""

# ----------------------------------------
# Imports
# ----------------------------------------

from dash import html, dcc  # Dash components for HTML structure and interactivity
import dash_bootstrap_components as dbc
# ----------------------------------------
# Function: get_sample_upset_layout
# ----------------------------------------

def get_sample_upset_layout():
    """
    Constructs a Bootstrap-styled layout for the UpSet Plot with dropdown filter.

    Returns:
        dbc.Card: A styled layout containing the sample selector and UpSet plot container.
    """

    return dbc.Card([
        dbc.CardHeader("Select Samples", class_name="fw-semibold text-muted"),
        
        dbc.CardBody([
            dbc.Row([
                dbc.Col(
                    dcc.Dropdown(
                        id='upsetplot-sample-dropdown',
                        multi=True,
                        placeholder="Select the samples",
                        className="mb-3"
                    ),
                    width=12
                )
            ]),

            dbc.Row([
                dbc.Col(
                    html.Div(
                        id='upset-plot-container',
                        children=[
                            html.P(
                                "No plot available. Please select samples.",
                                id="no-upset-plot-message",
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
