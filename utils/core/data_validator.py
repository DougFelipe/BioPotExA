"""
data_validator.py
-----------------
This script provides utilities for validating and processing `.txt` file inputs.
It includes functionality to:

- Validate the file type.
- Decode base64-encoded content.
- Parse the content using regular expressions.
- Convert the structured content into a pandas DataFrame.
- Provide internal logging for debugging and validation feedback.
"""

import re
import base64
import logging
import pandas as pd

# Configure logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def validate_and_process_input(contents: str, filename: str) -> tuple:
    """
    Validates and processes file input, decoding and extracting data from a text file.

    Steps:
    1. Verify the file format is valid (must be a `.txt` file).
    2. Decode the content if it is base64-encoded.
    3. Split the content into lines and extract structured data.
    4. Return the data as a pandas DataFrame or an error message.

    Parameters
    ----------
    contents : str
        The file content, base64-encoded if uploaded via Dash.
    filename : str
        The name of the file, used to validate its extension.

    Returns
    -------
    tuple
        A tuple containing:
        - pd.DataFrame: Structured data extracted from the file, or None if invalid.
        - str: An error message if applicable, otherwise None.
    """
    logger.info("Starting validation and processing of file: %s", filename)

    # 1. Validate file extension
    if not filename.lower().endswith('.txt'):
        error_msg = "Invalid file type. Only .txt files are supported."
        logger.error(error_msg)
        return None, error_msg

    # 2. Attempt to decode content
    try:
        decoded_content = decode_content_if_base64(contents)
        logger.info("File content decoded successfully.")
    except Exception as e:
        error_msg = f"Failed to decode file content: {e}"
        logger.exception(error_msg)
        return None, error_msg

    # 3. Parse content into structured format
    try:
        df, error = process_content_lines(decoded_content)
        if error:
            logger.warning("Content processing returned a validation error: %s", error)
            return None, error
        logger.info("Content parsed and DataFrame created successfully.")
        return df, None
    except Exception as e:
        error_msg = f"Error processing content: {e}"
        logger.exception(error_msg)
        return None, error_msg


def decode_content_if_base64(contents: str) -> str:
    """
    Decodes content from base64 encoding if it has a data URI scheme.

    Parameters
    ----------
    contents : str
        The file content, potentially base64-encoded.

    Returns
    -------
    str
        The decoded content as a plain UTF-8 string.

    Raises
    ------
    ValueError
        If decoding fails or the content is malformed.
    """
    if contents.startswith('data'):
        try:
            _, content_string = contents.split(',', 1)
            decoded_bytes = base64.b64decode(content_string)
            return decoded_bytes.decode('utf-8')
        except Exception as e:
            logger.exception("Failed to decode base64 content.")
            raise ValueError("Could not decode base64 content.") from e
    else:
        logger.info("Content is not base64-encoded. Using as-is.")
        return contents


def process_content_lines(content: str) -> tuple:
    """
    Parses lines from the file content to extract sample identifiers and KO entries.

    Expected format:
    - Lines beginning with `>` denote sample identifiers.
    - Lines matching "K\d+" are associated KO entries.

    Parameters
    ----------
    content : str
        Decoded plain text content from the input file.

    Returns
    -------
    tuple
        A tuple containing:
        - pd.DataFrame: Extracted data with 'sample' and 'ko' columns.
        - str: An error message if applicable, otherwise None.
    """
    lines = content.strip().split('\n')

    identifier_pattern = re.compile(r'^>([^\n]+)')
    ko_pattern = re.compile(r'^(K\d+)$')

    data = []
    current_sample = None

    for line_num, line in enumerate(lines, start=1):
        line = line.strip()

        if not line:
            continue  # skip empty lines

        id_match = identifier_pattern.match(line)
        ko_match = ko_pattern.match(line)

        if id_match:
            current_sample = id_match.group(1).strip()
            logger.debug("Sample identified at line %d: %s", line_num, current_sample)
        elif ko_match and current_sample:
            ko_value = ko_match.group(1).strip()
            data.append({'sample': current_sample, 'ko': ko_value})
            logger.debug("KO entry added: sample=%s, ko=%s", current_sample, ko_value)
        else:
            logger.warning("Invalid line at %d: '%s'", line_num, line)
            return None, (
                f"Invalid format at line {line_num}: '{line}'. "
                "Expected '>' for sample ID or 'Kxxxxx' for KO entries."
            )

    if not data:
        return None, "No valid sample or KO entries found in the file."

    df = pd.DataFrame(data)
    return df, None
