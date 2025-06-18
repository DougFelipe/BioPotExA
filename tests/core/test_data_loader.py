"""
test_data_loader.py: Automated unit tests for database loading utilities.

This script provides comprehensive tests for the `load_database` function, which is responsible for importing various database CSV files into pandas DataFrames. The tests ensure correct loading for different database schemas (HADEG, ToxCSM, BioRemPP, KEGG), as well as robust handling of edge cases such as empty files, missing files, and invalid formats. The goal is to guarantee reliability, correctness, and resilience of the data import layer.

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
- Assumes `load_database` is implemented in `utils.core.data_loader`.
- Run this file using a test runner such as pytest.
- Test fixtures for mock data are provided in `tests/conftest.py`.

Examples
--------
$ pytest test_data_loader.py
"""

import pytest
import pandas as pd
from utils.core.data_loader import load_database


def _save_df_to_csv(tmp_path, df):
    """
    Helper function to save a DataFrame to a temporary CSV file.

    Parameters
    ----------
    tmp_path : pathlib.Path
        Temporary directory provided by pytest.
    df : pd.DataFrame
        DataFrame to be saved.

    Returns
    -------
    str
        Path to the saved CSV file.
    """
    file_path = tmp_path / "mock_data.csv"
    df.to_csv(file_path, index=False)
    return str(file_path)


# ---------------------- Tests for Successful Database Loading ----------------------

@pytest.mark.usefixtures("get_mock_HADEG")
def test_load_database_success_hadeg(get_mock_HADEG, tmp_path):
    """
    Test successful loading of the HADEG database CSV file.

    Parameters
    ----------
    get_mock_HADEG : pd.DataFrame
        Fixture providing a mock HADEG DataFrame.
    tmp_path : pathlib.Path
        Temporary directory for test files.

    Returns
    -------
    None
        Asserts that the loaded DataFrame matches the expected columns and content.
    """
    file_path = _save_df_to_csv(tmp_path, get_mock_HADEG)
    df_loaded = load_database(file_path)
    expected_columns = ['sample', 'Gene', 'ko', 'Pathway', 'compound_pathway']
    assert list(df_loaded.columns) == expected_columns
    assert df_loaded.shape == get_mock_HADEG.shape
    pd.testing.assert_frame_equal(df_loaded, get_mock_HADEG, check_dtype=False)


@pytest.mark.usefixtures("get_mock_ToxCSM")
def test_load_database_success_toxcsm(get_mock_ToxCSM, tmp_path):
    """
    Test successful loading of the ToxCSM database CSV file.

    Parameters
    ----------
    get_mock_ToxCSM : pd.DataFrame
        Fixture providing a mock ToxCSM DataFrame.
    tmp_path : pathlib.Path
        Temporary directory for test files.

    Returns
    -------
    None
        Asserts that the loaded DataFrame matches the expected columns and content.
    """
    file_path = _save_df_to_csv(tmp_path, get_mock_ToxCSM)
    df_loaded = load_database(file_path)
    expected_columns = [
        'sample', 'cpd', 'compoundname', 'toxicity', 'LD50',
        'label_NR_AhR', 'SMILES', 'value_score'
    ]
    assert list(df_loaded.columns) == expected_columns
    assert df_loaded.shape == get_mock_ToxCSM.shape
    pd.testing.assert_frame_equal(df_loaded, get_mock_ToxCSM, check_dtype=False)


@pytest.mark.usefixtures("get_mock_BioRemPP")
def test_load_database_success_bioremp(get_mock_BioRemPP, tmp_path):
    """
    Test successful loading of the BioRemPP database CSV file.

    Parameters
    ----------
    get_mock_BioRemPP : pd.DataFrame
        Fixture providing a mock BioRemPP DataFrame.
    tmp_path : pathlib.Path
        Temporary directory for test files.

    Returns
    -------
    None
        Asserts that the loaded DataFrame matches the expected columns and content.
    """
    file_path = _save_df_to_csv(tmp_path, get_mock_BioRemPP)
    df_loaded = load_database(file_path)
    expected_columns = ['sample', 'ko', 'desc', 'compound', 'enzyme_activity']
    assert list(df_loaded.columns) == expected_columns
    assert df_loaded.shape == get_mock_BioRemPP.shape
    pd.testing.assert_frame_equal(df_loaded, get_mock_BioRemPP, check_dtype=False)


@pytest.mark.usefixtures("get_mock_KEGG")
def test_load_database_success_kegg(get_mock_KEGG, tmp_path):
    """
    Test successful loading of the KEGG database CSV file.

    Parameters
    ----------
    get_mock_KEGG : pd.DataFrame
        Fixture providing a mock KEGG DataFrame.
    tmp_path : pathlib.Path
        Temporary directory for test files.

    Returns
    -------
    None
        Asserts that the loaded DataFrame matches the expected columns and content.
    """
    file_path = _save_df_to_csv(tmp_path, get_mock_KEGG)
    df_loaded = load_database(file_path)
    expected_columns = ['sample', 'ko', 'pathname', 'genesymbol']
    assert list(df_loaded.columns) == expected_columns
    assert df_loaded.shape == get_mock_KEGG.shape
    pd.testing.assert_frame_equal(df_loaded, get_mock_KEGG, check_dtype=False)


# ---------------------- Tests for Edge Cases and Error Handling ----------------------

def test_load_database_empty_file(tmp_path):
    """
    Test loading an empty CSV file.

    Parameters
    ----------
    tmp_path : pathlib.Path
        Temporary directory for test files.

    Returns
    -------
    None
        Asserts that the loaded DataFrame is empty and has no columns.
    """
    empty_df = pd.DataFrame()
    file_path = _save_df_to_csv(tmp_path, empty_df)
    df_loaded = load_database(file_path)
    assert df_loaded.empty
    assert list(df_loaded.columns) == []


def test_load_database_file_not_found():
    """
    Test loading a non-existent CSV file.

    Returns
    -------
    None
        Asserts that a FileNotFoundError is raised.
    """
    with pytest.raises(FileNotFoundError):
        load_database("non_existent_file.csv")


def test_load_database_invalid_format(tmp_path):
    """
    Test loading a file with invalid (non-CSV) format.

    Parameters
    ----------
    tmp_path : pathlib.Path
        Temporary directory for test files.

    Returns
    -------
    None
        Asserts that an exception is raised due to invalid file format.
    """
    file_path = tmp_path / "not_csv.txt"
    file_path.write_text("This is not a CSV file.")
    with pytest.raises(Exception):
        load_database(str(file_path))
