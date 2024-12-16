"""
data_processing.py
------------------
This script contains utility functions for processing and merging data, specifically tailored 
for integrating input data with various external databases such as KEGG, HADEG, and ToxCSM.
"""

# -------------------------------
# Imports
# -------------------------------

# Import pandas for data manipulation and handling DataFrame structures.
import pandas as pd

# Import Plotly modules for creating visualizations (currently unused but included for extensibility).
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots

# -------------------------------
# Functions for Data Merging
# -------------------------------

def merge_input_with_database(input_data: pd.DataFrame, database_filepath: str = 'data/database.xlsx') -> pd.DataFrame:
    """
    Merges input data with the main database.

    Parameters:
    - input_data (pd.DataFrame): The input data to be merged.
    - database_filepath (str): Path to the Excel file containing the database. Default is 'data/database.xlsx'.

    Returns:
    - pd.DataFrame: The merged DataFrame.
    """
    # Load the database from the specified file.
    database_df = pd.read_excel(database_filepath)
    
    # Merge the input data with the database on the 'ko' column using an inner join.
    merged_df = pd.merge(input_data, database_df, on='ko', how='inner')
    
    # Return the resulting merged DataFrame.
    return merged_df

def merge_with_kegg(input_df: pd.DataFrame, kegg_path: str = 'data/kegg_20degradation_pathways.xlsx') -> pd.DataFrame:
    """
    Merges input data with KEGG pathway data.

    Parameters:
    - input_df (pd.DataFrame): The input data to be merged.
    - kegg_path (str): Path to the Excel file containing KEGG data. Default is 'data/kegg_20degradation_pathways.xlsx'.

    Returns:
    - pd.DataFrame: The merged DataFrame.
    """
    # Load the KEGG pathway data from the specified file.
    kegg_df = pd.read_excel(kegg_path)
    
    # Merge the input data with the KEGG data on the 'ko' column using an inner join.
    merged_df = pd.merge(input_df, kegg_df, on='ko', how='inner')
    
    # Return the resulting merged DataFrame.
    return merged_df

def merge_input_with_database_hadegDB(input_data: pd.DataFrame, database_filepath: str = 'data/database_hadegDB.xlsx') -> pd.DataFrame:
    """
    Merges input data with the HADEG database.

    Parameters:
    - input_data (pd.DataFrame): The input data to be merged.
    - database_filepath (str): Path to the Excel file containing the HADEG database. Default is 'data/database_hadegDB.xlsx'.

    Returns:
    - pd.DataFrame: The merged DataFrame.

    Raises:
    - KeyError: If the 'ko' column is not present in the resulting DataFrame.
    """
    # Load the HADEG database from the specified file.
    database_df = pd.read_excel(database_filepath)
    
    # Merge the input data with the HADEG database on the 'ko' column using an inner join.
    merged_df = pd.merge(input_data, database_df, on='ko', how='inner')
    
    # Verify that the 'ko' column exists in the merged DataFrame.
    if 'ko' not in merged_df.columns:
        raise KeyError("The 'ko' column is not present in the DataFrame after merging.")
    
    # Return the resulting merged DataFrame.
    return merged_df

def merge_with_toxcsm(merged_df: pd.DataFrame, toxcsm_filepath: str = 'data/database_toxcsm.xlsx') -> pd.DataFrame:
    """
    Merges the result of a previous merge with the ToxCSM database, retaining only specific columns.

    Parameters:
    - merged_df (pd.DataFrame): The DataFrame resulting from a previous merge operation.
    - toxcsm_filepath (str): Path to the Excel file containing the ToxCSM database. Default is 'data/database_toxcsm.xlsx'.

    Returns:
    - pd.DataFrame: The merged DataFrame.
    """
    # Load the ToxCSM database from the specified file.
    toxcsm_df = pd.read_excel(toxcsm_filepath)
    
    # Reduce the input DataFrame to retain only relevant columns and remove duplicates.
    merged_df_reduced = merged_df[['compoundclass', 'cpd', 'ko']].drop_duplicates()
    
    # Merge the reduced DataFrame with the ToxCSM database on the 'cpd' column using an inner join.
    final_merged_df = pd.merge(merged_df_reduced, toxcsm_df, on='cpd', how='inner')
    
    # Return the resulting merged DataFrame.
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


