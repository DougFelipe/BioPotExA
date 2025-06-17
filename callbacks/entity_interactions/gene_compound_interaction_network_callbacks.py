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

# Funções expostas diretamente via __init__.py do subpacote `entity_interactions`
from utils.entity_interactions import (
        generate_gene_compound_network
)

import plotly.graph_objects as go  # Plotly for creating graph components
import pandas as pd  # Pandas for data manipulation


# ----------------------------------------
# Callback: update_gene_compound_network
# ----------------------------------------

@app.callback(  
    Output("gene-compound-network-graph", "figure"),  # Output the network graph as a Plotly figure  
    Input("biorempp-merged-data", "data")  # MUDANÇA: usar store específico do BioRemPP  
)  
def update_gene_compound_network(biorempp_data):  
    """  
    Updates the Gene-Compound Network graph based on pre-processed data.  
  
    Behavior:  
    - If no processed data is provided, returns an empty graph with a message.  
    - Processes the pre-processed data to prepare network information.  
    - If no interactions are found, returns an empty graph with a message.  
    - Generates and returns a network graph showing the interactions between genes and compounds.  
  
    Parameters:  
    - biorempp_data (list of dict): Pre-processed data from BioRemPP store.  
  
    Returns:  
    - plotly.graph_objects.Figure: A Plotly figure representing the Gene-Compound Network.  
    """  
    if not biorempp_data:  
        # Returns an empty figure with a message  
        return go.Figure(  
            layout=go.Layout(  
                title="No data available to display the network",  # Message indicating no data  
                xaxis=dict(visible=False),  # Hides the X-axis  
                yaxis=dict(visible=False)   # Hides the Y-axis  
            )  
        )  
  
    # Convert stored processed data into a DataFrame (dados já processados)  
    merged_df = pd.DataFrame(biorempp_data)  
      
    # Filter relevant columns and remove duplicates for network generation  
    network_data = merged_df[['genesymbol', 'compoundname']].dropna().drop_duplicates()  
      
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
