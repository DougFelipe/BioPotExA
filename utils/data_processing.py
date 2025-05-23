"""
data_processing.py
------------------

This module provides utility functions for data processing, specifically focused on merging 
user-provided data with various biological and chemical reference databases. The supported 
databases include KEGG, HADEG, and ToxCSM, each used to enrich the input data with contextual 
information for further analysis or export.

The functions are designed to handle common file formats such as CSV and Excel and perform
validation checks on the presence of required columns for merging operations (e.g., 'ko', 'cpd').

Intended Use:
    This module is intended to be used in data-driven Dash applications or standalone data
    preparation scripts where enrichment of input tables with biological pathway, enzymatic,
    or toxicological metadata is required.

Modules and Tools Used:
    - pandas: for DataFrame operations and I/O
    - os: for file path handling and existence checks
    - scipy (optional): distance calculations and clustering (available for extensibility)
    - plotly (optional): placeholder for future data visualization components

Main Functions:
    - merge_input_with_database: Merges input data with the main reference database (BioRemPP).
    - merge_input_with_database_hadegDB: Merges with the HADEG enzyme database.
    - merge_with_kegg: Integrates KEGG degradation pathway metadata.
    - merge_with_toxcsm: Merges input with ToxCSM toxicity prediction data.

Example Usage:
    >>> import pandas as pd
    >>> from data_processing import merge_input_with_database
    >>> df_input = pd.DataFrame({"ko": ["K00001", "K00002"]})
    >>> merged_df = merge_input_with_database(df_input)

Author:
    Your Name (Douglas Felipe)

Version:
    1.0.0

Last Updated:
    2025-04-22

License:
    MIT License

Notes:
    Ensure that all required input columns are present before using these functions.
    File paths should point to valid CSV or Excel files.

"""

# -------------------------------
# Imports
# -------------------------------
import scipy.spatial.distance as ssd
import scipy.cluster.hierarchy as sch

# Data manipulation and handling DataFrame structures.
import pandas as pd

# Plotly modules for creating visualizations (unused in the current script but included for extensibility).
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots

# Scipy modules for distance calculations and hierarchical clustering.
import scipy.spatial.distance as ssd
import scipy.cluster.hierarchy as sch
# -------------------------------
# Functions for Data Merging
# -------------------------------
import os
import pandas as pd

def merge_input_with_database(input_data: pd.DataFrame, database_filepath: str = None) -> pd.DataFrame:
    """
    Merges input data with a reference database file (CSV or Excel format), using a default path if none is provided.

    Parameters:
        input_data (pd.DataFrame): The input DataFrame to be merged.
        database_filepath (str, optional): Path to the database file. Defaults to 'data/database.csv'.

    Returns:
        pd.DataFrame: The resulting merged DataFrame.

    Raises:
        FileNotFoundError: If the database file is not found at the specified path.
        ValueError: If the file extension is unsupported.
        KeyError: If the 'ko' column is missing from either DataFrame.

    Example:
        >>> df = pd.DataFrame({"ko": ["K00001"]})
        >>> merge_input_with_database(df)

    Notes:
        The input and database DataFrames must both contain a column named 'ko' to perform the merge.
    """
    if database_filepath is None:
        database_filepath = os.path.join("data", "database.csv")

    if not os.path.exists(database_filepath):
        raise FileNotFoundError(f"Database file not found: {database_filepath}")

    if database_filepath.endswith('.csv'):
        database_df = pd.read_csv(database_filepath, encoding='utf-8', sep=';')
    elif database_filepath.endswith('.xlsx'):
        database_df = pd.read_excel(database_filepath, engine='openpyxl')
    else:
        raise ValueError("Unsupported file format. Use .csv or .xlsx")

    if 'ko' not in input_data.columns or 'ko' not in database_df.columns:
        raise KeyError("Column 'ko' must be present in both input and database DataFrames.")

    merged_df = pd.merge(input_data, database_df, on='ko', how='inner')
    return merged_df


