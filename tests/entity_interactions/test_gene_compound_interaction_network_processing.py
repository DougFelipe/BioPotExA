import pytest
import pandas as pd
import networkx as nx
from utils.entity_interactions import gene_compound_interaction_network_processing as gcnet

@pytest.fixture
def minimal_gene_compound_df():
    """Minimal DataFrame with required columns for gene-compound graph."""
    return pd.DataFrame({
        "genesymbol": ["geneA", "geneB"],
        "compoundname": ["cmpd1", "cmpd2"]
    })

def test_build_gene_compound_graph_valid(minimal_gene_compound_df):
    """
    Test building a gene-compound bipartite graph from valid input.

    Parameters
    ----------
    minimal_gene_compound_df : fixture
        Minimal DataFrame with 'genesymbol' and 'compoundname' columns.

    Expected
    -------
    The resulting graph contains correct nodes and edges with appropriate types.
    """
    G = gcnet.build_gene_compound_graph(minimal_gene_compound_df)
    genes, compounds = gcnet.get_node_partitions(G)
    assert set(genes) == {"geneA", "geneB"}
    assert set(compounds) == {"cmpd1", "cmpd2"}
    assert G.has_edge("geneA", "cmpd1")
    assert G.has_edge("geneB", "cmpd2")
    for n in genes:
        assert G.nodes[n]["type"] == "gene"
    for n in compounds:
        assert G.nodes[n]["type"] == "compound"

def test_build_gene_compound_graph_empty():
    """
    Test that an empty DataFrame raises ValueError.

    Parameters
    ----------
    None

    Expected
    -------
    ValueError is raised when input DataFrame is empty.
    """
    df = pd.DataFrame(columns=["genesymbol", "compoundname"])
    with pytest.raises(ValueError, match="empty"):
        gcnet.build_gene_compound_graph(df)

def test_build_gene_compound_graph_missing_columns():
    """
    Test that missing required columns raises ValueError.

    Parameters
    ----------
    None

    Expected
    -------
    ValueError is raised if 'genesymbol' or 'compoundname' is missing.
    """
    df = pd.DataFrame({"foo": [1], "bar": [2]})
    with pytest.raises(ValueError, match="columns"):
        gcnet.build_gene_compound_graph(df)

def test_get_node_partitions_correct_types(minimal_gene_compound_df):
    """
    Test that get_node_partitions returns correct gene and compound lists.

    Parameters
    ----------
    minimal_gene_compound_df : fixture

    Expected
    -------
    Genes and compounds are partitioned by 'type' attribute.
    """
    G = gcnet.build_gene_compound_graph(minimal_gene_compound_df)
    genes, compounds = gcnet.get_node_partitions(G)
    assert set(genes) == {"geneA", "geneB"}
    assert set(compounds) == {"cmpd1", "cmpd2"}

def test_compute_node_positions_layout(minimal_gene_compound_df):
    """
    Test that compute_node_positions returns a position dict for all nodes.

    Parameters
    ----------
    minimal_gene_compound_df : fixture

    Expected
    -------
    All nodes have a 2D position assigned.
    """
    G = gcnet.build_gene_compound_graph(minimal_gene_compound_df)
    pos = gcnet.compute_node_positions(G)
    assert set(pos.keys()) == set(G.nodes)
    for coords in pos.values():
        assert len(coords) == 2

def test_prepare_plotly_traces_structure(minimal_gene_compound_df):
    """
    Test that prepare_plotly_traces returns three Plotly traces.

    Parameters
    ----------
    minimal_gene_compound_df : fixture

    Expected
    -------
    Returns edge, gene, and compound traces with correct types.
    """
    G = gcnet.build_gene_compound_graph(minimal_gene_compound_df)
    pos = gcnet.compute_node_positions(G)
    traces = gcnet.prepare_plotly_traces(G, pos)
    assert len(traces) == 3
    assert traces[0].mode == "lines"
    assert traces[1].name == "Gene"
    assert traces[2].name == "Compound"

def test_build_gene_compound_network_figure_layout(minimal_gene_compound_df):
    """
    Test that the final Plotly figure has correct layout and traces.

    Parameters
    ----------
    minimal_gene_compound_df : fixture

    Expected
    -------
    Figure contains three traces and correct title.
    """
    G = gcnet.build_gene_compound_graph(minimal_gene_compound_df)
    pos = gcnet.compute_node_positions(G)
    traces = gcnet.prepare_plotly_traces(G, pos)
    fig = gcnet.build_gene_compound_network_figure(traces)
    assert fig.layout.title.text == "Gene-Compound Network"
    assert len(fig.data) == 3

def test_build_gene_compound_graph_duplicate_edges():
    """
    Test that duplicate gene-compound pairs do not create duplicate edges.

    Expected
    -------
    Only one edge per unique gene-compound pair exists in the graph.
    """
    df = pd.DataFrame({
        "genesymbol": ["geneA", "geneA"],
        "compoundname": ["cmpd1", "cmpd1"]
    })
    G = gcnet.build_gene_compound_graph(df)
    assert G.number_of_edges() == 1
    assert G.has_edge("geneA", "cmpd1")

def test_get_node_partitions_empty_graph():
    """
    Test get_node_partitions on an empty graph.

    Expected
    -------
    Both returned lists are empty.
    """
    G = nx.Graph()
    genes, compounds = gcnet.get_node_partitions(G)
    assert genes == []
    assert compounds == []

def test_prepare_plotly_traces_handles_isolated_nodes():
    """
    Test prepare_plotly_traces with isolated gene and compound nodes.

    Expected
    -------
    Isolated nodes are included in the traces.
    """
    G = nx.Graph()
    G.add_node("geneX", type="gene")
    G.add_node("cmpdY", type="compound")
    pos = {"geneX": (0, 0), "cmpdY": (1, 1)}
    traces = gcnet.prepare_plotly_traces(G, pos)
    assert "geneX" in traces[1].text
    assert "cmpdY" in traces[2].text

def test_build_gene_compound_network_figure_custom_traces():
    """
    Test build_gene_compound_network_figure with custom traces.

    Expected
    -------
    The figure contains the provided traces.
    """
    import plotly.graph_objects as go
    dummy_trace = go.Scatter(x=[0], y=[0], mode="markers", name="Dummy")
    fig = gcnet.build_gene_compound_network_figure([dummy_trace])
    assert len(fig.data) == 1
    assert fig.data[0].name == "Dummy"
