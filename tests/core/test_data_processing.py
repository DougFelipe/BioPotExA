"""
test_data_processing.py: Unit tests for data processing and database merging utilities.

This script validates the behavior of the data merging functions (`merge_input_with_database`, `merge_input_with_database_hadegDB`, `merge_with_kegg`, `merge_with_toxcsm`) from the `utils.core.data_processing` module. The tests ensure robust handling of various input scenarios, including correct merges, missing columns, and exception handling, to guarantee data integrity and comprehensive coverage of edge cases.

Author
------
Douglas Felipe (github.com/DougFelipe)

Date
----
2024-06-09

Version
1.0.0

Dependencies
------------
- pytest >= 7.0
- pandas >= 1.0

Notes
-----
- This script assumes the tested functions are implemented in `utils.core.data_processing`.
- Run this file using a test runner such as pytest.
- Test fixtures are provided via `tests/conftest.py`.
- Temporary files are created using pytest's `tmp_path` fixture.

Examples
--------
$ pytest test_data_processing.py
"""

import os
import pandas as pd
import pytest
from utils.core.data_processing import (
    merge_input_with_database,
    merge_input_with_database_hadegDB,
    merge_with_kegg,
    merge_with_toxcsm,
)

class DummyOptimize:
    """Dummy optimize_dtypes for patching if needed."""
    def __call__(self, df):
        return df

@pytest.mark.usefixtures("get_mock_BioRemPP")
def test_merge_input_with_database_success_csv(tmp_path, get_mock_BioRemPP, monkeypatch):
    """
    Test successful merge of input DataFrame with BioRemPP database (CSV).

    Parameters
    ----------
    tmp_path : pathlib.Path
        Temporary directory for test files.
    get_mock_BioRemPP : fixture
        Provides a mock BioRemPP DataFrame.
    monkeypatch : pytest.MonkeyPatch
        Used to patch optimize_dtypes.

    Returns
    -------
    None

    Validates
    ---------
    - Merge returns a DataFrame with expected columns and rows.
    - Only matching 'ko' values are present in the result.
    """
    input_df = pd.DataFrame({"ko": ["K00001", "K00002"], "value": [1, 2]})
    db_path = tmp_path / "biorempp.csv"
    get_mock_BioRemPP.to_csv(db_path, sep=";", index=False, encoding="utf-8")
    monkeypatch.setattr("utils.core.data_processing.optimize_dtypes", DummyOptimize())
    result = merge_input_with_database(input_df, str(db_path))
    assert isinstance(result, pd.DataFrame)
    assert "desc" in result.columns
    assert set(result["ko"]).issubset(set(input_df["ko"]))
    assert result.shape[0] <= input_df.shape[0]

@pytest.mark.usefixtures("get_mock_BioRemPP")
def test_merge_input_with_database_missing_ko_column(monkeypatch, get_mock_BioRemPP, tmp_path):
    """
    Test error when input DataFrame lacks 'ko' column.

    Parameters
    ----------
    monkeypatch : pytest.MonkeyPatch
        Used to patch optimize_dtypes.
    get_mock_BioRemPP : fixture
        Provides a mock BioRemPP DataFrame.
    tmp_path : pathlib.Path
        Temporary directory for test files.

    Returns
    -------
    None

    Validates
    ---------
    - Raises KeyError if 'ko' is missing in input.
    """
    bad_input = pd.DataFrame({"not_ko": ["K00001"]})
    db_path = tmp_path / "biorempp.csv"
    get_mock_BioRemPP.to_csv(db_path, sep=";", index=False, encoding="utf-8")
    monkeypatch.setattr("utils.core.data_processing.optimize_dtypes", DummyOptimize())
    with pytest.raises(KeyError):
        merge_input_with_database(bad_input, str(db_path))

@pytest.mark.usefixtures("get_mock_HADEG")
def test_merge_input_with_database_hadegDB_success(tmp_path, get_mock_HADEG, monkeypatch):
    """
    Test successful merge with HADEG database.

    Parameters
    ----------
    tmp_path : pathlib.Path
        Temporary directory for test files.
    get_mock_HADEG : fixture
        Provides a mock HADEG DataFrame.
    monkeypatch : pytest.MonkeyPatch
        Used to patch optimize_hadeg_dtypes.

    Returns
    -------
    None

    Validates
    ---------
    - Merge returns DataFrame with expected columns and rows.
    """
    input_df = pd.DataFrame({"ko": get_mock_HADEG["ko"].tolist()})
    db_path = tmp_path / "hadeg.csv"
    get_mock_HADEG.to_csv(db_path, sep=";", index=False, encoding="utf-8")
    monkeypatch.setattr("utils.core.data_processing.optimize_hadeg_dtypes", DummyOptimize())
    result = merge_input_with_database_hadegDB(input_df, str(db_path))
    assert isinstance(result, pd.DataFrame)
    assert "enzyme" in result.columns or result.shape[1] > 1
    assert set(result["ko"]).issubset(set(input_df["ko"]))