def merge_with_kegg(input_df: pd.DataFrame, kegg_filepath: str = None) -> pd.DataFrame:
    """
    Merges input data with KEGG degradation pathway information from a CSV or Excel file.

    Parameters:
        input_df (pd.DataFrame): The input DataFrame to be merged.
        kegg_filepath (str, optional): Path to the KEGG data file. Defaults to 'data/kegg_20degradation_pathways.csv'.

    Returns:
        pd.DataFrame: The resulting merged DataFrame.

    Raises:
        FileNotFoundError: If the KEGG file does not exist.
        ValueError: If the file format is not supported.
        KeyError: If 'ko' column is missing in either DataFrame.

    Example:
        >>> df = pd.DataFrame({"ko": ["K00123"]})
        >>> merge_with_kegg(df)

    Notes:
        The 'ko' column must be present in both the input and KEGG pathway DataFrames.
    """
    if kegg_filepath is None:
        kegg_filepath = os.path.join("data", "kegg_20degradation_pathways.csv")

    if not os.path.exists(kegg_filepath):
        raise FileNotFoundError(f"KEGG file not found: {kegg_filepath}")

    if kegg_filepath.endswith('.csv'):
        kegg_df = pd.read_csv(kegg_filepath, encoding='utf-8', sep=';')
    elif kegg_filepath.endswith('.xlsx'):
        kegg_df = pd.read_excel(kegg_filepath, engine='openpyxl')
    else:
        raise ValueError("Unsupported file format. Use .csv or .xlsx")

    if 'ko' not in input_df.columns or 'ko' not in kegg_df.columns:
        raise KeyError("Column 'ko' must be present in both input and KEGG DataFrames.")

    merged_df = pd.merge(input_df, kegg_df, on='ko', how='inner')
    return merged_df


def merge_input_with_database_hadegDB(input_data: pd.DataFrame, database_filepath: str = None) -> pd.DataFrame:
    """
    Merges input data with the HADEG database (CSV or Excel), using a default path if none is provided.

    Parameters:
        input_data (pd.DataFrame): The input DataFrame to be merged.
        database_filepath (str, optional): Path to the HADEG database file. Defaults to 'data/database_hadegDB.csv'.

    Returns:
        pd.DataFrame: The resulting merged DataFrame.

    Raises:
        FileNotFoundError: If the HADEG database file is not found.
        ValueError: If the file format is not supported.
        KeyError: If the 'ko' column is missing in either DataFrame.

    Example:
        >>> df = pd.DataFrame({"ko": ["K00002"]})
        >>> merge_input_with_database_hadegDB(df)

    Notes:
        The merge is performed using the 'ko' column, which must exist in both input and HADEG database.
    """
    if database_filepath is None:
        database_filepath = os.path.join("data", "database_hadegDB.csv")

    if not os.path.exists(database_filepath):
        raise FileNotFoundError(f"HADEG database file not found: {database_filepath}")

    if database_filepath.endswith('.csv'):
        database_df = pd.read_csv(database_filepath, encoding='utf-8', sep=';')
    elif database_filepath.endswith('.xlsx'):
        database_df = pd.read_excel(database_filepath, engine='openpyxl')
    else:
        raise ValueError("Unsupported file format. Use .csv or .xlsx")

    if 'ko' not in input_data.columns or 'ko' not in database_df.columns:
        raise KeyError("Column 'ko' must be present in both input and HADEG database DataFrames.")

    merged_df = pd.merge(input_data, database_df, on='ko', how='inner')
    return merged_df


