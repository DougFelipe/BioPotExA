"""
data_validator.py
-----------------
This script provides utilities for validating and processing file inputs, specifically for text files. 
It includes functionality to:
- Validate the file type.
- Decode base64-encoded content.
- Process the content into structured data.
- Convert the structured data into a pandas DataFrame.
"""

# -------------------------------
# Imports
# -------------------------------

# Import pandas for data manipulation and DataFrame creation.
import pandas as pd

# Import regular expressions for pattern matching in text processing.
import re

# Import base64 for decoding base64-encoded content.
import base64

# -------------------------------
# Function: validate_and_process_input
# -------------------------------

def validate_and_process_input(contents: str, filename: str) -> tuple:
    """
    Validates and processes file input, decoding and extracting data from a text file.

    Steps:
    1. Verify the file format is valid (must be a `.txt` file).
    2. Decode the content if it is base64-encoded.
    3. Split the content into lines and process them using regular expressions.
    4. Create a pandas DataFrame from the extracted data.

    Parameters:
    - contents (str): The file content, base64-encoded if uploaded via Dash.
    - filename (str): The name of the file, used to check its extension.

    Returns:
    - tuple: A pandas DataFrame containing the extracted data and an error message (if applicable).
    """
    # 1. Verify that the file is a `.txt` file.
    if not filename.endswith('.txt'):
        return None, "The file is not a .txt file."
    
    # 2. Decode the content if it is base64-encoded.
    content = decode_content_if_base64(contents)
        
    # 3. Process the lines in the content.
    df, error = process_content_lines(content)
    
    return df, error

# -------------------------------
# Helper Function: decode_content_if_base64
# -------------------------------

def decode_content_if_base64(contents: str) -> str:
    """
    Decodes content from base64 encoding if necessary.

    Parameters:
    - contents (str): The file content, potentially base64-encoded.

    Returns:
    - str: The decoded content as a plain string.
    """
    # Check if the content starts with the prefix `data`, indicating base64 encoding.
    if contents.startswith('data'):
        content_type, content_string = contents.split(',')
        decoded = base64.b64decode(content_string)  # Decode the base64 content.
        return decoded.decode('utf-8')  # Convert the decoded bytes to a string.
    else:
        # Return the content as is if it is not base64-encoded.
        return contents

# -------------------------------
# Helper Function: process_content_lines
# -------------------------------

def process_content_lines(content: str) -> tuple:
    """
    Splits the content into lines and extracts data using regular expressions.

    Expected format:
    - Lines starting with `>` indicate a sample identifier.
    - Lines matching the pattern `K\d+` contain associated data.

    Parameters:
    - content (str): The decoded file content.

    Returns:
    - tuple: A pandas DataFrame with the extracted data and an error message (if applicable).
    """
    # Split the content into individual lines.
    lines = content.split('\n')
    
    # Define regular expressions for identifiers and data.
    identifier_pattern = re.compile(r'^>([^\n]+)')  # Matches lines starting with `>` for sample identifiers.
    data_pattern = re.compile(r'^(K\d+)')  # Matches lines with data entries like `K12345`.
    
    data = []  # List to hold the extracted data.
    current_identifier = None  # Tracks the current sample identifier.

    # Process each line in the content.
    for line in lines:
        identifier_match = identifier_pattern.match(line)  # Check if the line matches the identifier pattern.
        data_match = data_pattern.match(line)  # Check if the line matches the data pattern.
        
        if identifier_match:
            # Update the current identifier if an identifier is found.
            current_identifier = identifier_match.group(1).strip()
        elif data_match and current_identifier:
            # Add the data entry to the list if a data line is found and an identifier is set.
            ko_value = data_match.group(1).strip()
            data.append({'sample': current_identifier, 'ko': ko_value})
        elif line.strip() == '':
            # Skip empty lines.
            continue
        else:
            # Return an error if an invalid line is found.
            return None, f"File must be in a valid format, such as sample data! Invalid characters identified: {line}"
    
    # Return an error if no valid data was extracted.
    if not data:
        return None, "The file does not contain valid data."
    
    # Convert the extracted data into a pandas DataFrame and return it.
    return pd.DataFrame(data), None
