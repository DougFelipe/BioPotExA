"""
P6_rank_compounds_callbacks.py
------------------------------
This script defines the callbacks for handling the ranking of compounds by gene interaction in a Dash web application.

Key functionalities:
- Populate the dropdown with compound classes based on the processed data.
- Generate a bar plot visualizing the ranking of compounds by the number of unique genes interacting with them.

The callbacks handle user interactions, such as processing data after a button click and dynamically updating the plot based on the selected compound class.
"""

# ----------------------------------------
# Imports
# ----------------------------------------

from dash import callback, html, dcc  # Dash components for callbacks and layout
from dash.dependencies import Input, Output, State  # Input, Output, and State for callback interactivity
from dash.exceptions import PreventUpdate  # Exception to prevent unnecessary updates
import pandas as pd  # Data manipulation with pandas

from app import app  # Application instance
from utils.data_processing import merge_input_with_database  # Function to merge input data with the database
from utils.rankings.ranking_compounds_by_gene_interaction_processing import process_compound_gene_ranking  # Function to process compound gene ranking
from utils.rankings.ranking_compounds_by_gene_interaction_plot import plot_compound_gene_ranking  # Function to plot compound gene ranking

# ----------------------------------------
# Callback: Initialize Dropdown for Compound Classes
# ----------------------------------------

@app.callback(
    [Output('p6-compound-class-dropdown', 'options'),
     Output('p6-compound-class-dropdown', 'value')],
    [Input('process-data', 'n_clicks')],
    [State('stored-data', 'data')]
)
def initialize_compound_class_dropdown(n_clicks, stored_data):
    """
    Initializes the dropdown menu for selecting compound classes.

    Triggered when the "Process Data" button is clicked.

    Parameters:
    - n_clicks (int): Number of times the button has been clicked.
    - stored_data (list): Data stored in the browser's memory.

    Returns:
    - list: Options for the dropdown menu, populated with unique compound classes.
    - None: Initial value of the dropdown (unselected).
    """
    # If the data is not ready or the button has not been clicked
    if not stored_data or n_clicks < 1:
        return [], None

    input_df = pd.DataFrame(stored_data)  # Convert stored data to a pandas DataFrame
    merged_df = merge_input_with_database(input_df)  # Merge the input data with the database
    compound_classes = sorted(merged_df['compoundclass'].unique())  # Extract unique compound classes

    # Prepare options for the dropdown menu
    dropdown_options = [{'label': cls, 'value': cls} for cls in compound_classes]
    return dropdown_options, None  # No initial value selected

# ----------------------------------------
# Callback: Update Ranking Plot
# ----------------------------------------

@app.callback(
    Output('p6-compound-ranking-container', 'children'),
    [Input('p6-compound-class-dropdown', 'value')],
    [State('stored-data', 'data')]
)
def update_compound_gene_ranking_plot(selected_class, stored_data):
    """
    Updates the bar plot displaying the ranking of compounds by gene interaction.

    Triggered when a compound class is selected in the dropdown menu.

    Parameters:
    - selected_class (str): The selected compound class.
    - stored_data (list): Data stored in the browser's memory.

    Returns:
    - dash.html.P: Placeholder message if no data or selection is available.
    - dash.dcc.Graph: A bar plot visualizing the ranking of compounds by gene interaction.
    """
    # Ensure the placeholder message appears when no selection or data is available
    if not stored_data or not selected_class:
        return html.P(
            "No data available. Please select a compound class",  # Placeholder message
            id="p6-placeholder-message",
            style={"textAlign": "center", "color": "gray", "marginTop": "20px"}
        )

    # Prepare the input data
    input_df = pd.DataFrame(stored_data)
    merged_df = merge_input_with_database(input_df)

    # Filter the data by the selected compound class
    filtered_df = merged_df[merged_df['compoundclass'] == selected_class]

    # Display a message if no data is available for the selected class
    if filtered_df.empty:
        return html.P(
            "No data available for the selected compound class",  # No data message
            id="p6-no-data-message",
            style={"textAlign": "center", "color": "gray", "marginTop": "20px"}
        )

    # Process the data for the ranking plot
    compound_gene_ranking_df = process_compound_gene_ranking(filtered_df)

    # Generate the bar plot
    fig = plot_compound_gene_ranking(compound_gene_ranking_df)

    # Return the plot as a Dash Graph component
    return dcc.Graph(figure=fig, id="p6-rank-compounds-gene-bar-plot")