def merge_with_toxcsm(merged_df: pd.DataFrame, toxcsm_filepath: str = None) -> pd.DataFrame:
    """
    Merges a previously merged DataFrame with the ToxCSM database (CSV or Excel), based on the 'cpd' column.

    Parameters:
        merged_df (pd.DataFrame): DataFrame containing columns like 'sample', 'compoundclass', 'cpd', and 'ko'.
        toxcsm_filepath (str, optional): Path to the ToxCSM database file. Defaults to 'data/database_toxcsm.csv'.

    Returns:
        pd.DataFrame: The final merged DataFrame including ToxCSM data.

    Raises:
        FileNotFoundError: If the ToxCSM file does not exist.
        ValueError: If the file format is not supported.
        KeyError: If required columns ('cpd', etc.) are missing in the input DataFrame or ToxCSM database.

    Example:
        >>> df = pd.DataFrame({"sample": ["A"], "compoundclass": ["Aromatic"], "cpd": ["C00123"], "ko": ["K00003"]})
        >>> merge_with_toxcsm(df)

    Notes:
        The function filters and merges only the necessary columns before merging with the ToxCSM database.
    """
    if toxcsm_filepath is None:
        toxcsm_filepath = os.path.join("data", "database_toxcsm.csv")

    if not os.path.exists(toxcsm_filepath):
        raise FileNotFoundError(f"ToxCSM database file not found: {toxcsm_filepath}")

    if toxcsm_filepath.endswith('.csv'):
        toxcsm_df = pd.read_csv(toxcsm_filepath, encoding='utf-8', sep=';')
    elif toxcsm_filepath.endswith('.xlsx'):
        toxcsm_df = pd.read_excel(toxcsm_filepath, engine='openpyxl')
    else:
        raise ValueError("Unsupported file format. Use .csv or .xlsx")

    for col in ['sample', 'compoundclass', 'cpd', 'ko']:
        if col not in merged_df.columns:
            raise KeyError(f"Required column '{col}' is missing in the input DataFrame.")

    if 'cpd' not in toxcsm_df.columns:
        raise KeyError("Column 'cpd' is required in the ToxCSM database.")

    merged_df_reduced = merged_df[['sample', 'compoundclass', 'cpd', 'ko']].drop_duplicates()
    final_merged_df = pd.merge(merged_df_reduced, toxcsm_df, on='cpd', how='inner')

    return final_merged_df


"""
P1_COUNT_KO
-----------
This script contains utility functions to process KO (KEGG Orthology) data, 
including counting unique KOs per sample, pathway, or other groupings. 
It also includes basic preprocessing functions for compound data visualization.
"""

# -------------------------------
# Function: process_ko_data
# -------------------------------

def process_ko_data(merged_df):
    """
    Processes KO data to count unique KOs for each sample.

    Parameters:
    - merged_df: DataFrame with merged data or a list of dictionaries convertible to a DataFrame.

    Returns:
    - pd.DataFrame: A DataFrame containing the count of unique KOs per sample, sorted in descending order.
    """
    if isinstance(merged_df, list):
        # Convert the list of dictionaries to a pandas DataFrame if needed.
        merged_df = pd.DataFrame(merged_df)
    elif not isinstance(merged_df, pd.DataFrame):
        # Raise an error if the input is not a DataFrame or a list of dictionaries.
        raise ValueError("The merged_df argument must be a pandas DataFrame or a list of dictionaries.")
    
    # Count unique 'ko' values for each 'sample'.
    ko_count = merged_df.groupby('sample')['ko'].nunique().reset_index(name='ko_count')
    
    # Sort the results by the count of KOs in descending order.
    ko_count_sorted = ko_count.sort_values('ko_count', ascending=False)
    
    # Return the sorted DataFrame with KO counts.
    return ko_count_sorted

# -------------------------------
# Function: process_ko_data_violin
# -------------------------------

def process_ko_data_violin(df):
    """
    Processes KO data for generating violin plots by counting unique KOs per sample.

    Parameters:
    - df: DataFrame containing input data.

    Returns:
    - pd.DataFrame: A DataFrame with the count of unique KOs per sample.
    """
    # Count unique 'ko' values for each 'sample'.
    ko_count_per_sample = df.groupby('sample')['ko'].nunique().reset_index(name='ko_count')
    
    # Return the DataFrame with KO counts.
    return ko_count_per_sample

