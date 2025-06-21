import pytest
import pandas as pd
from utils.entity_interactions.enzyme_activity_by_sample_processing import count_unique_enzyme_activities

@pytest.fixture
def mock_bioreMPP_enzyme_activity_df(get_mock_BioRemPP):
    """
    Fixture to create a mock DataFrame with columns:
    ['sample', 'ko', 'desc', 'compound', 'enzyme_activity'].
    Adds duplicate and unique KOs for enzyme activities for robust testing.
    """
    df = get_mock_BioRemPP.copy()
    # Add more rows for richer test scenarios
    extra = pd.DataFrame([
        {"sample": "SampleA", "ko": "K00001", "desc": "desc1", "compound": "cmp1", "enzyme_activity": "EA1"},
        {"sample": "SampleA", "ko": "K00002", "desc": "desc2", "compound": "cmp2", "enzyme_activity": "EA1"},
        {"sample": "SampleA", "ko": "K00003", "desc": "desc3", "compound": "cmp3", "enzyme_activity": "EA2"},
        {"sample": "SampleB", "ko": "K00004", "desc": "desc4", "compound": "cmp4", "enzyme_activity": "EA1"},
        {"sample": "SampleB", "ko": "K00005", "desc": "desc5", "compound": "cmp5", "enzyme_activity": "EA3"},
        {"sample": "SampleC", "ko": "K00006", "desc": "desc6", "compound": "cmp6", "enzyme_activity": "EA2"},
    ])
    return pd.concat([df, extra], ignore_index=True)

def test_count_unique_enzyme_activities_basic(mock_bioreMPP_enzyme_activity_df):
    """
    Test that count_unique_enzyme_activities returns correct unique KO counts per enzyme activity
    for a valid sample with multiple enzyme activities.

    Parameters
    ----------
    mock_bioreMPP_enzyme_activity_df : pd.DataFrame
        Mock BioRemPP DataFrame with enzyme_activity, ko, and sample columns.

    Expected
    -------
    DataFrame with 'enzyme_activity' and 'unique_ko_count' columns, sorted descending.
    Verifies correct grouping and counting.
    """
    sample = "SampleA"
    result = count_unique_enzyme_activities(mock_bioreMPP_enzyme_activity_df, sample)
    assert isinstance(result, pd.DataFrame)
    assert set(result.columns) == {"enzyme_activity", "unique_ko_count"}
    # EA1 should have 2 unique KOs, EA2 should have 1 for SampleA
    ea1_count = result[result["enzyme_activity"] == "EA1"]["unique_ko_count"].iloc[0]
    ea2_count = result[result["enzyme_activity"] == "EA2"]["unique_ko_count"].iloc[0]
    assert ea1_count == 2
    assert ea2_count == 1
    # Sorted descending
    assert result["unique_ko_count"].iloc[0] >= result["unique_ko_count"].iloc[-1]

def test_count_unique_enzyme_activities_missing_columns(mock_bioreMPP_enzyme_activity_df):
    """
    Test that ValueError is raised if required columns are missing.

    Parameters
    ----------
    mock_bioreMPP_enzyme_activity_df : pd.DataFrame
        Mock BioRemPP DataFrame.

    Expected
    -------
    Raises ValueError if 'enzyme_activity' or 'ko' or 'sample' is missing.
    """
    df_missing = mock_bioreMPP_enzyme_activity_df.drop(columns=["enzyme_activity"])
    with pytest.raises(ValueError, match="Missing required columns"):
        count_unique_enzyme_activities(df_missing, "SampleA")

def test_count_unique_enzyme_activities_sample_not_found(mock_bioreMPP_enzyme_activity_df):
    """
    Test that ValueError is raised if the sample is not present in the DataFrame.

    Parameters
    ----------
    mock_bioreMPP_enzyme_activity_df : pd.DataFrame
        Mock BioRemPP DataFrame.

    Expected
    -------
    Raises ValueError if the sample is not found.
    """
    with pytest.raises(ValueError, match="Sample 'NonExistentSample' not found in data."):
        count_unique_enzyme_activities(mock_bioreMPP_enzyme_activity_df, "NonExistentSample")

def test_count_unique_enzyme_activities_single_enzyme_activity(mock_bioreMPP_enzyme_activity_df):
    """
    Test correct behavior when only one enzyme activity is present for a sample.

    Parameters
    ----------
    mock_bioreMPP_enzyme_activity_df : pd.DataFrame
        Mock BioRemPP DataFrame.

    Expected
    -------
    DataFrame with a single row for the enzyme activity.
    """
    # Add a sample with only one enzyme activity
    df = mock_bioreMPP_enzyme_activity_df.copy()
    df = pd.concat([df, pd.DataFrame([{
        "sample": "SampleD", "ko": "K99999", "desc": "descX", "compound": "cmpX", "enzyme_activity": "EA_UNIQUE"
    }])], ignore_index=True)
    result = count_unique_enzyme_activities(df, "SampleD")
    assert len(result) == 1
    assert result.iloc[0]["enzyme_activity"] == "EA_UNIQUE"
    assert result.iloc[0]["unique_ko_count"] == 1

def test_count_unique_enzyme_activities_duplicate_kos(mock_bioreMPP_enzyme_activity_df):
    """
    Test that duplicate KOs for the same enzyme activity and sample are counted only once.

    Parameters
    ----------
    mock_bioreMPP_enzyme_activity_df : pd.DataFrame
        Mock BioRemPP DataFrame.

    Expected
    -------
    Each unique KO is counted once per enzyme activity.
    """
    df = mock_bioreMPP_enzyme_activity_df.copy()
    # Add duplicate KO for SampleA, EA1
    df = pd.concat([df, pd.DataFrame([{
        "sample": "SampleA", "ko": "K00001", "desc": "desc1", "compound": "cmp1", "enzyme_activity": "EA1"
    }])], ignore_index=True)
    result = count_unique_enzyme_activities(df, "SampleA")
    # EA1 should still have 2 unique KOs
    ea1_count = result[result["enzyme_activity"] == "EA1"]["unique_ko_count"].iloc[0]
    assert ea1_count == 2
