"""
test_intersection_analysis.py: Unit tests for intersection analysis data preparation.

This script validates the behavior of the `prepare_upsetplot_data` function, ensuring it processes input DataFrames for UpSet plot visualization correctly. The tests cover a range of scenarios, including valid and invalid inputs, empty and partial selections, and error handling for missing columns or incorrect types. The goal is to guarantee robustness, comprehensive coverage of edge cases, and reliable exception handling.

Author
------
Douglas Felipe (github.com/DougFelipe)

Date
----
2025-06-18

Version
-------
1.0.0

Dependencies
------------
- pytest >= 7.0
- pandas >= 1.0

Notes
-----
- This script assumes `prepare_upsetplot_data` is implemented in `utils.intersections_and_groups.intersection_analysis_processing`.
- Run this file using a test runner such as pytest.
- Test fixtures for mock data are provided in `tests/conftest.py`.

Examples
--------
$ pytest test_intersection_analysis.py
"""

import pytest
import pandas as pd

from utils.intersections_and_groups.intersection_analysis_processing import (
    prepare_upsetplot_data,
)

# ------------------- Tests for prepare_upsetplot_data -------------------


@pytest.mark.usefixtures("get_mock_BioRemPP")
def test_prepare_upsetplot_data_valid_basic(get_mock_BioRemPP):
    """
    Test that prepare_upsetplot_data returns a valid DataFrame for basic valid input.

    Parameters
    ----------
    get_mock_BioRemPP : pd.DataFrame
        Fixture providing a mocked BioRemPP DataFrame.

    Returns
    -------
    None
        Asserts that the result is a non-empty DataFrame with no duplicates,
        and all selected samples are present in the output.
    """
    df = get_mock_BioRemPP.copy()
    selected_samples = df['sample'].unique().tolist()
    result = prepare_upsetplot_data(df, selected_samples)
    assert isinstance(result, pd.DataFrame)
    assert not result.empty
    assert not result.duplicated().any()
    assert set(selected_samples) <= set(result['sample'].unique())


@pytest.mark.usefixtures("get_mock_BioRemPP")
def test_prepare_upsetplot_data_empty_selection(get_mock_BioRemPP):
    """
    Test that prepare_upsetplot_data returns an empty DataFrame when no samples are selected.

    Parameters
    ----------
    get_mock_BioRemPP : pd.DataFrame
        Fixture providing a mocked BioRemPP DataFrame.

    Returns
    -------
    None
        Asserts that the result is an empty DataFrame with the expected columns.
    """
    df = get_mock_BioRemPP.copy()
    selected_samples = []
    result = prepare_upsetplot_data(df, selected_samples)
    assert isinstance(result, pd.DataFrame)
    assert result.empty
    assert set(result.columns) >= {"sample", "ko"}


def test_prepare_upsetplot_data_missing_columns():
    """
    Test that prepare_upsetplot_data raises ValueError if required columns are missing.

    Parameters
    ----------
    None
        Uses a manually created DataFrame without required columns.

    Returns
    -------
    None
        Asserts that a ValueError is raised with an appropriate message.
    """
    invalid_df = pd.DataFrame({"x": [1, 2], "y": [3, 4]})
    selected_samples = ["S1"]
    with pytest.raises(ValueError, match="Missing required column"):
        prepare_upsetplot_data(invalid_df, selected_samples)


def test_prepare_upsetplot_data_invalid_types():
    """
    Test that prepare_upsetplot_data raises ValueError for invalid input types.

    Parameters
    ----------
    None
        Uses invalid types for both merged_data and selected_samples.

    Returns
    -------
    None
        Asserts that ValueError is raised for each invalid input scenario.
    """
    with pytest.raises(ValueError, match="Expected merged_data to be a pandas DataFrame."):
        prepare_upsetplot_data("not_a_dataframe", ["S1"])

    with pytest.raises(ValueError, match="Expected selected_samples to be a list."):
        prepare_upsetplot_data(pd.DataFrame({"sample": [], "ko": []}), "S1")


@pytest.mark.usefixtures("get_mock_BioRemPP")
def test_prepare_upsetplot_data_partial_selection(get_mock_BioRemPP):
    """
    Test that prepare_upsetplot_data works with a subset of available samples.

    Parameters
    ----------
    get_mock_BioRemPP : pd.DataFrame
        Fixture providing a mocked BioRemPP DataFrame.

    Returns
    -------
    None
        Asserts that the result contains only the selected samples and is not empty.
    """
    df = get_mock_BioRemPP.copy()
    all_samples = df['sample'].unique().tolist()
    selected_samples = all_samples[:1]
    result = prepare_upsetplot_data(df, selected_samples)
    assert isinstance(result, pd.DataFrame)
    assert set(selected_samples) <= set(result['sample'].unique())
    assert not result.empty


@pytest.mark.usefixtures("get_mock_KEGG")
def test_prepare_upsetplot_data_multiple_samples(get_mock_KEGG):
    """
    Test that prepare_upsetplot_data handles multiple selected samples correctly.

    Parameters
    ----------
    get_mock_KEGG : pd.DataFrame
        Fixture providing a mocked KEGG DataFrame.

    Returns
    -------
    None
        Asserts that the result contains all selected samples, is not empty,
        and has no duplicate rows.
    """
    df = get_mock_KEGG.copy()
    selected_samples = df['sample'].unique().tolist()[:2]
    result = prepare_upsetplot_data(df, selected_samples)
    assert isinstance(result, pd.DataFrame)
    assert set(selected_samples) <= set(result['sample'].unique())
    assert not result.empty
    assert not result.duplicated().any()