"""
P7_gene_compound_association, P8_gene_sample_association, P9_sample_reference_heatmap, P10_group_by_class
---------------------------------------------------------------------------------------------------------
This script contains utility functions for processing and grouping data related to genes, compounds, 
and samples. The functionalities include:
- Ranking genes by the number of unique compounds or samples.
- Preparing data for a heatmap of sample and reference associations.
- Grouping samples by gene profiles for specific compound classes.
- Minimizing group redundancy for compound classifications.
"""

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

# ----------------------------------------
# P11 HADEG HEATMAP ORTHOLOGS BY pathway
# ----------------------------------------
def process_gene_sample_data(merged_df):
    """
    Processa os dados para gerar um DataFrame agrupado por sample e gene, contando os KOs únicos.

    :param merged_df: DataFrame mesclado com os dados de entrada e do banco de dados.
    :return: DataFrame agrupado por sample e gene com a contagem de KOs únicos.
    """
    grouped_df = merged_df.groupby(['sample', 'Gene', 'compound_pathway', 'Pathway'])['ko'].nunique().reset_index(name='ko_count')
    return grouped_df

# ----------------------------------------
# P12 HADEG HEATMAP ORTHOLOGS BY sample
# ----------------------------------------
def process_pathway_data(merged_df):
    """
    Processa os dados para gerar um DataFrame agrupado por Pathway, compound_pathway e sample, contando os KOs únicos.

    :param merged_df: DataFrame mesclado com os dados de entrada e do banco de dados.
    :return: DataFrame agrupado por Pathway, compound_pathway e sample com a contagem de KOs únicos.
    """
    grouped_df = merged_df.groupby(['Pathway', 'compound_pathway', 'sample'])['ko'].nunique().reset_index(name='ko_count')
    return grouped_df




def get_ko_per_sample_for_pathway(merged_df, selected_pathway):
    """
    Filtra os dados para retornar os KOs únicos associados a cada sample para a via selecionada.

    :param merged_df: DataFrame mesclado com os dados do KEGG.
    :param selected_pathway: A via metabólica selecionada.
    :return: DataFrame com as `sample` e os respectivos `ko` associados.
    """
    filtered_df = merged_df[merged_df['pathname'] == selected_pathway]  # Filtra pela via
    if filtered_df.empty:
        return pd.DataFrame(columns=['sample', 'genesymbol'])  # Retorna um DataFrame vazio
    return filtered_df[['sample', 'genesymbol']].drop_duplicates()  # Remove duplicatas e retorna sample e ko


# my_dash_app/utils/data_processing.py

def count_unique_enzyme_activities(merged_df, sample):
    """
    Conta as atividades enzimáticas únicas associadas a uma amostra.

    :param merged_df: DataFrame resultante da mesclagem com o banco de dados.
    :param sample: Nome da amostra selecionada.
    :return: DataFrame com a contagem de atividades enzimáticas únicas por amostra.
    """
    # Filtrar pelo nome da amostra
    filtered_df = merged_df[merged_df['sample'] == sample]

    # Agrupar pela atividade enzimática e contar
    enzyme_count = filtered_df.groupby('enzyme_activity')['ko'].nunique().reset_index(name='unique_ko_count')
    return enzyme_count.sort_values('unique_ko_count', ascending=False)


#P15
# my_dash_app/utils/data_processing.py
import scipy.spatial.distance as ssd
import scipy.cluster.hierarchy as sch
import pandas as pd

def calculate_sample_clustering(input_df, distance_metric, method):
    """
    Calcula a matriz de clustering com base no input do usuário.

    :param input_df: DataFrame com os dados de entrada (colunas `sample` e `ko`).
    :param distance_metric: Métrica de distância selecionada (e.g., 'euclidean', 'cityblock').
    :param method: Método de agrupamento selecionado (e.g., 'single', 'ward').
    :return: Matriz de clustering calculada.
    """
    # Pivotar os dados para criar uma matriz de amostras por KOs
    pivot_df = input_df.pivot_table(
        index='sample', columns='ko', aggfunc='size', fill_value=0
    )

    # Calcular a matriz de distância
    distance_matrix = ssd.pdist(pivot_df, metric=distance_metric)

    # Realizar o clustering hierárquico
    clustering_matrix = sch.linkage(distance_matrix, method=method)

    return clustering_matrix

#p16
import pandas as pd

