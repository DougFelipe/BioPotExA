"""
test_data_validator.py: Unit tests for data validation and parsing utilities.

This script provides comprehensive automated tests for the `process_content_lines`, `decode_content_if_base64`, and `validate_and_process_input` functions, which are responsible for parsing, validating, and decoding input data files containing sample and KO information. The tests ensure robust handling of valid and invalid formats, edge cases, error conditions, and integration with representative mock datasets.

The primary goal is to guarantee the correctness, reliability, and resilience of the data validation layer, covering scenarios such as empty input, malformed lines, duplicate entries, base64-encoded content, and trimming of whitespace.

Author
------
Douglas Felipe (github.com/DougFelipe)

Date
----
2024-06-07

Version
-------
1.0.0

Dependencies
------------
- pytest >= 7.0
- pandas >= 1.0

Notes
-----
- This script assumes `process_content_lines`, `decode_content_if_base64`, and `validate_and_process_input` are implemented in `utils.core.data_validator`.
- Run this file using a test runner such as pytest.
- Test fixtures for mock data are provided in `tests/conftest.py`.

Examples
--------
$ pytest test_data_validator.py
"""

import base64
import pytest
from utils.core.data_validator import process_content_lines, decode_content_if_base64
import pandas as pd
from utils.core.data_validator import validate_and_process_input, process_content_lines, decode_content_if_base64

# -------------------- process_content_lines Tests --------------------

@pytest.mark.usefixtures("get_mock_HADEG")
def test_process_content_lines_success(get_mock_HADEG):
        """
        Tests successful parsing of valid sample/KO content.

        Parameters
        ----------
        get_mock_HADEG : pd.DataFrame
                Fixture providing mocked HADEG data (not directly used).

        Returns
        -------
        None
                Asserts that the DataFrame is correctly parsed with expected columns and values.
        """
        content = ">Sample1\nK00001\nK00002\n>Sample2\nK00003"
        df, error = process_content_lines(content)
        assert error is None
        assert df is not None
        assert list(df.columns) == ['sample', 'ko']
        assert df.shape[0] == 3
        assert set(df['ko']) == {'K00001', 'K00002', 'K00003'}
        assert set(df['sample']) == {'Sample1', 'Sample2'}


def test_process_content_lines_invalid_format():
        """
        Tests handling of invalid KO line format.

        Parameters
        ----------
        None

        Returns
        -------
        None
                Asserts that an error message is returned for invalid KO lines.
        """
        content = ">Sample1\nK00001\nINVALID_LINE\nK00002"
        df, error = process_content_lines(content)
        assert df is None
        assert error is not None
        assert "Invalid format" in error


def test_process_content_lines_empty_input():
        """
        Tests behavior with empty input content.

        Parameters
        ----------
        None

        Returns
        -------
        None
                Asserts that an appropriate error is returned for empty input.
        """
        content = ""
        df, error = process_content_lines(content)
        assert df is None
        assert error == "No valid sample or KO entries found in the file."


def test_process_content_lines_only_sample_headers():
        """
        Tests input with only sample headers and no KOs.

        Parameters
        ----------
        None

        Returns
        -------
        None
                Asserts that an error is returned when no KO entries are present.
        """
        content = ">Sample1\n>Sample2"
        df, error = process_content_lines(content)
        assert df is None
        assert error == "No valid sample or KO entries found in the file."


def test_process_content_lines_ko_without_sample():
        """
        Tests input where KO entries appear before any sample header.

        Parameters
        ----------
        None

        Returns
        -------
        None
                Asserts that an error is returned for KO lines without a sample context.
        """
        content = "K00001\n>Sample1\nK00002"
        df, error = process_content_lines(content)
        assert df is None
        assert "Invalid format" in error


@pytest.mark.usefixtures("get_mock_BioRemPP")
def test_process_content_lines_with_fixture_ko(get_mock_BioRemPP):
        """
        Tests parsing with KO list from BioRemPP fixture.

        Parameters
        ----------
        get_mock_BioRemPP : pd.DataFrame
                Fixture providing mocked BioRemPP data.

        Returns
        -------
        None
                Asserts that all KOs from the fixture are parsed under a single sample.
        """
        ko_list = get_mock_BioRemPP['ko'].tolist()
        content = ">SampleA\n" + "\n".join(ko_list)
        df, error = process_content_lines(content)
        assert error is None
        assert df is not None
        assert list(df.columns) == ['sample', 'ko']
        assert set(df['ko']) == set(ko_list)
        assert set(df['sample']) == {'SampleA'}


