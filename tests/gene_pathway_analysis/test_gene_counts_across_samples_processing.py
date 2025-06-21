import pytest
import pandas as pd

from utils.gene_pathway_analysis.gene_counts_across_samples_processing import (
    validate_ko_dataframe,
    process_ko_data,
    process_ko_data_violin
)

def test_validate_ko_dataframe_success(get_mock_HADEG):
    """
    Test that validate_ko_dataframe passes with a valid DataFrame.

    Parameters
    ----------
    get_mock_HADEG : fixture
        Provides a mock DataFrame with columns ['sample', 'Gene', 'ko', 'Pathway', 'compound_pathway'].

    Expected
    -------
    No exception is raised if required columns are present.
    Verifies correct validation of DataFrame structure.
    """
    df = get_mock_HADEG
    # Should not raise
    validate_ko_dataframe(df, required_columns=['sample', 'ko'])

def test_validate_ko_dataframe_missing_column(get_mock_HADEG):
    """
    Test that validate_ko_dataframe raises ValueError if required columns are missing.

    Parameters
    ----------
    get_mock_HADEG : fixture
        Provides a mock DataFrame with columns ['sample', 'Gene', 'ko', 'Pathway', 'compound_pathway'].

    Expected
    -------
    ValueError is raised when a required column is missing.
    Verifies error handling for incomplete DataFrames.
    """
    df = get_mock_HADEG.drop(columns=['ko'])
    with pytest.raises(ValueError, match="Missing required columns"):
        validate_ko_dataframe(df, required_columns=['sample', 'ko'])

def test_process_ko_data_with_dataframe(get_mock_BioRemPP):
    """
    Test process_ko_data with a valid DataFrame input.

    Parameters
    ----------
    get_mock_BioRemPP : fixture
        Provides a mock DataFrame with columns ['sample', 'ko', 'desc', 'compound', 'enzyme_activity'].

    Expected
    -------
    Returns a DataFrame with unique KO counts per sample, sorted descending.
    Verifies correct grouping and counting logic.
    """
    df = get_mock_BioRemPP
    result = process_ko_data(df)
    assert isinstance(result, pd.DataFrame)
    assert 'sample' in result.columns and 'ko_count' in result.columns
    # Check sorting order
    assert result['ko_count'].is_monotonic_decreasing

def test_process_ko_data_with_list_of_dicts(get_mock_BioRemPP):
    """
    Test process_ko_data with a list of dictionaries as input.

    Parameters
    ----------
    get_mock_BioRemPP : fixture
        Provides a mock DataFrame; converted to list of dicts for this test.

    Expected
    -------
    Returns a DataFrame with unique KO counts per sample.
    Verifies input flexibility and correct output.
    """
    data = get_mock_BioRemPP.to_dict(orient='records')
    result = process_ko_data(data)
    assert isinstance(result, pd.DataFrame)
    assert 'sample' in result.columns and 'ko_count' in result.columns

def test_process_ko_data_invalid_input_type():
    """
    Test process_ko_data raises ValueError on invalid input type.

    Parameters
    ----------
    None

    Expected
    -------
    ValueError is raised if input is not DataFrame or list of dicts.
    Verifies input validation.
    """
    with pytest.raises(ValueError, match="must be a pandas DataFrame or a list of dictionaries"):
        process_ko_data("invalid_input")

def test_process_ko_data_violin_counts(get_mock_KEGG):
    """
    Test process_ko_data_violin returns correct KO counts per sample.

    Parameters
    ----------
    get_mock_KEGG : fixture
        Provides a mock DataFrame with columns ['sample', 'ko', 'pathname', 'genesymbol'].

    Expected
    -------
    Returns a DataFrame with unique KO counts per sample.
    Verifies grouping and counting for violin plot preparation.
    """
    df = get_mock_KEGG
    result = process_ko_data_violin(df)
    assert isinstance(result, pd.DataFrame)
    assert set(result.columns) == {'sample', 'ko_count'}
    # KO counts should match groupby nunique
    expected = df.groupby('sample')['ko'].nunique().reset_index(name='ko_count')
    pd.testing.assert_frame_equal(result.sort_values('sample').reset_index(drop=True),
                                  expected.sort_values('sample').reset_index(drop=True))

def test_process_ko_data_violin_missing_column(get_mock_KEGG):
    """
    Test process_ko_data_violin raises ValueError if required columns are missing.

    Parameters
    ----------
    get_mock_KEGG : fixture
        Provides a mock DataFrame with columns ['sample', 'ko', 'pathname', 'genesymbol'].

    Expected
    -------
    ValueError is raised when a required column is missing.
    Verifies error handling for incomplete DataFrames.
    """
    df = get_mock_KEGG.drop(columns=['ko'])
    with pytest.raises(ValueError, match="Missing required columns"):
        process_ko_data_violin(df)
