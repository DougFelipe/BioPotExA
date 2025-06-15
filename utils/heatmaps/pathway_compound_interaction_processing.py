import pandas as pd
import logging

# Configure logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def process_pathway_data(merged_df: pd.DataFrame) -> pd.DataFrame:
    """
    Processes merged input data to compute KO counts grouped by pathway, compound pathway, and sample.

    Parameters
    ----------
    merged_df : pd.DataFrame
        A DataFrame containing the columns 'Pathway', 'compound_pathway', 'sample', and 'ko'.

    Returns
    -------
    pd.DataFrame
        A grouped DataFrame with KO counts per 'Pathway', 'compound_pathway', and 'sample'.

    Raises
    ------
    ValueError
        If the required columns are not present in the input DataFrame.
    """
    required_columns = {'Pathway', 'compound_pathway', 'sample', 'ko'}
    if not required_columns.issubset(merged_df.columns):
        missing = required_columns - set(merged_df.columns)
        logger.error(f"Missing columns in input DataFrame: {missing}")
        raise ValueError(f"Missing columns in input DataFrame: {missing}")

    logger.info("Grouping data by 'Pathway', 'compound_pathway', and 'sample' to count unique KO entries.")

    grouped_df = (
        merged_df
        .groupby(['Pathway', 'compound_pathway', 'sample'])['ko']
        .nunique()
        .reset_index(name='ko_count')
    )

    logger.info("Grouping complete. Returning grouped DataFrame.")
    return grouped_df