# -------------------------------
# Function: count_ko_per_pathway
# -------------------------------

def count_ko_per_pathway(merged_df):
    """
    Counts unique KOs for each pathway in each sample.

    Parameters:
    - merged_df: DataFrame resulting from merging with KEGG data.

    Returns:
    - pd.DataFrame: A DataFrame containing the count of unique KOs per pathway for each sample.

    Raises:
    - KeyError: If the 'pathname' column is not present in the input DataFrame.
    """
    # Check if the 'pathname' column exists in the DataFrame.
    if 'pathname' not in merged_df.columns:
        print("The available columns in the DataFrame are:", merged_df.columns)
        raise KeyError("'pathname' column not found in the DataFrame.")
    
    # Group by 'sample' and 'pathname', counting unique 'ko' values.
    pathway_count = merged_df.groupby(['sample', 'pathname'])['ko'].nunique().reset_index(name='unique_ko_count')
    
    # Return the DataFrame with KO counts per pathway.
    return pathway_count

# -------------------------------
# Function: count_ko_per_sample_for_pathway
# -------------------------------

def count_ko_per_sample_for_pathway(merged_df, selected_pathway):
    """
    Counts unique KOs for a specific pathway in each sample.

    Parameters:
    - merged_df: DataFrame resulting from merging with KEGG data.
    - selected_pathway: The selected pathway to filter data.

    Returns:
    - pd.DataFrame: A DataFrame containing the count of unique KOs per sample for the selected pathway.
    """
    # Filter the DataFrame to include only the selected pathway.
    filtered_df = merged_df[merged_df['pathname'] == selected_pathway]
    
    # Group by 'sample', counting unique 'ko' values.
    sample_count = filtered_df.groupby('sample')['ko'].nunique().reset_index(name='unique_ko_count')
    
    # Sort the results by KO count in descending order.
    return sample_count.sort_values('unique_ko_count', ascending=False)

# -------------------------------
# Function: process_compound_data
# -------------------------------

def process_compound_data(merged_df):
    """
    Processes data for compound scatter plot visualization.

    Parameters:
    - merged_df: DataFrame containing merged data.

    Returns:
    - pd.DataFrame: The input DataFrame, potentially modified for visualization.
    """
    # Currently, the function returns the input DataFrame as is.
    # Additional processing logic can be implemented if needed.
    return merged_df

# Função para processar ranking de amostras
# utils/data_processing.py

# -------------------------------
# Function: process_sample_ranking (P4_rank_samples)
# -------------------------------

def process_sample_ranking(merged_df):
    """
    Processes the data to calculate the number of unique compounds associated with each sample.

    Parameters:
    - merged_df (pd.DataFrame): The DataFrame resulting from merging with the database.

    Returns:
    - pd.DataFrame: A DataFrame containing the samples and the count of unique compounds, 
                    sorted in descending order of compound count.
    """
    # Group by 'sample' and calculate the number of unique 'compoundname' entries for each sample.
    sample_ranking = merged_df.groupby('sample')['compoundname'].nunique().reset_index(name='num_compounds')
    
    # Sort the results by the number of unique compounds in descending order.
    sample_ranking = sample_ranking.sort_values(by='num_compounds', ascending=False)
    
    # Return the resulting ranked DataFrame.
    return sample_ranking

# -------------------------------
# Function: process_compound_ranking (P5_rank_compounds)
# -------------------------------

def process_compound_ranking(merged_df):
    """
    Processes the data to calculate the number of unique samples associated with each compound.

    Parameters:
    - merged_df (pd.DataFrame): The DataFrame resulting from merging with the database.

    Returns:
    - pd.DataFrame: A DataFrame containing the compounds and the count of unique samples, 
                    sorted in descending order of sample count.
    """
    # Group by 'compoundname' and calculate the number of unique 'sample' entries for each compound.
    compound_ranking = merged_df.groupby('compoundname')['sample'].nunique().reset_index(name='num_samples')
    
    # Sort the results by the number of unique samples in descending order.
    compound_ranking = compound_ranking.sort_values(by='num_samples', ascending=False)
    
    # Return the resulting ranked DataFrame.
    return compound_ranking

