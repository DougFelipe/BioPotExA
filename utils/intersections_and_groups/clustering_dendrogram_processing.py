import numpy as np
import pandas as pd
import scipy.spatial.distance as ssd
import scipy.cluster.hierarchy as sch
import logging

# Configuração básica de logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def calculate_sample_clustering(input_df: pd.DataFrame, distance_metric: str, method: str) -> np.ndarray:
    """
    Calculates a hierarchical clustering matrix based on sample-by-KO data.

    Parameters
    ----------
    input_df : pd.DataFrame
        DataFrame containing at least the columns 'sample' and 'ko'.
    distance_metric : str
        The distance metric to use (e.g., 'euclidean', 'cityblock').
    method : str
        The hierarchical clustering method to use (e.g., 'single', 'ward').

    Returns
    -------
    np.ndarray
        The linkage matrix representing hierarchical clustering.

    Raises
    ------
    ValueError
        If required columns are missing or input data is insufficient.
    Exception
        For unexpected errors during distance or clustering computation.
    """
    required_columns = {'sample', 'ko'}
    logger.info("Starting clustering with metric: %s and method: %s", distance_metric, method)

    # Verificação de colunas obrigatórias
    if not required_columns.issubset(input_df.columns):
        missing = required_columns - set(input_df.columns)
        logger.error("Missing required columns: %s", missing)
        raise ValueError(f"Missing required columns in input data: {missing}")

    try:
        # Pivot da tabela para obter matriz amostra vs KO
        pivot_df = input_df.pivot_table(
            index='sample',
            columns='ko',
            aggfunc='size',
            fill_value=0
        )

        if pivot_df.shape[0] < 2:
            logger.warning("Not enough samples for clustering (need at least 2, got %d)", pivot_df.shape[0])
            raise ValueError("At least two samples are required for clustering.")

        # Cálculo da matriz de distâncias
        distance_matrix = ssd.pdist(pivot_df, metric=distance_metric)

        # Clustering hierárquico
        clustering_matrix = sch.linkage(distance_matrix, method=method)

        logger.info("Clustering completed successfully.")
        return clustering_matrix

    except Exception as e:
        logger.exception("Unexpected error during clustering calculation.")
        raise Exception(f"An error occurred while calculating clustering: {e}")
