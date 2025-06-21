# plots/gene_compound_network_plot.py

import logging
import plotly.graph_objects as go
from utils.entity_interactions.gene_compound_interaction_network_processing import (
    build_gene_compound_graph,
    get_node_partitions,
    compute_node_positions
)


logger = logging.getLogger(__name__)

def generate_gene_compound_network(network_data):
    """
    Gera a figura Plotly do grafo gene-composto.

    Parâmetros
    ----------
    network_data : pd.DataFrame

    Retorna
    -------
    plotly.graph_objects.Figure
    """
    logger.info("Construindo o grafo a partir dos dados.")
    G = build_gene_compound_graph(network_data)
    gene_nodes, compound_nodes = get_node_partitions (G)
    pos = compute_node_positions(G)

    # Função utilitária para extrair coordenadas dos nós
    def get_node_coords(nodes):
        return [pos[n][0] for n in nodes], [pos[n][1] for n in nodes]

    # Arestas
    edge_x, edge_y = [], []
    for edge in G.edges():
        x0, y0 = pos[edge[0]]
        x1, y1 = pos[edge[1]]
        edge_x.extend([x0, x1, None])
        edge_y.extend([y0, y1, None])

    edge_trace = go.Scatter(
        x=edge_x, y=edge_y,
        mode='lines',
        line=dict(width=1, color='#888'),
        hoverinfo='none',
        showlegend=False
    )

    # Genes
    gene_x, gene_y = get_node_coords(gene_nodes)
    gene_trace = go.Scatter(
        x=gene_x, y=gene_y,
        mode='markers',
        name='Gene',
        marker=dict(size=10, color='blue', line=dict(width=2, color='black')),
        hoverinfo='text',
        text=gene_nodes,
        showlegend=True,
        legendgroup="gene"
    )

    # Compostos
    compound_x, compound_y = get_node_coords(compound_nodes)
    compound_trace = go.Scatter(
        x=compound_x, y=compound_y,
        mode='markers',
        name='Compound',
        marker=dict(size=10, color='green', line=dict(width=2, color='black')),
        hoverinfo='text',
        text=compound_nodes,
        showlegend=True,
        legendgroup="compound"
    )

    logger.info("Montando figura Plotly final.")
    fig = go.Figure(
        data=[edge_trace, gene_trace, compound_trace],
        layout=go.Layout(
            title=dict(
                text="Gene-Compound Network",
                font=dict(size=16)
            ),
            plot_bgcolor='white',
            paper_bgcolor='white',
            showlegend=True,
            legend=dict(
                x=0.01, y=0.99,
                bordercolor="Black",
                borderwidth=1,
                bgcolor="white"
            ),
            margin=dict(t=40, b=0, l=0, r=0),
            xaxis=dict(showgrid=False, zeroline=False, visible=False),
            yaxis=dict(showgrid=False, zeroline=False, visible=False)
        )
    )

    return fig
