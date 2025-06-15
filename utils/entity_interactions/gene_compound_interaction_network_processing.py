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
