"""
P1_KO_COUNT.py
---------------
This script defines the layouts for KO (KEGG Orthology) count visualizations in a Dash web application. 
It includes components for a bar chart and a violin/boxplot chart, along with filtering options.

The layouts are dynamically built using Dash HTML and Core Components, and include filters such as 
range sliders and dropdown menus for user interaction.

Functions:
- `get_ko_count_bar_chart_layout`: Builds the layout for the KO count bar chart.
- `get_ko_violin_boxplot_layout`: Builds the layout for the KO count violin and boxplot chart.
"""

# ----------------------------------------
# Imports
# ----------------------------------------

from dash import html, dcc  # Dash HTML and Core Components for layout
from utils.components import create_card  # Utility for creating reusable card components
from utils.filters import create_range_slider  # Utility for creating range slider filters

# ----------------------------------------
# Function: get_ko_count_bar_chart_layout
# ----------------------------------------

def get_ko_count_bar_chart_layout():
    """
    Constructs the layout for the KO count bar chart, including a range slider filter.

    The layout contains:
    - A range slider for filtering KO counts.
    - A bar chart visualization.

    Returns:
        html.Div: A Dash HTML Div containing the bar chart and the filter.
    """
    ko_slider = create_range_slider(slider_id='ko-count-range-slider')  # Create the range slider filter

    return html.Div(
        [
            # Filtering options for the bar chart
            html.Div(
                [
                    html.Div('Filter by Range', className='menu-text'),  # Filter label
                    ko_slider  # Range slider component
                ],
                className='navigation-menu'  # CSS class for styling the filter menu
            ),
            dcc.Graph(id='ko-count-bar-chart')  # Graph for the KO count bar chart
        ],
        className='graph-card'  # CSS class for styling the entire card
    )

# ----------------------------------------
# Function: get_ko_violin_boxplot_layout
# ----------------------------------------

def get_ko_violin_boxplot_layout():
    """
    Constructs the layout for the KO count violin and boxplot chart, including a dropdown filter.

    The layout contains:
    - A dropdown menu for selecting samples.
    - A combined violin and boxplot visualization.

    Returns:
        html.Div: A Dash HTML Div containing the violin/boxplot chart and the filter.
    """
    ko_violin_filter = dcc.Dropdown(
        id='sample-dropdown',  # ID for callback interaction
        multi=True,  # Allows multiple sample selections
        placeholder='Sample'  # Placeholder text for the dropdown
    )

    return html.Div(
        [
            # Filtering options for the violin/boxplot chart
            html.Div(
                [
                    'Filter by Sample',  # Filter label
                    ko_violin_filter  # Dropdown filter component
                ],
                className='navigation-menu'  # CSS class for styling the filter menu
            ),
            dcc.Graph(id='ko-violin-boxplot-chart')  # Graph for the violin and boxplot visualization
        ],
        className='graph-card'  # CSS class for styling the entire card
    )
