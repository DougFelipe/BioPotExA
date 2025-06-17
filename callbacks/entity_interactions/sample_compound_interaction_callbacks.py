"""
P3_compounds_callbacks.py
--------------------------
This script defines the callbacks for handling user interactions related to compound classes 
in a Dash web application.

The script includes:
- Initializing a dropdown menu with compound class options based on user data.
- Updating a scatter plot to display data filtered by the selected compound class.

Functions:
1. `initialize_compound_class_dropdown`: Populates the dropdown menu with available compound classes.
2. `update_compound_scatter_plot`: Updates the scatter plot based on the selected compound class 
   or displays a default message.
"""

# ----------------------------------------
# Imports
# ----------------------------------------

from dash import callback, html, dcc
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
import pandas as pd

from app import app

# Utilities for data handling and plotting
from utils.entity_interactions.sample_compound_interaction_plot import plot_compound_scatter


# ----------------------------------------
# Callback: Initialize Dropdown
# ----------------------------------------

@app.callback(  
    [Output('compound-class-dropdown', 'options'),  # Populate dropdown options  
     Output('compound-class-dropdown', 'value')],  # Set initial dropdown value  
    [Input('biorempp-merged-data', 'data')]  # MUDANÇA: usar store específico  
)  
def initialize_compound_class_dropdown(biorempp_data):  
    """  
    Initializes the dropdown menu with compound class options using pre-processed data.  
  
    Parameters:  
    - biorempp_data (list of dict): Pre-processed data from BioRemPP store.  
  
    Returns:  
    - list: Dropdown options formatted as [{'label': class, 'value': class}, ...].  
    - None: No initial value selected for the dropdown.  
    """  
    # Prevent update if no processed data is available  
    if not biorempp_data:  
        return [], None  
  
    # Convert stored processed data into a DataFrame (dados já processados)  
    merged_df = pd.DataFrame(biorempp_data)  
    compound_classes = sorted(merged_df['compoundclass'].unique())  # Extract unique compound classes  
  
    # Format dropdown options and clear default value  
    dropdown_options = [{'label': cls, 'value': cls} for cls in compound_classes]  
    return dropdown_options, None  # No initial selection

# ----------------------------------------
# Callback: Update Scatter Plot
# ----------------------------------------

@app.callback(  
    Output('compound-scatter-container', 'children'),  # Update scatter plot container  
    [Input('compound-class-dropdown', 'value')],  # Triggered by dropdown selection  
    [State('biorempp-merged-data', 'data')]  # MUDANÇA: usar store específico  
)  
def update_compound_scatter_plot(selected_class, biorempp_data):  
    """  
    Updates the scatter plot based on the selected compound class using pre-processed data.  
  
    Parameters:  
    - selected_class (str): The selected compound class from the dropdown menu.  
    - biorempp_data (list of dict): Pre-processed data from BioRemPP store.  
  
    Returns:  
    - dash.dcc.Graph: A Graph component displaying the scatter plot.  
    - dash.html.P: A default message if no data or class is selected.  
    """  
    # If no data or selection is made, display a default message  
    if not biorempp_data or not selected_class:  
        return html.P(  
            "No graph available. Please select a compound class",  # Default message  
            style={  # Styling for the default message  
                "textAlign": "center",  
                "color": "gray",  
                "fontSize": "16px",  
                "marginTop": "20px"  
            }  
        )  
  
    # Convert stored processed data into a DataFrame (dados já processados)  
    merged_df = pd.DataFrame(biorempp_data)  
    filtered_df = merged_df[merged_df['compoundclass'] == selected_class]  
  
    # Generate the scatter plot  
    fig = plot_compound_scatter(filtered_df)  
  
    # Return the scatter plot in a Dash Graph component  
    return dcc.Graph(figure=fig, style={"height": "100%"})
