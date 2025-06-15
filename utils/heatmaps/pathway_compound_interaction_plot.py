import logging
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Configure logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def plot_pathway_heatmap(df: pd.DataFrame, selected_sample: str) -> go.Figure:
    """
    Generates a heatmap figure to visualize KO counts across pathways and compound pathways 
    for a specific sample, with each compound pathway rendered in a separate facet.

    Parameters
    ----------
    df : pd.DataFrame
        A DataFrame containing columns: 'Pathway', 'compound_pathway', 'sample', and 'ko_count'.
    selected_sample : str
        The name of the sample to filter data for visualization.

    Returns
    -------
    go.Figure
        A Plotly figure object containing the heatmap with facets for each compound pathway.

    Raises
    ------
    ValueError
        If required columns are missing or no data is available for the selected sample.
    """
    required_columns = {'Pathway', 'compound_pathway', 'sample', 'ko_count'}
    if not required_columns.issubset(df.columns):
        missing = required_columns - set(df.columns)
        logger.error(f"Missing columns in input DataFrame: {missing}")
        raise ValueError(f"Missing columns in input DataFrame: {missing}")

    # Filter by selected sample
    df_sample = df[df['sample'] == selected_sample]

    if df_sample.empty:
        logger.warning(f"No data available for sample: {selected_sample}")
        raise ValueError(f"No data available for sample: {selected_sample}")

    compound_pathways = df_sample['compound_pathway'].unique()
    n_cols = len(compound_pathways)

    subplot_width = 100
    spacing = 500
    total_width = n_cols * subplot_width + (n_cols - 1) * spacing

    fig = make_subplots(
        rows=1,
        cols=n_cols,
        shared_yaxes=False,
        horizontal_spacing=spacing / total_width
    )

    for i, compound_pathway in enumerate(compound_pathways, start=1):
        df_filtered = df_sample[df_sample['compound_pathway'] == compound_pathway]

        heatmap_data = df_filtered.pivot_table(
            index='Pathway',
            columns='compound_pathway',
            values='ko_count',
            aggfunc='sum',
            fill_value=0
        )

        heatmap_data = heatmap_data.loc[
            (heatmap_data != 0).any(axis=1),
            (heatmap_data != 0).any(axis=0)
        ]

        if not heatmap_data.empty:
            logger.info(f"Adding heatmap for compound pathway: {compound_pathway}")
            heatmap = go.Heatmap(
                z=heatmap_data.values,
                x=heatmap_data.columns,
                y=heatmap_data.index,
                colorscale='Oranges',
                showscale=True,
                colorbar=dict(
                    title=dict(text='KO Count', side='right'),
                    x=(subplot_width * (i - 1) + (i - 1) * spacing + subplot_width) / total_width,
                    xanchor='left',
                    y=0.5,
                    yanchor='middle',
                    lenmode='fraction',
                    len=0.6
                )
            )
            fig.add_trace(heatmap, row=1, col=i)

        fig.update_xaxes(automargin=True, row=1, col=i)

    fig.update_layout(
        height=600,
        width=total_width,
        title=f"Heatmap of Pathway vs Compound Pathway for Sample {selected_sample}",
        yaxis_title="Pathway",
        template='simple_white',
        showlegend=False
    )

    for annotation in fig['layout']['annotations']:
        annotation['text'] = ''

    return fig
