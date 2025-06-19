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
import dash_bootstrap_components as dbc  # Bootstrap components for styling
from components.ui.filters import create_range_slider  # Utility for creating range slider filters

# ----------------------------------------
# Function: get_ko_count_bar_chart_layout
# ----------------------------------------

def get_ko_count_bar_chart_layout():
    """
    Constructs a Bootstrap-based layout for the KO count bar chart with a filter slider.

    Returns:
        html.Div: A layout containing the KO range filter and the bar chart.
    """

    # Slider para filtrar os dados
    ko_slider = create_range_slider(slider_id='ko-count-range-slider')

    return dbc.Card([
        dbc.CardHeader("Filter by KO Count", class_name="fw-semibold text-muted"),
        
        dbc.CardBody([
            dbc.Row([
                dbc.Col(ko_slider, width=12)
            ], class_name="mb-4"),

            dbc.Row([
                dbc.Col(
                    dcc.Graph(id='ko-count-bar-chart'),
                    width=12
                )
            ])
        ])
    ],
    class_name="shadow-sm border-0 my-3")

# ----------------------------------------
# Function: get_ko_violin_boxplot_layout
# ----------------------------------------

def get_ko_violin_boxplot_layout():
    """
    Constructs a Bootstrap-based layout for the KO violin + boxplot chart 
    without sample filtering controls.

    Returns
    -------
    dbc.Card
        A styled layout containing only the KO violin + boxplot chart.
    """
    return dbc.Card(
        [
            dbc.CardHeader("KO Violin and Boxplot", class_name="fw-bold"),
            dbc.CardBody(
                [
                    dbc.Row(
                        [
                            dbc.Col(
                                dcc.Graph(id='ko-violin-boxplot-chart'),
                                width=12
                            )
                        ]
                    )
                ]
            )
        ],
        class_name="shadow-sm border-0 my-3"
    )
