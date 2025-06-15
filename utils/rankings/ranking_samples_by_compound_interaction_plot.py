import logging
import plotly.express as px
import pandas as pd
from plotly.graph_objs import Figure

# Configure logging
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


def plot_sample_ranking(sample_ranking_df: pd.DataFrame) -> Figure:
    """
    Creates a bar chart to visualize the ranking of samples based on the number of unique compounds.

    Parameters
    ----------
    sample_ranking_df : pd.DataFrame
        DataFrame containing columns 'sample' and 'num_compounds'.

    Returns
    -------
    plotly.graph_objects.Figure
        A Plotly bar chart showing samples ranked by compound count.

    Raises
    ------
    ValueError
        If required columns are missing or if the input is not a DataFrame.
    """
    logger.info("Starting plot_sample_ranking...")

    if not isinstance(sample_ranking_df, pd.DataFrame):
        logger.error("Input is not a DataFrame.")
        raise ValueError("Expected input to be a pandas DataFrame.")

    required_cols = {'sample', 'num_compounds'}
    if not required_cols.issubset(sample_ranking_df.columns):
        missing = required_cols - set(sample_ranking_df.columns)
        logger.error(f"Missing required columns: {missing}")
        raise ValueError(f"Input DataFrame is missing required columns: {missing}")

    try:
        # Sort the DataFrame
        sample_ranking_df = sample_ranking_df.sort_values(
            by='num_compounds', ascending=False
        )
        logger.debug("Sorted sample_ranking_df.")

        # Create the bar chart
        fig = px.bar(
            sample_ranking_df,
            x='sample',
            y='num_compounds',
            text='num_compounds',
            template='simple_white'
        )

        fig.update_traces(
            textposition='auto',
            marker=dict(color='steelblue')
        )

        fig.update_layout(
            title='Ranking of Samples by Compound Interaction',
            xaxis_title='Sample',
            yaxis_title='Number of Compounds',
            xaxis=dict(
                categoryorder='total descending',
                tickangle=45
            ),
            uniformtext_minsize=10,
            uniformtext_mode='hide'
        )

        logger.info("UpSet plot successfully generated.")
        return fig

    except Exception as e:
        logger.exception("Failed to generate sample ranking plot.")
        raise RuntimeError("Failed to generate sample ranking plot.") from e
