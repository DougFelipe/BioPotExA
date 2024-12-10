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
    print("DEBUG: Dados mesclados carregados no DataFrame:")
    print(merged_data.head())

    # Filtrar pelas amostras selecionadas
    filtered_df = merged_data[merged_data['sample'].isin(selected_samples)]
    print("DEBUG: Dados filtrados pelas amostras selecionadas:")
    print(filtered_df.head())

    # Considerar apenas KOs únicos por amostra
    unique_ko_df = filtered_df.drop_duplicates(subset=['sample', 'ko'])
    print("DEBUG: Dados com valores únicos de KO por amostra:")
    print(unique_ko_df.head())

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
    print("DEBUG: Iniciando o merge com o banco ToxCSM...")
    
    # Verifica se os dados de entrada estão disponíveis
    if not input_data:
        print("WARNING: Nenhum dado fornecido para o merge.")
        return pd.DataFrame()  # Retorna um DataFrame vazio

    # Converte para DataFrame
    input_df = pd.DataFrame(input_data)
    print(f"DEBUG: DataFrame inicial:\n{input_df.head()}")

    # Primeiro merge com a base principal
    merged_df = merge_input_with_database(input_df)
    if merged_df.empty:
        print("WARNING: Merge inicial com a base principal resultou em um DataFrame vazio.")
        return pd.DataFrame()

    # Segundo merge com o ToxCSM
    final_merged_df = merge_with_toxcsm(merged_df)
    if final_merged_df.empty:
        print("WARNING: Merge com o banco ToxCSM resultou em um DataFrame vazio.")
        return pd.DataFrame()

    print(f"DEBUG: DataFrame final após o merge:\n{final_merged_df.head()}")
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