# -------------------------------
# Function: process_compound_gene_ranking (P6_rank_genes)
# -------------------------------

def process_compound_gene_ranking(merged_df):
    """
    Processes the data to calculate the number of unique genes associated with each compound.

    Parameters:
    - merged_df (pd.DataFrame): The DataFrame resulting from merging with the database.

    Returns:
    - pd.DataFrame: A DataFrame containing the compounds and the count of unique genes, 
                    sorted in descending order of gene count.
    """
    # Group by 'compoundname' and calculate the number of unique 'genesymbol' entries for each compound.
    compound_gene_ranking = merged_df.groupby('compoundname')['genesymbol'].nunique().reset_index(name='num_genes')
    
    # Sort the results by the number of unique genes in descending order.
    compound_gene_ranking = compound_gene_ranking.sort_values(by='num_genes', ascending=False)
    
    # Return the resulting ranked DataFrame.
    return compound_gene_ranking



# -------------------------------
# P7: Function: process_gene_compound_association
# -------------------------------

def process_gene_compound_association(merged_df):
    """
    Processes the data to calculate the number of unique compounds associated with each gene.

    Parameters:
    - merged_df (pd.DataFrame): The DataFrame resulting from merging with the database.

    Returns:
    - pd.DataFrame: A DataFrame containing the genes and the count of unique compounds, 
                    sorted in descending order of compound count.
    """
    # Group by 'genesymbol' and calculate the number of unique 'compoundname' entries.
    gene_compound_association = merged_df.groupby('genesymbol')['compoundname'].nunique().reset_index(name='num_compounds')
    
    # Sort the results by the number of unique compounds in descending order.
    gene_compound_association = gene_compound_association.sort_values(by='num_compounds', ascending=False)
    
    # Return the resulting ranked DataFrame.
    return gene_compound_association

# -------------------------------
# P8: Function: process_gene_sample_association
# -------------------------------

def process_gene_sample_association(merged_df):
    """
    Processes the data to calculate the number of unique compounds associated with each gene.

    Parameters:
    - merged_df (pd.DataFrame): The DataFrame resulting from merging with the database.

    Returns:
    - pd.DataFrame: A DataFrame containing the genes and the count of unique compounds, 
                    sorted in descending order of compound count.
    """
    # Group by 'genesymbol' and calculate the number of unique 'compoundname' entries.
    gene_sample_association = merged_df.groupby('genesymbol')['compoundname'].nunique().reset_index(name='num_compounds')
    
    # Sort the results by the number of unique compounds in descending order.
    gene_sample_association = gene_sample_association.sort_values(by='num_compounds', ascending=False)
    
    # Return the resulting ranked DataFrame.
    return gene_sample_association

# -------------------------------
# P9: Function: process_sample_reference_heatmap
# -------------------------------

def process_sample_reference_heatmap(merged_df):
    """
    Processes the data to calculate the count of 'compoundname' for each combination of 'sample' and 'referenceAG'.

    Parameters:
    - merged_df (pd.DataFrame): The DataFrame resulting from merging with the database.

    Returns:
    - pd.DataFrame: A pivoted DataFrame suitable for creating a heatmap.
    """
    # Group by 'sample' and 'referenceAG', counting unique 'compoundname' entries.
    heatmap_df = merged_df.groupby(['sample', 'referenceAG'])['compoundname'].nunique().reset_index()
    
    # Pivot the grouped DataFrame to create a matrix with 'referenceAG' as rows and 'sample' as columns.
    heatmap_pivot = heatmap_df.pivot(index='referenceAG', columns='sample', values='compoundname').fillna(0)
    
    # Return the pivoted DataFrame.
    return heatmap_pivot