@pytest.mark.usefixtures("get_mock_ToxCSM")
def test_process_content_lines_irrelevant_columns(get_mock_ToxCSM):
        """
        Tests parsing with irrelevant fixture columns (ToxCSM).

        Parameters
        ----------
        get_mock_ToxCSM : pd.DataFrame
                Fixture providing mocked ToxCSM data (not directly used).

        Returns
        -------
        None
                Asserts that a simple sample/KO input is parsed correctly.
        """
        content = ">TestSample\nK12345"
        df, error = process_content_lines(content)
        assert error is None
        assert df is not None
        assert list(df.columns) == ['sample', 'ko']
        assert df.iloc[0]['sample'] == 'TestSample'
        assert df.iloc[0]['ko'] == 'K12345'


@pytest.mark.usefixtures("get_mock_KEGG")
def test_process_content_lines_multiple_samples_and_kos(get_mock_KEGG):
        """
        Tests parsing of multiple samples with multiple KOs each.

        Parameters
        ----------
        get_mock_KEGG : pd.DataFrame
                Fixture providing mocked KEGG data.

        Returns
        -------
        None
                Asserts that all samples and KOs are parsed and counted correctly.
        """
        ko_list1 = get_mock_KEGG['ko'].iloc[:2].tolist()
        ko_list2 = get_mock_KEGG['ko'].iloc[2:4].tolist()
        content = f">SampleX\n{ko_list1[0]}\n{ko_list1[1]}\n>SampleY\n{ko_list2[0]}\n{ko_list2[1]}"
        df, error = process_content_lines(content)
        assert error is None
        assert df is not None
        assert set(df['sample']) == {'SampleX', 'SampleY'}
        assert set(df['ko']) == set(ko_list1 + ko_list2)
        assert df.shape[0] == 4


def test_process_content_lines_sample_with_no_ko():
        """
        Tests input with a sample header but no KO entries.

        Parameters
        ----------
        None

        Returns
        -------
        None
                Asserts that an error is returned for samples without KOs.
        """
        content = ">SampleOnly"
        df, error = process_content_lines(content)
        assert df is None
        assert error == "No valid sample or KO entries found in the file."


def test_process_content_lines_ko_with_spaces():
        """
        Tests parsing of KO entries with leading/trailing spaces.

        Parameters
        ----------
        None

        Returns
        -------
        None
                Asserts that spaces are trimmed and KOs are parsed correctly.
        """
        content = ">Sample1\n  K00010  \nK00011\n"
        df, error = process_content_lines(content)
        assert error is None
        assert df is not None
        assert set(df['ko']) == {'K00010', 'K00011'}
        assert set(df['sample']) == {'Sample1'}


def test_process_content_lines_duplicate_ko_entries():
        """
        Tests handling of duplicate KO entries for a sample.

        Parameters
        ----------
        None

        Returns
        -------
        None
                Asserts that duplicate KOs are preserved in the output DataFrame.
        """
        content = ">Sample1\nK00001\nK00001\nK00002"
        df, error = process_content_lines(content)
        assert error is None
        assert df is not None
        assert list(df['ko']) == ['K00001', 'K00001', 'K00002']
        assert df['sample'].nunique() == 1


@pytest.mark.usefixtures("get_mock_HADEG")
def test_process_content_lines_case_insensitive_ko(get_mock_HADEG):
        """
        Tests that KO entries are case-sensitive and invalid lowercase KOs are rejected.

        Parameters
        ----------
        get_mock_HADEG : pd.DataFrame
                Fixture providing mocked HADEG data (not directly used).

        Returns
        -------
        None
                Asserts that lowercase KO entries trigger an invalid format error.
        """
        content = ">Sample1\nk00001"
        df, error = process_content_lines(content)
        assert df is None
        assert error is not None
        assert "Invalid format" in error


