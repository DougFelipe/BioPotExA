"""
P15_sample_clustering_callbacks.py
-----------------------------------
This script defines a Dash callback for updating a dendrogram visualization based on sample clustering. 
The dendrogram is dynamically updated when the user selects a distance metric and clustering method 
from dropdown menus. 

Key functionalities:
- Takes stored data and user-selected parameters as input.
- Calculates a clustering matrix.
- Generates and returns a dendrogram image.
"""

# ----------------------------------------
# Imports
# ----------------------------------------

from dash import callback, html  # Dash core and HTML components
from dash.dependencies import Input, Output, State  # Dash callback dependencies
from dash.exceptions import PreventUpdate  # Exception to halt updates if inputs are invalid
import pandas as pd  # Data manipulation library
from app import app  # Main Dash app instance
from utils.intersections_and_groups.clustering_dendrogram_processing import calculate_sample_clustering  # Utility for clustering calculation
from utils.intersections_and_groups.clustering_dendrogram_plot import plot_dendrogram  # Utility for generating dendrogram plots

# ----------------------------------------
# Callback: Update Sample Clustering Graph
# ----------------------------------------

@app.callback(
    Output('sample-clustering-graph-container', 'children'),  # Updates the dendrogram container
    [Input('clustering-distance-dropdown', 'value'),  # Input: Distance metric selection
     Input('clustering-method-dropdown', 'value')],  # Input: Clustering method selection
    [State('stored-data', 'data')]  # State: Data stored in the application
)
def update_sample_clustering_graph(distance_metric, method, stored_data):
    """
    Updates the dendrogram visualization for sample clustering.

    Parameters:
    - distance_metric (str): The selected distance metric (e.g., 'euclidean').
    - method (str): The selected clustering method (e.g., 'ward').
    - stored_data (list[dict]): The dataset stored in the application, containing sample information.

    Returns:
    - dash.html.Img: A dynamically generated dendrogram image.

    Behavior:
    - If any input is missing (distance_metric, method, or stored_data), the callback prevents updates.
    - The clustering matrix is calculated based on the input dataset and selected parameters.
    - A dendrogram is generated using the clustering matrix and returned as an image.
    """
    # Check if dropdowns or stored data are empty
    if not distance_metric or not method or not stored_data:
        raise PreventUpdate  # Prevent updates if inputs are invalid or missing

    # Convert stored data into a pandas DataFrame
    input_df = pd.DataFrame(stored_data)

    # Calculate the clustering matrix based on user-selected parameters
    clustering_matrix = calculate_sample_clustering(input_df, distance_metric, method)

    # Extract sample names from the DataFrame
    sample_labels = input_df['sample'].unique().tolist()

    # Create the dendrogram with a dynamic title
    dendrogram_image = plot_dendrogram(clustering_matrix, sample_labels, distance_metric, method)

    return dendrogram_image  # Return the generated dendrogram as an image
