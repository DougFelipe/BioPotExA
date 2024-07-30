# my_dash_app/utils/data_processing.py


import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots

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
# MERGE COM HADEG DATABASE
# ----------------------------------------

import pandas as pd

def merge_input_with_database_hadegDB(input_data, database_filepath='data/database_hadegDB.xlsx'):
    """
    Mescla os dados de entrada com os dados do banco de dados.
    
    :param input_data: DataFrame com os dados de entrada.
    :param database_filepath: Caminho para o arquivo do banco de dados.
    :return: DataFrame resultante da mesclagem.
    """
    database_df = pd.read_excel(database_filepath)  # Carrega os dados do banco de dados
    merged_df = pd.merge(input_data, database_df, on='ko', how='inner')  # Mescla os DataFrames
    
    if 'ko' not in merged_df.columns:
        raise KeyError("A coluna 'ko' não está presente no DataFrame após a mesclagem.")
    
    return merged_df  # Retorna o DataFrame mesclado

# ----------------------------------------
# MERGE COM ToxCSM DATABASE

def merge_with_toxcsm(merged_df, toxcsm_filepath='data/database_toxcsm.xlsx'):
    """
    Mescla a tabela resultante do merge inicial com o banco de dados ToxCSM,
    mantendo apenas a coluna 'compoundclass' da tabela inicial.

    :param merged_df: DataFrame resultante do merge inicial.
    :param toxcsm_filepath: Caminho para o arquivo do banco de dados ToxCSM.
    :return: DataFrame resultante da mesclagem.
    """
    # Carrega os dados do banco de dados ToxCSM
    toxcsm_df = pd.read_excel(toxcsm_filepath)
    
    # Mantém apenas a coluna 'compoundclass' da tabela inicial
    merged_df_reduced = merged_df[['compoundclass', 'cpd','ko']].drop_duplicates()
    
    # Mescla os DataFrames pela coluna 'cpd'
    final_merged_df = pd.merge(merged_df_reduced, toxcsm_df, on='cpd', how='inner')
    
    return final_merged_df
# ----------------------------------------
# Funções de Processamento de Dados
# ----------------------------------------

# ----------------------------------------
# P1_COUNT_KO
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

# Função para processar dados de compostos P4
def process_compound_data(merged_df):
    """
    Processa os dados para o gráfico de pontos de compostos.

    :param merged_df: DataFrame com os dados mesclados.
    :return: DataFrame processado.
    """
    return merged_df  # Lógica de processamento aqui, se necessário

# Função para processar ranking de amostras
# utils/data_processing.py

# ----------------------------------------
# P4_rank_samples
# ----------------------------------------
def process_sample_ranking(merged_df):
    """
    Processa os dados para calcular o número de compostos únicos associados a cada amostra.

    :param merged_df: DataFrame resultante da mesclagem com o banco de dados.
    :return: DataFrame com as amostras e o número de compostos únicos associados.
    """
    sample_ranking = merged_df.groupby('sample')['compoundname'].nunique().reset_index(name='num_compounds')
    sample_ranking = sample_ranking.sort_values(by='num_compounds', ascending=False)
    return sample_ranking


# ----------------------------------------
# P5_rank_compounds
# ----------------------------------------

def process_compound_ranking(merged_df):
    """
    Processa os dados para calcular o número de amostras únicas associadas a cada composto.

    :param merged_df: DataFrame resultante da mesclagem com o banco de dados.
    :return: DataFrame com os compostos e o número de amostras únicas associadas.
    """
    compound_ranking = merged_df.groupby('compoundname')['sample'].nunique().reset_index(name='num_samples')
    compound_ranking = compound_ranking.sort_values(by='num_samples', ascending=False)
    return compound_ranking


# ----------------------------------------
# P6_rank_genes
# ----------------------------------------
def process_compound_gene_ranking(merged_df):
    """
    Processa os dados para calcular o número de genes únicos atuantes em cada composto.

    :param merged_df: DataFrame resultante da mesclagem com o banco de dados.
    :return: DataFrame com os compostos e o número de genes únicos atuantes.
    """
    compound_gene_ranking = merged_df.groupby('compoundname')['genesymbol'].nunique().reset_index(name='num_genes')
    compound_gene_ranking = compound_gene_ranking.sort_values(by='num_genes', ascending=False)
    return compound_gene_ranking