@pytest.mark.usefixtures("get_mock_KEGG")
def test_merge_with_kegg_success(tmp_path, get_mock_KEGG, monkeypatch):
    """
    Test successful merge with KEGG degradation pathways.

    Parameters
    ----------
    tmp_path : pathlib.Path
        Temporary directory for test files.
    get_mock_KEGG : fixture
        Provides a mock KEGG DataFrame.
    monkeypatch : pytest.MonkeyPatch
        Used to patch optimize_kegg_dtypes.

    Returns
    -------
    None

    Validates
    ---------
    - Merge returns DataFrame with expected columns and rows.
    """
    input_df = pd.DataFrame({"ko": get_mock_KEGG["ko"].tolist()})
    db_path = tmp_path / "kegg.csv"
    get_mock_KEGG.to_csv(db_path, sep=";", index=False, encoding="utf-8")
    monkeypatch.setattr("utils.core.data_processing.optimize_kegg_dtypes", DummyOptimize())
    result = merge_with_kegg(input_df, str(db_path))
    assert isinstance(result, pd.DataFrame)
    assert "pathway" in result.columns or result.shape[1] > 1
    assert set(result["ko"]).issubset(set(input_df["ko"]))

@pytest.mark.usefixtures("get_mock_ToxCSM")
def test_merge_with_toxcsm_success(tmp_path, get_mock_ToxCSM, monkeypatch):
    """
    Test successful merge with ToxCSM database.

    Parameters
    ----------
    tmp_path : pathlib.Path
        Temporary directory for test files.
    get_mock_ToxCSM : fixture
        Provides a mock ToxCSM DataFrame.
    monkeypatch : pytest.MonkeyPatch
        Used to patch optimize_toxcsm_dtypes.

    Returns
    -------
    None

    Validates
    ---------
    - Merge returns DataFrame with expected columns and rows.
    """
    # Setup: input DataFrame must have required columns and matching 'cpd'
    input_df = pd.DataFrame({
        "sample": ["A"] * len(get_mock_ToxCSM),
        "compoundclass": ["Class"] * len(get_mock_ToxCSM),
        "cpd": get_mock_ToxCSM["cpd"].tolist(),
        "ko": ["K00001"] * len(get_mock_ToxCSM)
    })
    db_path = tmp_path / "toxcsm.csv"
    get_mock_ToxCSM.to_csv(db_path, sep=";", index=False, encoding="utf-8")
    monkeypatch.setattr("utils.core.data_processing.optimize_toxcsm_dtypes", DummyOptimize())
    result = merge_with_toxcsm(input_df, str(db_path))
    assert isinstance(result, pd.DataFrame)
    assert "toxicity" in result.columns or result.shape[1] > 1
    assert set(result["cpd"]).issubset(set(input_df["cpd"]))

@pytest.mark.usefixtures("get_mock_ToxCSM")
def test_merge_with_toxcsm_missing_required_column(tmp_path, get_mock_ToxCSM, monkeypatch):
    """
    Test error when input DataFrame for ToxCSM is missing required columns.

    Parameters
    ----------
    tmp_path : pathlib.Path
        Temporary directory for test files.
    get_mock_ToxCSM : fixture
        Provides a mock ToxCSM DataFrame.
    monkeypatch : pytest.MonkeyPatch
        Used to patch optimize_toxcsm_dtypes.

    Returns
    -------
    None

    Validates
    ---------
    - Raises KeyError if required columns are missing in input.
    """
    input_df = pd.DataFrame({
        "sample": ["A"],
        "compoundclass": ["Class"],
        "ko": ["K00001"]
        # Missing 'cpd'
    })
    db_path = tmp_path / "toxcsm.csv"
    get_mock_ToxCSM.to_csv(db_path, sep=";", index=False, encoding="utf-8")
    monkeypatch.setattr("utils.core.data_processing.optimize_toxcsm_dtypes", DummyOptimize())
    with pytest.raises(KeyError):
        merge_with_toxcsm(input_df, str(db_path))
