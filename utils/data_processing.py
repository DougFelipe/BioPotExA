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

# Data manipulation and handling DataFrame structures.
import pandas as pd

# Plotly modules for creating visualizations (unused in the current script but included for extensibility).
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots

# Scipy modules for distance calculations and hierarchical clustering.
# -------------------------------
# Functions for Data Merging
# -------------------------------
import os
import pandas as pd

def merge_input_with_database(input_data: pd.DataFrame, database_filepath: str = None) -> pd.DataFrame:
    """
    Merges input data with a reference database file (CSV or Excel format), using a default path if none is provided.

    Parameters:
        input_data (pd.DataFrame): The input DataFrame to be merged.
        database_filepath (str, optional): Path to the database file. Defaults to 'data/database.csv'.

    Returns:
        pd.DataFrame: The resulting merged DataFrame.

    Raises:
        FileNotFoundError: If the database file is not found at the specified path.
        ValueError: If the file extension is unsupported.
        KeyError: If the 'ko' column is missing from either DataFrame.

    Example:
        >>> df = pd.DataFrame({"ko": ["K00001"]})
        >>> merge_input_with_database(df)

    Notes:
        The input and database DataFrames must both contain a column named 'ko' to perform the merge.
    """
    if database_filepath is None:
        database_filepath = os.path.join("data", "database.csv")

    if not os.path.exists(database_filepath):
        raise FileNotFoundError(f"Database file not found: {database_filepath}")

    if database_filepath.endswith('.csv'):
        database_df = pd.read_csv(database_filepath, encoding='utf-8', sep=';')
    elif database_filepath.endswith('.xlsx'):
        database_df = pd.read_excel(database_filepath, engine='openpyxl')
    else:
        raise ValueError("Unsupported file format. Use .csv or .xlsx")

    if 'ko' not in input_data.columns or 'ko' not in database_df.columns:
        raise KeyError("Column 'ko' must be present in both input and database DataFrames.")

    merged_df = pd.merge(input_data, database_df, on='ko', how='inner')
    return merged_df


def merge_with_kegg(input_df: pd.DataFrame, kegg_filepath: str = None) -> pd.DataFrame:
    """
    Merges input data with KEGG degradation pathway information from a CSV or Excel file.

    Parameters:
        input_df (pd.DataFrame): The input DataFrame to be merged.
        kegg_filepath (str, optional): Path to the KEGG data file. Defaults to 'data/kegg_degradation_pathways.csv'.

    Returns:
        pd.DataFrame: The resulting merged DataFrame.

    Raises:
        FileNotFoundError: If the KEGG file does not exist.
        ValueError: If the file format is not supported.
        KeyError: If 'ko' column is missing in either DataFrame.

    Example:
        >>> df = pd.DataFrame({"ko": ["K00123"]})
        >>> merge_with_kegg(df)

    Notes:
        The 'ko' column must be present in both the input and KEGG pathway DataFrames.
    """
    if kegg_filepath is None:
        kegg_filepath = os.path.join("data", "kegg_degradation_pathways.csv")

    if not os.path.exists(kegg_filepath):
        raise FileNotFoundError(f"KEGG file not found: {kegg_filepath}")

    if kegg_filepath.endswith('.csv'):
        kegg_df = pd.read_csv(kegg_filepath, encoding='utf-8', sep=';')
    elif kegg_filepath.endswith('.xlsx'):
        kegg_df = pd.read_excel(kegg_filepath, engine='openpyxl')
    else:
        raise ValueError("Unsupported file format. Use .csv or .xlsx")

    if 'ko' not in input_df.columns or 'ko' not in kegg_df.columns:
        raise KeyError("Column 'ko' must be present in both input and KEGG DataFrames.")

    merged_df = pd.merge(input_df, kegg_df, on='ko', how='inner')
    return merged_df