# ----------------------------------------
# P7_gene_compound_association
# ----------------------------------------
def process_gene_compound_association(merged_df):
    """
    Processa os dados para calcular a quantidade de compostos únicos associados a cada gene.

    :param merged_df: DataFrame resultante da mesclagem com o banco de dados.
    :return: DataFrame com os genes e a quantidade de compostos únicos associados.
    """
    gene_compound_association = merged_df.groupby('genesymbol')['compoundname'].nunique().reset_index(name='num_compounds')
    gene_compound_association = gene_compound_association.sort_values(by='num_compounds', ascending=False)
    return gene_compound_association


# ----------------------------------------
# P8_gene_sample_association
# ----------------------------------------

def process_gene_sample_association(merged_df):
    """
    Processa os dados para calcular a quantidade de compostos únicos associados a cada gene.

    :param merged_df: DataFrame resultante da mesclagem com o banco de dados.
    :return: DataFrame com os genes e a quantidade de compostos únicos associados.
    """
    gene_sample_association = merged_df.groupby('genesymbol')['compoundname'].nunique().reset_index(name='num_compounds')
    gene_sample_association = gene_sample_association.sort_values(by='num_compounds', ascending=False)
    return gene_sample_association


# ----------------------------------------
# P9_sample_reference_heatmap
# ----------------------------------------

def process_sample_reference_heatmap(merged_df):
    """
    Processa os dados para calcular a contagem de compoundname para cada combinação de samples e referenceAG.

    :param merged_df: DataFrame resultante da mesclagem com o banco de dados.
    :return: DataFrame pivotado para o heatmap.
    """
    heatmap_df = merged_df.groupby(['sample', 'referenceAG'])['compoundname'].nunique().reset_index()
    heatmap_pivot = heatmap_df.pivot(index='referenceAG', columns='sample', values='compoundname').fillna(0)
    return heatmap_pivot

# ----------------------------------------
# P10_group_by_class Agrupa amostras por perfil de genes para cada classe de compostos
# ----------------------------------------

def group_by_class(compoundclass_choice, tabela):
    dados_selecionados = tabela[tabela['compoundclass'] == compoundclass_choice]
    
    grupos = []
    for sample in dados_selecionados['sample'].unique():
        compostos = dados_selecionados.loc[dados_selecionados['sample'] == sample, 'compoundname'].unique().tolist()
        if len(compostos) > 0:
            grupo_existente = False
            for grupo in grupos:
                if set(compostos) == set(grupo['compostos']):
                    grupo_existente = True
                    grupo['samples'].append(sample)
                    break
            if not grupo_existente:
                novo_grupo = {'compostos': compostos, 'samples': [sample]}
                grupos.append(novo_grupo)
    
    tabela_grupos = tabela.copy()
    tabela_grupos['grupo'] = None
    for i, grupo in enumerate(grupos):
        grupo_samples = grupo['samples']
        grupo_compostos = grupo['compostos']
        tabela_grupos.loc[(tabela_grupos['sample'].isin(grupo_samples)) & 
                          (tabela_grupos['compoundname'].isin(grupo_compostos)), 'grupo'] = f"{compoundclass_choice} - Group {i+1}"
    
    tabela_grupos = tabela_grupos[tabela_grupos['compoundclass'] == compoundclass_choice]
    
    return tabela_grupos

def minimize_groups(df):
    group_compounds = df.groupby('grupo')['compoundname'].apply(lambda x: list(set(x))).reset_index()
    
    all_compounds = df['compoundname'].unique().tolist()
    selected_groups = []
    
    while len(all_compounds) > 0:
        max_cover = 0
        best_group = None
        for i in range(len(group_compounds)):
            group = group_compounds.iloc[i]['grupo']
            compounds = group_compounds.iloc[i]['compoundname']
            cover = len(set(all_compounds) & set(compounds))
            if cover > max_cover:
                max_cover = cover
                best_group = group
        
        all_compounds = list(set(all_compounds) - set(group_compounds.loc[group_compounds['grupo'] == best_group, 'compoundname'].values[0]))
        selected_groups.append(best_group)
        group_compounds = group_compounds[group_compounds['grupo'] != best_group]
    
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