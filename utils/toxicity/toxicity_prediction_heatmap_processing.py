import pandas as pd

# -------------------------------
# Function: process_heatmap_data
# -------------------------------

def process_heatmap_data(df):
    """
    Processes data for generating a faceted toxicity heatmap.

    Parameters:
    - df (pd.DataFrame): The input data containing 'value_' and 'label_' columns.

    Returns:
    - pd.DataFrame: A transformed DataFrame with categorized data for heatmap generation.

    Raises:
    - ValueError: If no valid columns are processed for the heatmap.
    """
    # Drop unnecessary columns if they exist.
    columns_to_drop = ['SMILES', 'cpd', 'ChEBI']
    df = df.drop(columns=columns_to_drop, errors='ignore')

    # Select columns for values and labels.
    value_columns = [col for col in df.columns if col.startswith('value_')]
    label_columns = [col for col in df.columns if col.startswith('label_')]

    # Map main categories to subcategories.
    category_mapping = {
        'NR': 'Nuclear Response',
        'SR': 'Stress Response',
        'Gen': 'Genomic',
        'Env': 'Environmental',
        'Org': 'Organic',
    }

    # Transform the data for heatmap generation.
    heatmap_data = []
    for value_col, label_col in zip(value_columns, label_columns):
        # Extract the subcategory and map it to a main category.
        subcategoria = value_col.split('_', 1)[1]
        category_prefix = subcategoria.split('_')[0]
        mapped_category = category_mapping.get(category_prefix, None)

        if mapped_category:
            # Create a subset of data for the current category.
            df_subset = df[['compoundname', value_col, label_col]].rename(
                columns={value_col: 'value', label_col: 'label'}
            )
            df_subset['category'] = mapped_category
            df_subset['subcategoria'] = subcategoria
            heatmap_data.append(df_subset)

    # Ensure at least one valid column was processed.
    if not heatmap_data:
        raise ValueError("No valid columns were processed for the heatmap.")

    # Combine the transformed data into a single DataFrame.
    result_df = pd.concat(heatmap_data, ignore_index=True)

    # Return the combined DataFrame.
    return result_df
