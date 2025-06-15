import logging
import pandas as pd

# Configure logging
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


def process_compound_ranking(merged_df: pd.DataFrame) -> pd.DataFrame:
    """
    Processes the merged dataset to compute the number of unique samples associated with each compound.

    Parameters
    ----------
    merged_df : pd.DataFrame
        Input DataFrame containing at least 'compoundname' and 'sample' columns.

    Returns
    -------
    pd.DataFrame
        DataFrame with columns 'compoundname' and 'num_samples',
        sorted in descending order of number of unique samples.

    Raises
    ------
    ValueError
        If required columns are missing in the input DataFrame.
    """
    required_columns = {'compoundname', 'sample'}

    logger.info("Starting compound ranking process.")

    # Validate required columns
    if not required_columns.issubset(merged_df.columns):
        missing = required_columns - set(merged_df.columns)
        logger.error(f"Missing required columns: {missing}")
        raise ValueError(f"Missing required columns: {missing}")

    try:
        # Compute unique sample count per compound
        compound_ranking = (
            merged_df.groupby("compoundname")["sample"]
            .nunique()
            .reset_index(name="num_samples")
        )

        logger.info("Successfully calculated compound ranking.")
        return compound_ranking.sort_values(by="num_samples", ascending=False)

    except Exception as e:
        logger.exception("Failed to compute compound ranking.")
        raise RuntimeError("Compound ranking processing failed.") from e
