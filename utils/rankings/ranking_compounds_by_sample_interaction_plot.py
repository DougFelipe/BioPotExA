import logging
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Configure logging
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


def plot_compound_ranking(compound_ranking_df: pd.DataFrame) -> go.Figure:
    """
    Creates a bar chart to visualize the ranking of compounds based on 
    the number of unique samples associated with each compound.

    Parameters
    ----------
    compound_ranking_df : pd.DataFrame
        DataFrame with columns 'compoundname' and 'num_samples'.

    Returns
    -------
    plotly.graph_objects.Figure
        A Plotly bar chart visualizing compound rankings.

    Raises
    ------
    ValueError
        If required columns are missing.
    RuntimeError
        If plot rendering fails.
    """
    required_columns = {'compoundname', 'num_samples'}

    logger.info("Rendering compound ranking plot.")

    # Validate required columns
    if not required_columns.issubset(compound_ranking_df.columns):
        missing = required_columns - set(compound_ranking_df.columns)
        logger.error(f"Missing required columns for plotting: {missing}")
        raise ValueError(f"Missing required columns for plotting: {missing}")

    try:
        # Sort data for plotting
        compound_ranking_df = compound_ranking_df.sort_values(
            by='num_samples', ascending=False
        )

        # Create Plotly bar chart
        fig = px.bar(
            compound_ranking_df,
            x='compoundname',
            y='num_samples',
            text='num_samples',
            title='Ranking of Compounds by Sample Interaction',
            template='simple_white'
        )

        # Update visual aesthetics
        fig.update_traces(
            textposition='auto',
            marker=dict(color='steelblue')
        )
        fig.update_layout(
            xaxis_title='Compound',
            yaxis_title='Number of Samples',
            xaxis=dict(
                categoryorder='total descending',
                tickangle=45
            ),
            uniformtext_minsize=10,
            uniformtext_mode='hide'
        )

        logger.info("Plot successfully rendered.")
        return fig

    except Exception as e:
        logger.exception("Failed to render compound ranking plot.")
        raise RuntimeError("Plotting compound ranking failed.") from e
