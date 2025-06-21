import pytest
import pandas as pd
from utils.heatmaps.sample_reference_agency_heatmap_processing import process_sample_reference_heatmap

def test_process_sample_reference_heatmap_basic(monkeypatch):
    """
    Test basic functionality of process_sample_reference_heatmap with minimal valid input.

    Parameters
    ----------
    None

    Returns
    -------
    None
        Asserts correct pivot table structure and values for a simple case.

    Purpose
    -------
    Verifies that the function correctly counts unique compounds per sample-referenceAG pair.
    """
    data = {
        'sample': ['S1', 'S1', 'S2', 'S2', 'S2'],
        'referenceAG': ['A', 'A', 'A', 'B', 'B'],
        'compoundname': ['C1', 'C2', 'C1', 'C3', 'C3']
    }
    df = pd.DataFrame(data)
    result = process_sample_reference_heatmap(df)
    assert isinstance(result, pd.DataFrame)
    assert set(result.columns) == {'S1', 'S2'}
    assert set(result.index) == {'A', 'B'}
    assert result.loc['A', 'S1'] == 2  # C1, C2 for S1/A
    assert result.loc['A', 'S2'] == 1  # C1 for S2/A
    assert result.loc['B', 'S2'] == 1  # C3 for S2/B
    assert result.loc['B', 'S1'] == 0  # No S1/B

def test_process_sample_reference_heatmap_missing_columns():
    """
    Test that ValueError is raised if required columns are missing.

    Parameters
    ----------
    None

    Returns
    -------
    None
        Asserts ValueError is raised for missing columns.

    Purpose
    -------
    Ensures robust error handling for incomplete input DataFrames.
    """
    df = pd.DataFrame({'sample': ['S1'], 'referenceAG': ['A']})
    with pytest.raises(ValueError) as excinfo:
        process_sample_reference_heatmap(df)
    assert "missing" in str(excinfo.value).lower()

def test_process_sample_reference_heatmap_empty_dataframe():
    """
    Test processing with an empty DataFrame containing required columns.

    Parameters
    ----------
    None

    Returns
    -------
    None
        Asserts that the result is an empty DataFrame with correct structure.

    Purpose
    -------
    Checks graceful handling of empty input.
    """
    df = pd.DataFrame(columns=['sample', 'referenceAG', 'compoundname'])
    result = process_sample_reference_heatmap(df)
    assert isinstance(result, pd.DataFrame)
    assert result.empty

def test_process_sample_reference_heatmap_duplicate_compounds():
    """
    Test that duplicate compoundnames within the same group are counted only once.

    Parameters
    ----------
    None

    Returns
    -------
    None
        Asserts unique counting of compounds per group.

    Purpose
    -------
    Ensures that only unique compoundnames are counted per sample-referenceAG pair.
    """
    data = {
        'sample': ['S1', 'S1', 'S1'],
        'referenceAG': ['A', 'A', 'A'],
        'compoundname': ['C1', 'C1', 'C2']
    }
    df = pd.DataFrame(data)
    result = process_sample_reference_heatmap(df)
    assert result.loc['A', 'S1'] == 2  # C1 and C2, C1 counted once

def test_process_sample_reference_heatmap_multiple_samples_and_refs():
    """
    Test with multiple samples and referenceAGs, ensuring correct pivoting.

    Parameters
    ----------
    None

    Returns
    -------
    None
        Asserts correct shape and values for a more complex input.

    Purpose
    -------
    Validates function with a realistic, multi-sample/reference scenario.
    """
    data = {
        'sample': ['S1', 'S1', 'S2', 'S2', 'S3', 'S3', 'S3'],
        'referenceAG': ['A', 'B', 'A', 'B', 'A', 'B', 'C'],
        'compoundname': ['C1', 'C2', 'C1', 'C3', 'C4', 'C2', 'C5']
    }
    df = pd.DataFrame(data)
    result = process_sample_reference_heatmap(df)
    assert set(result.columns) == {'S1', 'S2', 'S3'}
    assert set(result.index) == {'A', 'B', 'C'}
    assert result.loc['A', 'S1'] == 1
    assert result.loc['B', 'S1'] == 1
    assert result.loc['A', 'S2'] == 1
    assert result.loc['B', 'S2'] == 1
    assert result.loc['A', 'S3'] == 1
    assert result.loc['B', 'S3'] == 1
    assert result.loc['C', 'S3'] == 1
    assert result.loc['C', 'S1'] == 0
    assert result.loc['C', 'S2'] == 0
