import logging
import pandas as pd

# Setup básico de logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


def process_gene_sample_data(merged_df: pd.DataFrame) -> pd.DataFrame:
    """
    Processes the data to generate a DataFrame grouped by sample, gene, compound pathway, and pathway,
    counting the number of unique KOs.

    Parameters
    ----------
    merged_df : pd.DataFrame
        The DataFrame resulting from merging input data with the reference database.
        Must contain columns: 'sample', 'Gene', 'compound_pathway', 'Pathway', 'ko'.

    Returns
    -------
    pd.DataFrame
        Grouped DataFrame with columns ['sample', 'Gene', 'compound_pathway', 'Pathway', 'ko_count'].

    Raises
    ------
    ValueError
        If required columns are missing.
    RuntimeError
        If an internal processing error occurs.
    """
    logger.info("Starting gene-sample data processing...")

    required_columns = ['sample', 'Gene', 'compound_pathway', 'Pathway', 'ko']
    missing_columns = [col for col in required_columns if col not in merged_df.columns]

    if missing_columns:
        logger.error(f"Missing required columns: {missing_columns}")
        raise ValueError(f"Missing required columns in input DataFrame: {missing_columns}")
    else:
        logger.debug("All required columns are present in DataFrame.")

    try:
        grouped_df = (
            merged_df
            .groupby(['sample', 'Gene', 'compound_pathway', 'Pathway'])['ko']
            .nunique()
            .reset_index(name='ko_count')
        )
        logger.info("KO count by group calculated successfully.")
        return grouped_df

    except Exception as e:
        logger.exception("An unexpected error occurred during processing.")
        raise RuntimeError("Failed to process gene-sample data.") from e