# -------------------------------
# P10: Function: group_by_class
# -------------------------------

def group_by_class(compoundclass_choice, tabela):
    """
    Groups samples by their gene profiles for a specific class of compounds.

    Parameters:
    - compoundclass_choice (str): The selected compound class to filter the data.
    - tabela (pd.DataFrame): The input DataFrame containing compound, sample, and class information.

    Returns:
    - pd.DataFrame: A DataFrame with an additional 'grupo' column indicating group membership.
    """
    # Filter the table to include only rows matching the selected compound class.
    dados_selecionados = tabela[tabela['compoundclass'] == compoundclass_choice]
    
    grupos = []  # List to store groups of samples and compounds.
    
    # Iterate over unique samples in the filtered table.
    for sample in dados_selecionados['sample'].unique():
        # Get the list of unique compounds for the current sample.
        compostos = dados_selecionados.loc[dados_selecionados['sample'] == sample, 'compoundname'].unique().tolist()
        
        if len(compostos) > 0:
            grupo_existente = False
            # Check if the current compounds match any existing group.
            for grupo in grupos:
                if set(compostos) == set(grupo['compostos']):
                    grupo_existente = True
                    grupo['samples'].append(sample)
                    break
            
            # If no matching group exists, create a new group.
            if not grupo_existente:
                novo_grupo = {'compostos': compostos, 'samples': [sample]}
                grupos.append(novo_grupo)
    
    # Add a 'grupo' column to the table and assign group labels.
    tabela_grupos = tabela.copy()
    tabela_grupos['grupo'] = None
    
    for i, grupo in enumerate(grupos):
        grupo_samples = grupo['samples']
        grupo_compostos = grupo['compostos']
        tabela_grupos.loc[(tabela_grupos['sample'].isin(grupo_samples)) & 
                          (tabela_grupos['compoundname'].isin(grupo_compostos)), 
                          'grupo'] = f"{compoundclass_choice} - Group {i+1}"
    
    # Return the filtered table with group assignments.
    tabela_grupos = tabela_grupos[tabela_grupos['compoundclass'] == compoundclass_choice]
    return tabela_grupos

# -------------------------------
# Function: minimize_groups
# -------------------------------

def minimize_groups(df):
    """
    Reduces the number of groups to cover all compounds with minimal redundancy.

    Parameters:
    - df (pd.DataFrame): The input DataFrame containing group and compound information.

    Returns:
    - list: A list of selected groups that minimally cover all compounds.
    """
    # Group compounds by 'grupo' and convert to lists of unique compounds.
    group_compounds = df.groupby('grupo')['compoundname'].apply(lambda x: list(set(x))).reset_index()
    
    all_compounds = df['compoundname'].unique().tolist()  # List of all unique compounds.
    selected_groups = []  # List to store selected groups.
    
    # Iteratively select groups to cover all compounds.
    while len(all_compounds) > 0:
        max_cover = 0
        best_group = None
        
        # Find the group that covers the most remaining compounds.
        for i in range(len(group_compounds)):
            group = group_compounds.iloc[i]['grupo']
            compounds = group_compounds.iloc[i]['compoundname']
            cover = len(set(all_compounds) & set(compounds))
            
            if cover > max_cover:
                max_cover = cover
                best_group = group
        
        # Remove the compounds covered by the selected group from the remaining list.
        all_compounds = list(set(all_compounds) - set(group_compounds.loc[group_compounds['grupo'] == best_group, 'compoundname'].values[0]))
        
        # Add the selected group to the list and remove it from consideration.
        selected_groups.append(best_group)
        group_compounds = group_compounds[group_compounds['grupo'] != best_group]
    
    # Return the list of selected groups.
    return selected_groups



# -------------------------------
# P11: Function: process_gene_sample_data
# -------------------------------

