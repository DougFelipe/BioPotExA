"""
P3_compounds_layout.py
-----------------------
This script defines the layout for the compound scatter plot in a Dash web application.
It includes a dropdown for filtering by compound class and a container to display the scatter plot 
or a placeholder message when no data is available.

Functions:
- `get_compound_scatter_layout`: Constructs and returns the layout for the compound scatter plot.
"""

# ----------------------------------------
# Imports
# ----------------------------------------

from dash import html, dcc  # Dash HTML and Core Components
import dash_bootstrap_components as dbc

# ----------------------------------------
# Function: get_compound_scatter_layout
# ----------------------------------------

def get_compound_scatter_layout():
    """
    Constructs a Bootstrap-styled layout for the compound scatter plot
    with dropdown filter for compound class and a dynamic graph container.

    Returns:
        dbc.Card: A stylized Dash Bootstrap card component.
    """

    return dbc.Card([
        dbc.CardHeader("Filter by Compound Class", class_name="fw-bold text-muted"),

        dbc.CardBody([
            dbc.Row([
                dbc.Col(
                    dcc.Dropdown(
                        id='compound-class-dropdown',
                        multi=False,
                        placeholder='Select a Compound Class',
                        className="mb-3"
                    ),
                    width=12
                )
            ]),
            dbc.Row([
                dbc.Col(
                    html.Div(
                        id='compound-scatter-container',
                        children=[
                            html.P(
                                "No graph available. Please select a compound class.",
                                style={
                                    "textAlign": "center",
                                    "color": "gray",
                                    "fontSize": "16px",
                                    "marginTop": "20px"
                                }
                            )
                        ],
                        className='graph-container',
                        style={"height": "auto", "overflowY": "auto"}
                    ),
                    width=12
                )
            ])
        ])
    ],
    class_name="shadow-sm border-0 my-3")
    """
    Constructs the layout for the compound scatter plot, including a filter for compound class.

    The layout includes:
    - A dropdown menu for selecting a compound class.
    - A container to dynamically display the scatter plot or a placeholder message.

    Returns:
        dash.html.Div: A Dash HTML Div containing the dropdown and the scatter plot container.
    """
    return html.Div(
        [
            # Dropdown Filter Section
            html.Div(
                [
                    # Label for the dropdown
                    html.Div('Filter by Compound Class', className='menu-text'),
                    
                    # Dropdown component for selecting a compound class
                    dcc.Dropdown(
                        id='compound-class-dropdown',
                        multi=False,  # Allows single selection
                        placeholder='Select a Compound Class',  # Placeholder text in the dropdown
                        style={"marginBottom": "20px"}  # Adds spacing below the dropdown
                    )
                ],
                className='navigation-menu'  # CSS class for styling the dropdown section
            ),
            
            # Scatter Plot Container
            html.Div(
                id='compound-scatter-container',  # ID for dynamic updates of the container
                children=[
                    # Placeholder message displayed when no compound class is selected
                    html.P(
                        "No graph available. Please select a compound class",  # Informational message
                        style={
                            "textAlign": "center",  # Centers the text
                            "color": "gray",  # Sets the text color
                            "fontSize": "16px",  # Sets the font size
                            "marginTop": "20px"  # Adds spacing above the text
                        }
                    )
                ],
                className='graph-container',  # CSS class for styling the container
                style={"height": "auto", "overflowY": "auto"}  # Enables dynamic height and vertical scrolling
            )
        ],
        className='graph-card'  # CSS class for the main layout container
    )
