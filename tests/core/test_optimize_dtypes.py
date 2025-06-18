"""
test_optimize_dtypes.py: Unit tests for dtype optimization utilities in BioPotExA.

This script provides comprehensive automated tests for the dtype optimization functions:
`optimize_dtypes`, `optimize_kegg_dtypes`, `optimize_hadeg_dtypes`, and `optimize_toxcsm_dtypes`.
These utilities are responsible for converting DataFrame columns to more memory-efficient types
(e.g., categorical or float32) according to the schema of various biological datasets.

The tests ensure robust and correct dtype conversion for all relevant columns, including:
- Full and partial DataFrames
- Handling of invalid input types
- Edge cases such as non-numeric values in numeric columns

The goal is to guarantee reliability, exception handling, and broad coverage of typical and atypical scenarios.
Fixtures from `conftest.py` provide representative mock DataFrames for each supported schema.

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
- The tested functions are implemented in `utils.core.optimize_dtypes`.
- Run this file using a test runner (e.g., pytest).
- Required fixtures: get_mock_BioRemPP, get_mock_KEGG, get_mock_HADEG, get_mock_ToxCSM (see `tests/conftest.py`).

Examples
--------
$ pytest test_optimize_dtypes.py
"""

import pytest
import pandas as pd
from utils.core.optimize_dtypes import (
    optimize_dtypes,
    optimize_kegg_dtypes,
    optimize_hadeg_dtypes,
    optimize_toxcsm_dtypes
)

# =============================================================================
# Tests for optimize_dtypes
# =============================================================================

def test_optimize_dtypes_all_columns(get_mock_BioRemPP):
    """
    Tests dtype optimization on a full BioRemPP DataFrame.

    Parameters
    ----------
    get_mock_BioRemPP : pd.DataFrame
        Fixture providing a mock BioRemPP DataFrame.

    Returns
    -------
    None
        Asserts that specified columns are converted to categorical dtype.
    """
    df = get_mock_BioRemPP.copy()
    result = optimize_dtypes(df)
    for col in ['ko', 'enzyme_activity', 'sample']:
        assert pd.api.types.is_categorical_dtype(result[col])
    assert isinstance(result, pd.DataFrame)

def test_optimize_dtypes_partial_columns(get_mock_BioRemPP):
    """
    Tests dtype optimization on a partial BioRemPP DataFrame.

    Parameters
    ----------
    get_mock_BioRemPP : pd.DataFrame
        Fixture providing a mock BioRemPP DataFrame.

    Returns
    -------
    None
        Asserts that present columns are converted to categorical dtype.
    """
    df = get_mock_BioRemPP[['ko', 'sample']].copy()
    result = optimize_dtypes(df)
    assert pd.api.types.is_categorical_dtype(result['ko'])
    assert pd.api.types.is_categorical_dtype(result['sample'])

def test_optimize_dtypes_invalid_input():
    """
    Tests dtype optimization with invalid input type.

    Returns
    -------
    None
        Asserts that a TypeError is raised when input is not a DataFrame.
    """
    with pytest.raises(TypeError):
        optimize_dtypes("not a dataframe")

# =============================================================================
# Tests for optimize_kegg_dtypes
# =============================================================================

def test_optimize_kegg_dtypes_all_columns(get_mock_KEGG):
    """
    Tests dtype optimization on a full KEGG DataFrame.

    Parameters
    ----------
    get_mock_KEGG : pd.DataFrame
        Fixture providing a mock KEGG DataFrame.

    Returns
    -------
    None
        Asserts that all relevant columns are converted to categorical dtype.
    """
    df = get_mock_KEGG.copy()
    result = optimize_kegg_dtypes(df)
    for col in ['ko', 'pathname', 'genesymbol', 'sample']:
        assert pd.api.types.is_categorical_dtype(result[col])
    assert isinstance(result, pd.DataFrame)

def test_optimize_kegg_dtypes_partial_columns(get_mock_KEGG):
    """
    Tests dtype optimization on a partial KEGG DataFrame.

    Parameters
    ----------
    get_mock_KEGG : pd.DataFrame
        Fixture providing a mock KEGG DataFrame.

    Returns
    -------
    None
        Asserts that present columns are converted to categorical dtype.
    """
    df = get_mock_KEGG[['ko', 'sample']].copy()
    result = optimize_kegg_dtypes(df)
    assert pd.api.types.is_categorical_dtype(result['ko'])
    assert pd.api.types.is_categorical_dtype(result['sample'])

def test_optimize_kegg_dtypes_invalid_input():
    """
    Tests dtype optimization with invalid input type for KEGG.

    Returns
    -------
    None
        Asserts that a TypeError is raised when input is not a DataFrame.
    """
    with pytest.raises(TypeError):
        optimize_kegg_dtypes(123)

