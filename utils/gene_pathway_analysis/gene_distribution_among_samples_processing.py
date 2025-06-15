import logging
import pandas as pd

# Configure logging
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


def get_ko_per_sample_for_pathway(merged_df: pd.DataFrame, selected_pathway: str) -> pd.DataFrame:
    """
    Filters the data to return the unique KOs associated with each sample for a selected pathway.

    Parameters
    ----------
    merged_df : pd.DataFrame
        DataFrame resulting from merging with KEGG data. Must include 'sample', 'genesymbol', and 'pathname'.
    selected_pathway : str
        The selected metabolic pathway to filter the data.

    Returns
    -------
    pd.DataFrame
        DataFrame with columns ['sample', 'genesymbol'] filtered by the selected pathway.
        Returns an empty DataFrame if no match is found or if required columns are missing.

    Raises
    ------
    ValueError
        If required columns are missing from the input DataFrame.
    """
    logger.info("Filtering KOs for pathway: %s", selected_pathway)

    required_cols = {'sample', 'genesymbol', 'pathname'}
    if not required_cols.issubset(merged_df.columns):
        missing = required_cols - set(merged_df.columns)
        logger.error("Missing required columns in input DataFrame: %s", missing)
        raise ValueError(f"Missing required columns: {missing}")

    try:
        filtered_df = merged_df[merged_df['pathname'] == selected_pathway]

        if filtered_df.empty:
            logger.warning("No data found for selected pathway: %s", selected_pathway)
            return pd.DataFrame(columns=['sample', 'genesymbol'])

        result_df = filtered_df[['sample', 'genesymbol']].drop_duplicates()

        logger.info("Filtered %d records for pathway: %s", len(result_df), selected_pathway)
        return result_df

    except Exception as e:
        logger.exception("Error filtering data for selected pathway.")
        raise RuntimeError("Failed to filter KO data by pathway.") from e
