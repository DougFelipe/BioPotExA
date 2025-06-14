"""
P13_gene_sample_scatter_callbacks.py
-------------------------------------
This script defines the callback functions for generating and updating a scatter plot of KO (orthologs) 
counts per sample for a selected metabolic pathway. 

It includes:
- Initializing the pathway dropdown options based on the processed data.
- Updating the scatter plot when a pathway is selected.

The callbacks use Dash's callback mechanism to handle user interactions and update components dynamically.
"""

# ----------------------------------------
# Imports
# ----------------------------------------

from dash import callback, Output, Input, State, html, dcc  # Dash components and callback utilities
from dash.exceptions import PreventUpdate  # Exception to stop callback execution when no updates are required
import pandas as pd  # Pandas for data manipulation

# Application instance and utilities
from app import app  # Dash application instance
from utils.data_processing import merge_with_kegg, get_ko_per_sample_for_pathway  # Data processing utilities
from utils.plot_processing import plot_sample_ko_scatter  # Plotting utility for scatter plot generation

# ----------------------------------------
# Callback: Initialize Pathway Dropdown
# ----------------------------------------

@app.callback(
    [Output('pathway-dropdown-p13', 'options'),  # Dropdown options
     Output('pathway-dropdown-p13', 'value')],  # Selected value
    [Input('process-data', 'n_clicks')],  # Trigger: Button clicks
    [State('stored-data', 'data')]  # Data stored in the app state
)
def initialize_pathway_dropdown(n_clicks, stored_data):
    """
    Initializes the dropdown for pathway selection.

    - Populates the dropdown options with unique pathways derived from the stored data.
    - Resets the selected value.

    Parameters:
    - n_clicks (int): Number of times the "Process Data" button has been clicked.
    - stored_data (dict): Data stored in the app state, representing user-uploaded data.

    Returns:
    - list[dict]: A list of dropdown options (label-value pairs).
    - None: Resets the selected value in the dropdown.
    """
    # If no clicks have occurred or no data is available, prevent callback execution
    if n_clicks < 1 or not stored_data:
        raise PreventUpdate

    # Convert stored data to a DataFrame
    input_df = pd.DataFrame(stored_data)
    merged_df = merge_with_kegg(input_df)

    # Extract and sort unique pathway names
    pathways = sorted(merged_df['pathname'].unique())

    # Avoid errors if no pathways are available
    dropdown_options = [{'label': pathway, 'value': pathway} for pathway in pathways]
    return dropdown_options, None  # No default value

# ----------------------------------------
# Callback: Update Scatter Plot
# ----------------------------------------

@app.callback(
    Output('scatter-plot-container', 'children'),  # Container for the scatter plot
    [Input('pathway-dropdown-p13', 'value')],  # Selected pathway from the dropdown
    [State('stored-data', 'data')]  # Data stored in the app state
)
def update_scatter_plot(selected_pathway, stored_data):
    """
    Updates the scatter plot based on the selected pathway.

    - Retrieves KO data per sample for the selected pathway.
    - Generates a scatter plot or displays a message if no data is available.

    Parameters:
    - selected_pathway (str): The pathway selected from the dropdown.
    - stored_data (dict): Data stored in the app state, representing user-uploaded data.

    Returns:
    - dcc.Graph: A Dash Graph component containing the scatter plot.
    - html.P: A message if no data is available or the selected pathway has no associated data.
    """
    # Check if a pathway is selected and data is available
    if not selected_pathway or not stored_data:
        return html.P(
            "No data available. Please select a pathway",  # Message when no data is available
            id="no-data-message-p13",  # Unique ID for the message
            style={"textAlign": "center", "color": "gray"}  # Styling for the message
        )

    # Convert stored data to a DataFrame
    input_df = pd.DataFrame(stored_data)
    merged_df = merge_with_kegg(input_df)

    # Retrieve scatter plot data for the selected pathway
    scatter_data = get_ko_per_sample_for_pathway(merged_df, selected_pathway)

    # If no data is found for the selected pathway, display a message
    if scatter_data.empty:
        return html.P(
            "No data found for the selected pathway",  # Message when no data matches the selected pathway
            id="no-data-message-p13",
            style={"textAlign": "center", "color": "gray"}
        )

    # Generate and return the scatter plot
    fig = plot_sample_ko_scatter(scatter_data, selected_pathway)
    return dcc.Graph(figure=fig, style={'height': '600px'})  # Set the height of the plot
