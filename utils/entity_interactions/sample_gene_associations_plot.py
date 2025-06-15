import logging
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Configure logger
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


def plot_sample_gene_scatter(df: pd.DataFrame) -> go.Figure:
    """
    Generates a scatter plot to visualize the association between samples and gene symbols.
    
    The chart dynamically adjusts its dimensions based on the number of unique values
    on both axes, and prioritizes more frequent samples for better visualization.

    Parameters
    ----------
    df : pd.DataFrame
        A pandas DataFrame containing at least the columns 'sample' and 'genesymbol'.

    Returns
    -------
    plotly.graph_objects.Figure
        A Plotly scatter plot showing genes on the x-axis and samples on the y-axis.

    Raises
    ------
    ValueError
        If the required columns 'sample' or 'genesymbol' are missing.
    """
    logger.info("Starting generation of gene-sample scatter plot.")

    required_columns = {"sample", "genesymbol"}
    if not required_columns.issubset(df.columns):
        missing = required_columns - set(df.columns)
        logger.error(f"Missing required column(s): {missing}")
        raise ValueError(f"Input DataFrame is missing required column(s): {missing}")

    # Chart base dimensions and increment factors
    base_height = 400
    base_width = 800
    extra_height_per_label_y = 25
    extra_width_per_label_x = 10
    label_limit_y = 1
    label_limit_x = 10

    # Calculate dynamic height
    num_labels_y = df['sample'].nunique()
    height = (
        base_height + (num_labels_y - label_limit_y) * extra_height_per_label_y
        if num_labels_y > label_limit_y
        else base_height
    )
    logger.info(f"Calculated plot height: {height}px for {num_labels_y} unique samples.")

    # Calculate dynamic width
    num_labels_x = df['genesymbol'].nunique()
    width = (
        base_width + (num_labels_x - label_limit_x) * extra_width_per_label_x
        if num_labels_x > label_limit_x
        else base_width
    )
    logger.info(f"Calculated plot width: {width}px for {num_labels_x} unique genes.")

    # Order samples by frequency
    sample_order = df['sample'].value_counts().index.tolist()

    try:
        # Generate the plot
        fig = px.scatter(
            df,
            x='genesymbol',
            y='sample',
            title='Scatter Plot of Genes vs Samples',
            template='simple_white',
            category_orders={'sample': sample_order}
        )

        # Layout adjustments for readability
        fig.update_layout(
            height=height,
            width=width,
            yaxis=dict(
                tickmode='array',
                tickvals=df['sample'].unique(),
                ticktext=df['sample'].unique(),
                automargin=True,
                tickfont=dict(size=10)
            ),
            xaxis=dict(
                tickangle=45,
                tickmode='array',
                tickvals=df['genesymbol'].unique(),
                ticktext=df['genesymbol'].unique(),
                automargin=True,
                tickfont=dict(size=10)
            ),
            xaxis_title='Gene Symbol',
            yaxis_title='Sample',
            margin=dict(l=200, b=100)
        )

        logger.info("Successfully generated scatter plot.")
        return fig

    except Exception as e:
        logger.exception("An error occurred while generating the scatter plot.")
        raise RuntimeError("Failed to generate scatter plot.") from e
