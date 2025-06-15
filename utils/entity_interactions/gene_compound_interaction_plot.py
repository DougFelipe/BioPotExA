import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def plot_gene_compound_scatter(df: pd.DataFrame) -> go.Figure:
    """
    Generates a scatter plot showing the association between gene symbols and compound names.
    The layout is dynamically adjusted based on the number of unique labels to ensure readability.

    Parameters
    ----------
    df : pd.DataFrame
        A DataFrame containing gene-compound association data.
        Must include the columns: 'genesymbol' and 'compoundname'.

    Returns
    -------
    plotly.graph_objects.Figure
        A Plotly figure object representing the scatter plot.

    Raises
    ------
    ValueError
        If the required columns are missing from the input DataFrame.
    Exception
        For unexpected errors during plot generation.
    """
    logger.info("Starting scatter plot generation for gene-compound associations.")

    # --- Step 1: Validate required columns ---
    required_columns = {'genesymbol', 'compoundname'}
    if not required_columns.issubset(df.columns):
        missing = required_columns - set(df.columns)
        logger.error(f"Missing required columns: {missing}")
        raise ValueError(f"Missing required columns: {missing}")

    try:
        # --- Step 2: Calculate dynamic layout dimensions ---
        base_height = 400
        extra_height_per_label_y = 25
        base_width = 800
        extra_width_per_label_x = 10

        num_labels_y = df['compoundname'].nunique()
        height = base_height + max(0, (num_labels_y - 1)) * extra_height_per_label_y
        logger.debug(f"Dynamic height calculated: {height}")

        num_labels_x = df['genesymbol'].nunique()
        width = base_width + max(0, (num_labels_x - 10)) * extra_width_per_label_x
        logger.debug(f"Dynamic width calculated: {width}")

        # --- Step 3: Order compounds by frequency for better y-axis presentation ---
        compound_order = df['compoundname'].value_counts().index.tolist()
        logger.info("Compound order determined by frequency.")

        # --- Step 4: Create scatter plot ---
        fig = px.scatter(
            df,
            x='genesymbol',
            y='compoundname',
            title='Scatter Plot of Genes vs Compounds',
            template='simple_white',
            category_orders={'compoundname': compound_order}
        )

        # --- Step 5: Update layout with better spacing and label handling ---
        fig.update_layout(
            height=height,
            width=width,
            yaxis=dict(
                categoryorder='total ascending',
                tickmode='array',
                tickvals=df['compoundname'].unique(),
                ticktext=df['compoundname'].unique(),
                automargin=True,
                tickfont=dict(size=10)
            ),
            xaxis=dict(
                title='Gene Symbol',
                tickangle=45,
                tickmode='array',
                tickvals=df['genesymbol'].unique(),
                ticktext=df['genesymbol'].unique(),
                automargin=True,
                tickfont=dict(size=10)
            ),
            yaxis_title='Compound Name',
            margin=dict(l=200, b=100)
        )

        logger.info("Scatter plot successfully generated.")
        return fig

    except Exception as e:
        logger.exception("An error occurred while generating the scatter plot.")
        raise RuntimeError("Failed to generate gene-compound scatter plot.") from e
