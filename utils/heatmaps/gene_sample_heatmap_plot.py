import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


def plot_sample_gene_heatmap(grouped_df: pd.DataFrame) -> go.Figure:
    """
    Creates a heatmap to visualize the KO counts between genes and samples.

    Parameters
    ----------
    grouped_df : pd.DataFrame
        DataFrame with expected columns: 'Gene', 'sample', 'ko_count'.

    Returns
    -------
    plotly.graph_objects.Figure
        The generated heatmap as a Plotly figure.

    Raises
    ------
    ValueError
        If required columns are missing or the data is empty.
    Exception
        For any other failure in plot generation.
    """
    logger.debug("Starting heatmap generation...")

    # Checagem de colunas obrigatórias
    required_columns = ['Gene', 'sample', 'ko_count']
    if not all(col in grouped_df.columns for col in required_columns):
        missing = list(set(required_columns) - set(grouped_df.columns))
        logger.error(f"Missing columns for heatmap: {missing}")
        raise ValueError(f"Missing required columns: {missing}")

    # Checagem de dados vazios
    if grouped_df.empty:
        logger.warning("Input DataFrame is empty.")
        raise ValueError("Input DataFrame is empty. Cannot generate heatmap.")

    try:
        logger.debug("Pivotando a matriz de dados...")
        pivot_df = grouped_df.pivot(index='Gene', columns='sample', values='ko_count').fillna(0)

        logger.debug("Gerando figura com Plotly...")
        fig = px.imshow(
            pivot_df,
            color_continuous_scale='Oranges',
            labels={"x": "Sample", "y": "Gene", "color": "KO Count"},
            title="Heatmap of Ortholog Counts by Sample",
            zmin=0,
            zmax=pivot_df.values.max()
        )

        fig.update_layout(
            xaxis=dict(title='Sample', tickangle=45, automargin=True),
            yaxis=dict(title='Gene', automargin=True),
            coloraxis_colorbar=dict(title="KO Count"),
            plot_bgcolor='white',
            paper_bgcolor='white'
        )

        fig.update_xaxes(showgrid=False)
        fig.update_yaxes(showgrid=False)

        logger.info("Heatmap plot successfully created.")
        return fig

    except Exception as e:
        logger.exception("Unexpected error during heatmap creation.")
        raise RuntimeError("An error occurred while creating the heatmap.") from e