def process_gene_sample_data(merged_df):
    """
    Processes the data to generate a DataFrame grouped by sample, gene, compound pathway, and pathway, 
    counting the number of unique KOs.

    Parameters:
    - merged_df (pd.DataFrame): The DataFrame resulting from merging input data with the database.

    Returns:
    - pd.DataFrame: A DataFrame grouped by 'sample', 'Gene', 'compound_pathway', and 'Pathway' 
                    with the count of unique KOs.
    """
    # Group by 'sample', 'Gene', 'compound_pathway', and 'Pathway' and count unique 'ko' values.
    grouped_df = merged_df.groupby(['sample', 'Gene', 'compound_pathway', 'Pathway'])['ko'].nunique().reset_index(name='ko_count')
    
    # Return the grouped DataFrame with KO counts.
    return grouped_df

# -------------------------------
# P12: Function: process_pathway_data
# -------------------------------

def process_pathway_data(merged_df):
    """
    Processes the data to generate a DataFrame grouped by pathway, compound pathway, and sample, 
    counting the number of unique KOs.

    Parameters:
    - merged_df (pd.DataFrame): The DataFrame resulting from merging input data with the database.

    Returns:
    - pd.DataFrame: A DataFrame grouped by 'Pathway', 'compound_pathway', and 'sample' 
                    with the count of unique KOs.
    """
    # Group by 'Pathway', 'compound_pathway', and 'sample' and count unique 'ko' values.
    grouped_df = merged_df.groupby(['Pathway', 'compound_pathway', 'sample'])['ko'].nunique().reset_index(name='ko_count')
    
    # Return the grouped DataFrame with KO counts.
    return grouped_df

# -------------------------------
# Function: get_ko_per_sample_for_pathway
# -------------------------------

def get_ko_per_sample_for_pathway(merged_df, selected_pathway):
    """
    Filters the data to return the unique KOs associated with each sample for a selected pathway.

    Parameters:
    - merged_df (pd.DataFrame): The DataFrame resulting from merging with KEGG data.
    - selected_pathway (str): The selected metabolic pathway to filter data.

    Returns:
    - pd.DataFrame: A DataFrame containing 'sample' and 'genesymbol' for the selected pathway.
                    Returns an empty DataFrame if no data is found.
    """
    # Filter the DataFrame for the selected pathway.
    filtered_df = merged_df[merged_df['pathname'] == selected_pathway]
    
    # If the filtered DataFrame is empty, return a DataFrame with specified columns but no data.
    if filtered_df.empty:
        return pd.DataFrame(columns=['sample', 'genesymbol'])
    
    # Drop duplicates and return a DataFrame with 'sample' and 'genesymbol' columns.
    return filtered_df[['sample', 'genesymbol']].drop_duplicates()

# -------------------------------
# Function: count_unique_enzyme_activities
# -------------------------------

def count_unique_enzyme_activities(merged_df, sample):
    """
    Counts the unique enzyme activities associated with a selected sample.

    Parameters:
    - merged_df (pd.DataFrame): The DataFrame resulting from merging input data with the database.
    - sample (str): The name of the selected sample.

    Returns:
    - pd.DataFrame: A DataFrame containing the enzyme activities and the count of unique KOs 
                    associated with each activity, sorted in descending order.
    """
    # Filter the DataFrame for the selected sample.
    filtered_df = merged_df[merged_df['sample'] == sample]
    
    # Group by 'enzyme_activity' and count unique 'ko' values.
    enzyme_count = filtered_df.groupby('enzyme_activity')['ko'].nunique().reset_index(name='unique_ko_count')
    
    # Sort the results by the count of unique KOs in descending order.
    return enzyme_count.sort_values('unique_ko_count', ascending=False)



# -------------------------------
# P15: Function: calculate_sample_clustering
# -------------------------------


