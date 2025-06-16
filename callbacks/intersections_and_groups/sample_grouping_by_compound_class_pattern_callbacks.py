"""
P10_sample_grouping_profile_callbacks.py
----------------------------------------
This script defines callbacks for the "Sample Grouping by Compound Class Pattern" feature in a Dash web application. 

Key functionalities:
- Populates a dropdown with unique compound classes derived from the processed data.
- Updates and displays grouped sample data based on the selected compound class.
- Handles data grouping and visualization dynamically using utility functions.

Callbacks:
1. `initialize_compound_class_dropdown`: Initializes the compound class dropdown with options.
2. `update_sample_groups_plot`: Updates the sample grouping plot based on the selected compound class.
"""

# ----------------------------------------
# Imports
# ----------------------------------------

# Dash components and dependencies for interactivity
from dash import callback, html, dcc
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate

# Data manipulation
import pandas as pd

# Application instance
from app import app

# Utility functions for data processing and visualization
from utils.core.data_processing import merge_input_with_database
from utils.intersections_and_groups.sample_grouping_by_compound_class_plot import plot_sample_groups
from utils.intersections_and_groups.sample_grouping_by_compound_class_processing import group_by_class, minimize_groups

# ----------------------------------------
# Callback 1: Initialize Dropdown Options
# ----------------------------------------

@app.callback(  
    [Output('compound-class-dropdown-p10', 'options'),  # Dropdown options  
     Output('compound-class-dropdown-p10', 'value')],   # Selected value (initially None)  
    [Input('biorempp-merged-data', 'data')]             # MUDANÇA: usar store específico  
)  
def initialize_compound_class_dropdown(biorempp_data):  
    """  
    Initializes the compound class dropdown with unique values from pre-processed data.  
  
    Parameters:  
    - biorempp_data (list[dict]): Pre-processed data from BioRemPP store.  
  
    Returns:  
    - list[dict]: Options for the dropdown menu, each with 'label' and 'value'.  
    - None: Initial dropdown value (no pre-selection).  
    """  
    if not biorempp_data:  
        return [], None  
  
    # Convert stored processed data into a DataFrame (dados já processados)  
    merged_df = pd.DataFrame(biorempp_data)  
    compound_classes = sorted(merged_df['compoundclass'].unique())  # Get unique compound classes  
  
    # Prepare dropdown options  
    dropdown_options = [{'label': cls, 'value': cls} for cls in compound_classes]  
  
    return dropdown_options, None  # No initial selection

# ----------------------------------------
# Callback 2: Update Sample Group Plot
# ----------------------------------------

@app.callback(  
    Output('sample-groups-container', 'children'),  # Updates the sample group plot container  
    [Input('compound-class-dropdown-p10', 'value')],  # Selected compound class  
    [State('biorempp-merged-data', 'data')]           # MUDANÇA: usar store específico  
)  
def update_sample_groups_plot(compound_class, biorempp_data):  
    """  
    Updates the sample grouping plot based on the selected compound class using pre-processed data.  
  
    Parameters:  
    - compound_class (str): Selected compound class from the dropdown.  
    - biorempp_data (list[dict]): Pre-processed data from BioRemPP store.  
  
    Returns:  
    - dash.html.P: A message if no data is available.  
    - dash.dcc.Graph: A plot displaying sample groupings if data is available.  
    """  
    if not compound_class or not biorempp_data:  
        return html.P(  
            "No data available. Please select a compound class",  # Message for no data  
            id="no-sample-groups-message",  
            style={"textAlign": "center", "color": "gray"}  
        )  
  
    # Convert stored processed data into a DataFrame (dados já processados)  
    merged_df = pd.DataFrame(biorempp_data)  
  
    # Group data by the selected compound class  
    grouped_df = group_by_class(compound_class, merged_df)  
  
    # Minimize groups to handle excessive data  
    minimized_groups = minimize_groups(grouped_df)  
  
    # Filter grouped data to only include minimized groups  
    minimized_df = grouped_df[grouped_df['grupo'].isin(minimized_groups)]  
  
    # Handle empty results after processing  
    if minimized_df.empty:  
        return html.P(  
            "No data available for the selected compound class",  # Message for no data after processing  
            id="no-sample-groups-message",  
            style={"textAlign": "center", "color": "gray"}  
        )  
  
    # Generate the plot using the processed data  
    fig = plot_sample_groups(minimized_df)  
    return dcc.Graph(figure=fig, style={"height": "auto", "overflowY": "auto"})  # Return the plot as a Dash Graph
