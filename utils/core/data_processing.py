"""
data_processing.py
------------------

This module provides utility functions for data processing, specifically focused on merging 
user-provided data with various biological and chemical reference databases. The supported 
databases include KEGG, HADEG, and ToxCSM, each used to enrich the input data with contextual 
information for further analysis or export.

The functions are designed to handle common file formats such as CSV and Excel and perform
validation checks on the presence of required columns for merging operations (e.g., 'ko', 'cpd').

Intended Use:
    This module is intended to be used in data-driven Dash applications or standalone data
    preparation scripts where enrichment of input tables with biological pathway, enzymatic,
    or toxicological metadata is required.

Modules and Tools Used:
    - pandas: for DataFrame operations and I/O
    - os: for file path handling and existence checks
    - scipy (optional): distance calculations and clustering (available for extensibility)
    - plotly (optional): placeholder for future data visualization components

Main Functions:
    - merge_input_with_database: Merges input data with the main reference database (BioRemPP).
    - merge_input_with_database_hadegDB: Merges with the HADEG enzyme database.
    - merge_with_kegg: Integrates KEGG degradation pathway metadata.
    - merge_with_toxcsm: Merges input with ToxCSM toxicity prediction data.

Example Usage:
    >>> import pandas as pd
    >>> from data_processing import merge_input_with_database
    >>> df_input = pd.DataFrame({"ko": ["K00001", "K00002"]})
    >>> merged_df = merge_input_with_database(df_input)

Author:
    Your Name (Douglas Felipe)

Version:
    1.0.0

Last Updated:
    2025-04-22

License:
    MIT License

Notes:
    Ensure that all required input columns are present before using these functions.
    File paths should point to valid CSV or Excel files.

"""

# -------------------------------
# Imports
# -------------------------------

# Scipy modules for distance calculations and hierarchical clustering.
# -------------------------------
# Functions for Data Merging
# -------------------------------
import os
import pandas as pd
import logging


from utils.logger_config import setup_logger
logger = setup_logger(__name__)


def merge_input_with_database(input_data: pd.DataFrame, database_filepath: str = None) -> pd.DataFrame:
    """
    Merges input data with a reference database file (CSV or Excel format), 
    using a default path if none is provided.

    Parameters
    ----------
    input_data : pd.DataFrame
        The input DataFrame to be merged. Must contain a column named 'ko'.
    database_filepath : str, optional
        Path to the database file (CSV or XLSX). Defaults to 'data/database.csv'.

    Returns
    -------
    pd.DataFrame
        The resulting merged DataFrame based on the 'ko' column.

    Raises
    ------
    FileNotFoundError
        If the database file does not exist at the specified path.
    ValueError
        If the file extension is unsupported (.csv or .xlsx expected).
    KeyError
        If the column 'ko' is not found in either input or database DataFrame.
    Exception
        If any unexpected error occurs during the merge process.

    Examples
    --------
    >>> df = pd.DataFrame({"ko": ["K00001"]})
    >>> merge_input_with_database(df)
    """
    try:
        # Set default path if none provided
        if database_filepath is None:
            database_filepath = os.path.join("data", "database.csv")
        logging.info(f"Using database file at: {database_filepath}")

        # Check if file exists
        if not os.path.exists(database_filepath):
            logging.error("Database file not found.")
            raise FileNotFoundError(f"Database file not found: {database_filepath}")

        # Load database
        if database_filepath.endswith(".csv"):
            database_df = pd.read_csv(database_filepath, encoding="utf-8", sep=";")
            logging.info("Database loaded from CSV.")
        elif database_filepath.endswith(".xlsx"):
            database_df = pd.read_excel(database_filepath, engine="openpyxl")
            logging.info("Database loaded from Excel.")
        else:
            logging.error("Unsupported file extension.")
            raise ValueError("Unsupported file format. Use .csv or .xlsx")

        # Validate presence of 'ko' column
        for df_name, df in {"input_data": input_data, "database_df": database_df}.items():
            if "ko" not in df.columns:
                logging.error(f"Missing 'ko' column in {df_name}.")
                raise KeyError(f"Column 'ko' must be present in both input and database DataFrames.")

        # Merge operation
        merged_df = pd.merge(input_data, database_df, on="ko", how="inner")
        logging.info(f"Merged DataFrame shape: {merged_df.shape}")

        return merged_df

    except Exception as e:
        logging.exception("An error occurred during merging.")
        raise


