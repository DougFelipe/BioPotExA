import pytest
import pandas as pd
from utils.intersections_and_groups.sample_grouping_by_compound_class_processing import group_by_class, minimize_groups

@pytest.fixture
def mock_compound_table():
    """
    Provides a mock DataFrame simulating compound class, sample, and compoundname structure.

    Returns
    -------
    pd.DataFrame
        DataFrame with columns: 'compoundclass', 'sample', 'compoundname'
    """
    data = [
        {'compoundclass': 'Alkaloid', 'sample': 'S1', 'compoundname': 'Caffeine'},
        {'compoundclass': 'Alkaloid', 'sample': 'S1', 'compoundname': 'Theobromine'},
        {'compoundclass': 'Alkaloid', 'sample': 'S2', 'compoundname': 'Caffeine'},
        {'compoundclass': 'Alkaloid', 'sample': 'S2', 'compoundname': 'Theobromine'},
        {'compoundclass': 'Alkaloid', 'sample': 'S3', 'compoundname': 'Nicotine'},
        {'compoundclass': 'Alkaloid', 'sample': 'S4', 'compoundname': 'Caffeine'},
        {'compoundclass': 'Alkaloid', 'sample': 'S4', 'compoundname': 'Theobromine'},
        {'compoundclass': 'Alkaloid', 'sample': 'S4', 'compoundname': 'Nicotine'},
        {'compoundclass': 'Terpene', 'sample': 'S5', 'compoundname': 'Limonene'},
        {'compoundclass': 'Terpene', 'sample': 'S6', 'compoundname': 'Limonene'},
        {'compoundclass': 'Terpene', 'sample': 'S6', 'compoundname': 'Pinene'},
    ]
    return pd.DataFrame(data)

def test_group_by_class_basic_grouping(mock_compound_table):
    """
    Tests group_by_class for correct grouping of samples by compound profile.

    Parameters
    ----------
    mock_compound_table : pd.DataFrame
        Fixture providing mock compound data.

    Returns
    -------
    None
        Asserts correct group labeling and group count.
    """
    result = group_by_class('Alkaloid', mock_compound_table)
    assert not result.empty
    assert 'grupo' in result.columns
    # S1 and S2 have same compounds, should be in same group
    group_labels = result[result['sample'].isin(['S1', 'S2'])]['grupo'].unique()
    assert len(group_labels) == 1
    # S3 has unique compound, should be in its own group
    s3_group = result[result['sample'] == 'S3']['grupo'].unique()
    assert len(s3_group) == 1
    assert s3_group[0] != group_labels[0]
    # S4 has all three compounds, should be a separate group
    s4_group = result[result['sample'] == 'S4']['grupo'].unique()
    assert len(s4_group) == 1
    assert s4_group[0] not in [group_labels[0], s3_group[0]]

def test_group_by_class_missing_column_raises(mock_compound_table):
    """
    Tests group_by_class raises ValueError if required columns are missing.

    Parameters
    ----------
    mock_compound_table : pd.DataFrame
        Fixture providing mock compound data.

    Returns
    -------
    None
        Asserts ValueError is raised for missing columns.
    """
    df_missing = mock_compound_table.drop(columns=['compoundclass'])
    with pytest.raises(ValueError, match="Missing required columns"):
        group_by_class('Alkaloid', df_missing)

def test_group_by_class_no_data_for_class_raises(mock_compound_table):
    """
    Tests group_by_class raises ValueError if no data for given compound class.

    Parameters
    ----------
    mock_compound_table : pd.DataFrame
        Fixture providing mock compound data.

    Returns
    -------
    None
        Asserts ValueError is raised for empty selection.
    """
    with pytest.raises(ValueError, match="No data found for compound class"):
        group_by_class('NonexistentClass', mock_compound_table)

def test_minimize_groups_basic_coverage(mock_compound_table):
    """
    Tests minimize_groups selects minimal groups to cover all compounds.

    Parameters
    ----------
    mock_compound_table : pd.DataFrame
        Fixture providing mock compound data.

    Returns
    -------
    None
        Asserts that all unique compounds are covered by selected groups.
    """
    grouped = group_by_class('Alkaloid', mock_compound_table)
    selected = minimize_groups(grouped)
    # Collect all compounds covered by selected groups
    covered = set()
    for label in selected:
        covered |= set(grouped[grouped['grupo'] == label]['compoundname'].unique())
    all_compounds = set(grouped['compoundname'].unique())
    assert covered == all_compounds
    # Should use minimal number of groups (greedy set cover)
    assert len(selected) <= grouped['grupo'].nunique()

def test_minimize_groups_missing_column_raises(mock_compound_table):
    """
    Tests minimize_groups raises ValueError if required columns are missing.

    Parameters
    ----------
    mock_compound_table : pd.DataFrame
        Fixture providing mock compound data.

    Returns
    -------
    None
        Asserts ValueError is raised for missing columns.
    """
    grouped = group_by_class('Alkaloid', mock_compound_table)
    df_missing = grouped.drop(columns=['grupo'])
    with pytest.raises(ValueError, match="Missing required columns"):
        minimize_groups(df_missing)

def test_minimize_groups_empty_dataframe_raises():
    """
    Tests minimize_groups raises ValueError on empty DataFrame.

    Returns
    -------
    None
        Asserts ValueError is raised for empty input.
    """
    df = pd.DataFrame(columns=['grupo', 'compoundname'])
    with pytest.raises(ValueError, match="Input DataFrame is empty"):
        minimize_groups(df)

def test_group_by_class_multiple_classes(mock_compound_table):
    """
    Tests group_by_class can handle multiple compound classes.

    Parameters
    ----------
    mock_compound_table : pd.DataFrame
        Fixture providing mock compound data.

    Returns
    -------
    None
        Asserts correct grouping for different classes.
    """
    result_alkaloid = group_by_class('Alkaloid', mock_compound_table)
    result_terpene = group_by_class('Terpene', mock_compound_table)
    assert set(result_alkaloid['compoundclass'].unique()) == {'Alkaloid'}
    assert set(result_terpene['compoundclass'].unique()) == {'Terpene'}
    assert 'grupo' in result_alkaloid.columns
    assert 'grupo' in result_terpene.columns
    # Terpene: S5 and S6 have different compound sets, so should be in different groups
    terpene_groups = result_terpene.groupby('grupo')['sample'].nunique()
    assert terpene_groups.sum() == 2
