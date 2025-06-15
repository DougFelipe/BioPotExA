import pandas as pd
# Plotly for Interactive Visualizations
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# ----------------------------------------
# Function: plot_heatmap_faceted (P18)
# ----------------------------------------

def plot_heatmap_faceted(df):
    """
    Creates a faceted heatmap for toxicity categories with shared legends and customized hover text.

    Parameters:
    - df (pd.DataFrame): A DataFrame containing 'compoundname', 'value', 'label', 'category', and 'subcategoria' columns.

    Returns:
    - plotly.graph_objects.Figure: A Plotly figure object with faceted heatmaps.
    """
  
    # Get unique categories
    categories = df['category'].unique()
    n_cols = len(categories)
    if n_cols == 0:
        raise ValueError("No categories available for plotting.")

    # Configure subplots with shared Y-axes and a single legend
    fig = make_subplots(
        rows=1, cols=n_cols,
        shared_yaxes=True,
        horizontal_spacing=0.05,
        subplot_titles=categories
    )

    # Add heatmaps to the subplots
    for i, category in enumerate(categories, start=1):
        subset = df[df['category'] == category]

        # Group by necessary columns and calculate mean values
        subset_grouped = subset.groupby(['compoundname', 'subcategoria', 'label'], as_index=False)['value'].mean()

        # Create pivot table for heatmap data
        heatmap_data = subset_grouped.pivot(index='compoundname', columns='subcategoria', values='value')
        if heatmap_data.empty:
            continue

        hover_text = subset_grouped.pivot(index='compoundname', columns='subcategoria', values='label')

        # Add heatmap trace
        heatmap = go.Heatmap(
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
            colorbar=dict(
                title='Toxicity Score',
                len=0.8,
                x=1.02
            ) if i == 1 else None
        )
        fig.add_trace(heatmap, row=1, col=i)

        # Update x-axis for the current subplot
        fig.update_xaxes(
            tickangle=45,
            automargin=True,
            row=1, col=i
        )

    # Global layout settings
    fig.update_layout(
        height=600,
        width=300 * n_cols,
        title="Toxicity Predictions",
        template="simple_white",
        yaxis_title="Compound Names",
        margin=dict(l=100, r=50, t=80, b=100)
    )

    return fig
