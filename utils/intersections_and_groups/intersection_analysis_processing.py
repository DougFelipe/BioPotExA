import pandas as pd
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


def prepare_upsetplot_data(merged_data: pd.DataFrame, selected_samples: list) -> pd.DataFrame:
    """
    Prepares data for generating an UpSet plot based on merged input and database.

    Parameters
    ----------
    merged_data : pd.DataFrame
        The merged DataFrame containing at least the columns 'sample' and 'ko'.
    selected_samples : list
        A list of sample identifiers to include in the analysis.

    Returns
    -------
    pd.DataFrame
        A DataFrame with unique 'sample'-'ko' pairs for the selected samples.

    Raises
    ------
    ValueError
        If required columns are missing or inputs are invalid.
    """
    # Validação de tipos
    if not isinstance(merged_data, pd.DataFrame):
        raise ValueError("Expected merged_data to be a pandas DataFrame.")
    if not isinstance(selected_samples, list):
        raise ValueError("Expected selected_samples to be a list.")

    # Verificação de colunas
    required_cols = {"sample", "ko"}
    if not required_cols.issubset(merged_data.columns):
        missing = required_cols - set(merged_data.columns)
        raise ValueError(f"Missing required column(s): {missing}")

    logger.info("Filtering merged data for selected samples...")
    filtered_df = merged_data[merged_data['sample'].isin(selected_samples)]

    logger.info("Dropping duplicate sample/KO pairs...")
    unique_ko_df = filtered_df.drop_duplicates(subset=['sample', 'ko'])

    logger.info(f"Returning DataFrame with {len(unique_ko_df)} rows.")
    return unique_ko_df
