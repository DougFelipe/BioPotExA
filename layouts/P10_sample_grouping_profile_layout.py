"""
P10_sample_grouping_profile_layout.py
-------------------------------------
This script defines the layout for the scatter plot visualizing sample groups by compound class. 
It includes a dropdown for filtering by compound class and a container for displaying the plot or a 
message when no data is available.

Functions:
- `get_sample_groups_layout`: Creates the layout for the sample grouping visualization, including 
  a filter dropdown and a responsive container for the scatter plot.
"""

# ----------------------------------------
# Imports
# ----------------------------------------

from dash import html, dcc  # Dash components for building UI
import dash_bootstrap_components as dbc
# ----------------------------------------
# Function: get_sample_groups_layout
# ----------------------------------------
def get_sample_groups_layout():
    """
    Builds a Bootstrap-styled layout for the scatter plot of sample groups by compound class.

    Returns:
    - dbc.Card: A styled layout containing the dropdown filter and the scatter plot or a placeholder.
    """
    dropdown_filter = dcc.Dropdown(
        id='compound-class-dropdown-p10',
        multi=False,
        placeholder='Select a Compound Class',
        className='mb-3'
    )

    placeholder_message = html.P(
        "No data available. Please select a compound class.",
        id="no-sample-groups-message",
        className="text-center text-muted"
    )

    return dbc.Card([
        dbc.CardHeader("Filter by Compound Class", class_name="fw-semibold text-muted"),

        dbc.CardBody([
            dbc.Row([
                dbc.Col(dropdown_filter, width=12)
            ]),

            dbc.Row([
                dbc.Col(
                    html.Div(
                        id='sample-groups-container',
                        children=[placeholder_message],
                        style={'height': 'auto', 'overflowY': 'auto'}
                    ),
                    width=12
                )
            ])
        ])
    ],
    class_name="shadow-sm border-0 my-3")