def merge_input_with_database_hadegDB(input_data: pd.DataFrame, database_filepath: str = None) -> pd.DataFrame:
    """
    Merges input data with the HADEG database (CSV or Excel), using a default path if none is provided.

    Parameters:
        input_data (pd.DataFrame): The input DataFrame to be merged.
        database_filepath (str, optional): Path to the HADEG database file. Defaults to 'data/database_hadegDB.csv'.

    Returns:
        pd.DataFrame: The resulting merged DataFrame.

    Raises:
        FileNotFoundError: If the HADEG database file is not found.
        ValueError: If the file format is not supported.
        KeyError: If the 'ko' column is missing in either DataFrame.

    Example:
        >>> df = pd.DataFrame({"ko": ["K00002"]})
        >>> merge_input_with_database_hadegDB(df)

    Notes:
        The merge is performed using the 'ko' column, which must exist in both input and HADEG database.
    """
    if database_filepath is None:
        database_filepath = os.path.join("data", "database_hadegDB.csv")

    if not os.path.exists(database_filepath):
        raise FileNotFoundError(f"HADEG database file not found: {database_filepath}")

    if database_filepath.endswith('.csv'):
        database_df = pd.read_csv(database_filepath, encoding='utf-8', sep=';')
    elif database_filepath.endswith('.xlsx'):
        database_df = pd.read_excel(database_filepath, engine='openpyxl')
    else:
        raise ValueError("Unsupported file format. Use .csv or .xlsx")

    if 'ko' not in input_data.columns or 'ko' not in database_df.columns:
        raise KeyError("Column 'ko' must be present in both input and HADEG database DataFrames.")

    merged_df = pd.merge(input_data, database_df, on='ko', how='inner')
    return merged_df


def merge_with_toxcsm(merged_df: pd.DataFrame, toxcsm_filepath: str = None) -> pd.DataFrame:
    """
    Merges a previously merged DataFrame with the ToxCSM database (CSV or Excel), based on the 'cpd' column.

    Parameters:
        merged_df (pd.DataFrame): DataFrame containing columns like 'sample', 'compoundclass', 'cpd', and 'ko'.
        toxcsm_filepath (str, optional): Path to the ToxCSM database file. Defaults to 'data/database_toxcsm.csv'.

    Returns:
        pd.DataFrame: The final merged DataFrame including ToxCSM data.

    Raises:
        FileNotFoundError: If the ToxCSM file does not exist.
        ValueError: If the file format is not supported.
        KeyError: If required columns ('cpd', etc.) are missing in the input DataFrame or ToxCSM database.

    Example:
        >>> df = pd.DataFrame({"sample": ["A"], "compoundclass": ["Aromatic"], "cpd": ["C00123"], "ko": ["K00003"]})
        >>> merge_with_toxcsm(df)

    Notes:
        The function filters and merges only the necessary columns before merging with the ToxCSM database.
    """
    if toxcsm_filepath is None:
        toxcsm_filepath = os.path.join("data", "database_toxcsm.csv")

    if not os.path.exists(toxcsm_filepath):
        raise FileNotFoundError(f"ToxCSM database file not found: {toxcsm_filepath}")

    if toxcsm_filepath.endswith('.csv'):
        toxcsm_df = pd.read_csv(toxcsm_filepath, encoding='utf-8', sep=';')
    elif toxcsm_filepath.endswith('.xlsx'):
        toxcsm_df = pd.read_excel(toxcsm_filepath, engine='openpyxl')
    else:
        raise ValueError("Unsupported file format. Use .csv or .xlsx")

    for col in ['sample', 'compoundclass', 'cpd', 'ko']:
        if col not in merged_df.columns:
            raise KeyError(f"Required column '{col}' is missing in the input DataFrame.")

    if 'cpd' not in toxcsm_df.columns:
        raise KeyError("Column 'cpd' is required in the ToxCSM database.")

    merged_df_reduced = merged_df[['sample', 'compoundclass', 'cpd', 'ko']].drop_duplicates()
    final_merged_df = pd.merge(merged_df_reduced, toxcsm_df, on='cpd', how='inner')

    return final_merged_df







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











# -------------------------------
# P18: Function: get_merged_toxcsm_data
# -------------------------------

def get_merged_toxcsm_data(input_data):
    """
    Merges input data with the ToxCSM database.

    Parameters:
    - input_data (list): Raw data stored in 'stored-data'.

    Returns:
    - pd.DataFrame: A processed DataFrame containing `value_` and `label_` columns.
    """
    # Ensure input data is available.
    if not input_data:
        return pd.DataFrame()  # Return an empty DataFrame.

    # Convert the input data to a DataFrame.
    input_df = pd.DataFrame(input_data)

    # Perform the first merge with the main database.
    merged_df = merge_input_with_database(input_df)
    if merged_df.empty:
        return pd.DataFrame()

    # Perform the second merge with the ToxCSM database.
    final_merged_df = merge_with_toxcsm(merged_df)
    if final_merged_df.empty:
        return pd.DataFrame()

    # Return the final merged DataFrame.
    return final_merged_df
