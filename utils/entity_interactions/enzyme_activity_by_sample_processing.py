import pandas as pd
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def count_unique_enzyme_activities(merged_df: pd.DataFrame, sample: str) -> pd.DataFrame:
    """
    Counts the number of unique KOs associated with each enzyme activity for a given sample.

    Parameters
    ----------
    merged_df : pd.DataFrame
        DataFrame containing merged data, with expected columns: 'sample', 'enzyme_activity', 'ko'.
    sample : str
        The name of the sample to filter and analyze.

    Returns
    -------
    pd.DataFrame
        A DataFrame with columns 'enzyme_activity' and 'unique_ko_count',
        sorted in descending order of unique KO count.

    Raises
    ------
    ValueError
        If the required columns are missing or the sample is not found.
    """
    required_columns = {'sample', 'enzyme_activity', 'ko'}

    if not required_columns.issubset(merged_df.columns):
        missing = required_columns - set(merged_df.columns)
        logger.error(f"Missing required columns: {missing}")
        raise ValueError(f"Missing required columns: {missing}")

    if sample not in merged_df['sample'].unique():
        logger.error(f"Sample '{sample}' not found in data.")
        raise ValueError(f"Sample '{sample}' not found in data.")

    logger.info(f"Filtering data for sample: {sample}")
    filtered_df = merged_df[merged_df['sample'] == sample]

    logger.info("Counting unique KOs per enzyme activity.")
    enzyme_count = (
        filtered_df.groupby('enzyme_activity')['ko']
        .nunique()
        .reset_index(name='unique_ko_count')
    )

    logger.info("Sorting enzyme activities by unique KO count.")
    return enzyme_count.sort_values('unique_ko_count', ascending=False)
