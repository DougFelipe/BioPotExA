

# -------------------------------
# P17: Function: prepare_gene_compound_network_data
# -------------------------------

import pandas as pd
from utils.data_processing import merge_input_with_database

def prepare_gene_compound_network_data(stored_data):
    """
    Prepares data for creating a Gene-Compound network graph.

    Parameters:
    - stored_data (dict): The stored data in dictionary format.

    Returns:
    - pd.DataFrame: A DataFrame containing gene-compound relationships.

    Raises:
    - ValueError: If the stored data is empty.
    - KeyError: If required columns ('genesymbol', 'cpd') are missing.
    """
    input_df = pd.DataFrame(stored_data)

    # Ensure the data is not empty.
    if input_df.empty:
        raise ValueError("The stored-data is empty.")

    # Merge the input data with the database.
    merged_data = merge_input_with_database(input_df)

    # Check for required columns.
    if 'genesymbol' not in merged_data.columns or 'cpd' not in merged_data.columns:
        raise KeyError("Columns 'genesymbol' and 'cpd' are required to create the network graph.")

    # Filter relevant columns and remove duplicates.
    network_df = merged_data[['genesymbol', 'compoundname']].dropna().drop_duplicates()

    # Return the processed DataFrame.
    return network_df

# -------------------------------
# P18: Function: get_merged_toxcsm_data
# -------------------------------