def merge_with_kegg(input_df: pd.DataFrame, kegg_filepath: str = None) -> pd.DataFrame:
    """
    Merges input data with KEGG degradation pathway information from a CSV or Excel file.

    Parameters
    ----------
    input_df : pd.DataFrame
        DataFrame containing at least a 'ko' column representing KEGG Orthology identifiers.
    kegg_filepath : str, optional
        File path to the KEGG degradation pathways file. If not provided, defaults to
        'data/kegg_degradation_pathways.csv'.

    Returns
    -------
    pd.DataFrame
        A DataFrame resulting from the inner merge of the input data with KEGG pathways.

    Raises
    ------
    FileNotFoundError
        If the KEGG file does not exist at the provided path.
    ValueError
        If the file extension is not supported (must be '.csv' or '.xlsx').
    KeyError
        If the required column 'ko' is missing from either input_df or the KEGG file.

    Examples
    --------
    >>> df = pd.DataFrame({'ko': ['K00123', 'K00234']})
    >>> result = merge_with_kegg(df)
    
    Notes
    -----
    The 'ko' column must be present in both DataFrames for merging.
    The KEGG file must be encoded in UTF-8 if CSV, and use 'openpyxl' engine if Excel.
    """
    # Define default file path
    if kegg_filepath is None:
        kegg_filepath = os.path.join("data", "kegg_degradation_pathways.csv")
        logger.info(f"No filepath provided. Using default: {kegg_filepath}")

    # Validate file existence
    if not os.path.exists(kegg_filepath):
        logger.error(f"KEGG file not found at path: {kegg_filepath}")
        raise FileNotFoundError(f"KEGG file not found: {kegg_filepath}")

    # Load KEGG data
    try:
        if kegg_filepath.endswith(".csv"):
            logger.info("Reading KEGG data from CSV file.")
            kegg_df = pd.read_csv(kegg_filepath, encoding="utf-8", sep=";")
        elif kegg_filepath.endswith(".xlsx"):
            logger.info("Reading KEGG data from Excel file.")
            kegg_df = pd.read_excel(kegg_filepath, engine="openpyxl")
        else:
            logger.error("Unsupported file format provided.")
            raise ValueError("Unsupported file format. Use .csv or .xlsx")
    except Exception as e:
        logger.exception("Failed to read KEGG file.")
        raise e

    # Check required columns
    if "ko" not in input_df.columns:
        logger.error("Column 'ko' missing in input DataFrame.")
        raise KeyError("Column 'ko' must be present in the input DataFrame.")

    if "ko" not in kegg_df.columns:
        logger.error("Column 'ko' missing in KEGG DataFrame.")
        raise KeyError("Column 'ko' must be present in the KEGG DataFrame.")

    # Perform the merge
    try:
        logger.info("Merging input data with KEGG degradation pathways.")
        merged_df = pd.merge(input_df, kegg_df, on="ko", how="inner")
        logger.info(f"Merge successful. Resulting shape: {merged_df.shape}")
        return merged_df
    except Exception as e:
        logger.exception("Error occurred during merge.")
        raise e
    

def merge_input_with_database_hadegDB(input_data: pd.DataFrame, database_filepath: str = None) -> pd.DataFrame:
    """
    Merges input data with the HADEG database using a common 'ko' column.

    Parameters
    ----------
    input_data : pd.DataFrame
        DataFrame containing at least the 'ko' column, representing KEGG Orthologs.
    
    database_filepath : str, optional
        Filepath to the HADEG database in CSV or Excel format. If not provided, defaults
        to 'data/database_hadegDB.csv'.

    Returns
    -------
    pd.DataFrame
        A merged DataFrame containing columns from both input and HADEG database where 'ko' matches.

    Raises
    ------
    FileNotFoundError
        If the specified database file does not exist.
    
    ValueError
        If the file format is unsupported (not .csv or .xlsx).
    
    KeyError
        If the 'ko' column is missing from either the input or the HADEG database.

    Examples
    --------
    >>> df = pd.DataFrame({'ko': ['K00001', 'K00002']})
    >>> merge_input_with_database_hadegDB(df)

    Notes
    -----
    This function performs an inner join on the 'ko' column. Ensure both input and
    database contain this column.
    """
    logger.info("Starting merge with HADEG database.")

    if database_filepath is None:
        database_filepath = os.path.join("data", "database_hadegDB.csv")
        logger.info(f"No path provided. Using default path: {database_filepath}")

    if not os.path.exists(database_filepath):
        logger.error(f"Database file not found: {database_filepath}")
        raise FileNotFoundError(f"HADEG database file not found: {database_filepath}")

    try:
        if database_filepath.endswith(".csv"):
            database_df = pd.read_csv(database_filepath, encoding="utf-8", sep=";")
            logger.info("HADEG database loaded from CSV.")
        elif database_filepath.endswith(".xlsx"):
            database_df = pd.read_excel(database_filepath, engine="openpyxl")
            logger.info("HADEG database loaded from Excel.")
        else:
            logger.error("Unsupported file format.")
            raise ValueError("Unsupported file format. Use .csv or .xlsx.")
    except Exception as e:
        logger.exception(f"Failed to load HADEG database: {e}")
        raise

    # Check if required columns exist
    if "ko" not in input_data.columns:
        logger.error("Missing 'ko' column in input data.")
        raise KeyError("Column 'ko' must be present in the input DataFrame.")

    if "ko" not in database_df.columns:
        logger.error("Missing 'ko' column in HADEG database.")
        raise KeyError("Column 'ko' must be present in the HADEG database.")

    # Perform merge
    try:
        merged_df = pd.merge(input_data, database_df, on="ko", how="inner")
        logger.info(f"Merge successful. Resulting rows: {len(merged_df)}")
    except Exception as e:
        logger.exception(f"Merge operation failed: {e}")
        raise

    return merged_df


