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
# Funções de Criação de Gráficos
# ----------------------------------------

def create_violin_boxplot(df):
    """
    Cria um gráfico de violino com caixa para a contagem de KOs únicos por amostra.
    
    :param df: DataFrame com os dados a serem plotados.
    :return: Objeto Figure com o gráfico de violino.
    """
    # Calcula a contagem de KOs únicos por sample
    ko_count_per_sample = df.groupby('sample')['ko'].nunique().reset_index(name='ko_count')


    fig = go.Figure()

    # Adiciona o boxplot
    # Adiciona o boxplot com pontos individuais
    fig.add_trace(go.Box(
        y=ko_count_per_sample['ko_count'],
        name='',
        boxpoints='all',  # Exibe todos os pontos de dados
        jitter=0.3,  # Espaçamento entre os pontos
        pointpos= 0  # Posição dos pontos em relação ao boxplot
    ))

    fig = px.box(ko_count_per_sample, y='ko_count', points='all',
                 hover_name = 'sample')
    
    fig.update_traces(marker=dict(size=5, opacity=1),
                      line=dict(width=1),
                      jitter=0.3, pointpos=0)

    # Atualiza o layout do gráfico
    fig.update_layout(title_text="Distribuição da Contagem de KOs Únicos por Sample",
                      yaxis_title='Contagem de KOs Únicos',
                      showlegend=False, template='plotly_white',
                      yaxis=dict(range=[0, ko_count_per_sample['ko_count'].max() + 1]),
                      xaxis_title='')  # Definindo o título do eixo x como vazio

    return fig
