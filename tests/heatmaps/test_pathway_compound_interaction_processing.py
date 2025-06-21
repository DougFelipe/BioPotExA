import pytest
import pandas as pd
from utils.heatmaps.pathway_compound_interaction_processing import process_pathway_data

def test_process_pathway_data_basic_grouping():
    """
    Tests basic grouping and KO counting functionality.

    Parameters
    ----------
    None

    Returns
    -------
    None
        Asserts correct KO counts per group.
    """
    data = {
        'Pathway': ['A', 'A', 'A', 'B', 'B'],
        'compound_pathway': ['cp1', 'cp1', 'cp2', 'cp1', 'cp1'],
        'sample': ['s1', 's1', 's2', 's1', 's1'],
        'ko': ['K1', 'K2', 'K1', 'K1', 'K1']
    }
    df = pd.DataFrame(data)
    result = process_pathway_data(df)
    assert set(result.columns) == {'Pathway', 'compound_pathway', 'sample', 'ko_count'}
    assert result.loc[(result['Pathway'] == 'A') & (result['compound_pathway'] == 'cp1') & (result['sample'] == 's1'), 'ko_count'].iloc[0] == 2
    assert result.loc[(result['Pathway'] == 'A') & (result['compound_pathway'] == 'cp2') & (result['sample'] == 's2'), 'ko_count'].iloc[0] == 1

def test_process_pathway_data_missing_columns():
    """
    Tests that ValueError is raised if required columns are missing.

    Parameters
    ----------
    None

    Returns
    -------
    None
        Asserts ValueError is raised for missing columns.
    """
    df = pd.DataFrame({'Pathway': ['A'], 'compound_pathway': ['cp1'], 'sample': ['s1']})
    with pytest.raises(ValueError) as excinfo:
        process_pathway_data(df)
    assert "Missing columns" in str(excinfo.value)

def test_process_pathway_data_empty_input():
    """
    Tests that an empty DataFrame returns an empty grouped DataFrame.

    Parameters
    ----------
    None

    Returns
    -------
    None
        Asserts output DataFrame is empty.
    """
    df = pd.DataFrame(columns=['Pathway', 'compound_pathway', 'sample', 'ko'])
    result = process_pathway_data(df)
    assert result.empty
    assert set(result.columns) == {'Pathway', 'compound_pathway', 'sample', 'ko_count'}

def test_process_pathway_data_single_group(get_mock_KEGG):
    """
    Tests grouping when all rows belong to a single group.

    Parameters
    ----------
    get_mock_KEGG : pd.DataFrame
        Mocked KEGG fixture with columns including 'Pathway', 'compound_pathway', 'sample', 'ko'.

    Returns
    -------
    None
        Asserts correct KO count for a single group.
    """
    # Simulate all rows in one group, but with duplicate KOs
    df = pd.DataFrame({
        'Pathway': ['P1', 'P1', 'P1'],
        'compound_pathway': ['cpX', 'cpX', 'cpX'],
        'sample': ['sA', 'sA', 'sA'],
        'ko': ['K1', 'K1', 'K2']
    })
    result = process_pathway_data(df)
    assert len(result) == 1
    assert result['ko_count'].iloc[0] == 2

def test_process_pathway_data_with_realistic_fixture(get_mock_HADEG):
    """
    Tests grouping and KO counting using a realistic fixture.

    Parameters
    ----------
    get_mock_HADEG : pd.DataFrame
        Mocked HADEG fixture with columns 'Pathway', 'compound_pathway', 'sample', 'ko'.

    Returns
    -------
    None
        Asserts correct grouping and KO counting.
    """
    # Ensure fixture has required columns, or adapt as needed
    df = get_mock_HADEG.copy()
    required = {'Pathway', 'compound_pathway', 'sample', 'ko'}
    if not required.issubset(df.columns):
        # Add dummy columns for test if missing
        for col in required - set(df.columns):
            df[col] = 'dummy'
    result = process_pathway_data(df)
    assert set(result.columns) == {'Pathway', 'compound_pathway', 'sample', 'ko_count'}
    assert all(result['ko_count'] >= 1)

def test_process_pathway_data_multiple_samples(get_mock_BioRemPP):
    """
    Tests grouping and KO counting across multiple samples.

    Parameters
    ----------
    get_mock_BioRemPP : pd.DataFrame
        Mocked BioRemPP fixture with columns 'Pathway', 'compound_pathway', 'sample', 'ko'.

    Returns
    -------
    None
        Asserts correct KO counts for each sample group.
    """
    df = get_mock_BioRemPP.copy()
    required = {'Pathway', 'compound_pathway', 'sample', 'ko'}
    if not required.issubset(df.columns):
        for col in required - set(df.columns):
            df[col] = 'dummy'
    # Add a second sample for testing
    df2 = df.copy()
    df2['sample'] = 'sample2'
    df = pd.concat([df, df2], ignore_index=True)
    result = process_pathway_data(df)
    assert result['sample'].nunique() >= 2
    assert all(result['ko_count'] >= 1)
