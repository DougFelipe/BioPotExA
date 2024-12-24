"""
P17_gene_compound_network_callbacks.py
--------------------------------------
This script defines a callback for updating the Gene-Compound Network visualization in a Dash web application. 
The network shows the interactions between genes and compounds based on the provided data.

The callback processes input data, validates it, and generates a network graph using Plotly. 
If no data is available, it returns an empty graph with an appropriate message.
"""

# ----------------------------------------
# Imports
# ----------------------------------------

from dash import callback, Output, Input, State  # Dash callback components for interactivity
from app import app  # Dash application instance
from utils.data_processing import prepare_gene_compound_network_data  # Utility to process network data
from utils.plot_processing import generate_gene_compound_network  # Utility to generate the network graph
import plotly.graph_objects as go  # Plotly for creating graph components

# ----------------------------------------
# Callback: update_gene_compound_network
# ----------------------------------------

@app.callback(
    Output("gene-compound-network-graph", "figure"),  # Output the network graph as a Plotly figure
    Input("stored-data", "data")  # Input: Data from the application's storage
)
def update_gene_compound_network(stored_data):
    """
    Updates the Gene-Compound Network graph based on stored data.

    Behavior:
    - If no data is provided, returns an empty graph with a message.
    - Processes the input data to prepare network information.
    - If no interactions are found, returns an empty graph with a message.
    - Generates and returns a network graph showing the interactions between genes and compounds.

    Parameters:
    - stored_data (dict): Data stored in the application, representing gene-compound relationships.

    Returns:
    - plotly.graph_objects.Figure: A Plotly figure representing the Gene-Compound Network.
    """
    if not stored_data:
        # Returns an empty figure with a message
        return go.Figure(
            layout=go.Layout(
                title="No data available to display the network",  # Message indicating no data
                xaxis=dict(visible=False),  # Hides the X-axis
                yaxis=dict(visible=False)   # Hides the Y-axis
            )
        )

    # Process the input data to prepare it for the network graph
    network_data = prepare_gene_compound_network_data(stored_data)
    if network_data.empty:
        # Returns an empty figure with a message if no interactions are found
        return go.Figure(
            layout=go.Layout(
                title="No interactions found between genes and compounds",  # Message indicating no interactions
                xaxis=dict(visible=False),  # Hides the X-axis
                yaxis=dict(visible=False)   # Hides the Y-axis
            )
        )

    # Generate the network graph using the processed data
    return generate_gene_compound_network(network_data)
