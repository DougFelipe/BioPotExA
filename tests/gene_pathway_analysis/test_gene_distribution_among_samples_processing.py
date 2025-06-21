import pytest
import pandas as pd
from utils.gene_pathway_analysis.gene_distribution_among_samples_processing import get_ko_per_sample_for_pathway

@pytest.mark.usefixtures("get_mock_KEGG")
def test_get_ko_per_sample_for_pathway_basic(get_mock_KEGG):
    """
    Test that get_ko_per_sample_for_pathway returns correct unique (sample, genesymbol) pairs
    for a valid pathway present in the mock KEGG DataFrame.

    Parameters
    ----------
    get_mock_KEGG : fixture
        Provides a mock DataFrame with columns ['sample', 'ko', 'pathname', 'genesymbol'].

    Expected
    -------
    The returned DataFrame contains only rows where 'pathname' matches the selected pathway,
    with unique (sample, genesymbol) pairs.
    """
    selected_pathway = get_mock_KEGG['pathname'].iloc[0]
    result = get_ko_per_sample_for_pathway(get_mock_KEGG, selected_pathway)
    assert not result.empty
    assert set(result.columns) == {'sample', 'genesymbol'}
    assert all(get_mock_KEGG[get_mock_KEGG['pathname'] == selected_pathway]['genesymbol'].isin(result['genesymbol']))
    assert result.drop_duplicates().shape[0] == result.shape[0]


def test_get_ko_per_sample_for_pathway_no_match(get_mock_KEGG):
    """
    Test that get_ko_per_sample_for_pathway returns an empty DataFrame when the selected pathway
    does not exist in the input DataFrame.

    Parameters
    ----------
    get_mock_KEGG : fixture
        Provides a mock DataFrame with columns ['sample', 'ko', 'pathname', 'genesymbol'].

    Expected
    -------
    The returned DataFrame is empty with columns ['sample', 'genesymbol'].
    """
    result = get_ko_per_sample_for_pathway(get_mock_KEGG, "nonexistent_pathway")
    assert isinstance(result, pd.DataFrame)
    assert result.empty
    assert list(result.columns) == ['sample', 'genesymbol']


def test_get_ko_per_sample_for_pathway_missing_columns(get_mock_KEGG):
    """
    Test that get_ko_per_sample_for_pathway raises ValueError if required columns are missing.

    Parameters
    ----------
    get_mock_KEGG : fixture
        Provides a mock DataFrame with columns ['sample', 'ko', 'pathname', 'genesymbol'].

    Expected
    -------
    ValueError is raised if any of ['sample', 'genesymbol', 'pathname'] are missing.
    """
    df_missing = get_mock_KEGG.drop(columns=['genesymbol'])
    with pytest.raises(ValueError) as excinfo:
        get_ko_per_sample_for_pathway(df_missing, "any_pathway")
    assert "Missing required columns" in str(excinfo.value)


def test_get_ko_per_sample_for_pathway_duplicates_removed(get_mock_KEGG):
    """
    Test that get_ko_per_sample_for_pathway removes duplicate (sample, genesymbol) pairs.

    Parameters
    ----------
    get_mock_KEGG : fixture
        Provides a mock DataFrame with columns ['sample', 'ko', 'pathname', 'genesymbol'].

    Expected
    -------
    The returned DataFrame contains only unique (sample, genesymbol) pairs for the selected pathway.
    """
    # Add duplicate row for testing
    selected_pathway = get_mock_KEGG['pathname'].iloc[0]
    duplicate_row = get_mock_KEGG[get_mock_KEGG['pathname'] == selected_pathway].iloc[0]
    df_with_duplicate = pd.concat([get_mock_KEGG, pd.DataFrame([duplicate_row])], ignore_index=True)
    result = get_ko_per_sample_for_pathway(df_with_duplicate, selected_pathway)
    assert result.duplicated().sum() == 0


def test_get_ko_per_sample_for_pathway_empty_input():
    """
    Test that get_ko_per_sample_for_pathway returns an empty DataFrame when input is empty.

    Parameters
    ----------
    None (creates empty DataFrame with required columns)

    Expected
    -------
    The returned DataFrame is empty with columns ['sample', 'genesymbol'].
    """
    empty_df = pd.DataFrame(columns=['sample', 'ko', 'pathname', 'genesymbol'])
    result = get_ko_per_sample_for_pathway(empty_df, "any_pathway")
    assert isinstance(result, pd.DataFrame)
    assert result.empty
    assert list(result.columns) == ['sample', 'genesymbol']
