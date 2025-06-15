import pandas as pd
import logging

# Configure basic logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def process_sample_reference_heatmap(merged_df: pd.DataFrame) -> pd.DataFrame:
    """
    Process the input DataFrame to compute a pivot table representing the count 
    of unique compounds per sample-referenceAG combination.

    Parameters
    ----------
    merged_df : pd.DataFrame
        Input DataFrame containing columns: 'sample', 'referenceAG', 'compoundname'.

    Returns
    -------
    pd.DataFrame
        Pivoted DataFrame with 'referenceAG' as rows, 'sample' as columns, and 
        values representing the count of unique 'compoundname' entries.

    Raises
    ------
    ValueError
        If required columns are missing in the input DataFrame.
    """
    required_columns = {'sample', 'referenceAG', 'compoundname'}
    if not required_columns.issubset(merged_df.columns):
        missing = required_columns - set(merged_df.columns)
        logger.error(f"Missing required columns: {missing}")
        raise ValueError(f"The following required columns are missing: {missing}")

    logger.info("Grouping data by 'sample' and 'referenceAG' to count unique 'compoundname'")
    try:
        grouped_df = (
            merged_df.groupby(['sample', 'referenceAG'])['compoundname']
            .nunique()
            .reset_index()
        )

        logger.debug(f"Grouped DataFrame:\n{grouped_df.head()}")

        heatmap_pivot = (
            grouped_df.pivot(index='referenceAG', columns='sample', values='compoundname')
            .fillna(0)
        )

        logger.info("Successfully created pivot table for heatmap")
        return heatmap_pivot

    except Exception as e:
        logger.exception("Error while processing heatmap data")
        raise RuntimeError("Failed to process data for heatmap.") from e
