import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import logging

# Configure logger
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")


def plot_heatmap_faceted(df: pd.DataFrame) -> go.Figure:
    """
    Creates a faceted heatmap visualizing toxicity predictions by subcategories and compound names.

    Parameters
    ----------
    df : pd.DataFrame
        A long-format DataFrame containing at least the columns:
        'compoundname', 'value', 'label', 'category', 'subcategoria'.

    Returns
    -------
    go.Figure
        A Plotly Figure object representing the faceted heatmaps.

    Raises
    ------
    ValueError
        If required columns are missing or no categories are found for plotting.
    """
    logger.info("Generating faceted heatmap...")

    required_cols = {'compoundname', 'value', 'label', 'category', 'subcategoria'}
    if not required_cols.issubset(df.columns):
        logger.error(f"Missing required columns: {required_cols - set(df.columns)}")
        raise ValueError(f"Missing required columns: {required_cols - set(df.columns)}")

    categories = df['category'].dropna().unique()
    if len(categories) == 0:
        logger.warning("No categories found for plotting.")
        raise ValueError("No categories available for plotting.")

    n_cols = len(categories)
    fig = make_subplots(
        rows=1,
        cols=n_cols,
        shared_yaxes=True,
        horizontal_spacing=0.05,
        subplot_titles=categories
    )

    for i, category in enumerate(categories, start=1):
        subset = df[df['category'] == category]

        grouped = subset.groupby(
            ['compoundname', 'subcategoria', 'label'], as_index=False
        )['value'].mean()

        heatmap_data = grouped.pivot(
            index='compoundname', columns='subcategoria', values='value'
        )
        hover_text = grouped.pivot(
            index='compoundname', columns='subcategoria', values='label'
        )

        if heatmap_data.empty:
            logger.warning(f"No data for category '{category}', skipping plot.")
            continue

        fig.add_trace(
            go.Heatmap(
                z=heatmap_data.values,
                x=heatmap_data.columns,
                y=heatmap_data.index,
                text=hover_text.values,
                hovertemplate=(
                    "<b>Compound:</b> %{y}<br>"
                    "<b>Subcategory:</b> %{x}<br>"
                    "<b>Label:</b> %{text}<br>"
                    "<b>Toxicity Score:</b> %{z}<extra></extra>"
                ),
                colorscale="reds",
                showscale=(i == 1),
                colorbar=dict(title="Toxicity Score", len=0.8, x=1.02) if i == 1 else None
            ),
            row=1,
            col=i
        )

        fig.update_xaxes(tickangle=45, automargin=True, row=1, col=i)

    fig.update_layout(
        height=600,
        width=300 * n_cols,
        title="Toxicity Predictions",
        template="simple_white",
        yaxis_title="Compound Names",
        margin=dict(l=100, r=50, t=80, b=100)
    )

    logger.info("Faceted heatmap generation complete.")
    return fig
