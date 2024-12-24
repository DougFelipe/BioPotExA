"""
P2_KO_20PATHWAY.py
-------------------
This script defines layouts for two bar chart components in a Dash web application:
1. A bar chart for analyzing KOs (KEGG Orthologs) in pathways based on selected samples.
2. A bar chart for analyzing KOs in samples for a selected pathway.

Each layout includes:
- A filter dropdown for user selection.
- A placeholder message if no data is available for the selected filter.
"""

# ----------------------------------------
# Imports
# ----------------------------------------

from dash import html, dcc  # Dash components for building UI layouts

# ----------------------------------------
# Function: get_pathway_ko_bar_chart_layout
# ----------------------------------------

def get_pathway_ko_bar_chart_layout():
    """
    Constructs the layout for the KO pathway analysis bar chart, including a sample filter.

    The layout contains:
    - A dropdown menu for filtering the chart by sample.
    - A container to display the bar chart or a placeholder message if no sample is selected.

    Returns:
    - dash.html.Div: A Dash HTML Div component containing the dropdown and chart container.
    """
    return html.Div([
        # Filter Section: Dropdown to select a sample
        html.Div([
            html.Div('Filter by Sample', className='menu-text'),  # Label for the dropdown
            dcc.Dropdown(
                id='pathway-sample-dropdown',  # Dropdown ID for interactivity
                placeholder="Select a sample",  # Placeholder text for the dropdown
                style={"margin-bottom": "20px"}  # Adds spacing below the dropdown
            ),
        ], className='navigation-menu'),  # CSS class for styling the navigation menu

        # Chart Container: Displays the bar chart or a message
        html.Div(
            id='pathway-ko-chart-container',  # ID for the chart container
            children=[
                # Placeholder message when no chart is available
                html.P(
                    "No chart available. Please select a sample",  # Message displayed when no sample is selected
                    id="no-pathway-ko-chart-message",  # ID for the message
                    style={"textAlign": "center", "color": "gray"}  # Center-align the text and use gray color
                )
            ],
            className='graph-card'  # CSS class for styling the chart container
        )
    ])

# ----------------------------------------
# Function: get_sample_ko_pathway_bar_chart_layout
# ----------------------------------------

def get_sample_ko_pathway_bar_chart_layout():
    """
    Constructs the layout for the bar chart analyzing KOs in samples for a selected pathway.

    The layout contains:
    - A dropdown menu for filtering the chart by pathway.
    - A container to display the bar chart or a placeholder message if no pathway is selected.

    Returns:
    - dash.html.Div: A Dash HTML Div component containing the dropdown and chart container.
    """
    return html.Div([
        # Filter Section: Dropdown to select a pathway
        html.Div([
            html.Div('Filter by Pathway', className='menu-text'),  # Label for the dropdown
            dcc.Dropdown(
                id='via-dropdown',  # Dropdown ID for interactivity
                placeholder="Select a pathway",  # Placeholder text for the dropdown
                style={"margin-bottom": "20px"}  # Adds spacing below the dropdown
            ),
        ], className='navigation-menu'),  # CSS class for styling the navigation menu

        # Chart Container: Displays the bar chart or a message
        html.Div(
            id='via-ko-chart-container',  # ID for the chart container
            children=[
                # Placeholder message when no chart is available
                html.P(
                    "No chart available. Please select a pathway",  # Message displayed when no pathway is selected
                    id="no-via-ko-chart-message",  # ID for the message
                    style={"textAlign": "center", "color": "gray"}  # Center-align the text and use gray color
                )
            ],
            className='graph-card'  # CSS class for styling the chart container
        )
    ])
