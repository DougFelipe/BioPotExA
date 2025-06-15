import logging
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Configure logging
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


def plot_sample_ko_scatter(scatter_data: pd.DataFrame, selected_pathway: str) -> go.Figure:
    """
    Creates a scatter plot to display the KOs (KEGG Orthology) associated with each sample 
    for a selected pathway.

    Parameters
    ----------
    scatter_data : pd.DataFrame
        A DataFrame containing 'sample' and 'genesymbol' columns.
    selected_pathway : str
        The selected metabolic pathway to use in the plot title.

    Returns
    -------
    plotly.graph_objects.Figure
        A Plotly scatter plot object.

    Raises
    ------
    ValueError
        If required columns are missing from the input DataFrame.
    """
    logger.info("Generating KO scatter plot for pathway: %s", selected_pathway)

    # Validate required columns
    required_cols = {'sample', 'genesymbol'}
    if not required_cols.issubset(scatter_data.columns):
        missing = required_cols - set(scatter_data.columns)
        logger.error("Missing required columns: %s", missing)
        raise ValueError(f"Input data must contain the following columns: {missing}")

    try:
        # Base dimensions
        base_height = 400
        base_width = 800
        extra_width_per_label = 10
        extra_height_per_label = 15
        label_limit_x = 20
        label_limit_y = 1

        # Count unique samples and genes
        num_labels_x = scatter_data['sample'].nunique()
        num_labels_y = scatter_data['genesymbol'].nunique()

        # Dynamic sizing
        width = base_width + max(0, (num_labels_x - label_limit_x) * extra_width_per_label)
        height = base_height + max(0, (num_labels_y - label_limit_y) * extra_height_per_label)
        tick_spacing_x = max(1, num_labels_x // 20)

        logger.debug("Calculated figure dimensions: width=%d, height=%d", width, height)

        # Create figure
        fig = px.scatter(
            scatter_data,
            x='sample',
            y='genesymbol',
            title=f'Scatter Plot of KOs by Sample for Pathway: {selected_pathway}',
            template='simple_white'
        )

        # Update layout
        fig.update_layout(
            height=height,
            width=width,
            yaxis=dict(
                categoryorder='total ascending',
                title='Genesymbol',
                tickmode='array',
                tickvals=scatter_data['genesymbol'].unique(),
                ticktext=scatter_data['genesymbol'].unique(),
                automargin=True,
                tickfont=dict(size=10),
            ),
            xaxis=dict(
                title='Sample',
                tickangle=45,
                tickmode='linear',
                tickvals=scatter_data['sample'].unique()[::tick_spacing_x],
                ticktext=scatter_data['sample'].unique()[::tick_spacing_x],
                automargin=True,
            ),
            margin=dict(l=200, b=150)
        )

        logger.info("Plot generated successfully for %d samples and %d genes.",
                    num_labels_x, num_labels_y)

        return fig

    except Exception as e:
        logger.exception("Failed to generate scatter plot.")
        raise RuntimeError("Failed to generate KO scatter plot.") from e