def prepare_upsetplot_data(merged_data, selected_samples):
    """
    Prepara os dados para o UpSet Plot com base no merge do input com o database.

    :param merged_data: Dados mesclados contendo as colunas `sample` e `ko`.
    :param selected_samples: Lista de amostras selecionadas.
    :return: DataFrame contendo as amostras e seus respectivos KOs únicos.
    """
    print(merged_data.head())

    # Filtrar pelas amostras selecionadas
    filtered_df = merged_data[merged_data['sample'].isin(selected_samples)]
    print(filtered_df.head())

    # Considerar apenas KOs únicos por amostra
    unique_ko_df = filtered_df.drop_duplicates(subset=['sample', 'ko'])

    return unique_ko_df


#P17
# my_dash_app/utils/data_processing.py
# my_dash_app/utils/data_processing.py
import pandas as pd
from utils.data_processing import merge_input_with_database

def prepare_gene_compound_network_data(stored_data):
    """
    Prepara os dados para o gráfico de rede Gene-Compound.

    :param stored_data: Dados armazenados no formato dicionário.
    :return: DataFrame contendo as relações gene-composto.
    """
    input_df = pd.DataFrame(stored_data)

    # Garantir que os dados estão no formato esperado
    if input_df.empty:
        raise ValueError("O stored-data está vazio.")

    # Realizar o merge com o banco de dados
    merged_data = merge_input_with_database(input_df)


    # Verificar se as colunas necessárias existem
    if 'genesymbol' not in merged_data.columns or 'cpd' not in merged_data.columns:
        raise KeyError("As colunas 'genesymbol' e 'cpd' são necessárias para criar o gráfico de rede.")

    # Filtrar apenas as colunas relevantes e remover duplicatas
    network_df = merged_data[['genesymbol', 'compoundname']].dropna().drop_duplicates()


    return network_df


#P18
# utils/data_processing.py
# utils/data_processing.py

def get_merged_toxcsm_data(input_data):
    """
    Realiza o merge do input_data com o banco ToxCSM.

    :param input_data: Dados brutos armazenados no `stored-data`.
    :return: DataFrame processado com as colunas de `value_` e `label_`.
    """
    
    # Verifica se os dados de entrada estão disponíveis
    if not input_data:
        return pd.DataFrame()  # Retorna um DataFrame vazio

    # Converte para DataFrame
    input_df = pd.DataFrame(input_data)

    # Primeiro merge com a base principal
    merged_df = merge_input_with_database(input_df)
    if merged_df.empty:
        return pd.DataFrame()

    # Segundo merge com o ToxCSM
    final_merged_df = merge_with_toxcsm(merged_df)
    if final_merged_df.empty:
        return pd.DataFrame()

    return final_merged_df


# utils/data_processing.py

def process_heatmap_data(df):
    """
    Processa os dados para gerar o heatmap de toxicidade com facetas.

    :param df: DataFrame de entrada com colunas de 'value_' e 'label_'.
    :return: DataFrame transformado com as categorias e valores necessários.
    """

    # Remover colunas desnecessárias
    columns_to_drop = ['SMILES', 'cpd', 'ChEBI']
    df = df.drop(columns=columns_to_drop, errors='ignore')

    # Selecionar colunas de valores e labels
    value_columns = [col for col in df.columns if col.startswith('value_')]
    label_columns = [col for col in df.columns if col.startswith('label_')]

    # Mapear as categorias principais
    category_mapping = {
        'NR': 'Nuclear Response',
        'SR': 'Stress Response',
        'Gen': 'Genomic',
        'Env': 'Environmental',
        'Org': 'Organic',
    }

    # Transformar os dados
    heatmap_data = []
    for value_col, label_col in zip(value_columns, label_columns):
        # Extrair a subcategoria
        subcategoria = value_col.split('_', 1)[1]  # NR_AR, SR_ARE, etc.
        category_prefix = subcategoria.split('_')[0]  # NR, SR, etc.
        mapped_category = category_mapping.get(category_prefix, None)

        if mapped_category:
            df_subset = df[['compoundname', value_col, label_col]].rename(
                columns={value_col: 'value', label_col: 'label'}
            )
            df_subset['category'] = mapped_category
            df_subset['subcategoria'] = subcategoria  # Adicionar a subcategoria
            heatmap_data.append(df_subset)

    if not heatmap_data:
        raise ValueError("Nenhuma coluna válida foi processada para o heatmap.")

    # Combinar os dados transformados
    result_df = pd.concat(heatmap_data, ignore_index=True)
    return result_df
