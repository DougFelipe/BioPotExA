import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import logging

# Configure logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)  # Set to DEBUG for more detailed logs
handler = logging.StreamHandler()
formatter = logging.Formatter('[%(asctime)s] %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)


def plot_compound_scatter(df: pd.DataFrame) -> go.Figure:
    """
    Generates a scatter plot to visualize the relationship between samples and compounds.

    The layout is dynamically adjusted based on the number of unique samples and compound names.
    The function validates the input and logs key steps in the plotting process.

    Parameters
    ----------
    df : pd.DataFrame
        A DataFrame containing the columns 'sample', 'compoundname', and 'compoundclass'.

    Returns
    -------
    plotly.graph_objects.Figure
        A Plotly figure object representing the scatter plot.

    Raises
    ------
    ValueError
        If the DataFrame is empty or missing required columns.
    """
    required_columns = {'sample', 'compoundname', 'compoundclass'}

    logger.info("Starting generation of compound scatter plot.")

    # Check for empty DataFrame
    if df.empty:
        logger.error("Input DataFrame is empty.")
        raise ValueError("The input DataFrame is empty. No data to plot.")

    # Validate required columns
    missing_columns = required_columns - set(df.columns)
    if missing_columns:
        logger.error(f"Missing required columns: {missing_columns}")
        raise ValueError(f"The input DataFrame is missing required columns: {missing_columns}")

    logger.info("Input data validated successfully.")
    logger.debug(f"DataFrame shape: {df.shape}")

    # Dynamic chart size based on unique label count
    base_height = 400
    base_width = 800
    extra_width_per_label = 10
    extra_height_per_label = 15
    label_limit_x = 20

    num_labels_x = df['sample'].nunique()
    num_labels_y = df['compoundname'].nunique()

    width = base_width + max(0, (num_labels_x - label_limit_x) * extra_width_per_label)
    height = base_height + max(0, (num_labels_y - 1) * extra_height_per_label)

    tick_spacing_x = max(1, num_labels_x // 20)

    logger.debug(f"Calculated chart dimensions: width={width}, height={height}")

    try:
        # Create the scatter plot
        fig = px.scatter(
            df,
            x='sample',
            y='compoundname',
            color='compoundclass',
            title='Scatter Plot of Samples vs Compounds',
            template='simple_white'
        )

        fig.update_layout(
            height=height,
            width=width,
            yaxis=dict(
                categoryorder='total ascending',
                title='Compound Name',
                tickmode='array',
                tickvals=df['compoundname'].unique(),
                ticktext=df['compoundname'].unique(),
                automargin=True,
                tickfont=dict(size=10)
            ),
            xaxis=dict(
                title='Sample',
                tickangle=45,
                tickmode='linear',
                tickvals=df['sample'].unique()[::tick_spacing_x],
                ticktext=df['sample'].unique()[::tick_spacing_x],
                automargin=True
            ),
            margin=dict(l=200, b=150)
        )

        logger.info("Scatter plot created successfully.")
        return fig

    except Exception as e:
        logger.exception("An error occurred while generating the scatter plot.")
        raise RuntimeError("Failed to generate scatter plot.") from e
