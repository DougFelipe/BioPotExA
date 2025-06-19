"""
Automated tests for the upload_handlers module in the BioPotExA core.

This test suite validates the behavior of file upload handling, including:
- File size validation
- File content and structure validation
- Processing of uploaded and example files
- Handling of user actions (upload vs. example data)
- Error and warning reporting

All tests are compatible with pytest and leverage fixtures defined in conftest.py.
"""

import pytest
import pandas as pd
import base64
import re
from io import StringIO
import builtins

from utils.core import upload_handlers
from utils.core.upload_handlers import (
    validate_upload_size,
    load_example_data,
    process_uploaded_file,
    handle_upload_or_example,
    validate_upload_comprehensive,
)

# -------------------------------
# Upload Size Validation Tests
# -------------------------------

def test_validate_upload_size_within_limit():
    """
    Test that validate_upload_size accepts content within the allowed size limit.

    Returns
    -------
    None
        Asserts that the function returns True and no error for content just under 5MB.
    """
    content = "a" * (5 * 1024 * 1024 - 1)
    is_valid, error = validate_upload_size(content)
    assert is_valid
    assert error is None

def test_validate_upload_size_exceeds_limit():
    """
    Test that validate_upload_size rejects content exceeding the allowed size.

    Returns
    -------
    None
        Asserts that the function returns False and an error message for content just over 5MB.
    """
    content = "a" * (5 * 1024 * 1024 + 1)
    is_valid, error = validate_upload_size(content)
    assert not is_valid
    assert "ultrapassa" in error

# -------------------------------
# Comprehensive Upload Validation
# -------------------------------

def test_validate_upload_comprehensive_valid_txt():
    """
    Test validate_upload_comprehensive with a valid .txt file and correct structure.

    Returns
    -------
    None
        Asserts that the function validates the structure and returns no errors.
    """
    contents = ">Sample1\nK00001\nK00002\n>Sample2\nK00003\n"
    filename = "test.txt"
    is_valid, error, warnings = validate_upload_comprehensive(contents, filename)
    assert is_valid
    assert error is None
    assert isinstance(warnings, list)

def test_validate_upload_comprehensive_invalid_extension():
    """
    Test validate_upload_comprehensive rejects files with invalid extensions.

    Returns
    -------
    None
        Asserts that the function returns an error for non-.txt files.
    """
    contents = ">Sample1\nK00001\n"
    filename = "test.csv"
    is_valid, error, warnings = validate_upload_comprehensive(contents, filename)
    assert not is_valid
    assert "Apenas arquivos .txt" in error

def test_validate_upload_comprehensive_missing_sample():
    """
    Test validate_upload_comprehensive with KO lines before any sample identifier.

    Returns
    -------
    None
        Asserts that the function returns an error for KO without a sample.
    """
    contents = "K00001\n>Sample1\nK00002\n"
    filename = "test.txt"
    is_valid, error, warnings = validate_upload_comprehensive(contents, filename)
    assert not is_valid
    assert "sem amostra definida" in error

def test_validate_upload_comprehensive_no_ko():
    """
    Test validate_upload_comprehensive with no KO identifiers present.

    Returns
    -------
    None
        Asserts that the function returns an error if no KO is present.
    """
    contents = ">Sample1\n>Sample2\n"
    filename = "test.txt"
    is_valid, error, warnings = validate_upload_comprehensive(contents, filename)
    assert not is_valid
    assert "Nenhum identificador KO" in error

def test_validate_upload_comprehensive_no_sample():
    """
    Test validate_upload_comprehensive with no sample identifiers present.

    Returns
    -------
    None
        Asserts that the function returns an error if no sample is present.
    """
    contents = "K00001\nK00002\n"
    filename = "test.txt"
    is_valid, error, warnings = validate_upload_comprehensive(contents, filename)
    assert not is_valid
    assert "Identificador KO encontrado sem amostra definida" in error

def test_validate_upload_comprehensive_invalid_format_line():
    """
    Test validate_upload_comprehensive with an invalid line format.

    Returns
    -------
    None
        Asserts that the function returns an error for lines not matching sample or KO patterns.
    """
    contents = ">Sample1\nK00001\nINVALID_LINE\n"
    filename = "test.txt"
    is_valid, error, warnings = validate_upload_comprehensive(contents, filename)
    assert not is_valid
    assert "Formato inválido" in error

