import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
from plotly.subplots import make_subplots
import math



def plot_ko_count(ko_count_df):
    """
    Cria um gráfico de barras da contagem de KOs por amostra com base no DataFrame processado.

    :param ko_count_df: DataFrame com a contagem de KOs por amostra.
    :return: Objeto Figure com o gráfico de barras.
    """
    fig = px.bar(ko_count_df, x='sample', y='ko_count',template="simple_white")
    # Ajustar o layout do gráfico, se necessário
    fig.update_layout(
        xaxis_title='Sample',
        yaxis_title='Unique Gene Count',
        xaxis={'categoryorder':'total descending'},
        xaxis_tickangle=45  # Garante que a ordenação será mantida no gráfico
    )

    
    return fig


def create_violin_plot(ko_count_per_sample):
    """
    Cria um gráfico de violino com caixa para a contagem de KOs únicos por amostra.

    :param ko_count_per_sample: DataFrame com a contagem de KOs por amostra.
    :return: Objeto Figure com o gráfico de violino.
    """

    fig = go.Figure()

    # Adiciona o boxplot
    # Adiciona o boxplot com pontos individuais
     # Cria o gráfico de violino
    fig = px.violin(ko_count_per_sample, y='ko_count', box=True, points='all',
                    hover_name='sample', hover_data={'sample': False, 'ko_count': True}, template="simple_white")
    

    
    fig.update_traces(marker=dict(size=5, opacity=1),
                      line=dict(width=1),
                      jitter=0.3, pointpos=0)

    # Atualiza o layout do gráfico
    fig.update_layout(yaxis_title='Unique Gene Count',
                      showlegend=False, template='plotly_white',
                      #yaxis=dict(range=[0, ko_count_per_sample['ko_count'].max() + 100]),
                      xaxis_title='')  # Definindo o título do eixo x como vazio

    return fig


# ----------------------------------------
# Plots p/ analise das 20 vias
# ----------------------------------------

def plot_pathway_ko_counts(pathway_count_df, selected_sample):
    """
    Plota um gráfico de barras dos KOs únicos para cada pathway na amostra selecionada.

    :param pathway_count_df: DataFrame com a contagem de KOs únicos por pathway por amostra.
    :param selected_sample: Amostra selecionada para o plot.
    :return: Objeto Figure com o gráfico de barras.
    """
    # Filtrar o DataFrame pela amostra selecionada
    filtered_df = pathway_count_df[pathway_count_df['sample'] == selected_sample]

    # Ordenar os valores de forma decrescente pela contagem de KOs únicos
    filtered_df = filtered_df.sort_values('unique_ko_count', ascending=False)

    # Plotar o gráfico de barras
    fig = px.bar(
        filtered_df,
        x='pathname',  # Certifique-se de que 'pathway' é o nome correto da coluna no seu DataFrame
        y='unique_ko_count',
        title=f'Unique Gene Count to {selected_sample}',
        text='unique_ko_count',  # Adiciona o valor da contagem sobre as barras
        template="simple_white"
    )

    # Ajustar o layout do gráfico, se necessário
    fig.update_layout(
        xaxis_title='Pathway',
        yaxis_title='Unique Gene Count',
        xaxis={'categoryorder':'total descending'}  # Garante que a ordenação será mantida no gráfico
    )

    return fig

# Função para plotar o gráfico de barras
def plot_sample_ko_counts(sample_count_df, selected_pathway):
    """
    Plota um gráfico de barras dos KOs únicos para uma via metabólica selecionada em cada sample.

    :param sample_count_df: DataFrame com a contagem de KOs únicos por sample para a via selecionada.
    :param selected_pathway: A via metabólica selecionada.
    :return: Objeto Figure com o gráfico de barras.
    """
    # Verificação dos dados de entrada
    if sample_count_df.empty:
        raise ValueError("O DataFrame de contagem de amostras está vazio.")
    
    if 'sample' not in sample_count_df.columns or 'unique_ko_count' not in sample_count_df.columns:
        raise ValueError("O DataFrame de contagem de amostras não contém as colunas necessárias: 'sample' e 'unique_ko_count'.")

    # Verificando se há valores inválidos nas colunas 'sample' e 'unique_ko_count'
    if sample_count_df['sample'].isnull().any() or sample_count_df['unique_ko_count'].isnull().any():
        raise ValueError("Há valores nulos nas colunas 'sample' ou 'unique_ko_count'.")

    fig = px.bar(
        sample_count_df,
        x='sample',
        y='unique_ko_count',
        title=f'Unique Gene Count for Pathway: {selected_pathway}',
        text='unique_ko_count',
        template="simple_white"
    )
    fig.update_layout(
        xaxis_title='Sample',
        yaxis_title='Unique Gene Count',
        xaxis={'categoryorder':'total descending'},
        xaxis_tickangle=45
    )
    return fig




