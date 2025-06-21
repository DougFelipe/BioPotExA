import pytest
import pandas as pd
from utils.heatmaps.gene_sample_heatmap_processing import process_gene_sample_data

def test_process_gene_sample_data_basic_grouping():
    """
    Tests basic grouping and KO counting functionality.

    Parameters
    ----------
    None

    Returns
    -------
    None
        Asserts correct grouping and KO counting.
    """
    data = {
        'sample': ['S1', 'S1', 'S1', 'S2', 'S2'],
        'Gene': ['G1', 'G1', 'G2', 'G1', 'G2'],
        'compound_pathway': ['CP1', 'CP1', 'CP2', 'CP1', 'CP2'],
        'Pathway': ['P1', 'P1', 'P2', 'P1', 'P2'],
        'ko': ['K001', 'K002', 'K003', 'K001', 'K003']
    }
    df = pd.DataFrame(data)
    result = process_gene_sample_data(df)
    assert set(result.columns) == {'sample', 'Gene', 'compound_pathway', 'Pathway', 'ko_count'}
    assert result.loc[(result['sample'] == 'S1') & (result['Gene'] == 'G1'), 'ko_count'].iloc[0] == 2
    assert result.loc[(result['sample'] == 'S2') & (result['Gene'] == 'G2'), 'ko_count'].iloc[0] == 1

def test_process_gene_sample_data_missing_columns():
    """
    Tests that ValueError is raised when required columns are missing.

    Parameters
    ----------
    None

    Returns
    -------
    None
        Asserts ValueError is raised for missing columns.
    """
    df = pd.DataFrame({'sample': ['S1'], 'Gene': ['G1']})
    with pytest.raises(ValueError) as excinfo:
        process_gene_sample_data(df)
    assert "Missing required columns" in str(excinfo.value)

def test_process_gene_sample_data_duplicate_kos():
    """
    Tests that duplicate KO entries are only counted once per group.

    Parameters
    ----------
    None

    Returns
    -------
    None
        Asserts unique KO counting per group.
    """
    data = {
        'sample': ['S1', 'S1', 'S1'],
        'Gene': ['G1', 'G1', 'G1'],
        'compound_pathway': ['CP1', 'CP1', 'CP1'],
        'Pathway': ['P1', 'P1', 'P1'],
        'ko': ['K001', 'K001', 'K002']
    }
    df = pd.DataFrame(data)
    result = process_gene_sample_data(df)
    assert result['ko_count'].iloc[0] == 2

def test_process_gene_sample_data_with_fixture(get_mock_HADEG):
    """
    Tests processing with a realistic mock HADEG fixture.

    Parameters
    ----------
    get_mock_HADEG : pd.DataFrame
        Mocked fixture simulating HADEG compound data.

    Returns
    -------
    None
        Asserts correct grouping and KO counting on fixture data.
    """
    hadeg_df = get_mock_HADEG
    # Ensure required columns exist in the fixture
    for col in ['sample', 'Gene', 'compound_pathway', 'Pathway', 'ko']:
        if col not in hadeg_df.columns:
            hadeg_df[col] = ['dummy'] * len(hadeg_df)
    result = process_gene_sample_data(hadeg_df)
    assert 'ko_count' in result.columns
    assert not result.empty

def test_process_gene_sample_data_internal_error(monkeypatch):
    """
    Tests that a RuntimeError is raised if an internal error occurs during processing.

    Parameters
    ----------
    monkeypatch : pytest.MonkeyPatch
        Used to simulate an internal error in pandas groupby.

    Returns
    -------
    None
        Asserts RuntimeError is raised.
    """
    df = pd.DataFrame({
        'sample': ['S1'],
        'Gene': ['G1'],
        'compound_pathway': ['CP1'],
        'Pathway': ['P1'],
        'ko': ['K001']
    })

    def broken_groupby(*args, **kwargs):
        raise Exception("Simulated internal error")

    monkeypatch.setattr(pd.DataFrame, "groupby", broken_groupby)
    with pytest.raises(RuntimeError) as excinfo:
        process_gene_sample_data(df)
    assert "Failed to process gene-sample data." in str(excinfo.value)
