"""
This script contains utility functions to process KO (KEGG Orthology) data, 
including counting unique KOs per sample, pathway, or other groupings. 
It also includes basic preprocessing functions for compound data visualization.
"""

import pandas as pd
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] [%(levelname)s] - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)


def validate_ko_dataframe(df: pd.DataFrame, required_columns: list = ['sample', 'ko']) -> None:
    """
    Validates the structure and columns of a KO DataFrame.

    Parameters
    ----------
    df : pd.DataFrame
        The DataFrame to validate.
    required_columns : list, optional
        List of column names required in the DataFrame.

    Raises
    ------
    ValueError
        If the DataFrame is missing required columns or has invalid type.
    """
    if not isinstance(df, pd.DataFrame):
        raise ValueError("Input must be a pandas DataFrame.")
    
    missing = [col for col in required_columns if col not in df.columns]
    if missing:
        raise ValueError(f"Missing required columns: {missing}")
    
    logging.info("Validation successful: All required columns are present.")


def process_ko_data(merged_df) -> pd.DataFrame:
    """
    Processes KO data to count unique KOs for each sample.

    Parameters
    ----------
    merged_df : pd.DataFrame or list of dict
        Merged KO data containing at least 'sample' and 'ko' columns.

    Returns
    -------
    pd.DataFrame
        A DataFrame with samples and their respective unique KO counts, sorted in descending order.

    Raises
    ------
    ValueError
        If input data is not valid or lacks required columns.
    """
    logging.info("Starting KO data processing...")

    # Convert input to DataFrame if needed
    if isinstance(merged_df, list):
        logging.info("Converting list of dicts to DataFrame...")
        merged_df = pd.DataFrame(merged_df)
    elif not isinstance(merged_df, pd.DataFrame):
        raise ValueError("The merged_df argument must be a pandas DataFrame or a list of dictionaries.")

    # Validate essential columns
    validate_ko_dataframe(merged_df)

    # Count unique KOs per sample
    logging.info("Counting unique KOs per sample...")
    ko_count = merged_df.groupby('sample')['ko'].nunique().reset_index(name='ko_count')

    # Sort the counts
    ko_count_sorted = ko_count.sort_values('ko_count', ascending=False)

    logging.info("KO data processing complete.")
    return ko_count_sorted


def process_ko_data_violin(df: pd.DataFrame) -> pd.DataFrame:
    """
    Processes KO data for generating violin plots by counting unique KOs per sample.

    Parameters
    ----------
    df : pd.DataFrame
        Input DataFrame containing 'sample' and 'ko' columns.

    Returns
    -------
    pd.DataFrame
        A DataFrame with the count of unique KOs per sample.

    Raises
    ------
    ValueError
        If the DataFrame is invalid or missing required columns.
    """
    logging.info("Starting KO data preprocessing for violin plot...")

    # Validate structure
    validate_ko_dataframe(df)

    # Group and count KOs
    ko_count_per_sample = df.groupby('sample')['ko'].nunique().reset_index(name='ko_count')

    logging.info("Violin plot data processing complete.")
    return ko_count_per_sample
