import pandas as pd
import plotly.express as px
import logging

# Configuração básica do logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def plot_pathway_ko_counts(pathway_count_df: pd.DataFrame, selected_sample: str):
    """
    Creates a bar chart showing the count of unique KOs for each pathway in a selected sample.

    Parameters
    ----------
    pathway_count_df : pd.DataFrame
        DataFrame containing KO counts grouped by pathways and samples.
        Expected columns: 'sample', 'pathname', 'unique_ko_count'.

    selected_sample : str
        The sample name to filter the data.

    Returns
    -------
    plotly.graph_objects.Figure
        A Plotly bar chart object showing KO counts per pathway.

    Raises
    ------
    ValueError
        If required columns are missing, null values exist, or the sample is not found.
    """
    logger.info("Iniciando plotagem de KO por via metabólica para a amostra: %s", selected_sample)

    expected_columns = {'sample', 'pathname', 'unique_ko_count'}
    if not expected_columns.issubset(pathway_count_df.columns):
        missing = expected_columns - set(pathway_count_df.columns)
        logger.error("Colunas ausentes no DataFrame: %s", missing)
        raise ValueError(f"Missing required columns in DataFrame: {missing}")

    if pathway_count_df.empty:
        logger.warning("O DataFrame fornecido está vazio.")
        raise ValueError("Input DataFrame is empty.")

    if pathway_count_df[['sample', 'pathname', 'unique_ko_count']].isnull().any().any():
        logger.warning("Valores nulos detectados nas colunas obrigatórias.")
        raise ValueError("Null values detected in required columns.")

    filtered_df = pathway_count_df[pathway_count_df['sample'] == selected_sample]

    if filtered_df.empty:
        logger.warning("Nenhum dado encontrado para a amostra selecionada: %s", selected_sample)
        raise ValueError(f"No data found for selected sample: {selected_sample}")

    filtered_df = filtered_df.sort_values('unique_ko_count', ascending=False)

    fig = px.bar(
        filtered_df,
        x='pathname',
        y='unique_ko_count',
        title=f'Unique Gene Count for Sample: {selected_sample}',
        text='unique_ko_count',
        template="simple_white"
    )

    fig.update_layout(
        xaxis_title='Pathway',
        yaxis_title='Unique Gene Count',
        xaxis={'categoryorder': 'total descending'},
        xaxis_tickangle=45
    )

    logger.info("Gráfico gerado com sucesso para a amostra: %s", selected_sample)
    return fig


def plot_sample_ko_counts(sample_count_df: pd.DataFrame, selected_pathway: str):
    """
    Creates a bar chart showing the count of unique KOs for a selected metabolic pathway across samples.

    Parameters
    ----------
    sample_count_df : pd.DataFrame
        DataFrame containing KO counts per sample for the selected pathway.
        Expected columns: 'sample', 'unique_ko_count'.

    selected_pathway : str
        The name of the selected metabolic pathway.

    Returns
    -------
    plotly.graph_objects.Figure
        A Plotly bar chart object visualizing KO counts.

    Raises
    ------
    ValueError
        If the DataFrame is empty, contains nulls, or lacks required columns.
    """
    logger.info("Iniciando plotagem de KO por amostra para a via: %s", selected_pathway)

    expected_columns = {'sample', 'unique_ko_count'}
    if not expected_columns.issubset(sample_count_df.columns):
        missing = expected_columns - set(sample_count_df.columns)
        logger.error("Colunas ausentes no DataFrame: %s", missing)
        raise ValueError(f"Missing required columns in DataFrame: {missing}")

    if sample_count_df.empty:
        logger.warning("O DataFrame fornecido está vazio.")
        raise ValueError("The sample count DataFrame is empty.")

    if sample_count_df[['sample', 'unique_ko_count']].isnull().any().any():
        logger.warning("Valores nulos detectados nas colunas 'sample' ou 'unique_ko_count'.")
        raise ValueError("Null values detected in 'sample' or 'unique_ko_count' columns.")

    fig = px.bar(
        sample_count_df,
        x='sample',
        y='unique_ko_count',
        title=f'Unique Gene Count for Pathway: {selected_pathway}',
        text='unique_ko_count',
        template="simple_white"
    )

    fig.update_layout(
        xaxis_title='Sample',
        yaxis_title='Unique Gene Count',
        xaxis={'categoryorder': 'total descending'},
        xaxis_tickangle=45
    )

    logger.info("Gráfico gerado com sucesso para a via metabólica: %s", selected_pathway)
    return fig