def plot_compound_scatter(df):
    """
    Cria um gráfico de dispersão para visualizar a relação entre amostras e compostos, filtrados por classe de composto.

    :param df: DataFrame filtrado contendo as colunas 'sample', 'compoundname', e 'compoundclass'.
    :return: Objeto Figure com o gráfico de dispersão.
    """
    # Define a altura base do gráfico e a altura adicional por rótulo excedente
    base_height = 400  # Altura base do gráfico
    extra_height_per_label = 20  # Altura adicional por cada rótulo excedente

    # Calcula o número de rótulos no eixo y
    num_labels = df['compoundname'].nunique()

    # Define um limite para quando adicionar altura extra
    label_limit = 20  # Número de rótulos que podem caber na altura base

    # Calcula a altura total do gráfico
    if num_labels > label_limit:
        height = base_height + (num_labels - label_limit) * extra_height_per_label
    else:
        height = base_height

    # Cria o gráfico de dispersão
    fig = px.scatter(df, x='sample', y='compoundname', color='compoundclass', title='Scatter Plot of Samples vs Compounds', template="simple_white")

    # Ajusta o layout do gráfico com a altura calculada
    fig.update_layout(
        height=height,
        yaxis=dict(
            tickmode='array',
            tickvals=df['compoundname'].unique(),
            ticktext=df['compoundname'].unique(),
        ),
        xaxis_tickangle=45
    )

    return fig





def plot_sample_ranking(sample_ranking_df):
    """
    Cria um gráfico de barras para visualizar o ranking das amostras com base no número de compostos únicos.

    :param sample_ranking_df: DataFrame com as amostras e o número de compostos únicos associados.
    :return: Objeto Figure com o gráfico de barras.
    """
    # Ordena os dados pelo número de compostos em ordem decrescente
    sample_ranking_df = sample_ranking_df.sort_values(by='num_compounds', ascending=False)

    # Cria o gráfico de barras
    fig = px.bar(sample_ranking_df, x='sample', y='num_compounds',
                 title='Ranking of Samples by Compound Interaction', template='simple_white')

    # Atualiza o layout do gráfico
    fig.update_layout(
        xaxis_title='Sample',
        yaxis_title='Number of Compounds',
        xaxis={'categoryorder': 'total descending'}  # Ordena o eixo x de forma decrescente
    )

    return fig


# ----------------------------------------
# P5_rank_compounds
# ----------------------------------------

def plot_compound_ranking(compound_ranking_df):
    """
    Cria um gráfico de barras para visualizar o ranking dos compostos com base no número de amostras únicas.

    :param compound_ranking_df: DataFrame com os compostos e o número de amostras únicas associadas.
    :return: Objeto Figure com o gráfico de barras.
    """
    # Cria o gráfico de barras
    fig = px.bar(compound_ranking_df, x='compoundname', y='num_samples',
                 title='Ranking of Compounds by Sample Interaction', template='simple_white')

    # Atualiza o layout do gráfico
    fig.update_layout(
        xaxis_title='Compound',
        yaxis_title='Number of Samples',
        xaxis={'categoryorder': 'total descending'},  # Ordena o eixo x de forma decrescente
        xaxis_tickangle=45
    )

    return fig

# ----------------------------------------
# P6_rank_genes
# ----------------------------------------
def plot_compound_gene_ranking(compound_gene_ranking_df):
    """
    Cria um gráfico de barras para visualizar o ranking dos compostos com base no número de genes únicos atuantes.

    :param compound_gene_ranking_df: DataFrame com os compostos e o número de genes únicos atuantes.
    :return: Objeto Figure com o gráfico de barras.
    """
    # Cria o gráfico de barras
    fig = px.bar(compound_gene_ranking_df, x='compoundname', y='num_genes',
                 title='Ranking of Compounds by Gene Interaction', template='simple_white')

    # Atualiza o layout do gráfico
    fig.update_layout(
        xaxis_title='Compound',
        yaxis_title='Number of Genes',
        xaxis={'categoryorder': 'total descending'},  # Ordena o eixo x de forma decrescente
        xaxis_tickangle=45
    )

    return fig


# ----------------------------------------
# P7_gene_compound_association
# ----------------------------------------

def plot_gene_compound_scatter(df):
    """
    Cria um scatter plot para visualizar a relação entre genes e compostos, filtrados pela quantidade de compostos únicos associados.

    :param df: DataFrame filtrado contendo as colunas 'genesymbol' e 'compoundname'.
    :return: Objeto Figure com o scatter plot.
    """
    fig = px.scatter(df, x='genesymbol', y='compoundname', title='Scatter Plot of Genes vs Compounds', template='simple_white')
    fig.update_layout(
        xaxis_title='Gene Symbol',
        yaxis_title='Compound Name'
    )
    return fig

