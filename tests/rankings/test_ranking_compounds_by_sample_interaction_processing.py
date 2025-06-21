import pytest
import pandas as pd
from utils.rankings.ranking_compounds_by_sample_interaction_processing import process_compound_ranking

def test_process_compound_ranking_basic(get_mock_ToxCSM):
    """
    Tests basic functionality of process_compound_ranking with ToxCSM mock data.

    Parameters
    ----------
    get_mock_ToxCSM : pd.DataFrame
        Mocked fixture simulating ToxCSM compound data with 'sample' and 'compoundname' columns.

    Returns
    -------
    None
        Asserts that the output DataFrame contains the correct columns and is sorted by 'num_samples'.

    Behavior Verified
    -----------------
    - Correct grouping by 'compoundname'
    - Accurate count of unique 'sample' per compound
    - Output is sorted in descending order of 'num_samples'
    """
    # Setup
    merged_df = get_mock_ToxCSM[["sample", "compoundname"]].copy()

    # Execution
    result = process_compound_ranking(merged_df)

    # Assertion
    assert not result.empty
    assert set(result.columns) == {"compoundname", "num_samples"}
    assert result["num_samples"].is_monotonic_decreasing

def test_process_compound_ranking_missing_columns(get_mock_KEGG):
    """
    Tests that process_compound_ranking raises ValueError if required columns are missing.

    Parameters
    ----------
    get_mock_KEGG : pd.DataFrame
        Mocked fixture simulating KEGG data, which lacks 'compoundname' and 'sample' columns.

    Returns
    -------
    None
        Asserts that ValueError is raised when required columns are missing.

    Behavior Verified
    -----------------
    - Proper error handling for missing columns
    """
    # Setup: KEGG fixture does not have required columns
    merged_df = get_mock_KEGG.copy()

    # Execution & Assertion
    with pytest.raises(ValueError) as excinfo:
        process_compound_ranking(merged_df)
    assert "Missing required columns" in str(excinfo.value)

def test_process_compound_ranking_multiple_samples_per_compound(get_mock_ToxCSM):
    """
    Tests that process_compound_ranking correctly counts unique samples per compound.
    """
    # Setup: Garanta que pelo menos um composto aparece em mais de uma amostra
    df = pd.DataFrame({
        "sample": ["Sample1", "Sample2", "Sample3", "Sample4"],
        "compoundname": ["Phenol", "Phenol", "Naphthalene", "Naphthalene"]
    })

    # Execution
    result = process_compound_ranking(df)

    # Assertion
    assert all(result["num_samples"] >= 1)
    assert result["num_samples"].max() > 1


def test_process_compound_ranking_with_biorempp(get_mock_BioRemPP):
    """
    Tests process_compound_ranking with BioRemPP mock data after renaming columns to match requirements.

    Parameters
    ----------
    get_mock_BioRemPP : pd.DataFrame
        Mocked fixture simulating BioRemPP data.

    Returns
    -------
    None
        Asserts correct output structure and sample counting.

    Behavior Verified
    -----------------
    - Function works with data from other sources if columns are renamed appropriately
    """
    # Setup: Rename columns to match required input
    df = get_mock_BioRemPP.rename(columns={"compound": "compoundname"})
    df = df[["sample", "compoundname"]]

    # Execution
    result = process_compound_ranking(df)

    # Assertion
    assert not result.empty
    assert set(result.columns) == {"compoundname", "num_samples"}
    assert result["num_samples"].is_monotonic_decreasing

def test_process_compound_ranking_empty_input():
    """
    Tests process_compound_ranking with an empty DataFrame.

    Parameters
    ----------
    None

    Returns
    -------
    None
        Asserts that the output is also empty and has correct columns.

    Behavior Verified
    -----------------
    - Graceful handling of empty input
    """
    # Setup
    df = pd.DataFrame(columns=["sample", "compoundname"])

    # Execution
    result = process_compound_ranking(df)

    # Assertion
    assert result.empty
    assert set(result.columns) == {"compoundname", "num_samples"}
