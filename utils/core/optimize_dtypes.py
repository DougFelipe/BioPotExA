import pandas as pd
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def optimize_dtypes(df: pd.DataFrame) -> pd.DataFrame:
    """
    Optimize data types by converting repetitive string columns to categorical.

    Parameters
    ----------
    df : pd.DataFrame
        Input DataFrame to be optimized.

    Returns
    -------
    pd.DataFrame
        DataFrame with optimized dtypes to reduce memory usage.
    
    Raises
    ------
    TypeError
        If input is not a pandas DataFrame.
    """
    if not isinstance(df, pd.DataFrame):
        logger.error("Input must be a pandas DataFrame.")
        raise TypeError("Input must be a pandas DataFrame.")

    categorical_columns = [
        'ko', 'genesymbol', 'genename', 'cpd', 'compoundclass',
        'referenceAG', 'compoundname', 'enzyme_activity', 'sample'
    ]

    for col in categorical_columns:
        if col in df.columns:
            logger.debug(f"Converting column '{col}' to categorical.")
            df[col] = df[col].astype('category')
        else:
            logger.info(f"Column '{col}' not found. Skipping.")

    logger.info("DataFrame optimization (general) completed.")
    return df


def optimize_kegg_dtypes(df: pd.DataFrame) -> pd.DataFrame:
    """
    Optimize KEGG DataFrame by converting repetitive columns to categorical.

    Parameters
    ----------
    df : pd.DataFrame
        Input KEGG DataFrame.

    Returns
    -------
    pd.DataFrame
        Optimized KEGG DataFrame.
    
    Raises
    ------
    TypeError
        If input is not a pandas DataFrame.
    """
    if not isinstance(df, pd.DataFrame):
        logger.error("Input must be a pandas DataFrame.")
        raise TypeError("Input must be a pandas DataFrame.")

    kegg_columns = ['ko', 'pathname', 'genesymbol', 'sample']

    for col in kegg_columns:
        if col in df.columns:
            logger.debug(f"Converting column '{col}' to categorical.")
            df[col] = df[col].astype('category')
        else:
            logger.info(f"Column '{col}' not found in KEGG DataFrame. Skipping.")

    logger.info("KEGG DataFrame optimization completed.")
    return df


def optimize_hadeg_dtypes(df: pd.DataFrame) -> pd.DataFrame:
    """
    Optimize HADEG DataFrame by converting repetitive columns to categorical.

    Parameters
    ----------
    df : pd.DataFrame
        Input HADEG DataFrame.

    Returns
    -------
    pd.DataFrame
        Optimized HADEG DataFrame.
    
    Raises
    ------
    TypeError
        If input is not a pandas DataFrame.
    """
    if not isinstance(df, pd.DataFrame):
        logger.error("Input must be a pandas DataFrame.")
        raise TypeError("Input must be a pandas DataFrame.")

    hadeg_columns = ['Gene', 'ko', 'Pathway', 'compound_pathway', 'sample']

    for col in hadeg_columns:
        if col in df.columns:
            logger.debug(f"Converting column '{col}' to categorical.")
            df[col] = df[col].astype('category')
        else:
            logger.info(f"Column '{col}' not found in HADEG DataFrame. Skipping.")

    logger.info("HADEG DataFrame optimization completed.")
    return df


def optimize_toxcsm_dtypes(df: pd.DataFrame) -> pd.DataFrame:
    """
    Optimize ToxCSM DataFrame by converting repetitive columns to categorical and
    numeric columns to float32.

    Parameters
    ----------
    df : pd.DataFrame
        Input ToxCSM DataFrame.

    Returns
    -------
    pd.DataFrame
        Optimized ToxCSM DataFrame.
    
    Raises
    ------
    TypeError
        If input is not a pandas DataFrame.
    """
    if not isinstance(df, pd.DataFrame):
        logger.error("Input must be a pandas DataFrame.")
        raise TypeError("Input must be a pandas DataFrame.")

    categorical_columns = ['SMILES', 'cpd', 'ChEBI', 'compoundname', 'sample']
    for col in categorical_columns:
        if col in df.columns:
            logger.debug(f"Converting column '{col}' to categorical.")
            df[col] = df[col].astype('category')
        else:
            logger.info(f"Column '{col}' not found in ToxCSM DataFrame. Skipping.")

    # Handle label_* columns
    label_columns = [col for col in df.columns if col.startswith('label_')]
    for col in label_columns:
        logger.debug(f"Converting label column '{col}' to categorical.")
        df[col] = df[col].astype('category')

    # Handle value_* columns
    value_columns = [col for col in df.columns if col.startswith('value_')]
    for col in value_columns:
        try:
            logger.debug(f"Converting value column '{col}' to float32.")
            df[col] = pd.to_numeric(df[col], errors='coerce').astype('float32')
        except Exception as e:
            logger.warning(f"Failed to convert column '{col}' to float32: {e}")

    logger.info("ToxCSM DataFrame optimization completed.")
    return df
