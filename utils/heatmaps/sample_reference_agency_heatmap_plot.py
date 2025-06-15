import plotly.express as px
import pandas as pd
import logging

# Configure basic logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def plot_sample_reference_heatmap(df: pd.DataFrame):
    """
    Create a dynamic Plotly heatmap to visualize compound counts across 
    sample and referenceAG combinations.

    Parameters
    ----------
    df : pd.DataFrame
        Pivoted DataFrame where rows are 'referenceAG', columns are 'sample',
        and values represent compound counts.

    Returns
    -------
    plotly.graph_objects.Figure
        A Plotly heatmap figure object.

    Raises
    ------
    ValueError
        If the input DataFrame is empty or lacks proper structure.
    """
    if df.empty:
        logger.error("The input DataFrame is empty. Cannot generate heatmap.")
        raise ValueError("Input DataFrame for heatmap is empty.")

    if df.index.name != 'referenceAG' or not all(isinstance(i, str) for i in df.columns):
        logger.warning("DataFrame may not have the expected format for heatmap axes.")

    logger.info("Calculating heatmap dimensions based on label counts")
    try:
        base_height = 400
        base_width = 400
        extra_height_per_label = 20
        extra_width_per_label = 20

        num_labels_x = len(df.columns)
        num_labels_y = len(df.index)
        height = base_height + (num_labels_y * extra_height_per_label)
        width = base_width + (num_labels_x * extra_width_per_label)

        logger.debug(f"Calculated dimensions: width={width}, height={height}")

        fig = px.imshow(
            df,
            labels=dict(x="Sample", y="Reference AG", color="Compound Count"),
            x=df.columns,
            y=df.index,
            color_continuous_scale="Viridis",
            title="Heatmap of Samples vs Reference AG"
        )

        fig.update_layout(
            xaxis=dict(
                title=dict(text="Sample", standoff=50),
                tickangle=45,
                tickfont=dict(size=10),
                automargin=True
            ),
            yaxis=dict(
                title=dict(text="Reference AG", standoff=50),
                tickfont=dict(size=10),
                automargin=True
            ),
            margin=dict(l=200, b=200),
            height=height,
            width=width
        )

        logger.info("Heatmap successfully created")
        return fig

    except Exception as e:
        logger.exception("Failed to generate heatmap figure")
        raise RuntimeError("An error occurred while creating the heatmap.") from e
