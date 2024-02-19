# my_dash_app/utils/data_processing.py
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

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

    fig = px.bar(ko_count, x='sample', y='ko_count', title="Contagem de KO por Sample")
    
    return fig

def create_violin_boxplot(df):
    # Calcula a contagem de KOs únicos por sample
    ko_count_per_sample = df.groupby('sample')['ko'].nunique().reset_index(name='ko_count')

    fig = go.Figure()

    # Adiciona o gráfico de violino para a contagem de KOs únicos por sample
    fig.add_trace(go.Violin(y=ko_count_per_sample['ko_count'],
                            box_visible=True, line_color='black',
                            meanline_visible=True, fillcolor='lightseagreen', opacity=0.6,
                            points='all',  # Mostra todos os pontos de dados
                            jitter=0,  # Os pontos não são espalhados lateralmente
                            pointpos=0))


    # Atualiza o layout para remover legendas e ajustar títulos
    fig.update_layout(title_text="Distribuição da Contagem de KOs Únicos por Sample",
                      yaxis_title='Contagem de KOs Únicos',
                      xaxis_title='',
                      showlegend=False,
                      template='plotly_white')

    return fig



###### PROCESSAMENTO E PLOT DO GRÁFICO P2_KO_20PATHWAY #####

def merge_with_kegg(input_df, kegg_path='data/kegg_20degradation_pathways.xlsx'):
    # Carregando os dados do KEGG
    kegg_df = pd.read_excel(kegg_path)
    
    # Mesclando os dados de entrada com os dados do KEGG pela coluna 'ko'
    merged_df = pd.merge(input_df, kegg_df, on='ko', how='inner')
    
    return merged_df