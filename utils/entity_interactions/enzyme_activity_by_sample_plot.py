import logging
import pandas as pd
import plotly.express as px
from plotly.graph_objects import Figure

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def plot_enzyme_activity_counts(enzyme_count_df: pd.DataFrame, sample: str) -> Figure:
    """
    Generates a bar chart showing the number of unique KOs per enzyme activity for a given sample.

    Parameters
    ----------
    enzyme_count_df : pd.DataFrame
        DataFrame with enzyme activity data. Expected columns: 'enzyme_activity', 'unique_ko_count'.
    sample : str
        The sample name used in the chart title.

    Returns
    -------
    plotly.graph_objects.Figure
        A bar chart displaying enzyme activities and their unique KO counts.

    Raises
    ------
    ValueError
        If the DataFrame is empty or missing required columns.
    """
    required_columns = {'enzyme_activity', 'unique_ko_count'}

    if enzyme_count_df.empty:
        logger.error("Input DataFrame is empty.")
        raise ValueError("The enzyme activity count DataFrame is empty.")

    if not required_columns.issubset(enzyme_count_df.columns):
        missing = required_columns - set(enzyme_count_df.columns)
        logger.error(f"Missing required columns: {missing}")
        raise ValueError(f"Missing required columns: {missing}")

    logger.info("Generating enzyme activity bar chart.")
    fig = px.bar(
        enzyme_count_df,
        x='enzyme_activity',
        y='unique_ko_count',
        title=f'Unique Enzyme Activities for {sample}',
        text='unique_ko_count',
        template="simple_white"
    )

    fig.update_layout(
        xaxis_title='Enzyme Activity',
        yaxis_title='Unique Gene Count',
        xaxis_tickangle=45
    )

    logger.info("Bar chart successfully generated.")
    return fig
