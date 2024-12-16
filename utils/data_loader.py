"""
data_loader.py
--------------
This script provides a utility function to load a database from an Excel file and return it as a pandas DataFrame.
"""

# -------------------------------
# Imports
# -------------------------------

# Import pandas for data manipulation and DataFrame handling.
import pandas as pd

# -------------------------------
# Function: load_database
# -------------------------------

def load_database(filepath: str) -> pd.DataFrame:
    """
    Loads a database from an Excel file and returns its contents as a pandas DataFrame.

    Parameters:
    - filepath (str): Path to the Excel file to be loaded.

    Returns:
    - pd.DataFrame: A pandas DataFrame containing the data from the Excel file.
    """
    # Read the Excel file into a pandas DataFrame.
    df = pd.read_excel(filepath)
    
    # Return the DataFrame with the loaded data.
    return df
