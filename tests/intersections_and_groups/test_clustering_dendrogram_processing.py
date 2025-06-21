import pytest
import pandas as pd
import numpy as np
from utils.intersections_and_groups import clustering_dendrogram_processing as cdp

@pytest.fixture
def minimal_input_df():
    """Fixture providing a minimal valid DataFrame for clustering.

    Returns
    -------
    pd.DataFrame
        DataFrame with 'sample' and 'ko' columns, two samples, two KOs.
    """
    return pd.DataFrame({
        'sample': ['S1', 'S1', 'S2', 'S2'],
        'ko': ['K001', 'K002', 'K001', 'K003']
    })

@pytest.fixture
def single_sample_df():
    """Fixture providing a DataFrame with only one sample.

    Returns
    -------
    pd.DataFrame
        DataFrame with 'sample' and 'ko' columns, only one sample.
    """
    return pd.DataFrame({
        'sample': ['S1', 'S1'],
        'ko': ['K001', 'K002']
    })

@pytest.fixture
def missing_column_df():
    """Fixture providing a DataFrame missing the 'ko' column.

    Returns
    -------
    pd.DataFrame
        DataFrame missing required 'ko' column.
    """
    return pd.DataFrame({
        'sample': ['S1', 'S2'],
        'not_ko': ['K001', 'K002']
    })

def test_calculate_sample_clustering_basic(minimal_input_df):
    """
    Test basic hierarchical clustering with valid minimal input.

    Parameters
    ----------
    minimal_input_df : pd.DataFrame
        Minimal valid DataFrame with two samples and two KOs.

    Returns
    -------
    None
        Asserts that the linkage matrix is returned and has correct shape.
    """
    cdp.clear_distance_cache()
    linkage = cdp.calculate_sample_clustering(
        minimal_input_df, distance_metric='euclidean', method='single'
    )
    assert isinstance(linkage, np.ndarray)
    # For 2 samples, linkage should have shape (n-1, 4)
    assert linkage.shape == (1, 4)

def test_calculate_sample_clustering_cache(minimal_input_df):
    """
    Test that distance matrix caching works as expected.

    Parameters
    ----------
    minimal_input_df : pd.DataFrame
        Minimal valid DataFrame for clustering.

    Returns
    -------
    None
        Asserts that repeated calls use the cache (check via log or internal state).
    """
    cdp.clear_distance_cache()
    # First call: should compute and cache
    _ = cdp.calculate_sample_clustering(minimal_input_df, 'euclidean', 'single')
    # Second call: should hit cache (no error, same result)
    _ = cdp.calculate_sample_clustering(minimal_input_df, 'euclidean', 'single')
    # There should be only one entry in the cache
    assert len(cdp._distance_cache) == 1

def test_calculate_sample_clustering_different_metric(minimal_input_df):
    """
    Test clustering with a different distance metric.

    Parameters
    ----------
    minimal_input_df : pd.DataFrame
        Minimal valid DataFrame for clustering.

    Returns
    -------
    None
        Asserts that clustering works with 'cityblock' metric.
    """
    cdp.clear_distance_cache()
    linkage = cdp.calculate_sample_clustering(
        minimal_input_df, distance_metric='cityblock', method='single'
    )
    assert isinstance(linkage, np.ndarray)
    assert linkage.shape == (1, 4)

def test_calculate_sample_clustering_missing_column(missing_column_df):
    """
    Test error handling when required columns are missing.

    Parameters
    ----------
    missing_column_df : pd.DataFrame
        DataFrame missing the 'ko' column.

    Returns
    -------
    None
        Asserts that ValueError is raised for missing columns.
    """
    cdp.clear_distance_cache()
    with pytest.raises(ValueError) as excinfo:
        cdp.calculate_sample_clustering(missing_column_df, 'euclidean', 'single')
    assert "Missing required columns" in str(excinfo.value)

def test_calculate_sample_clustering_single_sample(single_sample_df):
    """
    Test error handling when only one sample is present.

    Parameters
    ----------
    single_sample_df : pd.DataFrame
        DataFrame with only one sample.

    Returns
    -------
    None
        Asserts that ValueError is raised for insufficient samples.
    """
    cdp.clear_distance_cache()
    with pytest.raises(ValueError) as excinfo:
        cdp.calculate_sample_clustering(single_sample_df, 'euclidean', 'single')
    assert "At least two samples are required for clustering." in str(excinfo.value)

def test_clear_distance_cache(minimal_input_df):
    """
    Test that the cache clearing function works.

    Parameters
    ----------
    minimal_input_df : pd.DataFrame
        Minimal valid DataFrame for clustering.

    Returns
    -------
    None
        Asserts that the cache is empty after clearing.
    """
    cdp.clear_distance_cache()
    _ = cdp.calculate_sample_clustering(minimal_input_df, 'euclidean', 'single')
    assert len(cdp._distance_cache) == 1
    cdp.clear_distance_cache()
    assert len(cdp._distance_cache) == 0

def test_cache_eviction_policy(minimal_input_df):
    """
    Test that the cache evicts the oldest entry when exceeding size limit.

    Parameters
    ----------
    minimal_input_df : pd.DataFrame
        Minimal valid DataFrame for clustering.

    Returns
    -------
    None
        Asserts that cache size does not exceed 10.
    """
    cdp.clear_distance_cache()
    # Generate 11 unique DataFrames by changing column names
    for i in range(11):
        df = minimal_input_df.copy()
        df['ko'] = df['ko'] + str(i)
        cdp.calculate_sample_clustering(df, 'euclidean', 'single')
    assert len(cdp._distance_cache) == 10
