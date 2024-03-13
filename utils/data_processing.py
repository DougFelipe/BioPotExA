import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

# ----------------------------------------
# Funções de Mesclagem de Dados
# ----------------------------------------

def merge_input_with_database(input_data, database_filepath='data/database.xlsx'):
    """
    Mescla os dados de entrada com os dados do banco de dados.
    
    :param input_data: DataFrame com os dados de entrada.
    :param database_filepath: Caminho para o arquivo do banco de dados.
    :return: DataFrame resultante da mesclagem.
    """
    # Carrega os dados do banco de dados
    database_df = pd.read_excel(database_filepath)
    
    # Mescla os DataFrames
    merged_df = pd.merge(input_data, database_df, on='ko', how='inner')
    
    return merged_df

def merge_with_kegg(input_df, kegg_path='data/kegg_20degradation_pathways.xlsx'):
    """
    Mescla os dados de entrada com os dados do KEGG.
    
    :param input_df: DataFrame com os dados de entrada.
    :param kegg_path: Caminho para o arquivo de dados do KEGG.
    :return: DataFrame resultante da mesclagem.
    """
    # Carregando os dados do KEGG
    kegg_df = pd.read_excel(kegg_path)
    
    # Mesclando os dados de entrada com os dados do KEGG
    merged_df = pd.merge(input_df, kegg_df, on='ko', how='inner')
    
    return merged_df

# ----------------------------------------
# Funções de Processamento de Dados
# ----------------------------------------

import pandas as pd

def process_ko_data(merged_df):
    """
    Processa os dados de KO, contando os KOs únicos por amostra.

    :param merged_df: DataFrame com os dados mesclados ou uma lista de dicionários que possa ser convertida para DataFrame.
    :return: DataFrame com a contagem de KOs únicos por amostra.
    """
    # Verifica se merged_df é uma lista e converte para DataFrame
    if isinstance(merged_df, list):
        merged_df = pd.DataFrame(merged_df)
    elif not isinstance(merged_df, pd.DataFrame):
        raise ValueError("O argumento merged_df deve ser um pandas DataFrame ou uma lista de dicionários.")

    # Contagem de 'ko' únicos por 'sample'
    ko_count = merged_df.groupby('sample')['ko'].nunique().reset_index(name='ko_count')
    
    # Ordenar os dados pela contagem de KOs em ordem decrescente
    ko_count_sorted = ko_count.sort_values('ko_count', ascending=False)

    return ko_count_sorted




# ----------------------------------------
# Processamento de Dados p/ o Violin
# ----------------------------------------


def process_ko_data_violin(df):
    """
    Processa os dados para obter a contagem de KOs únicos por amostra.

    :param df: DataFrame com os dados de entrada.
    :return: DataFrame com a contagem de KOs por amostra.
    """
    ko_count_per_sample = df.groupby('sample')['ko'].nunique().reset_index(name='ko_count')
    return ko_count_per_sample

# ----------------------------------------
# Processamento de Dados p/ analise das 20 vias
# ----------------------------------------

def count_ko_per_pathway(merged_df):
    """
    Conta os KOs únicos para cada pathway em cada amostra.

    :param merged_df: DataFrame resultante da mesclagem com os dados do KEGG.
    :return: DataFrame com a contagem de KOs únicos por pathway por amostra.
    """
    # Verificar se a coluna 'pathname' existe
    if 'pathname' not in merged_df.columns:
        print("As colunas disponíveis no DataFrame são:", merged_df.columns)
        raise KeyError("'pathname' não encontrada no DataFrame.")

    pathway_count = merged_df.groupby(['sample', 'pathname'])['ko'].nunique().reset_index(name='unique_ko_count')
    return pathway_count


def count_ko_per_sample_for_pathway(merged_df, selected_pathway):
    """
    Conta os KOs únicos para uma via metabólica em cada sample.

    :param merged_df: DataFrame resultante da mesclagem com os dados do KEGG.
    :param selected_pathway: A via metabólica selecionada.
    :return: DataFrame com a contagem de KOs únicos por sample para a via selecionada.
    """
    filtered_df = merged_df[merged_df['pathname'] == selected_pathway]
    sample_count = filtered_df.groupby('sample')['ko'].nunique().reset_index(name='unique_ko_count')
    return sample_count.sort_values('unique_ko_count', ascending=False)