def test_process_content_lines_sample_header_in_middle():
        """
        Tests parsing with multiple sample headers interleaved with KOs.

        Parameters
        ----------
        None

        Returns
        -------
        None
                Asserts that KOs are correctly assigned to their respective samples.
        """
        content = ">Sample1\nK00001\nK00002\n>Sample2\nK00003\nK00004"
        df, error = process_content_lines(content)
        assert error is None
        assert df is not None
        assert set(df['sample']) == {'Sample1', 'Sample2'}
        assert set(df['ko']) == {'K00001', 'K00002', 'K00003', 'K00004'}
        assert df[df['sample'] == 'Sample1'].shape[0] == 2
        assert df[df['sample'] == 'Sample2'].shape[0] == 2


def test_process_content_lines_invalid_ko_format():
        """
        Tests rejection of KO entries with invalid format.

        Parameters
        ----------
        None

        Returns
        -------
        None
                Asserts that invalid KO formats are not accepted and trigger an error.
        """
        content = ">Sample1\nKABC01"
        df, error = process_content_lines(content)
        assert df is None
        assert error is not None
        assert "Invalid format" in error


def test_process_content_lines_sample_header_with_spaces():
        """
        Tests trimming of spaces in sample headers.

        Parameters
        ----------
        None

        Returns
        -------
        None
                Asserts that sample names are stripped of leading/trailing spaces.
        """
        content = ">  SampleTrim  \nK00001"
        df, error = process_content_lines(content)
        assert error is None
        assert df is not None
        assert set(df['sample']) == {'SampleTrim'}
        assert set(df['ko']) == {'K00001'}


@pytest.mark.usefixtures("get_mock_ToxCSM")
def test_process_content_lines_with_irrelevant_lines(get_mock_ToxCSM):
        """
        Tests rejection of lines that are not valid KO entries.

        Parameters
        ----------
        get_mock_ToxCSM : pd.DataFrame
                Fixture providing mocked ToxCSM data (not directly used).

        Returns
        -------
        None
                Asserts that non-KO lines trigger an invalid format error.
        """
        content = ">Sample1\nK00001\nSomeText\nK00002"
        df, error = process_content_lines(content)
        assert df is None
        assert error is not None
        assert "Invalid format" in error

# -------------------- decode_content_if_base64 Tests --------------------

def test_decode_content_if_base64_plain_text():
        """
        Tests decoding of plain text content (no base64).

        Parameters
        ----------
        None

        Returns
        -------
        None
                Asserts that plain text is returned unchanged.
        """
        plain_text = ">Sample1\nK00001\nK00002"
        result = decode_content_if_base64(plain_text)
        assert result == plain_text


def test_decode_content_if_base64_valid_base64():
        """
        Tests decoding of valid base64-encoded content.

        Parameters
        ----------
        None

        Returns
        -------
        None
                Asserts that the decoded content matches the original plain text.
        """
        original = ">Sample1\nK00001\nK00002"
        encoded = base64.b64encode(original.encode("utf-8")).decode("utf-8")
        data_uri = f"data:text/plain;base64,{encoded}"
        result = decode_content_if_base64(data_uri)
        assert result == original


def test_decode_content_if_base64_invalid_base64():
        """
        Tests error handling for invalid base64 input.

        Parameters
        ----------
        None

        Returns
        -------
        None
                Asserts that a ValueError is raised for invalid base64 content.
        """
        data_uri = "data:text/plain;base64,not_base64!!"
        with pytest.raises(ValueError) as excinfo:
                decode_content_if_base64(data_uri)
        assert "Could not decode base64 content." in str(excinfo.value)


@pytest.mark.usefixtures("get_mock_HADEG")
def test_decode_content_if_base64_with_fixture_hadeg(get_mock_HADEG):
        """
        Tests decoding of base64-encoded content generated from HADEG fixture.

        Parameters
        ----------
        get_mock_HADEG : pd.DataFrame
                Fixture providing mocked HADEG data.

        Returns
        -------
        None
                Asserts that the decoded content matches the original.
        """
        content = ">SampleHADEG\n" + "\n".join(get_mock_HADEG['ko'].astype(str).tolist())
        encoded = base64.b64encode(content.encode("utf-8")).decode("utf-8")
        data_uri = f"data:text/plain;base64,{encoded}"
        result = decode_content_if_base64(data_uri)
        assert result == content


