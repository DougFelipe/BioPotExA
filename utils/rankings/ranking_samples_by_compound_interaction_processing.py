import logging
import pandas as pd

# Configure logging
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


def process_sample_ranking(merged_df: pd.DataFrame) -> pd.DataFrame:
    """
    Calculates the number of unique compounds associated with each sample.

    Parameters
    ----------
    merged_df : pd.DataFrame
        DataFrame that must include the columns 'sample' and 'compoundname'.

    Returns
    -------
    pd.DataFrame
        Ranked DataFrame with columns 'sample' and 'num_compounds', sorted by count.

    Raises
    ------
    ValueError
        If required columns are missing or if input is not a valid DataFrame.
    """
    logger.info("Starting process_sample_ranking...")

    if not isinstance(merged_df, pd.DataFrame):
        logger.error("Input is not a pandas DataFrame.")
        raise ValueError("Input must be a pandas DataFrame.")

    required_cols = {'sample', 'compoundname'}
    if not required_cols.issubset(merged_df.columns):
        missing = required_cols - set(merged_df.columns)
        logger.error(f"Missing required columns: {missing}")
        raise ValueError(f"Missing required columns: {missing}")

    try:
        # Group and count unique compounds per sample
        sample_ranking = (
            merged_df.groupby('sample')['compoundname']
            .nunique()
            .reset_index(name='num_compounds')
            .sort_values(by='num_compounds', ascending=False)
        )

        logger.info("Sample ranking successfully processed.")
        return sample_ranking

    except Exception as e:
        logger.exception("Failed to process sample ranking.")
        raise RuntimeError("Error occurred while processing sample ranking.") from e