def test_validate_upload_comprehensive_warning_many_samples():
    """
    Test validate_upload_comprehensive issues a warning for excessive sample count.

    Returns
    -------
    None
        Asserts that a warning is present if sample count exceeds 1000.
    """
    contents = ""
    for i in range(1001):
        contents += f">Sample{i}\nK00001\n"
    filename = "test.txt"
    is_valid, error, warnings = validate_upload_comprehensive(contents, filename)
    assert is_valid
    assert any("amostras" in w for w in warnings)

def test_validate_upload_comprehensive_warning_many_kos():
    """
    Test validate_upload_comprehensive issues a warning for excessive KO identifiers.

    Returns
    -------
    None
        Asserts that a warning is present if KO count exceeds 10000.
    """
    contents = ">Sample1\n" + "\n".join([f"K{str(i).zfill(5)}" for i in range(10001)]) + "\n"
    filename = "test.txt"
    is_valid, error, warnings = validate_upload_comprehensive(contents, filename)
    assert is_valid
    assert any("identificadores KO" in w for w in warnings)

def test_validate_upload_comprehensive_warning_low_ko_per_sample():
    """
    Test validate_upload_comprehensive issues a warning for low KO per sample ratio.

    Returns
    -------
    None
        Asserts that a warning is present if average KO per sample is less than 5.
    """
    contents = ">Sample1\nK00001\n>Sample2\nK00002\n"
    filename = "test.txt"
    is_valid, error, warnings = validate_upload_comprehensive(contents, filename)
    assert is_valid
    assert any("Poucas entradas KO" in w for w in warnings)

# -------------------------------
# Uploaded File Processing Tests
# -------------------------------

def test_process_uploaded_file_valid_content(get_mock_HADEG):
    """
    Test process_uploaded_file with valid content and DataFrame output.

    Parameters
    ----------
    get_mock_HADEG : pd.DataFrame
        Fixture providing mocked HADEG compound data.

    Returns
    -------
    None
        Asserts that the function returns a DataFrame and no error for valid input.
    """
    contents = ">Sample1\nK00001\nK00002\n"
    filename = "test.txt"
    original_validator = upload_handlers.validate_and_process_input
    upload_handlers.validate_and_process_input = lambda c, f: (get_mock_HADEG, None)
    df, error = upload_handlers.process_uploaded_file(contents, filename)
    upload_handlers.validate_and_process_input = original_validator
    assert isinstance(df, pd.DataFrame)
    assert error is None

def test_process_uploaded_file_invalid_content(get_mock_HADEG):
    """
    Test process_uploaded_file with invalid content structure.

    Parameters
    ----------
    get_mock_HADEG : pd.DataFrame
        Fixture providing mocked HADEG compound data.

    Returns
    -------
    None
        Asserts that the function returns None and an error message for invalid input.
    """
    contents = "INVALID_LINE\n"
    filename = "test.txt"
    original_validator = upload_handlers.validate_and_process_input
    upload_handlers.validate_and_process_input = lambda c, f: (get_mock_HADEG, None)
    df, error = upload_handlers.process_uploaded_file(contents, filename)
    upload_handlers.validate_and_process_input = original_validator
    assert df is None
    assert error is not None

# -------------------------------
# Upload/Example Data Handling Tests
# -------------------------------

def test_handle_upload_or_example_example_data(get_mock_ToxCSM):
    """
    Test handle_upload_or_example for loading example data.

    Parameters
    ----------
    get_mock_ToxCSM : pd.DataFrame
        Fixture providing mocked ToxCSM compound data.

    Returns
    -------
    None
        Asserts that the function returns a records list, disables submit, and provides a success alert.
    """
    original_validator = upload_handlers.validate_and_process_input
    upload_handlers.validate_and_process_input = lambda c, f: (get_mock_ToxCSM, None)
    class DummyContext:
        triggered = [{'prop_id': 'see-example-data.n_clicks'}]
    upload_handlers.dash.callback_context = DummyContext()
    result = upload_handlers.handle_upload_or_example(None, 1, None)
    upload_handlers.validate_and_process_input = original_validator
    assert isinstance(result, tuple)
    assert isinstance(result[0], list)
    assert result[1] is False
    assert hasattr(result[2], 'children')
    assert result[3] == 'loaded'