@pytest.mark.usefixtures("get_mock_ToxCSM")
def test_decode_content_if_base64_with_fixture_toxcsm(get_mock_ToxCSM):
        """
        Tests decoding of base64-encoded content generated from ToxCSM fixture.

        Parameters
        ----------
        get_mock_ToxCSM : pd.DataFrame
                Fixture providing mocked ToxCSM data.

        Returns
        -------
        None
                Asserts that the decoded content matches the original.
        """
        content = ">SampleToxCSM\nK12345"
        encoded = base64.b64encode(content.encode("utf-8")).decode("utf-8")
        data_uri = f"data:text/plain;base64,{encoded}"
        result = decode_content_if_base64(data_uri)
        assert result == content


@pytest.mark.usefixtures("get_mock_BioRemPP")
def test_decode_content_if_base64_with_fixture_biorempp(get_mock_BioRemPP):
        """
        Tests decoding of base64-encoded content generated from BioRemPP fixture.

        Parameters
        ----------
        get_mock_BioRemPP : pd.DataFrame
                Fixture providing mocked BioRemPP data.

        Returns
        -------
        None
                Asserts that the decoded content matches the original.
        """
        content = ">SampleBioRemPP\n" + "\n".join(get_mock_BioRemPP['ko'].astype(str).tolist())
        encoded = base64.b64encode(content.encode("utf-8")).decode("utf-8")
        data_uri = f"data:text/plain;base64,{encoded}"
        result = decode_content_if_base64(data_uri)
        assert result == content


@pytest.mark.usefixtures("get_mock_KEGG")
def test_decode_content_if_base64_with_fixture_kegg(get_mock_KEGG):
        """
        Tests decoding of base64-encoded content generated from KEGG fixture.

        Parameters
        ----------
        get_mock_KEGG : pd.DataFrame
                Fixture providing mocked KEGG data.

        Returns
        -------
        None
                Asserts that the decoded content matches the original.
        """
        content = ">SampleKEGG\n" + "\n".join(get_mock_KEGG['ko'].astype(str).tolist())
        encoded = base64.b64encode(content.encode("utf-8")).decode("utf-8")
        data_uri = f"data:text/plain;base64,{encoded}"
        result = decode_content_if_base64(data_uri)
        assert result == content


def test_decode_content_if_base64_empty_string():
        """
        Tests decoding of an empty string.

        Parameters
        ----------
        None

        Returns
        -------
        None
                Asserts that an empty string is returned unchanged.
        """
        content = ""
        result = decode_content_if_base64(content)
        assert result == ""

# -------------------- validate_and_process_input Tests --------------------

def test_validate_and_process_input_valid_txt(get_mock_HADEG):
    """
    Tests successful validation and processing of a valid .txt file with correct content.

    Parameters
    ----------
    get_mock_HADEG : pd.DataFrame
        Mocked HADEG fixture (not directly used).

    Returns
    -------
    None
        Asserts that a DataFrame is returned with no error.
    """
    content = ">Sample1\nK00001\nK00002"
    filename = "testfile.txt"
    df, error = validate_and_process_input(content, filename)
    assert error is None
    assert df is not None
    assert list(df.columns) == ['sample', 'ko']
    assert set(df['ko']) == {'K00001', 'K00002'}
    assert set(df['sample']) == {'Sample1'}


def test_validate_and_process_input_invalid_extension():
    """
    Tests rejection of files with invalid extension.

    Parameters
    ----------
    None

    Returns
    -------
    None
        Asserts that an error message is returned for non-txt files.
    """
    content = ">Sample1\nK00001"
    filename = "testfile.csv"
    df, error = validate_and_process_input(content, filename)
    assert df is None
    assert error == "Invalid file type. Only .txt files are supported."


def test_validate_and_process_input_base64_content(get_mock_BioRemPP):
    """
    Tests processing of base64-encoded content with valid .txt extension.

    Parameters
    ----------
    get_mock_BioRemPP : pd.DataFrame
        Mocked BioRemPP fixture.

    Returns
    -------
    None
        Asserts that the decoded and parsed DataFrame matches the input.
    """
    ko_list = get_mock_BioRemPP['ko'].astype(str).tolist()
    content = ">SampleBioRemPP\n" + "\n".join(ko_list)
    encoded = base64.b64encode(content.encode("utf-8")).decode("utf-8")
    data_uri = f"data:text/plain;base64,{encoded}"
    filename = "biorempp.txt"
    df, error = validate_and_process_input(data_uri, filename)
    assert error is None
    assert df is not None
    assert set(df['ko']) == set(ko_list)
    assert set(df['sample']) == {'SampleBioRemPP'}


