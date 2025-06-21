import pytest
import pandas as pd
from utils.rankings.ranking_samples_by_compound_interaction_processing import process_sample_ranking

def test_process_sample_ranking_valid_toxcsm(get_mock_ToxCSM):
    """
    Test process_sample_ranking with a valid ToxCSM mock DataFrame.

    Parameters
    ----------
    get_mock_ToxCSM : pd.DataFrame
        Mocked fixture simulating ToxCSM compound data, including 'sample' and 'compoundname'.

    Returns
    -------
    None
        Asserts that the output DataFrame is ranked and contains correct columns.

    Verifies
    --------
    - Correct counting of unique compounds per sample.
    - Output DataFrame structure and sorting.
    """
    # Setup
    df = get_mock_ToxCSM[['sample', 'compoundname']].copy()
    # Execution
    ranked = process_sample_ranking(df)
    # Assertion
    assert isinstance(ranked, pd.DataFrame)
    assert set(ranked.columns) == {'sample', 'num_compounds'}
    assert ranked['num_compounds'].is_monotonic_decreasing

def test_process_sample_ranking_missing_columns(get_mock_HADEG):
    """
    Test process_sample_ranking raises ValueError if required columns are missing.

    Parameters
    ----------
    get_mock_HADEG : pd.DataFrame
        Mocked fixture simulating HADEG data, missing 'compoundname'.

    Returns
    -------
    None
        Asserts that ValueError is raised for missing columns.

    Verifies
    --------
    - Proper error handling for missing required columns.
    """
    # Setup: Remove 'compoundname' column
    df = get_mock_HADEG[['sample']].copy()
    # Execution & Assertion
    with pytest.raises(ValueError, match="Missing required columns"):
        process_sample_ranking(df)

def test_process_sample_ranking_invalid_input_type():
    """
    Test process_sample_ranking raises ValueError for non-DataFrame input.

    Parameters
    ----------
    None

    Returns
    -------
    None
        Asserts that ValueError is raised for invalid input type.

    Verifies
    --------
    - Type checking for input parameter.
    """
    # Setup: Use a list instead of DataFrame
    invalid_input = [{'sample': 'A', 'compoundname': 'Benzene'}]
    # Execution & Assertion
    with pytest.raises(ValueError, match="Input must be a pandas DataFrame"):
        process_sample_ranking(invalid_input)

def test_process_sample_ranking_multiple_samples(get_mock_ToxCSM):
    """
    Test process_sample_ranking with multiple samples and overlapping compounds.

    Parameters
    ----------
    get_mock_ToxCSM : pd.DataFrame
        Mocked fixture simulating ToxCSM data with multiple samples.

    Returns
    -------
    None
        Asserts correct unique compound counts per sample.

    Verifies
    --------
    - Accurate grouping and counting of unique compounds per sample.
    """
    # Setup: Duplicate some compounds across samples
    df = get_mock_ToxCSM[['sample', 'compoundname']].copy()
    df = pd.concat([df, pd.DataFrame({'sample': ['SampleX', 'SampleX'], 'compoundname': ['Benzene', 'Toluene']})])
    # Execution
    ranked = process_sample_ranking(df)
    # Assertion
    assert 'SampleX' in ranked['sample'].values
    assert ranked.loc[ranked['sample'] == 'SampleX', 'num_compounds'].values[0] == 2

def test_process_sample_ranking_empty_dataframe():
    """
    Test process_sample_ranking with an empty DataFrame.

    Parameters
    ----------
    None

    Returns
    -------
    None
        Asserts that the output is an empty DataFrame with correct columns.

    Verifies
    --------
    - Graceful handling of empty input.
    """
    # Setup: Empty DataFrame with required columns
    df = pd.DataFrame(columns=['sample', 'compoundname'])
    # Execution
    ranked = process_sample_ranking(df)
    # Assertion
    assert ranked.empty
    assert set(ranked.columns) == {'sample', 'num_compounds'}
