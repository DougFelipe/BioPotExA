import pytest
from utils.core.data_validator import process_content_lines

@pytest.mark.usefixtures("get_mock_HADEG")
def test_process_content_lines_success(get_mock_HADEG):
    """
    Test successful parsing of valid content with sample and KO entries.

    Parameters
    ----------
    get_mock_HADEG : fixture
        Provides a DataFrame with columns ['Gene', 'ko', 'Pathway', 'compound_pathway'].

    Returns
    -------
    None

    Validates
    ---------
    That process_content_lines correctly parses valid input and returns a DataFrame
    with columns ['sample', 'ko'] and correct row count.
    """
    # Setup: create valid content string
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
    Test parsing fails with invalid line format.

    Parameters
    ----------
    None

    Returns
    -------
    None

    Validates
    ---------
    That process_content_lines returns an error message when encountering an invalid line.
    """
    content = ">Sample1\nK00001\nINVALID_LINE\nK00002"
    df, error = process_content_lines(content)
    assert df is None
    assert error is not None
    assert "Invalid format" in error

def test_process_content_lines_empty_input():
    """
    Test parsing with empty input content.

    Parameters
    ----------
    None

    Returns
    -------
    None

    Validates
    ---------
    That process_content_lines returns an error message for empty input.
    """
    content = ""
    df, error = process_content_lines(content)
    assert df is None
    assert error == "No valid sample or KO entries found in the file."

def test_process_content_lines_only_sample_headers():
    """
    Test parsing with only sample headers and no KO entries.

    Parameters
    ----------
    None

    Returns
    -------
    None

    Validates
    ---------
    That process_content_lines returns an error when there are no KO entries.
    """
    content = ">Sample1\n>Sample2"
    df, error = process_content_lines(content)
    assert df is None
    assert error == "No valid sample or KO entries found in the file."

def test_process_content_lines_ko_without_sample():
    """
    Test parsing with KO entries before any sample header.

    Parameters
    ----------
    None

    Returns
    -------
    None

    Validates
    ---------
    That process_content_lines returns an error when KO entries appear before any sample header.
    """
    content = "K00001\n>Sample1\nK00002"
    df, error = process_content_lines(content)
    assert df is None
    assert "Invalid format" in error

@pytest.mark.usefixtures("get_mock_BioRemPP")
def test_process_content_lines_with_fixture_ko(get_mock_BioRemPP):
    """
    Test parsing using KO values from the BioRemPP fixture.

    Parameters
    ----------
    get_mock_BioRemPP : fixture
        Provides a DataFrame with columns ['ko', 'desc', 'compound', 'enzyme_activity'].

    Returns
    -------
    None

    Validates
    ---------
    That process_content_lines correctly parses KO entries present in the fixture.
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
def test_process_content_lines_fixture_irrelevant_columns(get_mock_ToxCSM):
    """
    Test that process_content_lines ignores irrelevant columns from unrelated fixtures.

    Parameters
    ----------
    get_mock_ToxCSM : fixture
        Provides a DataFrame with columns ['cpd', 'compoundname', 'toxicity', 'LD50', 'label_NR_AhR'].

    Returns
    -------
    None

    Validates
    ---------
    That process_content_lines is unaffected by fixture columns unrelated to 'ko' or 'sample'.
    """
    # This fixture does not provide KO entries, so we simulate a valid input
    content = ">TestSample\nK12345"
    df, error = process_content_lines(content)
    assert error is None
    assert df is not None
    assert list(df.columns) == ['sample', 'ko']
    assert df.iloc[0]['sample'] == 'TestSample'
    assert df.iloc[0]['ko'] == 'K12345'