def merge_with_toxcsm(merged_df: pd.DataFrame, toxcsm_filepath: str = None) -> pd.DataFrame:
    """
    Merges a previously merged DataFrame with the ToxCSM database, based on the 'cpd' column.

    Parameters
    ----------
    merged_df : pd.DataFrame
        DataFrame containing at least the columns 'sample', 'compoundclass', 'cpd', and 'ko'.

    toxcsm_filepath : str, optional
        Path to the ToxCSM database file. Accepts CSV or Excel (.xlsx) formats.
        If not provided, defaults to 'data/database_toxcsm.csv'.

    Returns
    -------
    pd.DataFrame
        Final merged DataFrame containing ToxCSM annotations for matched compounds.

    Raises
    ------
    FileNotFoundError
        If the specified ToxCSM file does not exist.
    
    ValueError
        If the file format is not supported (.csv or .xlsx only).
    
    KeyError
        If required columns are missing in either input DataFrame or ToxCSM data.

    Example
    -------
    >>> df = pd.DataFrame({
    ...     "sample": ["A"],
    ...     "compoundclass": ["Aromatic"],
    ...     "cpd": ["C00123"],
    ...     "ko": ["K00003"]
    ... })
    >>> result = merge_with_toxcsm(df)
    >>> print(result.head())

    Notes
    -----
    The merge is performed as an inner join on the 'cpd' column.
    """
    logging.info("Starting merge_with_toxcsm process...")

    # Set default path if not provided
    if toxcsm_filepath is None:
        toxcsm_filepath = os.path.join("data", "database_toxcsm.csv")
        logging.info(f"No file path provided. Using default: {toxcsm_filepath}")

    # Check if file exists
    if not os.path.exists(toxcsm_filepath):
        logging.error(f"ToxCSM database file not found at: {toxcsm_filepath}")
        raise FileNotFoundError(f"ToxCSM database file not found: {toxcsm_filepath}")

    # Load ToxCSM data based on file extension
    try:
        if toxcsm_filepath.endswith('.csv'):
            toxcsm_df = pd.read_csv(toxcsm_filepath, encoding='utf-8', sep=';')
        elif toxcsm_filepath.endswith('.xlsx'):
            toxcsm_df = pd.read_excel(toxcsm_filepath, engine='openpyxl')
        else:
            raise ValueError("Unsupported file format. Use .csv or .xlsx")
        logging.info(f"ToxCSM data loaded from: {toxcsm_filepath}")
    except Exception as e:
        logging.exception("Failed to read ToxCSM file.")
        raise

    # Validate required columns in merged_df
    required_cols = ['sample', 'compoundclass', 'cpd', 'ko']
    for col in required_cols:
        if col not in merged_df.columns:
            logging.error(f"Column '{col}' is missing from input DataFrame.")
            raise KeyError(f"Required column '{col}' is missing in the input DataFrame.")

    # Validate presence of 'cpd' in ToxCSM data
    if 'cpd' not in toxcsm_df.columns:
        logging.error("Column 'cpd' is missing in ToxCSM database.")
        raise KeyError("Column 'cpd' is required in the ToxCSM database.")

    # Reduce and deduplicate input before merge
    logging.info("Reducing and deduplicating input DataFrame...")
    merged_df_reduced = merged_df[required_cols].drop_duplicates()

    # Perform inner join on 'cpd'
    logging.info("Merging input data with ToxCSM database...")
    final_merged_df = pd.merge(merged_df_reduced, toxcsm_df, on='cpd', how='inner')

    logging.info(f"Merge completed. Final DataFrame shape: {final_merged_df.shape}")
    return final_merged_df