def test_validate_and_process_input_invalid_base64():
    """
    Tests error handling for invalid base64-encoded content.

    Parameters
    ----------
    None

    Returns
    -------
    None
        Asserts that an error message is returned for invalid base64 input.
    """
    data_uri = "data:text/plain;base64,not_base64!!"
    filename = "invalid.txt"
    df, error = validate_and_process_input(data_uri, filename)
    assert df is None
    assert "Failed to decode file content" in error


def test_validate_and_process_input_invalid_content_format():
    """
    Tests error handling for content with invalid format.

    Parameters
    ----------
    None

    Returns
    -------
    None
        Asserts that an error message is returned for invalid content.
    """
    content = ">Sample1\nINVALID_LINE"
    filename = "testfile.txt"
    df, error = validate_and_process_input(content, filename)
    assert df is None
    assert "Invalid format" in error


def test_validate_and_process_input_empty_content():
    """
    Tests behavior when the input content is empty.

    Parameters
    ----------
    None

    Returns
    -------
    None
        Asserts that an error message is returned for empty content.
    """
    content = ""
    filename = "empty.txt"
    df, error = validate_and_process_input(content, filename)
    assert df is None
    assert error == "No valid sample or KO entries found in the file."


def test_validate_and_process_input_sample_header_only():
    """
    Tests input with only sample header and no KO entries.

    Parameters
    ----------
    None

    Returns
    -------
    None
        Asserts that an error message is returned for missing KO entries.
    """
    content = ">SampleOnly"
    filename = "sampleonly.txt"
    df, error = validate_and_process_input(content, filename)
    assert df is None
    assert error == "No valid sample or KO entries found in the file."


def test_validate_and_process_input_multiple_samples(get_mock_KEGG):
    """
    Tests processing of multiple samples and KOs from KEGG fixture.

    Parameters
    ----------
    get_mock_KEGG : pd.DataFrame
        Mocked KEGG fixture.

    Returns
    -------
    None
        Asserts that all samples and KOs are parsed and counted correctly.
    """
    ko_list1 = get_mock_KEGG['ko'].iloc[:2].tolist()
    ko_list2 = get_mock_KEGG['ko'].iloc[2:4].tolist()
    content = f">SampleX\n{ko_list1[0]}\n{ko_list1[1]}\n>SampleY\n{ko_list2[0]}\n{ko_list2[1]}"
    filename = "kegg.txt"
    df, error = validate_and_process_input(content, filename)
    assert error is None
    assert df is not None
    assert set(df['sample']) == {'SampleX', 'SampleY'}
    assert set(df['ko']) == set(ko_list1 + ko_list2)
    assert df.shape[0] == 4


def test_validate_and_process_input_spaces_in_sample_and_ko():
    """
    Tests that leading/trailing spaces in sample headers and KO entries are trimmed.

    Parameters
    ----------
    None

    Returns
    -------
    None
        Asserts that spaces are removed and values are parsed correctly.
    """
    content = ">  SampleTrim  \n  K00010  \nK00011"
    filename = "spaces.txt"
    df, error = validate_and_process_input(content, filename)
    assert error is None
    assert df is not None
    assert set(df['sample']) == {'SampleTrim'}
    assert set(df['ko']) == {'K00010', 'K00011'}


def test_validate_and_process_input_duplicate_ko_entries():
    """
    Tests that duplicate KO entries for a sample are preserved.

    Parameters
    ----------
    None

    Returns
    -------
    None
        Asserts that duplicate KOs are present in the output DataFrame.
    """
    content = ">Sample1\nK00001\nK00001\nK00002"
    filename = "duplicates.txt"
    df, error = validate_and_process_input(content, filename)
    assert error is None
    assert df is not None
    assert list(df['ko']) == ['K00001', 'K00001', 'K00002']
    assert df['sample'].nunique() == 1

        