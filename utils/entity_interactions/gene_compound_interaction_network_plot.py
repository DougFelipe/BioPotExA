# ----------------------------------------
# Imports
# ----------------------------------------

# Standard Library Imports
import base64
import io
import math

# Third-Party Libraries
import pandas as pd  # Data manipulation
import matplotlib.pyplot as plt  # Visualization with Matplotlib
from matplotlib import use as set_matplotlib_backend  # Backend configuration for Matplotlib
from scipy.cluster.hierarchy import dendrogram  # For hierarchical clustering
import networkx as nx  # For creating and visualizing networks

# Plotly for Interactive Visualizations
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Dash for Web Components and Interactivity
from dash import html, dcc, Input, Output, State

# ----------------------------------------
# Function: generate_gene_compound_network (P17)
# ----------------------------------------

def generate_gene_compound_network(network_data):
    """
    Generates a Gene-Compound network graph using Plotly and NetworkX.

    Parameters:
    - network_data (pd.DataFrame): A DataFrame containing 'genesymbol' and 'compoundname' columns.

    Returns:
    - plotly.graph_objects.Figure: A Plotly figure object representing the network.
    """


    # Create a NetworkX graph
    G = nx.Graph()

    # Add nodes and edges
    for _, row in network_data.iterrows():
        G.add_node(row['genesymbol'], type='gene')
        G.add_node(row['compoundname'], type='compound')
        G.add_edge(row['genesymbol'], row['compoundname'])

    # Calculate positions using spring layout
    pos = nx.spring_layout(G, seed=42)

    # Extract node and edge positions
    node_x, node_y, node_text, node_color = [], [], [], []
    for node, position in pos.items():
        node_x.append(position[0])
        node_y.append(position[1])
        node_text.append(node)
        node_color.append('blue' if G.nodes[node]['type'] == 'gene' else 'green')

    edge_x, edge_y = [], []
    for edge in G.edges():
        x0, y0 = pos[edge[0]]
        x1, y1 = pos[edge[1]]
        edge_x.extend([x0, x1, None])
        edge_y.extend([y0, y1, None])

    # Create edge traces
    edge_trace = go.Scatter(
        x=edge_x, y=edge_y,
        line=dict(width=1, color='#888'),
        hoverinfo='none',
        mode='lines'
    )

    # Create node traces
    node_trace = go.Scatter(
        x=node_x, y=node_y,
        mode='markers',
        hoverinfo='text',
        marker=dict(size=10, color=node_color, line=dict(width=2)),
        text=node_text
    )

    # Build the Plotly figure
    fig = go.Figure(
        data=[edge_trace, node_trace],
        layout = go.Layout(
            title={
                'text': "Gene-Compound Network",
                'font': {
                    'size': 16  # Aqui ajusta o tamanho da fonte do título
                }
            },
            showlegend=False,
            margin=dict(b=0, l=0, r=0, t=40),
            xaxis=dict(showgrid=False, zeroline=False),
            yaxis=dict(showgrid=False, zeroline=False)
        )
    )

    return fig
