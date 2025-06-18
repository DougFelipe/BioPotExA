import pandas as pd
import os

def load_database(filepath: str) -> pd.DataFrame:
    """
    Loads a database file into a pandas DataFrame.

    Supports both CSV and Excel (.xlsx) formats. If the file is empty,
    returns an empty DataFrame instead of raising an exception.

    Parameters
    ----------
    filepath : str
        Path to the database file (.csv or .xlsx).

    Returns
    -------
    pd.DataFrame
        The loaded DataFrame. If the file is empty, returns an empty DataFrame.

    Raises
    ------
    FileNotFoundError
        If the file does not exist at the specified path.
    ValueError
        If the file extension is not .csv or .xlsx.
    """
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"File not found: {filepath}")

    try:
        if filepath.endswith(".csv"):
            return pd.read_csv(filepath, encoding="utf-8", sep=",")
        elif filepath.endswith(".xlsx"):
            return pd.read_excel(filepath, engine="openpyxl")
        else:
            raise ValueError("Unsupported file format. Use .csv or .xlsx")
    except pd.errors.EmptyDataError:
        # Handles empty file gracefully
        return pd.DataFrame()
