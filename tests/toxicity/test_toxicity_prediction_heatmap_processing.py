"""
test_toxicity_prediction_heatmap_processing.py: Unit tests for toxicity prediction heatmap data processing.

This script aims to validate the `process_heatmap_data` function, which transforms DataFrames containing toxicity prediction results into a format suitable for heatmap visualization.
It is intended to ensure the robustness, integrity, and coverage of use cases for the processing function, including scenarios with valid, invalid, incomplete, or mixed data.

Author
------
Author (github.com/DougFelipe)

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
- dash_bootstrap_components

Notes
-----
- The tests assume that the `process_heatmap_data` function is implemented in `utils.toxicity.toxicity_prediction_heatmap_processing`.
- This script should not be run directly, but via a test framework (e.g., `pytest`).
- Ensure all dependencies are installed and accessible in the execution environment.

Examples
--------
$ pytest test_toxicity_prediction_heatmap_processing.py
"""


import pytest
import pandas as pd
import dash_bootstrap_components as dbc  # Bootstrap components for enhanced UI styling

from utils.toxicity.toxicity_prediction_heatmap_processing import process_heatmap_data

def test_process_heatmap_data_basic():
    """
    Test the basic functionality of `process_heatmap_data` with a valid DataFrame.

    Ensures that the returned DataFrame has the correct columns, length, and expected categories.

    Examples
    --------
    >>> test_process_heatmap_data_basic()
    """
    df = pd.DataFrame({
        'compoundname': ['cmpd1', 'cmpd2'],
        'value_NR_AhR': [0.1, 0.2],
        'label_NR_AhR': ['active', 'inactive'],
        'value_SR_p53': [0.3, 0.4],
        'label_SR_p53': ['inactive', 'active'],
        'SMILES': ['C1=CC=CC=C1', 'C2=CC=CC=C2'],
        'cpd': [1, 2],
        'ChEBI': ['CHEBI:1', 'CHEBI:2']
    })
    result = process_heatmap_data(df)
    assert set(result.columns) == {'compoundname', 'value', 'label', 'category', 'subcategoria'}
    assert len(result) == 4
    assert set(result['category']) == {'Nuclear Response', 'Stress Response'}
    assert set(result['subcategoria']) == {'NR_AhR', 'SR_p53'}
    assert not any(col in result.columns for col in ['SMILES', 'cpd', 'ChEBI'])

def test_process_heatmap_data_missing_value_label_columns():
    """
    Test `process_heatmap_data` with a DataFrame missing 'value_' and 'label_' columns.

    Ensures that a ValueError is raised when required columns are missing.

    Raises
    ------
    ValueError
        If the input DataFrame does not contain 'value_' and 'label_' columns.

    Examples
    --------
    >>> test_process_heatmap_data_missing_value_label_columns()
    """
    df = pd.DataFrame({
        'compoundname': ['cmpd1'],
        'SMILES': ['C1=CC=CC=C1']
    })
    with pytest.raises(ValueError, match="Input DataFrame must contain 'value_' and 'label_' columns."):
        process_heatmap_data(df)

def test_process_heatmap_data_no_valid_category():
    """
    Test `process_heatmap_data` with columns that do not map to any valid category.

    Ensures that a ValueError is raised when no valid columns are processed.

    Raises
    ------
    ValueError
        If no valid columns are processed for the heatmap.

    Examples
    --------
    >>> test_process_heatmap_data_no_valid_category()
    """
    df = pd.DataFrame({
        'compoundname': ['cmpd1'],
        'value_XXX_test': [0.5],
        'label_XXX_test': ['unknown']
    })
    with pytest.raises(ValueError, match="No valid columns were processed for the heatmap."):
        process_heatmap_data(df)

def test_process_heatmap_data_partial_category_mapping():
    """
    Test `process_heatmap_data` with a mix of valid and invalid category columns.

    Ensures that only valid categories are processed and included in the result.

    Examples
    --------
    >>> test_process_heatmap_data_partial_category_mapping()
    """
    df = pd.DataFrame({
        'compoundname': ['cmpd1'],
        'value_NR_AhR': [0.1],
        'label_NR_AhR': ['active'],
        'value_XXX_test': [0.5],
        'label_XXX_test': ['unknown']
    })
    result = process_heatmap_data(df)
    assert len(result) == 1
    assert result.iloc[0]['category'] == 'Nuclear Response'
    assert result.iloc[0]['subcategoria'] == 'NR_AhR'

def test_process_heatmap_data_column_order_independence():
    """
    Test that `process_heatmap_data` works regardless of column order in the DataFrame.

    Ensures that the function is robust to different column arrangements.

    Examples
    --------
    >>> test_process_heatmap_data_column_order_independence()
    """
    df = pd.DataFrame({
        'compoundname': ['cmpd1'],
        'value_SR_p53': [0.3],
        'label_SR_p53': ['inactive'],
        'value_NR_AhR': [0.1],
        'label_NR_AhR': ['active'],
    })
    result = process_heatmap_data(df)
    assert set(result['category']) == {'Nuclear Response', 'Stress Response'}
    assert set(result['subcategoria']) == {'NR_AhR', 'SR_p53'}