def calculate_sample_clustering(input_df, distance_metric, method):
    """
    Calculates a clustering matrix based on user input.

    Parameters:
    - input_df (pd.DataFrame): The input data containing 'sample' and 'ko' columns.
    - distance_metric (str): The selected distance metric (e.g., 'euclidean', 'cityblock').
    - method (str): The selected clustering method (e.g., 'single', 'ward').

    Returns:
    - np.ndarray: The clustering matrix calculated using the given metric and method.
    """
    # Pivot the input data to create a sample-by-KO matrix.
    pivot_df = input_df.pivot_table(index='sample', columns='ko', aggfunc='size', fill_value=0)

    # Calculate the distance matrix using the specified metric.
    distance_matrix = ssd.pdist(pivot_df, metric=distance_metric)

    # Perform hierarchical clustering using the specified method.
    clustering_matrix = sch.linkage(distance_matrix, method=method)

    # Return the clustering matrix.
    return clustering_matrix

# -------------------------------
# P16: Function: prepare_upsetplot_data
# -------------------------------

def prepare_upsetplot_data(merged_data, selected_samples):
    """
    Prepares data for generating an UpSet plot based on merged input and database.

    Parameters:
    - merged_data (pd.DataFrame): The merged data containing 'sample' and 'ko' columns.
    - selected_samples (list): A list of selected samples.

    Returns:
    - pd.DataFrame: A DataFrame containing the selected samples and their unique KOs.
    """
    # Filter the data to include only the selected samples.
    filtered_df = merged_data[merged_data['sample'].isin(selected_samples)]

    # Drop duplicate entries for 'sample' and 'ko' pairs.
    unique_ko_df = filtered_df.drop_duplicates(subset=['sample', 'ko'])

    # Return the filtered DataFrame.
    return unique_ko_df

# -------------------------------
# P17: Function: prepare_gene_compound_network_data
# -------------------------------

import pandas as pd
from utils.data_processing import merge_input_with_database

def prepare_gene_compound_network_data(stored_data):
    """
    Prepares data for creating a Gene-Compound network graph.

    Parameters:
    - stored_data (dict): The stored data in dictionary format.

    Returns:
    - pd.DataFrame: A DataFrame containing gene-compound relationships.

    Raises:
    - ValueError: If the stored data is empty.
    - KeyError: If required columns ('genesymbol', 'cpd') are missing.
    """
    input_df = pd.DataFrame(stored_data)

    # Ensure the data is not empty.
    if input_df.empty:
        raise ValueError("The stored-data is empty.")

    # Merge the input data with the database.
    merged_data = merge_input_with_database(input_df)

    # Check for required columns.
    if 'genesymbol' not in merged_data.columns or 'cpd' not in merged_data.columns:
        raise KeyError("Columns 'genesymbol' and 'cpd' are required to create the network graph.")

    # Filter relevant columns and remove duplicates.
    network_df = merged_data[['genesymbol', 'compoundname']].dropna().drop_duplicates()

    # Return the processed DataFrame.
    return network_df

# -------------------------------
# P18: Function: get_merged_toxcsm_data
# -------------------------------

def get_merged_toxcsm_data(input_data):
    """
    Merges input data with the ToxCSM database.

    Parameters:
    - input_data (list): Raw data stored in 'stored-data'.

    Returns:
    - pd.DataFrame: A processed DataFrame containing `value_` and `label_` columns.
    """
    # Ensure input data is available.
    if not input_data:
        return pd.DataFrame()  # Return an empty DataFrame.

    # Convert the input data to a DataFrame.
    input_df = pd.DataFrame(input_data)

    # Perform the first merge with the main database.
    merged_df = merge_input_with_database(input_df)
    if merged_df.empty:
        return pd.DataFrame()

    # Perform the second merge with the ToxCSM database.
    final_merged_df = merge_with_toxcsm(merged_df)
    if final_merged_df.empty:
        return pd.DataFrame()

    # Return the final merged DataFrame.
    return final_merged_df

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
