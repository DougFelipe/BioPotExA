import logging
import pandas as pd

# Configuração do logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

def process_compound_gene_ranking(merged_df: pd.DataFrame) -> pd.DataFrame:



    """
    Calculates the number of unique genes associated with each compound.

    Parameters
    ----------
    merged_df : pd.DataFrame
        DataFrame containing at least the columns 'compoundname' and 'genesymbol'.

    Returns
    -------
    pd.DataFrame
        A DataFrame with columns 'compoundname' and 'num_genes', sorted in descending order.

    Raises
    ------
    ValueError
        If the required columns are missing or if the input is empty.
    """
    required_columns = {'compoundname', 'genesymbol'}

    if merged_df.empty:
        logger.warning("Input DataFrame is empty.")
        raise ValueError("Input DataFrame is empty.")

    if not required_columns.issubset(merged_df.columns):
        missing = required_columns - set(merged_df.columns)
        logger.error(f"Missing required columns for gene ranking: {missing}")
        raise ValueError(f"Missing required columns: {missing}")

    logger.info("Grouping data by 'compoundname' and counting unique 'genesymbol'.")
    compound_gene_ranking = (
        merged_df.groupby('compoundname')['genesymbol']
        .nunique()
        .reset_index(name='num_genes')
        .sort_values(by='num_genes', ascending=False)
    )

    logger.info("Compound gene ranking DataFrame successfully generated.")
    return compound_gene_ranking
