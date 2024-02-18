# my_dash_app/utils/data_processing.py
import pandas as pd

## Função para mesclar os dados de entrada com os dados do banco de dados
def merge_input_with_database(input_data, database_filepath='data/database.xlsx'):
    # Carrega os dados do banco de dados
    database_df = pd.read_excel(database_filepath)
    
    # Supõe que 'input_data' é um DataFrame e possui a mesma coluna de interesse que 'database_df'
    # Faça o merge (ou a operação desejada) dos DataFrames aqui
    merged_df = pd.merge(input_data, database_df, on='ko', how='inner')
    
    return merged_df


#GRÁFICO P1_KO_COUNT
## Função para processar os dados de entrada
def process_ko_data(merged_df):
    # Contagem de 'ko' únicos por 'sample'
    ko_count = merged_df.groupby('sample')['ko'].nunique().reset_index(name='ko_count')
    
    return ko_count