def test_handle_upload_or_example_upload_data(get_mock_BioRemPP):
    """
    Test handle_upload_or_example for file upload scenario.

    Parameters
    ----------
    get_mock_BioRemPP : pd.DataFrame
        Fixture providing mocked BioRemPP enzyme-gene-compound data.

    Returns
    -------
    None
        Asserts that the function returns a records list, disables submit, and provides a success alert.
    """
    original_validator = upload_handlers.validate_and_process_input
    upload_handlers.validate_and_process_input = lambda c, f: (get_mock_BioRemPP, None)
    class DummyContext:
        triggered = [{'prop_id': 'upload-data.contents'}]
    upload_handlers.dash.callback_context = DummyContext()
    contents = ">Sample1\nK00001\n"
    filename = "test.txt"
    result = upload_handlers.handle_upload_or_example(contents, 0, filename)
    upload_handlers.validate_and_process_input = original_validator
    assert isinstance(result, tuple)
    assert isinstance(result[0], list)
    assert result[1] is False
    assert hasattr(result[2], 'children')
    assert result[3] == 'loaded'

# -------------------------------
# Example Data Loading Tests
# -------------------------------

def test_load_example_data_success(get_mock_KEGG):
    """
    Test load_example_data returns DataFrame and no error when example file is present.

    Parameters
    ----------
    get_mock_KEGG : pd.DataFrame
        Fixture providing mocked KEGG pathway mapping data.

    Returns
    -------
    None
        Asserts that the function returns a DataFrame and no error.
    """
    original_open = builtins.open
    def mock_open(*args, **kwargs):
        return StringIO(">Sample1\nK00001\n")
    builtins.open = mock_open
    original_validator = upload_handlers.validate_and_process_input
    upload_handlers.validate_and_process_input = lambda c, f: (get_mock_KEGG, None)
    df, error = upload_handlers.load_example_data()
    builtins.open = original_open
    upload_handlers.validate_and_process_input = original_validator
    assert isinstance(df, pd.DataFrame)
    assert error is None

def test_load_example_data_file_not_found():
    """
    Test load_example_data returns error if the example file is missing.

    Returns
    -------
    None
        Asserts that the function returns None and an error message.
    """
    original_open = builtins.open
    def mock_open(*args, **kwargs):
        raise FileNotFoundError("No such file")
    builtins.open = mock_open
    df, error = upload_handlers.load_example_data()
    builtins.open = original_open
    assert df is None
    assert "No such file" in error

def test_load_example_data_success_monkeypatch(get_mock_KEGG, monkeypatch):
    """
    Test load_example_data successfully loads and processes the example file using monkeypatch.

    Parameters
    ----------
    get_mock_KEGG : pd.DataFrame
        Fixture providing mocked KEGG pathway mapping data.
    monkeypatch : pytest.MonkeyPatch
        Pytest fixture for patching builtins and functions.

    Returns
    -------
    None
        Asserts that the function returns a DataFrame and no error when the file exists and is valid.
    """
    example_content = ">Sample1\nK00001\n"
    monkeypatch.setattr("builtins.open", lambda *a, **k: StringIO(example_content))
    monkeypatch.setattr("utils.core.upload_handlers.validate_and_process_input", lambda c, f: (get_mock_KEGG, None))
    df, error = upload_handlers.load_example_data()
    assert isinstance(df, pd.DataFrame)
    assert error is None

def test_load_example_data_file_not_found_monkeypatch(monkeypatch):
    """
    Test load_example_data returns an error if the example file is missing using monkeypatch.

    Parameters
    ----------
    monkeypatch : pytest.MonkeyPatch
        Pytest fixture for patching builtins.

    Returns
    -------
    None
        Asserts that the function returns None and an error message when the file is not found.
    """
    def raise_file_not_found(*args, **kwargs):
        raise FileNotFoundError("No such file")
    monkeypatch.setattr("builtins.open", raise_file_not_found)
    df, error = upload_handlers.load_example_data()
    assert df is None
    assert "No such file" in error

def test_load_example_data_validation_error(get_mock_KEGG, monkeypatch):
    """
    Test load_example_data returns an error if validate_and_process_input fails.

    Parameters
    ----------
    get_mock_KEGG : pd.DataFrame
        Fixture providing mocked KEGG pathway mapping data.
    monkeypatch : pytest.MonkeyPatch
        Pytest fixture for patching builtins and functions.

    Returns
    -------
    None
        Asserts that the function returns None and the error message from the validator.
    """
    example_content = ">Sample1\nK00001\n"
    monkeypatch.setattr("builtins.open", lambda *a, **k: StringIO(example_content))
    monkeypatch.setattr("utils.core.upload_handlers.validate_and_process_input", lambda c, f: (None, "Validation failed"))
    df, error = upload_handlers.load_example_data()
    assert df is None
    assert error == "Validation failed"
