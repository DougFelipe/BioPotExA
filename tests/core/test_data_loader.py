import pytest
import pandas as pd
from utils.core.data_loader import load_database

def _save_df_to_csv(tmp_path, df):
    """Helper to save a DataFrame to a temporary CSV file and return its path."""
    file_path = tmp_path / "mock_data.csv"
    df.to_csv(file_path, index=False)
    return str(file_path)

@pytest.mark.usefixtures("get_mock_HADEG")
def test_load_database_success_HADEG(get_mock_HADEG, tmp_path):
    file_path = _save_df_to_csv(tmp_path, get_mock_HADEG)
    df_loaded = load_database(file_path)
    expected_columns = ['Gene', 'ko', 'Pathway', 'compound_pathway']
    assert list(df_loaded.columns) == expected_columns
    assert df_loaded.shape == get_mock_HADEG.shape
    pd.testing.assert_frame_equal(df_loaded, get_mock_HADEG, check_dtype=False)

@pytest.mark.usefixtures("get_mock_ToxCSM")
def test_load_database_success_ToxCSM(get_mock_ToxCSM, tmp_path):
    file_path = _save_df_to_csv(tmp_path, get_mock_ToxCSM)
    df_loaded = load_database(file_path)
    expected_columns = ['cpd', 'compoundname', 'toxicity', 'LD50', 'label_NR_AhR']
    assert list(df_loaded.columns) == expected_columns
    assert df_loaded.shape == get_mock_ToxCSM.shape
    pd.testing.assert_frame_equal(df_loaded, get_mock_ToxCSM, check_dtype=False)

@pytest.mark.usefixtures("get_mock_BioRemPP")
def test_load_database_success_BioRemPP(get_mock_BioRemPP, tmp_path):
    file_path = _save_df_to_csv(tmp_path, get_mock_BioRemPP)
    df_loaded = load_database(file_path)
    expected_columns = ['ko', 'desc', 'compound', 'enzyme_activity']
    assert list(df_loaded.columns) == expected_columns
    assert df_loaded.shape == get_mock_BioRemPP.shape
    pd.testing.assert_frame_equal(df_loaded, get_mock_BioRemPP, check_dtype=False)

@pytest.mark.usefixtures("get_mock_KEGG")
def test_load_database_success_KEGG(get_mock_KEGG, tmp_path):
    file_path = _save_df_to_csv(tmp_path, get_mock_KEGG)
    df_loaded = load_database(file_path)
    expected_columns = ['ko', 'pathname', 'genesymbol']
    assert list(df_loaded.columns) == expected_columns
    assert df_loaded.shape == get_mock_KEGG.shape
    pd.testing.assert_frame_equal(df_loaded, get_mock_KEGG, check_dtype=False)

def test_load_database_empty_file(tmp_path):
    empty_df = pd.DataFrame()
    file_path = _save_df_to_csv(tmp_path, empty_df)
    df_loaded = load_database(file_path)
    assert df_loaded.empty
    assert list(df_loaded.columns) == []

def test_load_database_file_not_found():
    with pytest.raises(FileNotFoundError):
        load_database("non_existent_file.csv")

def test_load_database_invalid_format(tmp_path):
    file_path = tmp_path / "not_csv.txt"
    file_path.write_text("This is not a CSV file.")
    with pytest.raises(Exception):
        load_database(str(file_path))
