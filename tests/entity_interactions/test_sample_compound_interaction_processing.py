import pytest
import pandas as pd

from utils.entity_interactions.sample_compound_interaction_processing import (
    extract_compound_classes,
    filter_by_compound_class,
)

@pytest.fixture
def mock_biorempp_compoundclass():
    """Fixture: Simulated BioRemPP data with 'compoundclass' column for compound class extraction/filtering."""
    return [
        {"sample": "S1", "ko": "K001", "desc": "desc1", "compound": "cmpd1", "enzyme_activity": 1.2, "compoundclass": "Hydrocarbon"},
        {"sample": "S2", "ko": "K002", "desc": "desc2", "compound": "cmpd2", "enzyme_activity": 2.3, "compoundclass": "Pesticide"},
        {"sample": "S3", "ko": "K003", "desc": "desc3", "compound": "cmpd3", "enzyme_activity": 0.9, "compoundclass": "Hydrocarbon"},
        {"sample": "S4", "ko": "K004", "desc": "desc4", "compound": "cmpd4", "enzyme_activity": 1.5, "compoundclass": None},
    ]


def test_extract_compound_classes_unique_sorted(mock_biorempp_compoundclass):
    """
    Test extraction of unique, sorted compound classes from BioRemPP-like data.

    Parameters
    ----------
    mock_biorempp_compoundclass : fixture
        Simulated BioRemPP data with 'compoundclass' field.

    Returns
    -------
    None

    Verifies
    --------
    - Only unique, non-null compound classes are returned.
    - The result is sorted alphabetically.
    """
    result = extract_compound_classes(mock_biorempp_compoundclass)
    assert result == ["Hydrocarbon", "Pesticide"]


def test_extract_compound_classes_empty_input():
    """
    Test extraction of compound classes from empty input.

    Parameters
    ----------
    None

    Returns
    -------
    None

    Verifies
    --------
    - Returns an empty list when input is empty.
    """
    assert extract_compound_classes([]) == []
    assert extract_compound_classes(None) == []


def test_extract_compound_classes_dataframe_input(mock_biorempp_compoundclass):
    """
    Test extraction of compound classes when input is a pandas DataFrame.

    Parameters
    ----------
    mock_biorempp_compoundclass : fixture
        Simulated BioRemPP data.

    Returns
    -------
    None

    Verifies
    --------
    - Function works with DataFrame input as well as list of dicts.
    """
    df = pd.DataFrame(mock_biorempp_compoundclass)
    result = extract_compound_classes(df)
    assert result == ["Hydrocarbon", "Pesticide"]


def test_filter_by_compound_class_found(mock_biorempp_compoundclass):
    """
    Test filtering BioRemPP data by a valid compound class.

    Parameters
    ----------
    mock_biorempp_compoundclass : fixture
        Simulated BioRemPP data.

    Returns
    -------
    None

    Verifies
    --------
    - Only rows matching the selected class are returned.
    - DataFrame shape and content are as expected.
    """
    df_filtered = filter_by_compound_class(mock_biorempp_compoundclass, "Hydrocarbon")
    assert isinstance(df_filtered, pd.DataFrame)
    assert set(df_filtered["compoundclass"].unique()) == {"Hydrocarbon"}
    assert len(df_filtered) == 2


def test_filter_by_compound_class_not_found(mock_biorempp_compoundclass):
    """
    Test filtering BioRemPP data by a compound class not present in the data.

    Parameters
    ----------
    mock_biorempp_compoundclass : fixture
        Simulated BioRemPP data.

    Returns
    -------
    None

    Verifies
    --------
    - Returns an empty DataFrame if the class is not found.
    """
    df_filtered = filter_by_compound_class(mock_biorempp_compoundclass, "Pharmaceutical")
    assert isinstance(df_filtered, pd.DataFrame)
    assert df_filtered.empty


def test_filter_by_compound_class_empty_input():
    """
    Test filtering with empty input data or empty class.

    Parameters
    ----------
    None

    Returns
    -------
    None

    Verifies
    --------
    - Returns empty DataFrame if input data or selected class is empty/None.
    """
    assert filter_by_compound_class([], "Hydrocarbon").empty
    assert filter_by_compound_class(None, "Hydrocarbon").empty
    assert filter_by_compound_class([{"compoundclass": "Hydrocarbon"}], None).empty


def test_filter_by_compound_class_dataframe_input(mock_biorempp_compoundclass):
    """
    Test filtering when input is a pandas DataFrame.

    Parameters
    ----------
    mock_biorempp_compoundclass : fixture
        Simulated BioRemPP data.

    Returns
    -------
    None

    Verifies
    --------
    - Function works with DataFrame input as well as list of dicts.
    """
    df = pd.DataFrame(mock_biorempp_compoundclass)
    df_filtered = filter_by_compound_class(df, "Pesticide")
    assert isinstance(df_filtered, pd.DataFrame)
    assert set(df_filtered["compoundclass"].unique()) == {"Pesticide"}
    assert len(df_filtered) == 1
