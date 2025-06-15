import pandas as pd
import logging

# Configure o logger
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")


def process_heatmap_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Processes input data to prepare a long-format DataFrame suitable for generating faceted heatmaps.

    Parameters
    ----------
    df : pd.DataFrame
        The input DataFrame containing 'compoundname', and multiple 'value_' and 'label_' prefixed columns.

    Returns
    -------
    pd.DataFrame
        A long-format DataFrame with standardized columns: 'compoundname', 'value', 'label', 'category', 'subcategoria'.

    Raises
    ------
    ValueError
        If no valid value/label pairs are found or the expected columns are missing.
    """
    logger.info("Starting processing of heatmap data.")

    # Drop unnecessary columns
    drop_cols = ['SMILES', 'cpd', 'ChEBI']
    df = df.drop(columns=drop_cols, errors='ignore')
    logger.debug(f"Dropped columns if present: {drop_cols}")

    # Identify value and label columns
    value_columns = [col for col in df.columns if col.startswith('value_')]
    label_columns = [col for col in df.columns if col.startswith('label_')]

    if not value_columns or not label_columns:
        logger.error("No 'value_' or 'label_' columns found in DataFrame.")
        raise ValueError("Input DataFrame must contain 'value_' and 'label_' columns.")

    # Category mapping
    category_mapping = {
        'NR': 'Nuclear Response',
        'SR': 'Stress Response',
        'Gen': 'Genomic',
        'Env': 'Environmental',
        'Org': 'Organic',
    }

    heatmap_data = []

    # Process each pair of value and label columns
    for value_col, label_col in zip(value_columns, label_columns):
        subcategoria = value_col.split('_', 1)[1]
        category_prefix = subcategoria.split('_')[0]
        mapped_category = category_mapping.get(category_prefix)

        if mapped_category:
            logger.debug(f"Processing: {value_col}, Category: {mapped_category}")
            subset = df[['compoundname', value_col, label_col]].rename(
                columns={value_col: 'value', label_col: 'label'}
            )
            subset['category'] = mapped_category
            subset['subcategoria'] = subcategoria
            heatmap_data.append(subset)

    if not heatmap_data:
        logger.error("No valid data was processed for heatmap generation.")
        raise ValueError("No valid columns were processed for the heatmap.")

    result_df = pd.concat(heatmap_data, ignore_index=True)
    logger.info("Heatmap data processing complete.")

    return result_df
