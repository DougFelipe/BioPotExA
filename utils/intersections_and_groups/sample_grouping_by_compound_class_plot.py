import logging
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots


def plot_sample_groups(df: pd.DataFrame) -> go.Figure:
    """
    Creates a scatter plot with subplots to visualize sample groups 
    based on compound interactions.

    Parameters
    ----------
    df : pd.DataFrame
        A DataFrame containing at least the columns 'sample', 
        'compoundname', and 'grupo' (group identifier).

    Returns
    -------
    plotly.graph_objects.Figure
        A Plotly figure with one subplot per group, showing the
        relationship between samples and compounds.

    Raises
    ------
    ValueError
        If required columns are missing or the DataFrame is empty.
    """
    required_columns = {'sample', 'compoundname', 'grupo'}

    # Validar DataFrame e colunas obrigatórias
    if df.empty:
        logging.warning("The input DataFrame is empty.")
        raise ValueError("The input DataFrame is empty.")

    missing_columns = required_columns - set(df.columns)
    if missing_columns:
        logging.error(f"Missing required columns: {missing_columns}")
        raise ValueError(f"The DataFrame must contain the following columns: {missing_columns}")

    # Obter grupos únicos
    unique_groups = df['grupo'].dropna().unique()
    if len(unique_groups) == 0:
        logging.warning("No valid groups found in the 'grupo' column.")
        raise ValueError("No valid groups found in the 'grupo' column.")

    logging.info(f"Generating subplots for {len(unique_groups)} groups.")

    # Criar subplots
    fig = make_subplots(
        rows=1,
        cols=len(unique_groups),
        shared_yaxes=True,
        subplot_titles=unique_groups,
        horizontal_spacing=0.1
    )

    # Adicionar cada grupo como scatter
    for i, group in enumerate(unique_groups):
        group_df = df[df['grupo'] == group].dropna(subset=['sample', 'compoundname'])

        if group_df.empty:
            logging.warning(f"No valid data points for group '{group}'. Skipping subplot.")
            continue

        fig.add_trace(
            go.Scatter(
                x=group_df['sample'],
                y=group_df['compoundname'],
                mode='markers',
                name=str(group),
                showlegend=False
            ),
            row=1,
            col=i + 1
        )

        logging.info(f"Added {len(group_df)} points for group '{group}'.")

    # Layout e ajustes visuais
    fig.update_layout(
        title_text='Sample Groups by Compound Interaction',
        template='simple_white',
        showlegend=False,
        height=600,
        width=max(300 * len(unique_groups), 600)
    )

    fig.update_yaxes(
        tickangle=0,
        tickfont=dict(size=10)
    )

    for i in range(1, len(unique_groups) + 1):
        fig.update_xaxes(
            row=1, col=i,
            tickangle=45,
            title_text=None
        )

    logging.info("Plot generation completed successfully.")
    return fig
