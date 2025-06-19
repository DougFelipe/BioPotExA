"""
test_table_utils.py: Unit tests for table creation utilities.

This script validates the behavior of the `create_table_from_dataframe` function, ensuring it correctly generates table structures from pandas DataFrames. The tests cover scenarios such as column visibility, data integrity, column order preservation, handling of empty DataFrames, special characters in column names, duplicate columns, and various data types. The goal is to guarantee robustness, comprehensive coverage, and proper exception handling for table generation logic.

Author
------
Douglas Felipe (https://github.com/DougFelipe)

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
- This script assumes `create_table_from_dataframe` is implemented in `utils.core.table_utils`.
- Run this file using a test runner such as pytest.
- Test fixtures are provided via `tests/conftest.py`.

Examples
--------
$ pytest test_table_utils.py
"""

import pytest
import pandas as pd
from utils.core.table_utils import create_table_from_dataframe


# === Basic Table Creation and Structure ===

def test_create_table_all_columns_visible(get_mock_BioRemPP):
    """
    Test creation of a table with all columns visible.

    Parameters
    ----------
    get_mock_BioRemPP : pd.DataFrame
        Fixture providing a mocked BioRemPP DataFrame.

    Returns
    -------
    None
        Asserts that all columns are present and visible in the resulting table.
    """
    df = get_mock_BioRemPP
    ag_grid = create_table_from_dataframe(df, "test-table")
    assert hasattr(ag_grid, "rowData")
    assert hasattr(ag_grid, "columnDefs")
    fields = [col["field"] for col in ag_grid.columnDefs]
    assert set(fields) == set(df.columns)
    assert all("hide" not in col or not col["hide"] for col in ag_grid.columnDefs)


def test_create_table_column_order_preserved(get_mock_HADEG):
    """
    Test that the column order is preserved in the table.

    Parameters
    ----------
    get_mock_HADEG : pd.DataFrame
        Fixture providing a mocked HADEG DataFrame.

    Returns
    -------
    None
        Asserts that the order of columns in the table matches the DataFrame.
    """
    df = get_mock_HADEG
    ag_grid = create_table_from_dataframe(df, "hadeg-table")
    col_order = [col["field"] for col in ag_grid.columnDefs]
    assert col_order == list(df.columns)


def test_create_table_row_data_integrity(get_mock_KEGG):
    """
    Test that the row data in the table matches the DataFrame records.

    Parameters
    ----------
    get_mock_KEGG : pd.DataFrame
        Fixture providing a mocked KEGG DataFrame.

    Returns
    -------
    None
        Asserts that the table's rowData matches the DataFrame's records.
    """
    df = get_mock_KEGG
    ag_grid = create_table_from_dataframe(df, "kegg-table")
    assert ag_grid.rowData == df.to_dict("records")


def test_create_table_empty_dataframe():
    """
    Test table creation with an empty DataFrame.

    Parameters
    ----------
    None

    Returns
    -------
    None
        Asserts that the table has no row data and the correct columns.
    """
    df = pd.DataFrame(columns=["A", "B", "C"])
    ag_grid = create_table_from_dataframe(df, "empty-table")
    assert ag_grid.rowData == []
    assert [col["field"] for col in ag_grid.columnDefs] == ["A", "B", "C"]


# === Column Visibility and Hidden Columns ===

def test_create_table_with_hidden_columns(get_mock_ToxCSM):
    """
    Test that specified columns are hidden in the table.

    Parameters
    ----------
    get_mock_ToxCSM : pd.DataFrame
        Fixture providing a mocked ToxCSM DataFrame.

    Returns
    -------
    None
        Asserts that only the specified columns are hidden.
    """
    df = get_mock_ToxCSM
    hidden_cols = [df.columns[0]]
    ag_grid = create_table_from_dataframe(df, "tox-table", hidden_columns=hidden_cols)
    for col in ag_grid.columnDefs:
        if col["field"] in hidden_cols:
            assert col.get("hide", False) is True
        else:
            assert col.get("hide", False) is not True


def test_create_table_all_columns_hidden():
    """
    Test that all columns can be hidden in the table.

    Parameters
    ----------
    None

    Returns
    -------
    None
        Asserts that all columns are marked as hidden.
    """
    df = pd.DataFrame({"A": [1, 2], "B": [3, 4]})
    hidden_cols = list(df.columns)
    ag_grid = create_table_from_dataframe(df, "all-hidden-table", hidden_columns=hidden_cols)
    for col in ag_grid.columnDefs:
        assert col.get("hide", False) is True


def test_create_table_no_hidden_columns_argument():
    """
    Test that passing None for hidden_columns does not hide any columns.

    Parameters
    ----------
    None

    Returns
    -------
    None
        Asserts that no columns are hidden when hidden_columns is None.
    """
    df = pd.DataFrame({"X": [1], "Y": [2]})
    ag_grid = create_table_from_dataframe(df, "no-hidden-table", hidden_columns=None)
    assert all("hide" not in col or not col["hide"] for col in ag_grid.columnDefs)


# === Special Cases and Edge Conditions ===

def test_create_table_with_special_characters():
    """
    Test table creation with columns containing special characters.

    Parameters
    ----------
    None

    Returns
    -------
    None
        Asserts that columns with special characters are handled correctly.
    """
    df = pd.DataFrame({"A&B": [1], "C D": [2], "E-F": [3]})
    ag_grid = create_table_from_dataframe(df, "special-char-table")
    fields = [col["field"] for col in ag_grid.columnDefs]
    assert set(fields) == set(df.columns)


def test_create_table_with_duplicate_column_names():
    """
    Test table creation with duplicate column names in the DataFrame.

    Parameters
    ----------
    None

    Returns
    -------
    None
        Asserts that duplicate column names are preserved in the table definition.
    """
    df = pd.DataFrame([[1, 2]], columns=["A", "A"])
    ag_grid = create_table_from_dataframe(df, "duplicate-col-table")
    fields = [col["field"] for col in ag_grid.columnDefs]
    assert fields == list(df.columns)


def test_create_table_with_various_dtypes():
    """
    Test table creation with columns of various data types.

    Parameters
    ----------
    None

    Returns
    -------
    None
        Asserts that the table correctly represents different data types.
    """
    df = pd.DataFrame({
        "int_col": [1, 2],
        "float_col": [1.1, 2.2],
        "str_col": ["a", "b"],
        "bool_col": [True, False]
    })
    ag_grid = create_table_from_dataframe(df, "dtypes-table")
    assert ag_grid.rowData == df.to_dict("records")
