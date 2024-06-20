# my_dash_app/utils/data_processing.py


import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

# ----------------------------------------
# Funções de Mesclagem de Dados
# ----------------------------------------

# Função para mesclar dados de entrada com o banco de dados
def merge_input_with_database(input_data, database_filepath='data/database.xlsx'):
    """
    Mescla os dados de entrada com os dados do banco de dados.
    
    :param input_data: DataFrame com os dados de entrada.
    :param database_filepath: Caminho para o arquivo do banco de dados.
    :return: DataFrame resultante da mesclagem.
    """
    database_df = pd.read_excel(database_filepath)  # Carrega os dados do banco de dados
    merged_df = pd.merge(input_data, database_df, on='ko', how='inner')  # Mescla os DataFrames
    return merged_df  # Retorna o DataFrame mesclado

# Função para mesclar dados de entrada com os dados do KEGG
def merge_with_kegg(input_df, kegg_path='data/kegg_20degradation_pathways.xlsx'):
    """
    Mescla os dados de entrada com os dados do KEGG.
    
    :param input_df: DataFrame com os dados de entrada.
    :param kegg_path: Caminho para o arquivo de dados do KEGG.
    :return: DataFrame resultante da mesclagem.
    """
    kegg_df = pd.read_excel(kegg_path)  # Carregando os dados do KEGG
    merged_df = pd.merge(input_df, kegg_df, on='ko', how='inner')  # Mesclando os dados de entrada com os dados do KEGG
    return merged_df  # Retorna o DataFrame mesclado

# ----------------------------------------
# Funções de Processamento de Dados
# ----------------------------------------

# Função para processar dados de KO
def process_ko_data(merged_df):
    """
    Processa os dados de KO, contando os KOs únicos por amostra.

    :param merged_df: DataFrame com os dados mesclados ou uma lista de dicionários que possa ser convertida para DataFrame.
    :return: DataFrame com a contagem de KOs únicos por amostra.
    """
    if isinstance(merged_df, list):  # Verifica se merged_df é uma lista e converte para DataFrame
        merged_df = pd.DataFrame(merged_df)
    elif not isinstance(merged_df, pd.DataFrame):
        raise ValueError("O argumento merged_df deve ser um pandas DataFrame ou uma lista de dicionários.")

    ko_count = merged_df.groupby('sample')['ko'].nunique().reset_index(name='ko_count')  # Contagem de 'ko' únicos por 'sample'
    ko_count_sorted = ko_count.sort_values('ko_count', ascending=False)  # Ordenar os dados pela contagem de KOs em ordem decrescente

    return ko_count_sorted  # Retorna o DataFrame com a contagem de KOs

# Função para processar dados para gráfico de violino
def process_ko_data_violin(df):
    """
    Processa os dados para obter a contagem de KOs únicos por amostra.

    :param df: DataFrame com os dados de entrada.
    :return: DataFrame com a contagem de KOs por amostra.
    """
    ko_count_per_sample = df.groupby('sample')['ko'].nunique().reset_index(name='ko_count')  # Contagem de KOs únicos por amostra
    return ko_count_per_sample  # Retorna o DataFrame com a contagem de KOs

# Função para contar KOs por pathway
def count_ko_per_pathway(merged_df):
    """
    Conta os KOs únicos para cada pathway em cada amostra.

    :param merged_df: DataFrame resultante da mesclagem com os dados do KEGG.
    :return: DataFrame com a contagem de KOs únicos por pathway por amostra.
    """
    if 'pathname' not in merged_df.columns:  # Verificar se a coluna 'pathname' existe
        print("As colunas disponíveis no DataFrame são:", merged_df.columns)
        raise KeyError("'pathname' não encontrada no DataFrame.")

    pathway_count = merged_df.groupby(['sample', 'pathname'])['ko'].nunique().reset_index(name='unique_ko_count')  # Contagem de KOs únicos por pathway
    return pathway_count  # Retorna o DataFrame com a contagem de KOs por pathway

# Função para contar KOs por sample para uma via metabólica
def count_ko_per_sample_for_pathway(merged_df, selected_pathway):
    """
    Conta os KOs únicos para uma via metabólica em cada sample.

    :param merged_df: DataFrame resultante da mesclagem com os dados do KEGG.
    :param selected_pathway: A via metabólica selecionada.
    :return: DataFrame com a contagem de KOs únicos por sample para a via selecionada.
    """
    filtered_df = merged_df[merged_df['pathname'] == selected_pathway]  # Filtra o DataFrame pela via selecionada
    sample_count = filtered_df.groupby('sample')['ko'].nunique().reset_index(name='unique_ko_count')  # Contagem de KOs únicos por sample
    return sample_count.sort_values('unique_ko_count', ascending=False)  # Retorna o DataFrame ordenado pela contagem de KOs

# Função para processar dados de compostos
def process_compound_data(merged_df):
    """
    Processa os dados para o gráfico de pontos de compostos.

    :param merged_df: DataFrame com os dados mesclados.
    :return: DataFrame processado.
    """
    return merged_df  # Lógica de processamento aqui, se necessário

# Função para processar ranking de amostras
def process_sample_ranking(merged_df):
    """
    Processa os dados para calcular o ranking das amostras com base no número de compostos únicos.

    :param merged_df: DataFrame mesclado.
    :return: DataFrame com as amostras e o número de compostos únicos associados, ordenado por número de compostos.
    """
    sample_ranking = merged_df.groupby('sample')['compoundname'].nunique().reset_index()  # Agrupa por sample e conta compostos únicos
    sample_ranking.columns = ['sample', 'num_compounds']  # Renomeia as colunas
    sample_ranking = sample_ranking.sort_values(by='num_compounds', ascending=False)  # Ordena por número de compostos
    return sample_ranking  # Retorna o DataFrame com o ranking das amostras
