import logging
import plotly.express as px
import pandas as pd
from plotly.graph_objects import Figure

# Configuração básica do logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

def plot_compound_gene_ranking(compound_gene_ranking_df: pd.DataFrame) -> Figure:
    """
    Creates a bar chart to visualize the ranking of compounds based on the number 
    of unique genes associated.

    Parameters
    ----------
    compound_gene_ranking_df : pd.DataFrame
        DataFrame containing the columns 'compoundname' and 'num_genes', where each
        row represents a compound and the corresponding count of unique genes.

    Returns
    -------
    plotly.graph_objects.Figure
        A Plotly bar chart object displaying the ranking of compounds.

    Raises
    ------
    ValueError
        If required columns are missing or if the DataFrame is empty.
    """
    required_columns = {'compoundname', 'num_genes'}

    if compound_gene_ranking_df.empty:
        logger.warning("Input DataFrame for plotting is empty.")
        raise ValueError("Input DataFrame is empty.")

    if not required_columns.issubset(compound_gene_ranking_df.columns):
        missing = required_columns - set(compound_gene_ranking_df.columns)
        logger.error(f"Missing required columns for plotting: {missing}")
        raise ValueError(f"Missing required columns: {missing}")

    logger.info("Sorting compound_gene_ranking_df by 'num_genes' in descending order.")
    compound_gene_ranking_df = compound_gene_ranking_df.sort_values(by='num_genes', ascending=False)

    logger.info("Generating bar chart with Plotly Express.")
    fig = px.bar(
        compound_gene_ranking_df,
        x='compoundname',
        y='num_genes',
        text='num_genes',
        title='Ranking of Compounds by Gene Interaction',
        template='simple_white'
    )

    fig.update_traces(
        textposition='auto',
        marker=dict(color='steelblue')
    )
    fig.update_layout(
        xaxis_title='Compound',
        yaxis_title='Number of Genes',
        xaxis=dict(
            categoryorder='total descending',
            tickangle=45
        ),
        uniformtext_minsize=10,
        uniformtext_mode='hide'
    )

    logger.info("Bar chart successfully generated.")
    return fig
