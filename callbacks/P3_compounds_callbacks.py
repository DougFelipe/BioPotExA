"""
P3_compounds_callbacks.py
--------------------------
This script defines the callbacks for handling user interactions related to compound classes in a Dash web application. 

The script includes:
- Initializing a dropdown menu with compound class options based on user data.
- Updating a scatter plot to display data filtered by the selected compound class.

Functions:
1. `initialize_compound_class_dropdown`: Populates the dropdown menu with available compound classes.
2. `update_compound_scatter_plot`: Updates the scatter plot based on the selected compound class or displays a default message.
"""

# ----------------------------------------
# Imports
# ----------------------------------------

from dash import callback, html, dcc  # Dash components and callback utilities
from dash.dependencies import Input, Output, State  # Input, Output, and State for callbacks
from dash.exceptions import PreventUpdate  # Prevent unnecessary updates
import pandas as pd  # Data manipulation
from app import app  # Dash app instance
from utils.data_processing import merge_input_with_database  # Data processing utility
from utils.plot_processing import plot_compound_scatter  # Plot generation utility

# ----------------------------------------
# Callback: Initialize Dropdown
# ----------------------------------------

@app.callback(
    [Output('compound-class-dropdown', 'options'),  # Populate dropdown options
     Output('compound-class-dropdown', 'value')],  # Set initial dropdown value
    [Input('process-data', 'n_clicks')],  # Triggered when the "process data" button is clicked
    [State('stored-data', 'data')]  # Uses stored data as input
)
def initialize_compound_class_dropdown(n_clicks, stored_data):
    """
    Initializes the dropdown menu with compound class options.

    Parameters:
    - n_clicks (int): Number of times the process-data button has been clicked.
    - stored_data (list): The stored input data in JSON format.

    Returns:
    - list: Dropdown options formatted as [{'label': class, 'value': class}, ...].
    - None: No initial value selected for the dropdown.
    """
    # Prevent update if there is no data or the button has not been clicked
    if not stored_data or n_clicks < 1:
        raise PreventUpdate

    # Process the input data
    input_df = pd.DataFrame(stored_data)
    merged_df = merge_input_with_database(input_df)
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
    [State('stored-data', 'data')]  # Uses stored data as input
)
def update_compound_scatter_plot(selected_class, stored_data):
    """
    Updates the scatter plot based on the selected compound class or displays a default message.

    Parameters:
    - selected_class (str): The selected compound class from the dropdown menu.
    - stored_data (list): The stored input data in JSON format.

    Returns:
    - dash.dcc.Graph: A Graph component displaying the scatter plot.
    - dash.html.P: A default message if no data or class is selected.
    """
    # If no data or selection is made, display a default message
    if not stored_data or not selected_class:
        return html.P(
            "No graph available. Please select a compound class",  # Default message
            style={  # Styling for the default message
                "textAlign": "center",
                "color": "gray",
                "fontSize": "16px",
                "marginTop": "20px"
            }
        )

    # Process the input data and filter by the selected compound class
    input_df = pd.DataFrame(stored_data)
    merged_df = merge_input_with_database(input_df)
    filtered_df = merged_df[merged_df['compoundclass'] == selected_class]

    # Generate the scatter plot
    fig = plot_compound_scatter(filtered_df)

    # Return the scatter plot in a Dash Graph component
    return dcc.Graph(figure=fig, style={"height": "100%"})
