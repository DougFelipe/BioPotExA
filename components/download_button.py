"""
download_button.py
------------------
This script defines a function to generate a download button in a Dash web application. 
The button allows users to download an example data file (`sample_data.txt`) for testing or demonstration purposes.

The button is implemented as an HTML anchor (`html.A`) with specific attributes configured for file download.
"""

# ----------------------------------------
# Imports
# ----------------------------------------

from dash import html  # Dash HTML components for building UI

# ----------------------------------------
# Function: get_sample_data_button
# ----------------------------------------

def get_sample_data_button():
    """
    Generates a download button for the example data file (`biorempp_sample_data.txt`).

    The button:
    - Displays a text label: "Download Example Data".
    - Links to the file stored in the application's assets folder.
    - Triggers a file download when clicked.

    Returns:
    - dash.html.A: An HTML anchor tag (`<a>`) styled as a button, configured for downloading the file.
    """
    return html.A(
        "Download Example Data",  # Text displayed on the button
        id="download-sample-data-button",  # Unique ID for styling and testing
        href="/assets/biorempp_sample_data.txt",  # Path to the file in the assets directory
        download="biorempp_sample_data.txt",  # Specifies the file name for the downloaded file
        className="download-button"  # CSS class for styling the button
    )