# -------------------------------
#get_merged_toxcsm_data
# -------------------------------





def get_merged_toxcsm_data(input_data: list) -> pd.DataFrame:
    """
    Merges input data with the ToxCSM database after verifying input validity.

    Parameters
    ----------
    input_data : list
        List of dictionaries representing rows of input data (typically from Dash 'stored-data').

    Returns
    -------
    pd.DataFrame
        A DataFrame resulting from successive merges with the main database and ToxCSM database.
        Returns an empty DataFrame if input is invalid or if any merge fails.

    Notes
    -----
    - The input data must include at least the column 'sample'.
    - The merged data must include the column 'compound' to proceed with ToxCSM association.

    Raises
    ------
    None. All errors are logged internally, and the function returns an empty DataFrame on failure.
    """
    try:
        # Validate input presence
        if not input_data:
            logger.warning("Input data is empty. Returning empty DataFrame.")
            return pd.DataFrame()

        # Convert list of dicts to DataFrame
        input_df = pd.DataFrame(input_data)
        logger.info(f"Input data loaded with shape {input_df.shape}")

        # Check required column in input
        if 'sample' not in input_df.columns:
            logger.error("Missing required column 'sample' in input data.")
            return pd.DataFrame()

        # First merge with the main database
        merged_df = merge_input_with_database(input_df)
        if merged_df.empty:
            logger.warning("First merge with database returned empty DataFrame.")
            return pd.DataFrame()
        logger.info(f"First merge successful. Shape: {merged_df.shape}")

        # Check required column before ToxCSM merge
        if 'compound' not in merged_df.columns:
            logger.error("Missing required column 'compound' in merged data.")
            return pd.DataFrame()

        # Second merge with ToxCSM database
        final_df = merge_with_toxcsm(merged_df)
        if final_df.empty:
            logger.warning("Merge with ToxCSM returned empty DataFrame.")
            return pd.DataFrame()

        logger.info(f"ToxCSM merge successful. Final shape: {final_df.shape}")
        return final_df

    except Exception as e:
        logger.exception("An unexpected error occurred during ToxCSM data merge.")
        return pd.DataFrame()







# -------------------------------
# P7: Function: process_gene_compound_association
# -------------------------------

def process_gene_compound_association(merged_df):
    """
    Processes the data to calculate the number of unique compounds associated with each gene.

    Parameters:
    - merged_df (pd.DataFrame): The DataFrame resulting from merging with the database.

    Returns:
    - pd.DataFrame: A DataFrame containing the genes and the count of unique compounds, 
                    sorted in descending order of compound count.
    """
    # Group by 'genesymbol' and calculate the number of unique 'compoundname' entries.
    gene_compound_association = merged_df.groupby('genesymbol')['compoundname'].nunique().reset_index(name='num_compounds')
    
    # Sort the results by the number of unique compounds in descending order.
    gene_compound_association = gene_compound_association.sort_values(by='num_compounds', ascending=False)
    
    # Return the resulting ranked DataFrame.
    return gene_compound_association

# -------------------------------
# P8: Function: process_gene_sample_association
# -------------------------------

def process_gene_sample_association(merged_df):
    """
    Processes the data to calculate the number of unique compounds associated with each gene.

    Parameters:
    - merged_df (pd.DataFrame): The DataFrame resulting from merging with the database.

    Returns:
    - pd.DataFrame: A DataFrame containing the genes and the count of unique compounds, 
                    sorted in descending order of compound count.
    """
    # Group by 'genesymbol' and calculate the number of unique 'compoundname' entries.
    gene_sample_association = merged_df.groupby('genesymbol')['compoundname'].nunique().reset_index(name='num_compounds')
    
    # Sort the results by the number of unique compounds in descending order.
    gene_sample_association = gene_sample_association.sort_values(by='num_compounds', ascending=False)
    
    # Return the resulting ranked DataFrame.
    return gene_sample_association