# =============================================================================
# Tests for optimize_hadeg_dtypes
# =============================================================================

def test_optimize_hadeg_dtypes_all_columns(get_mock_HADEG):
    """
    Tests dtype optimization on a full HADEG DataFrame.

    Parameters
    ----------
    get_mock_HADEG : pd.DataFrame
        Fixture providing a mock HADEG DataFrame.

    Returns
    -------
    None
        Asserts that all relevant columns are converted to categorical dtype.
    """
    df = get_mock_HADEG.copy()
    result = optimize_hadeg_dtypes(df)
    for col in ['Gene', 'ko', 'Pathway', 'compound_pathway', 'sample']:
        assert pd.api.types.is_categorical_dtype(result[col])
    assert isinstance(result, pd.DataFrame)

def test_optimize_hadeg_dtypes_partial_columns(get_mock_HADEG):
    """
    Tests dtype optimization on a partial HADEG DataFrame.

    Parameters
    ----------
    get_mock_HADEG : pd.DataFrame
        Fixture providing a mock HADEG DataFrame.

    Returns
    -------
    None
        Asserts that present columns are converted to categorical dtype.
    """
    df = get_mock_HADEG[['Gene', 'sample']].copy()
    result = optimize_hadeg_dtypes(df)
    assert pd.api.types.is_categorical_dtype(result['Gene'])
    assert pd.api.types.is_categorical_dtype(result['sample'])

def test_optimize_hadeg_dtypes_invalid_input():
    """
    Tests dtype optimization with invalid input type for HADEG.

    Returns
    -------
    None
        Asserts that a TypeError is raised when input is not a DataFrame.
    """
    with pytest.raises(TypeError):
        optimize_hadeg_dtypes("invalid")

# =============================================================================
# Tests for optimize_toxcsm_dtypes
# =============================================================================

def test_optimize_toxcsm_dtypes_all_columns(get_mock_ToxCSM):
    """
    Tests dtype optimization on a full ToxCSM DataFrame.

    Parameters
    ----------
    get_mock_ToxCSM : pd.DataFrame
        Fixture providing a mock ToxCSM DataFrame.

    Returns
    -------
    None
        Asserts that all relevant columns are converted to categorical or float32 dtype.
    """
    df = get_mock_ToxCSM.copy()
    result = optimize_toxcsm_dtypes(df)
    for col in ['SMILES', 'cpd', 'compoundname', 'sample']:
        assert pd.api.types.is_categorical_dtype(result[col])
    for col in [c for c in df.columns if c.startswith('label_')]:
        assert pd.api.types.is_categorical_dtype(result[col])
    for col in [c for c in df.columns if c.startswith('value_')]:
        assert result[col].dtype == 'float32'
    assert isinstance(result, pd.DataFrame)

def test_optimize_toxcsm_dtypes_partial_columns(get_mock_ToxCSM):
    """
    Tests dtype optimization on a partial ToxCSM DataFrame.

    Parameters
    ----------
    get_mock_ToxCSM : pd.DataFrame
        Fixture providing a mock ToxCSM DataFrame.

    Returns
    -------
    None
        Asserts that present columns are converted to the correct dtype.
    """
    df = get_mock_ToxCSM[['SMILES', 'value_score']].copy()
    result = optimize_toxcsm_dtypes(df)
    assert pd.api.types.is_categorical_dtype(result['SMILES'])
    assert result['value_score'].dtype == 'float32'

def test_optimize_toxcsm_dtypes_non_numeric_value(get_mock_ToxCSM):
    """
    Tests dtype optimization when non-numeric values are present in a numeric column.

    Parameters
    ----------
    get_mock_ToxCSM : pd.DataFrame
        Fixture providing a mock ToxCSM DataFrame.

    Returns
    -------
    None
        Asserts that non-numeric values are converted to NaN and dtype is float32.
    """
    df = get_mock_ToxCSM.copy()
    df['value_score'] = ['a', '2.2'] + list(df['value_score'][2:])
    result = optimize_toxcsm_dtypes(df)
    assert result['value_score'].dtype == 'float32'
    assert pd.isna(result['value_score'][0])
    assert result['value_score'][1] == 2.2

def test_optimize_toxcsm_dtypes_invalid_input():
    """
    Tests dtype optimization with invalid input type for ToxCSM.

    Returns
    -------
    None
        Asserts that a TypeError is raised when input is not a DataFrame.
    """
    with pytest.raises(TypeError):
        optimize_toxcsm_dtypes(None)
