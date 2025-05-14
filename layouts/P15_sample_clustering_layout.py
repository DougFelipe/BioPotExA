"""
P15_sample_clustering_layout.py
--------------------------------
This script defines the layout for the sample clustering dendrogram in a Dash web application.
The layout includes dropdowns for selecting distance metrics and clustering methods, as well as
a container for displaying the dendrogram.

Functions:
- `get_sample_clustering_layout`: Constructs and returns the layout containing dropdown menus and the dendrogram graph container.
"""

# ----------------------------------------
# Imports
# ----------------------------------------

from dash import html, dcc  # Dash components for building HTML and interactive elements
import dash_bootstrap_components as dbc
# ----------------------------------------
# Function: get_sample_clustering_layout
# ----------------------------------------

def get_sample_clustering_layout():
    """
    Constructs the layout for the sample clustering dendrogram, including options for distance metrics 
    and clustering methods.

    The layout includes:
    - A dropdown to select the distance metric (e.g., Euclidean, Manhattan, Cosine).
    - A dropdown to select the clustering method (e.g., Single Linkage, Complete Linkage, Ward).
    - A container for displaying the dendrogram graph.

    Returns:
    - dash.html.Div: A Dash HTML Div component containing the layout for the sample clustering page.
    """
    return html.Div([
        # Dropdown for selecting the distance metric
        html.Div([
            html.Div('Select Distance Metric', className='menu-text'),  # Label for the dropdown
            dcc.Dropdown(
                id='clustering-distance-dropdown',  # Unique ID for the distance metric dropdown
                options=[
                    {'label': 'Euclidean', 'value': 'euclidean'},  # Option for Euclidean distance
                    {'label': 'Manhattan', 'value': 'cityblock'},  # Option for Manhattan distance
                    {'label': 'Cosine', 'value': 'cosine'}  # Option for Cosine distance
                ],
                value=None,  # Default value is empty
                placeholder='Select a distance metric',  # Placeholder text for the dropdown
            ),
        ], className='navigation-menu'),  # CSS class for styling the dropdown container
        
        # Dropdown for selecting the clustering method
        html.Div([
            html.Div('Select Clustering Method', className='menu-text'),  # Label for the dropdown
            dcc.Dropdown(
                id='clustering-method-dropdown',  # Unique ID for the clustering method dropdown
                options=[
                    {'label': 'Single Linkage', 'value': 'single'},  # Option for Single Linkage method
                    {'label': 'Complete Linkage', 'value': 'complete'},  # Option for Complete Linkage method
                    {'label': 'Average Linkage', 'value': 'average'},  # Option for Average Linkage method
                    {'label': 'Ward', 'value': 'ward'}  # Option for Ward method
                ],
                value=None,  # Default value is empty
                placeholder='Select a clustering method',  # Placeholder text for the dropdown
            ),
        ], className='navigation-menu'),  # CSS class for styling the dropdown container
        
        # Container for the dendrogram graph
        html.Div(
            id='sample-clustering-graph-container',  # Unique ID for the graph container
            children=[],  # Initially empty, will be populated dynamically
            className='graph-card'  # CSS class for styling the graph container
        ),
    ])
