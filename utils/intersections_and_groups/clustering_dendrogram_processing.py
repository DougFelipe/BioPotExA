import hashlib  
import pickle  
from functools import lru_cache  
from typing import Tuple, Optional  
import numpy as np  
import pandas as pd  
import scipy.spatial.distance as ssd  
import scipy.cluster.hierarchy as sch  
import logging  
  
# Configuração básica de logging  
logging.basicConfig(level=logging.INFO)  
logger = logging.getLogger(__name__)  
  
# Cache global para matrizes de distância  
_distance_cache = {}  
  
def _generate_data_hash(pivot_df: pd.DataFrame) -> str:  
    """  
    Gera um hash único para os dados de entrada para uso como chave de cache.  
      
    Parameters  
    ----------  
    pivot_df : pd.DataFrame  
        DataFrame pivotado com amostras vs KO  
          
    Returns  
    -------  
    str  
        Hash MD5 dos dados  
    """  
    # Serializar o DataFrame de forma determinística  
    data_string = f"{pivot_df.shape}_{pivot_df.values.tobytes()}_{list(pivot_df.index)}_{list(pivot_df.columns)}"  
    return hashlib.md5(data_string.encode()).hexdigest()  
  
def _get_cached_distance_matrix(pivot_df: pd.DataFrame, distance_metric: str) -> Optional[np.ndarray]:  
    """  
    Recupera matriz de distância do cache se disponível.  
      
    Parameters  
    ----------  
    pivot_df : pd.DataFrame  
        DataFrame pivotado  
    distance_metric : str  
        Métrica de distância utilizada  
          
    Returns  
    -------  
    Optional[np.ndarray]  
        Matriz de distância cached ou None se não encontrada  
    """  
    data_hash = _generate_data_hash(pivot_df)  
    cache_key = f"{data_hash}_{distance_metric}"  
      
    if cache_key in _distance_cache:  
        logger.info("Cache hit for distance matrix with metric: %s", distance_metric)  
        return _distance_cache[cache_key]  
      
    logger.info("Cache miss for distance matrix with metric: %s", distance_metric)  
    return None  
  
def _cache_distance_matrix(pivot_df: pd.DataFrame, distance_metric: str, distance_matrix: np.ndarray) -> None:  
    """  
    Armazena matriz de distância no cache.  
      
    Parameters  
    ----------  
    pivot_df : pd.DataFrame  
        DataFrame pivotado  
    distance_metric : str  
        Métrica de distância utilizada  
    distance_matrix : np.ndarray  
        Matriz de distância calculada  
    """  
    data_hash = _generate_data_hash(pivot_df)  
    cache_key = f"{data_hash}_{distance_metric}"  
      
    # Limitar tamanho do cache (manter apenas 10 entradas mais recentes)  
    if len(_distance_cache) >= 10:  
        # Remove a entrada mais antiga  
        oldest_key = next(iter(_distance_cache))  
        del _distance_cache[oldest_key]  
        logger.info("Cache size limit reached, removed oldest entry")  
      
    _distance_cache[cache_key] = distance_matrix.copy()  
    logger.info("Cached distance matrix for metric: %s", distance_metric)  
  
def clear_distance_cache() -> None:  
    """  
    Limpa o cache de matrizes de distância.  
    """  
    global _distance_cache  
    _distance_cache.clear()  
    logger.info("Distance matrix cache cleared")  
  
def calculate_sample_clustering(input_df: pd.DataFrame, distance_metric: str, method: str) -> np.ndarray:  
    """  
    Calculates a hierarchical clustering matrix based on sample-by-KO data with caching optimization.  
  
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
  
        # Tentar recuperar matriz de distância do cache  
        distance_matrix = _get_cached_distance_matrix(pivot_df, distance_metric)  
          
        if distance_matrix is None:  
            # Calcular nova matriz de distância  
            logger.info("Computing new distance matrix with metric: %s", distance_metric)  
            distance_matrix = ssd.pdist(pivot_df, metric=distance_metric)  
              
            # Armazenar no cache  
            _cache_distance_matrix(pivot_df, distance_metric, distance_matrix)  
          
        # Clustering hierárquico (sempre recalculado pois é rápido)  
        clustering_matrix = sch.linkage(distance_matrix, method=method)  
  
        logger.info("Clustering completed successfully.")  
        return clustering_matrix  
  
    except Exception as e:  
        logger.exception("Unexpected error during clustering calculation.")  
        raise Exception(f"An error occurred while calculating clustering: {e}")
