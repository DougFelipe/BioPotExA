import logging
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Configuração de logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Se o logger ainda não tiver handlers (útil para evitar logs duplicados)
if not logger.handlers:
    handler = logging.StreamHandler()
    formatter = logging.Formatter('[%(levelname)s] %(asctime)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)


def plot_ko_count(ko_count_df: pd.DataFrame) -> go.Figure:
    """
    Creates a bar chart showing the count of unique KOs (genes) per sample.

    Parameters
    ----------
    ko_count_df : pd.DataFrame
        A DataFrame containing the KO counts per sample.
        Expected columns: 'sample', 'ko_count'.

    Returns
    -------
    plotly.graph_objects.Figure
        A Plotly bar chart object with KO counts.

    Raises
    ------
    ValueError
        If required columns are missing or the DataFrame is empty.
    """
    logger.debug("Starting KO count bar plot generation.")

    # Validação de entrada
    required_columns = {'sample', 'ko_count'}
    if ko_count_df.empty:
        logger.error("Input DataFrame is empty.")
        raise ValueError("Input DataFrame is empty.")

    if not required_columns.issubset(ko_count_df.columns):
        missing = required_columns - set(ko_count_df.columns)
        logger.error(f"Missing required columns: {missing}")
        raise ValueError(f"Missing required columns: {missing}")

    logger.info(f"Generating KO count bar chart for {len(ko_count_df)} samples.")

    # Criação do gráfico de barras
    fig = px.bar(
        ko_count_df,
        x='sample',
        y='ko_count',
        text='ko_count',
        template="simple_white"
    )

    fig.update_traces(
        textposition='auto',
        marker=dict(color='steelblue')
    )

    fig.update_layout(
        title="Gene Count by Sample",
        xaxis_title='Sample',
        yaxis_title='Unique Gene Count',
        xaxis={'categoryorder': 'total descending'},
        xaxis_tickangle=45,
        uniformtext_minsize=10,
        uniformtext_mode='hide'
    )

    logger.debug("Bar chart generation complete.")
    return fig


def create_violin_plot(ko_count_per_sample: pd.DataFrame) -> go.Figure:
    """
    Creates a violin plot with a boxplot overlay to visualize the distribution 
    of unique KO counts per sample.

    Parameters
    ----------
    ko_count_per_sample : pd.DataFrame
        A DataFrame containing the KO counts per sample.
        Expected columns: 'ko_count' and optionally 'sample' for hover.

    Returns
    -------
    plotly.graph_objects.Figure
        A Plotly violin plot object.

    Raises
    ------
    ValueError
        If required columns are missing or the DataFrame is empty.
    """
    logger.debug("Starting violin plot generation.")

    # Validação de entrada
    if ko_count_per_sample.empty:
        logger.error("Input DataFrame is empty.")
        raise ValueError("Input DataFrame is empty.")

    if 'ko_count' not in ko_count_per_sample.columns:
        logger.error("Missing required column: 'ko_count'")
        raise ValueError("Missing required column: 'ko_count'")

    logger.info("Generating violin plot with box overlay.")

    # Criação do gráfico violin com boxplot e pontos
    fig = px.violin(
        ko_count_per_sample,
        y='ko_count',
        box=True,
        points='all',
        hover_name='sample' if 'sample' in ko_count_per_sample.columns else None,
        hover_data={'sample': False, 'ko_count': True} if 'sample' in ko_count_per_sample.columns else {'ko_count': True},
        template="simple_white"
    )

    fig.update_traces(
        marker=dict(size=5, opacity=1),
        line=dict(width=1),
        jitter=0.3,
        pointpos=0
    )

    fig.update_layout(
        yaxis_title='Unique Gene Count',
        showlegend=False,
        template='plotly_white',
        xaxis_title=''
    )

    logger.debug("Violin plot generation complete.")
    return fig