def test_process_heatmap_data_empty_dataframe():
    """
    Test `process_heatmap_data` with an empty DataFrame.

    Ensures that a ValueError is raised for empty input.

    Raises
    ------
    ValueError
        If the input DataFrame does not contain 'value_' and 'label_' columns.

    Examples
    --------
    >>> test_process_heatmap_data_empty_dataframe()
    """
    df = pd.DataFrame()
    with pytest.raises(ValueError, match="Input DataFrame must contain 'value_' and 'label_' columns."):
        process_heatmap_data(df)

def test_process_heatmap_data_only_compoundname():
    """
    Test `process_heatmap_data` with a DataFrame containing only the 'compoundname' column.

    Ensures that a ValueError is raised when required columns are missing.

    Raises
    ------
    ValueError
        If the input DataFrame does not contain 'value_' and 'label_' columns.

    Examples
    --------
    >>> test_process_heatmap_data_only_compoundname()
    """
    df = pd.DataFrame({'compoundname': ['cmpd1', 'cmpd2']})
    with pytest.raises(ValueError, match="Input DataFrame must contain 'value_' and 'label_' columns."):
        process_heatmap_data(df)

def test_process_heatmap_data_all_invalid_categories():
    """
    Test `process_heatmap_data` with only invalid category columns.

    Ensures that a ValueError is raised when no valid columns are processed.

    Raises
    ------
    ValueError
        If no valid columns are processed for the heatmap.

    Examples
    --------
    >>> test_process_heatmap_data_all_invalid_categories()
    """
    df = pd.DataFrame({
        'compoundname': ['cmpd1'],
        'value_XXX_1': [0.1],
        'label_XXX_1': ['a'],
        'value_YYY_2': [0.2],
        'label_YYY_2': ['b'],
    })
    with pytest.raises(ValueError, match="No valid columns were processed for the heatmap."):
        process_heatmap_data(df)

def test_process_heatmap_data_mixed_valid_and_invalid_categories():
    """
    Test `process_heatmap_data` with a mix of valid and invalid category columns.

    Ensures that only valid categories are included in the result.

    Examples
    --------
    >>> test_process_heatmap_data_mixed_valid_and_invalid_categories()
    """
    df = pd.DataFrame({
        'compoundname': ['cmpd1', 'cmpd2'],
        'value_NR_AhR': [0.1, 0.2],
        'label_NR_AhR': ['active', 'inactive'],
        'value_XXX_test': [0.5, 0.6],
        'label_XXX_test': ['unknown', 'unknown'],
    })
    result = process_heatmap_data(df)
    assert len(result) == 2
    assert set(result['category']) == {'Nuclear Response'}
    assert set(result['subcategoria']) == {'NR_AhR'}

def test_process_heatmap_data_multiple_valid_categories():
    """
    Test `process_heatmap_data` with multiple valid categories.

    Ensures that all valid categories and subcategories are processed and included.

    Examples
    --------
    >>> test_process_heatmap_data_multiple_valid_categories()
    """
    df = pd.DataFrame({
        'compoundname': ['cmpd1'],
        'value_NR_AhR': [0.1],
        'label_NR_AhR': ['active'],
        'value_SR_p53': [0.2],
        'label_SR_p53': ['inactive'],
        'value_Gen_DNA': [0.3],
        'label_Gen_DNA': ['damaged'],
        'value_Env_Tox': [0.4],
        'label_Env_Tox': ['high'],
        'value_Org_Carbon': [0.5],
        'label_Org_Carbon': ['present'],
    })
    result = process_heatmap_data(df)
    assert set(result['category']) == {
        'Nuclear Response', 'Stress Response', 'Genomic', 'Environmental', 'Organic'
    }
    assert set(result['subcategoria']) == {
        'NR_AhR', 'SR_p53', 'Gen_DNA', 'Env_Tox', 'Org_Carbon'
    }
    assert len(result) == 5

def test_process_heatmap_data_non_string_labels():
    """
    Test `process_heatmap_data` with non-string label values.

    Ensures that non-string labels are handled correctly.

    Examples
    --------
    >>> test_process_heatmap_data_non_string_labels()
    """
    df = pd.DataFrame({
        'compoundname': ['cmpd1'],
        'value_NR_AhR': [0.1],
        'label_NR_AhR': [1],
        'value_SR_p53': [0.2],
        'label_SR_p53': [0],
    })
    result = process_heatmap_data(df)
    assert set(result['category']) == {'Nuclear Response', 'Stress Response'}
    assert set(result['subcategoria']) == {'NR_AhR', 'SR_p53'}
    assert result.loc[result['subcategoria'] == 'NR_AhR', 'label'].iloc[0] == 1
    assert result.loc[result['subcategoria'] == 'SR_p53', 'label'].iloc[0] == 0

def test_process_heatmap_data_with_nan_values():
    """
    Test `process_heatmap_data` with NaN values in value and label columns.

    Ensures that NaN values are preserved in the output DataFrame.

    Examples
    --------
    >>> test_process_heatmap_data_with_nan_values()
    """
    df = pd.DataFrame({
        'compoundname': ['cmpd1', 'cmpd2'],
        'value_NR_AhR': [0.1, None],
        'label_NR_AhR': ['active', None],
        'value_SR_p53': [None, 0.4],
        'label_SR_p53': [None, 'active'],
    })
    result = process_heatmap_data(df)
    assert set(result['category']) == {'Nuclear Response', 'Stress Response'}
    assert set(result['subcategoria']) == {'NR_AhR', 'SR_p53'}
    assert result.isnull().any().any()
