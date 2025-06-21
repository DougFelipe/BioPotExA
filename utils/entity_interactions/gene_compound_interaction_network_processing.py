import logging
import networkx as nx
import plotly.graph_objects as go

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def build_gene_compound_graph(network_data):
    """
    Cria o grafo bipartido Gene-Compound usando NetworkX.
    """
    if network_data.empty:
        logger.warning("Received empty network data.")
        raise ValueError("The network data is empty.")

    if not {'genesymbol', 'compoundname'}.issubset(network_data.columns):
        logger.error("Missing required columns in network_data.")
        raise ValueError("DataFrame must contain 'genesymbol' and 'compoundname' columns.")

    G = nx.Graph()
    for _, row in network_data.iterrows():
        gene = row['genesymbol']
        compound = row['compoundname']
        G.add_node(gene, type='gene')
        G.add_node(compound, type='compound')
        G.add_edge(gene, compound)
    return G

def compute_node_positions(G, seed=42):
    """
    Calcula as posições dos nós do grafo usando spring_layout.
    """
    return nx.spring_layout(G, seed=seed)

def prepare_plotly_traces(G, pos):
    """
    Prepara os traces (arestas e nós) para o Plotly.
    """
    gene_nodes = [n for n, attr in G.nodes(data=True) if attr['type'] == 'gene']
    compound_nodes = [n for n, attr in G.nodes(data=True) if attr['type'] == 'compound']

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
    return [edge_trace, gene_trace, compound_trace]

def build_gene_compound_network_figure(traces):
    """
    Monta a figura Plotly final com os traces fornecidos.
    """
    return go.Figure(
        data=traces,
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

# Função principal de interface (mantém API compatível)
def generate_gene_compound_network(network_data) -> go.Figure:
    """
    Pipeline completo: recebe DataFrame, processa o grafo, calcula posições e monta a figura Plotly.
    """
    logger.info("Gerando grafo Gene-Compound (modularizado)")
    G = build_gene_compound_graph(network_data)
    pos = compute_node_positions(G)
    traces = prepare_plotly_traces(G, pos)
    fig = build_gene_compound_network_figure(traces)
    return fig
