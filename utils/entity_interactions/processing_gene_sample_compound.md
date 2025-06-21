
# Functions related to sample_compound_interaction_plot and sample_gene_associations_plot

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
# Network procesing
# -------------------------------



import logging
import pandas as pd
from utils.core.data_processing import merge_input_with_database

# Configuração básica de logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def prepare_gene_compound_network_data(stored_data: dict) -> pd.DataFrame:
    """
    Prepares data for creating a Gene-Compound network graph.

    Parameters
    ----------
    stored_data : dict
        The stored data in dictionary format, typically from a Dash callback.

    Returns
    -------
    pd.DataFrame
        A DataFrame containing non-null and unique gene-compound relationships.

    Raises
    ------
    ValueError
        If the stored data is empty or conversion to DataFrame fails.
    KeyError
        If required columns ('genesymbol', 'compoundname') are missing in the merged data.
    """
    logger.info("Starting data preparation for gene-compound network.")

    try:
        input_df = pd.DataFrame(stored_data)
    except Exception as e:
        logger.exception("Failed to convert stored_data to DataFrame.")
        raise ValueError("Invalid input format for stored_data.") from e

    if input_df.empty:
        logger.warning("Input DataFrame is empty.")
        raise ValueError("The input data is empty.")

    logger.info("Merging input data with the reference database.")
    merged_data = merge_input_with_database(input_df)

    required_cols = {'genesymbol', 'compoundname'}
    if not required_cols.issubset(merged_data.columns):
        missing = required_cols - set(merged_data.columns)
        logger.error(f"Missing required columns: {missing}")
        raise KeyError(f"Missing required columns: {', '.join(missing)}")

    logger.info("Filtering and cleaning network data.")
    network_df = (
        merged_data[['genesymbol', 'compoundname']]
        .dropna()
        .drop_duplicates()
    )

    logger.info(f"Prepared network data with {len(network_df)} unique interactions.")
    return network_df