# ----------------------------------------
# P8_gene_sample_association
# ----------------------------------------
def plot_sample_gene_scatter(df):
    """
    Cria um scatter plot para visualizar a relação entre samples e genes, filtrados pela quantidade de compostos únicos associados.

    :param df: DataFrame filtrado contendo as colunas 'sample' e 'genesymbol'.
    :return: Objeto Figure com o scatter plot.
    """
    fig = px.scatter(df, x='sample', y='genesymbol', title='Scatter Plot of Samples vs Genes', template='simple_white')
    fig.update_layout(
        xaxis_title='Sample',
        yaxis_title='Gene Symbol'
    )
    return fig


# ----------------------------------------
# P9_sample_reference_heatmap
# ----------------------------------------

def plot_sample_reference_heatmap(df):
    """
    Cria um heatmap para visualizar a contagem de compoundname para cada combinação de samples e referenceAG.

    :param df: DataFrame pivotado contendo as contagens.
    :return: Objeto Figure com o heatmap.
    """
    fig = px.imshow(df, 
                    labels=dict(x="Sample", y="Reference AG", color="Compound Count"), 
                    x=df.columns, 
                    y=df.index, 
                    color_continuous_scale='Viridis', 
                    title='Heatmap of Samples vs Reference AG')
    fig.update_layout(template='simple_white')
    return fig



# ----------------------------------------
# P10_group_by_class Agrupa amostras por perfil de genes para cada classe de compostos
# ----------------------------------------


import plotly.graph_objects as go
from plotly.subplots import make_subplots

def plot_sample_groups(df):
    """
    Cria um scatter plot para visualizar os grupos de samples baseados na relação com compoundname utilizando subplots.
    
    :param df: DataFrame contendo os grupos de samples.
    :return: Objeto Figure com os subplots.
    """
    unique_groups = df['grupo'].unique()
    fig = make_subplots(rows=1, cols=len(unique_groups), shared_yaxes=True, subplot_titles=unique_groups)

    # Iterar sobre cada grupo e criar subplots
    for i, group in enumerate(unique_groups):
        group_df = df[df['grupo'] == group]
        fig.add_trace(go.Scatter(x=group_df['sample'], y=group_df['compoundname'], mode='markers', name=group, showlegend=False), row=1, col=i+1)
    
    fig.update_layout(
        title_text='Sample Groups by Compound Interaction', 
        template='simple_white',
        showlegend=False
    )

    # Atualizar eixos para cada subplot
    for i in range(1, len(unique_groups) + 1):
        fig.update_xaxes(row=1, col=i, tickangle= -45, title_text=None)
        fig.update_yaxes(row=1, col=i, tickangle=-45, title_text=None)
    
    return fig



# ----------------------------------------
# P11 HADEG HEATMAP ORTHOLOGS BY SAMPLE
# ----------------------------------------
def plot_sample_gene_heatmap(grouped_df):
    """
    Cria um heatmap para visualizar a relação entre genes e samples com a contagem de KOs únicos.

    :param grouped_df: DataFrame agrupado por gene e sample com a contagem de KOs únicos.
    :return: Objeto Figure com o heatmap.
    """
    fig = px.density_heatmap(grouped_df, x='sample', y='Gene', z='ko_count', color_continuous_scale='Oranges', template='simple_white')
    fig.update_layout(
        xaxis_title='',  # Remove o título do eixo x
        yaxis_title='',  # Remove o título do eixo y
        xaxis_tickangle=-45,
        yaxis_tickangle=-45,
    )
    return fig


# ----------------------------------------
# P12 HADEG HEATMAP ORTHOLOGS BY sample
# ----------------------------------------
def plot_pathway_heatmap(df, selected_sample):
    """
    Plota um heatmap mostrando a contagem de KOs por Pathway e Compound Pathway para uma amostra selecionada.

    :param df: DataFrame mesclado contendo os dados de entrada e do banco de dados.
    :param selected_sample: Amostra selecionada para visualização no heatmap.
    :return: Objeto Figure com o heatmap.
    """
    df = df[df['sample'] == selected_sample]  # Filtra os dados para a amostra selecionada

    compound_pathways = df['compound_pathway'].unique()
    n_rows = len(compound_pathways)

    fig = make_subplots(
        rows=n_rows, cols=1,
        shared_xaxes=True,
        vertical_spacing=0.02,
        subplot_titles=[f'Compound Pathway: {cp}' for cp in compound_pathways]
    )

    for i, compound_pathway in enumerate(compound_pathways, start=1):
        df_filtered = df[df['compound_pathway'] == compound_pathway]
        heatmap_data = df_filtered.pivot_table(index='Pathway', columns='compound_pathway', values='ko', aggfunc='count', fill_value=0)

        heatmap = go.Heatmap(
            z=heatmap_data.values,
            x=heatmap_data.columns,
            y=heatmap_data.index,
            colorscale='Oranges'
        )

        fig.add_trace(heatmap, row=i, col=1)

    fig.update_layout(
        height=300 * n_rows,
        title=f'Heatmap of Pathway vs Compound Pathway for Sample {selected_sample}',
        coloraxis=dict(colorbar=dict(title='KO Count'))
    )

    return fig