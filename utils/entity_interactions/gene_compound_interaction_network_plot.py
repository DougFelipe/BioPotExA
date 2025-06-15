import logging
import base64
import io
import networkx as nx
import plotly.graph_objects as go

# Configuração de logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def generate_gene_compound_network(network_data) -> go.Figure:
    """
    Generates an interactive Gene-Compound network using Plotly and NetworkX.

    Parameters
    ----------
    network_data : pd.DataFrame
        DataFrame containing columns 'genesymbol' and 'compoundname'.

    Returns
    -------
    plotly.graph_objects.Figure
        Plotly figure object representing the network.

    Raises
    ------
    ValueError
        If the input DataFrame is empty or lacks required columns.
    """
    logger.info("Generating Gene-Compound network graph.")

    if network_data.empty:
        logger.warning("Received empty network data.")
        raise ValueError("The network data is empty.")

    if not {'genesymbol', 'compoundname'}.issubset(network_data.columns):
        logger.error("Missing required columns in network_data.")
        raise ValueError("DataFrame must contain 'genesymbol' and 'compoundname' columns.")

    G = nx.Graph()

    logger.info("Adding nodes and edges to the network.")
    for _, row in network_data.iterrows():
        gene = row['genesymbol']
        compound = row['compoundname']
        G.add_node(gene, type='gene')
        G.add_node(compound, type='compound')
        G.add_edge(gene, compound)

    logger.info("Calculating node positions.")
    pos = nx.spring_layout(G, seed=42)

    node_x, node_y, node_text, node_color = [], [], [], []
    for node, (x, y) in pos.items():
        node_x.append(x)
        node_y.append(y)
        node_text.append(node)
        node_color.append('blue' if G.nodes[node]['type'] == 'gene' else 'green')

    edge_x, edge_y = [], []
    for edge in G.edges():
        x0, y0 = pos[edge[0]]
        x1, y1 = pos[edge[1]]
        edge_x.extend([x0, x1, None])
        edge_y.extend([y0, y1, None])

    logger.info("Creating Plotly traces.")
    edge_trace = go.Scatter(
        x=edge_x, y=edge_y,
        mode='lines',
        line=dict(width=1, color='#888'),
        hoverinfo='none'
    )

    node_trace = go.Scatter(
        x=node_x, y=node_y,
        mode='markers',
        hoverinfo='text',
        marker=dict(size=10, color=node_color, line=dict(width=2)),
        text=node_text
    )

    logger.info("Assembling final Plotly figure.")
    fig = go.Figure(
        data=[edge_trace, node_trace],
        layout=go.Layout(
            title=dict(
                text="Gene-Compound Network",
                font=dict(size=16)
            ),
            showlegend=False,
            margin=dict(t=40, b=0, l=0, r=0),
            xaxis=dict(showgrid=False, zeroline=False),
            yaxis=dict(showgrid=False, zeroline=False)
        )
    )

    return fig
