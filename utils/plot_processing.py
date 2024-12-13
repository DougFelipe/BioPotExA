import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
from plotly.subplots import make_subplots
import math
from utils.data_processing import prepare_upsetplot_data
from utils.data_processing import merge_input_with_database  # Importa a função de merge



def plot_ko_count(ko_count_df):
    """
    Cria um gráfico de barras da contagem de KOs por amostra com base no DataFrame processado.
    Inclui os valores acima das barras.

    :param ko_count_df: DataFrame com a contagem de KOs por amostra.
    :return: Objeto Figure com o gráfico de barras.
    """
    # Criação do gráfico com valores textuais exibidos
    fig = px.bar(
        ko_count_df, 
        x='sample', 
        y='ko_count', 
        text='ko_count',  # Adiciona os valores da coluna `ko_count` como texto
        template="simple_white"
    )
    
    # Ajustar a posição do texto e o layout do gráfico
    fig.update_traces(
        textposition='auto',  # Posiciona o texto fora das barras
        marker=dict(color='steelblue')  # Configura a cor das barras
    )
    
    fig.update_layout(
        title="KO Count by Sample",
        xaxis_title='Sample',
        yaxis_title='Unique Gene Count',
        xaxis={'categoryorder': 'total descending'},
        xaxis_tickangle=45,  # Inclina os rótulos do eixo X
        uniformtext_minsize=10,  # Garante tamanho mínimo do texto
        uniformtext_mode='hide'  # Oculta texto que não couber
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



#get_compound_scatter_layout
#get_compound_scatter_layout
def plot_compound_scatter(df):
    """
    Cria um gráfico de dispersão para visualizar a relação entre amostras e compostos,
    recalculando o layout dinamicamente para cada novo conjunto de dados.

    :param df: DataFrame filtrado contendo as colunas 'sample', 'compoundname', e 'compoundclass'.
    :return: Objeto Figure com o gráfico de dispersão.
    """
    # Certifica-se de que o DataFrame não está vazio
    if df.empty:
        raise ValueError("O DataFrame está vazio. Não há dados para exibir.")

    # Define parâmetros base
    base_height = 400  # Altura base do gráfico
    base_width = 800   # Largura base do gráfico
    extra_width_per_label = 10  # Largura extra por rótulo adicional no eixo X
    label_limit_x = 20  # Limite de rótulos no eixo X antes de ajustar a largura

    # Calcula o número de rótulos únicos no eixo X (samples)
    num_labels_x = df['sample'].nunique()

    # Ajusta a largura do gráfico dinamicamente
    if num_labels_x > label_limit_x:
        width = base_width + (num_labels_x - label_limit_x) * extra_width_per_label
    else:
        width = base_width

    # Calcula a altura do gráfico com base nos rótulos do eixo Y (compoundname)
    base_height = 400
    extra_height_per_label = 15
    num_labels_y = df['compoundname'].nunique()
    label_limit_y = 1

    if num_labels_y > label_limit_y:
        height = base_height + (num_labels_y - label_limit_y) * extra_height_per_label
    else:
        height = base_height

    # Define espaçamento dinâmico para rótulos no eixo X
    tick_spacing_x = max(1, num_labels_x // 20)  # Exibe no máximo 20 rótulos no eixo X

    # Cria o scatter plot
    fig = px.scatter(
        df,
        x='sample',
        y='compoundname',
        title='Scatter Plot of Samples vs Compounds',
        template='simple_white'
    )

    # Recalcula o layout e garante configurações consistentes
    fig.update_layout(
        height=height,
        width=width,
        yaxis=dict(
            categoryorder='total ascending',
            title='Compoundname',  # Rótulo do eixo Y
            tickmode='array',
            tickvals=df['compoundname'].unique(),
            ticktext=df['compoundname'].unique(),
            automargin=True,
            tickfont=dict(size=10),
        ),
        xaxis=dict(
            title='Sample',  # Rótulo do eixo X
            tickangle=45,  # Rotaciona rótulos no eixo X em 45 graus
            tickmode='linear',
            tickvals=df['sample'].unique()[::tick_spacing_x],
            ticktext=df['sample'].unique()[::tick_spacing_x],
            automargin=True,
        ),
        margin=dict(l=200, b=150)  # Margens para rótulos longos
    )

    return fig






# utils/plot_processing.py

import plotly.express as px

def plot_sample_ranking(sample_ranking_df):
    """
    Cria um gráfico de barras para visualizar o ranking das amostras com base no número de compostos únicos.

    :param sample_ranking_df: DataFrame com as amostras e o número de compostos únicos associados.
    :return: Objeto Figure com o gráfico de barras.
    """
    # Ordena os dados pelo número de compostos em ordem decrescente
    sample_ranking_df = sample_ranking_df.sort_values(by='num_compounds', ascending=False)

    # Cria o gráfico de barras com valores textuais
    fig = px.bar(
        sample_ranking_df,
        x='sample',
        y='num_compounds',
        text='num_compounds',  # Adiciona valores textuais às barras
        template='simple_white'
    )

    # Ajusta o layout e os textos do gráfico
    fig.update_traces(
        textposition='auto',
        marker=dict(color='steelblue')  # Define a cor das barras
    )
    fig.update_layout(
        title='Ranking of Samples by Compound Interaction',
        xaxis_title='Sample',
        yaxis_title='Number of Compounds',
        xaxis=dict(
            categoryorder='total descending',
            tickangle=45  # Rotaciona os rótulos do eixo X
        ),
        uniformtext_minsize=10,
        uniformtext_mode='hide'
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
    # Ordena os dados pelo número de amostras em ordem decrescente
    compound_ranking_df = compound_ranking_df.sort_values(by='num_samples', ascending=False)

    # Cria o gráfico de barras com valores textuais exibidos
    fig = px.bar(
        compound_ranking_df,
        x='compoundname',
        y='num_samples',
        text='num_samples',  # Adiciona valores textuais às barras
        title='Ranking of Compounds by Sample Interaction',
        template='simple_white'
    )

    # Ajusta a posição do texto e o layout do gráfico
    fig.update_traces(
        textposition='auto',  # Posiciona o texto sobre as barras
        marker=dict(color='steelblue')  # Define a cor das barras
    )
    fig.update_layout(
        xaxis_title='Compound',
        yaxis_title='Number of Samples',
        xaxis=dict(
            categoryorder='total descending',
            tickangle=45  # Rotaciona os rótulos do eixo X
        ),
        uniformtext_minsize=10,  # Define um tamanho mínimo para o texto
        uniformtext_mode='hide'  # Oculta textos que não cabem
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
    # Ordena os dados pelo número de genes em ordem decrescente
    compound_gene_ranking_df = compound_gene_ranking_df.sort_values(by='num_genes', ascending=False)

    # Cria o gráfico de barras com valores textuais exibidos
    fig = px.bar(
        compound_gene_ranking_df,
        x='compoundname',
        y='num_genes',
        text='num_genes',  # Adiciona valores textuais às barras
        title='Ranking of Compounds by Gene Interaction',
        template='simple_white'
    )

    # Ajusta a posição do texto e o layout do gráfico
    fig.update_traces(
        textposition='auto',  # Posiciona o texto automaticamente sobre as barras
        marker=dict(color='steelblue')  # Define a cor das barras
    )
    fig.update_layout(
        xaxis_title='Compound',
        yaxis_title='Number of Genes',
        xaxis=dict(
            categoryorder='total descending',  # Ordena compostos em ordem decrescente
            tickangle=45  # Rotaciona os rótulos do eixo X
        ),
        uniformtext_minsize=10,  # Define um tamanho mínimo para o texto
        uniformtext_mode='hide'  # Oculta textos que não cabem
    )

    return fig


# ----------------------------------------
# P7_gene_compound_association
# ----------------------------------------

def plot_gene_compound_scatter(df):
    """
    Cria um scatter plot para visualizar a relação entre genes e compostos, garantindo que todos os rótulos nos eixos X e Y 
    estejam visíveis e que a ordenação seja feita com os compostos mais frequentes na parte superior.

    :param df: DataFrame filtrado contendo as colunas 'genesymbol' e 'compoundname'.
    :return: Objeto Figure com o scatter plot.
    """
    # Define a altura base do gráfico e a altura adicional por rótulo excedente para o eixo Y
    base_height = 400  # Altura base do gráfico
    extra_height_per_label_y = 25  # Altura adicional por cada rótulo excedente no eixo Y

    # Define a largura base do gráfico e a largura adicional por rótulo excedente para o eixo X
    base_width = 800  # Largura base do gráfico
    extra_width_per_label_x = 10  # Largura adicional por cada rótulo excedente no eixo X

    # Calcula o número de rótulos no eixo Y
    num_labels_y = df['compoundname'].nunique()

    # Define um limite para quando adicionar altura extra
    label_limit_y = 1  # Garante que a altura será ajustada mesmo com poucos rótulos

    # Calcula a altura total do gráfico
    if num_labels_y > label_limit_y:
        height = base_height + (num_labels_y - label_limit_y) * extra_height_per_label_y
    else:
        height = base_height

    # Calcula o número de rótulos no eixo X
    num_labels_x = df['genesymbol'].nunique()

    # Define um limite para quando adicionar largura extra
    label_limit_x = 10  # Número de rótulos que cabem na largura base

    # Calcula a largura total do gráfico
    if num_labels_x > label_limit_x:
        width = base_width + (num_labels_x - label_limit_x) * extra_width_per_label_x
    else:
        width = base_width

    # Ordena os compostos pela frequência de ocorrência para priorizar os mais comuns no topo
    compound_order = df['compoundname'].value_counts().index.tolist()

    # Cria o scatter plot
    fig = px.scatter(
        df,
        x='genesymbol',
        y='compoundname',
        title='Scatter Plot of Genes vs Compounds',
        template='simple_white',
        category_orders={'compoundname': compound_order}  # Define a ordem do eixo Y
    )

    # Ajusta o layout do gráfico
    fig.update_layout(
        height=height,
        width=width,
        yaxis=dict(
            categoryorder='total ascending',
            tickmode='array',
            tickvals=df['compoundname'].unique(),
            ticktext=df['compoundname'].unique(),
            automargin=True,  # Garante margens automáticas para rótulos longos
            tickfont=dict(size=10),  # Ajusta o tamanho da fonte dos rótulos
        ),
        xaxis=dict(
            tickangle=45,  # Rotaciona os rótulos do eixo X
            tickmode='array',
            tickvals=df['genesymbol'].unique(),
            ticktext=df['genesymbol'].unique(),
            automargin=True,  # Garante margens automáticas para rótulos longos
            tickfont=dict(size=10),  # Ajusta o tamanho da fonte dos rótulos do eixo X
        ),
        xaxis_title='Gene Symbol',
        yaxis_title='Compound Name',
        margin=dict(l=200, b=100)  # Adiciona margens extras para os eixos X e Y
    )

    return fig


# ----------------------------------------
# P8_gene_sample_association
# ----------------------------------------

def plot_sample_gene_scatter(df):
    """
    Cria um scatter plot para visualizar a relação entre samples e genes, garantindo que todos os rótulos nos eixos X e Y 
    estejam visíveis e que a ordenação seja feita com os samples mais frequentes na parte superior.

    :param df: DataFrame filtrado contendo as colunas 'sample' e 'genesymbol'.
    :return: Objeto Figure com o scatter plot.
    """
    # Define a altura base do gráfico e a altura adicional por rótulo excedente para o eixo Y
    base_height = 400  # Altura base do gráfico
    extra_height_per_label_y = 25  # Altura adicional por cada rótulo excedente no eixo Y

    # Define a largura base do gráfico e a largura adicional por rótulo excedente para o eixo X
    base_width = 800  # Largura base do gráfico
    extra_width_per_label_x = 10  # Largura adicional por cada rótulo excedente no eixo X

    # Calcula o número de rótulos no eixo Y
    num_labels_y = df['sample'].nunique()

    # Define um limite para quando adicionar altura extra
    label_limit_y = 1  # Garante que a altura será ajustada mesmo com poucos rótulos

    # Calcula a altura total do gráfico
    if num_labels_y > label_limit_y:
        height = base_height + (num_labels_y - label_limit_y) * extra_height_per_label_y
    else:
        height = base_height

    # Calcula o número de rótulos no eixo X
    num_labels_x = df['genesymbol'].nunique()

    # Define um limite para quando adicionar largura extra
    label_limit_x = 10  # Número de rótulos que cabem na largura base

    # Calcula a largura total do gráfico
    if num_labels_x > label_limit_x:
        width = base_width + (num_labels_x - label_limit_x) * extra_width_per_label_x
    else:
        width = base_width

    # Ordena os samples pela frequência de ocorrência para priorizar os mais comuns no topo
    sample_order = df['sample'].value_counts().index.tolist()

    # Cria o scatter plot
    fig = px.scatter(
        df,
        x='genesymbol',
        y='sample',
        title='Scatter Plot of Genes vs Samples',
        template='simple_white',
        category_orders={'sample': sample_order}  # Define a ordem do eixo Y
    )

    # Ajusta o layout do gráfico
    fig.update_layout(
        height=height,
        width=width,
        yaxis=dict(
            tickmode='array',
            tickvals=df['sample'].unique(),
            ticktext=df['sample'].unique(),
            automargin=True,  # Garante margens automáticas para rótulos longos
            tickfont=dict(size=10),  # Ajusta o tamanho da fonte dos rótulos
        ),
        xaxis=dict(
            tickangle=45,  # Rotaciona os rótulos do eixo X
            tickmode='array',
            tickvals=df['genesymbol'].unique(),
            ticktext=df['genesymbol'].unique(),
            automargin=True,  # Garante margens automáticas para rótulos longos
            tickfont=dict(size=10),  # Ajusta o tamanho da fonte dos rótulos do eixo X
        ),
        xaxis_title='Gene Symbol',
        yaxis_title='Sample',
        margin=dict(l=200, b=100)  # Adiciona margens extras para os eixos X e Y
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
    # Calcula o número de rótulos nos eixos X e Y
    num_labels_x = len(df.columns)  # Número de rótulos no eixo X (Samples)
    num_labels_y = len(df.index)    # Número de rótulos no eixo Y (Reference AG)

    # Define parâmetros para o tamanho do gráfico
    base_height = 400  # Altura base do gráfico
    base_width = 400   # Largura base do gráfico
    extra_height_per_label = 20  # Altura adicional por rótulo no eixo Y
    extra_width_per_label = 20   # Largura adicional por rótulo no eixo X

    # Calcula altura e largura finais com base no número de rótulos
    height = base_height + (num_labels_y * extra_height_per_label)
    width = base_width + (num_labels_x * extra_width_per_label)

    # Cria o heatmap
    fig = px.imshow(
        df,
        labels=dict(x="Sample", y="Reference AG", color="Compound Count"),
        x=df.columns,
        y=df.index,
        color_continuous_scale="Viridis",
        title="Heatmap of Samples vs Reference AG"
    )

    # Ajusta o layout para exibir todos os rótulos
    fig.update_layout(
        xaxis=dict(
            title=dict(
                text="Sample",
                standoff=50  # Distância entre os rótulos e o eixo X
            ),
            tickangle=45,
            tickfont=dict(size=10),
            automargin=True
        ),
        yaxis=dict(
            title=dict(
                text="Reference AG",
                standoff=50  # Distância entre os rótulos e o eixo Y
            ),
            tickfont=dict(size=10),
            automargin=True
        ),
        margin=dict(l=200, b=200)  # Ajusta as margens gerais do gráfico
    )

    return fig



# ----------------------------------------
# P10_group_by_class Agrupa amostras por perfil de genes para cada classe de compostos
# ----------------------------------------
def plot_sample_groups(df):
    """
    Cria um scatter plot para visualizar os grupos de samples baseados na relação com compoundname utilizando subplots.
    
    :param df: DataFrame contendo os grupos de samples.
    :return: Objeto Figure com os subplots.
    """
    unique_groups = df['grupo'].unique()

    fig = make_subplots(
        rows=1,
        cols=len(unique_groups),
        shared_yaxes=True,  # Compartilha o eixo y para evitar duplicação
        subplot_titles=unique_groups,
        horizontal_spacing=0.1  # Ajustar espaçamento entre as facetas
    )

    # Iterar sobre cada grupo e criar subplots
    for i, group in enumerate(unique_groups):
        group_df = df[df['grupo'] == group]

        # Remover NaNs e garantir dados limpos
        group_df = group_df.dropna(subset=['sample', 'compoundname'])

        # Adicionar trace ao subplot
        fig.add_trace(
            go.Scatter(
                x=group_df['sample'],
                y=group_df['compoundname'],
                mode='markers',
                name=group,
                showlegend=False
            ),
            row=1,
            col=i+1
        )
    
    # Configurar layout
    fig.update_layout(
        title_text='Sample Groups by Compound Interaction',
        template='simple_white',
        showlegend=False,
        height=600,  # Altura total do gráfico
        width=300 * len(unique_groups),  # Largura proporcional ao número de facetas
    )

    # Configurar eixos
    fig.update_yaxes(
        tickangle=0,  # Rótulos verticais
        tickfont=dict(size=10),  # Reduzir o tamanho da fonte
    )

    for i in range(1, len(unique_groups) + 1):
        fig.update_xaxes(row=1, col=i, tickangle=45, title_text=None)
    
    return fig

# ----------------------------------------
# P11 HADEG HEATMAP ORTHOLOGS BY SAMPLE
# ----------------------------------------
def plot_sample_gene_heatmap(grouped_df):
    """
    Cria um heatmap para visualizar a relação entre genes e samples com a contagem de KOs únicos, 
    lidando corretamente com células vazias para evitar fundo indesejado.

    :param grouped_df: DataFrame agrupado por gene e sample com a contagem de KOs únicos.
    :return: Objeto Figure com o heatmap.
    """
    # Criação do DataFrame pivotado
    pivot_df = grouped_df.pivot(index='Gene', columns='sample', values='ko_count')

    # Substituir valores nulos por um indicador (opcional: 0 ou '')
    pivot_df = pivot_df.fillna(0)  # Substituir NaN por 0 (ou escolha um valor adequado para células vazias)
    
    # Criação do heatmap
    fig = px.imshow(
        pivot_df,
        color_continuous_scale='Oranges',  # Escala de cor para valores inteiros
        labels=dict(x="Sample", y="Gene", color="KO Count"),
        title="Heatmap of Ortholog Counts by Sample",
        zmin=0,  # Define o mínimo da escala para garantir valores consistentes
        zmax=pivot_df.max().max(),  # Define o máximo da escala com base nos dados
    )

    # Ajuste do layout para melhorar visualização
    fig.update_layout(
        xaxis=dict(
            title='Sample',
            tickangle=45,  # Rotaciona os labels no eixo X
            automargin=True
        ),
        yaxis=dict(
            title='Gene',
            automargin=True
        ),
        coloraxis_colorbar=dict(
            title="KO Count",
            tickvals=list(range(int(grouped_df['ko_count'].min()), int(grouped_df['ko_count'].max()) + 1)),
            ticktext=list(range(int(grouped_df['ko_count'].min()), int(grouped_df['ko_count'].max()) + 1))
        ),
        plot_bgcolor='white',  # Define o fundo branco
        paper_bgcolor='white'  # Define o fundo branco para o layout
    )

    # Removendo as linhas da grade
    fig.update_xaxes(showgrid=False)
    fig.update_yaxes(showgrid=False)

    return fig

# ----------------------------------------
# P12 HADEG HEATMAP ORTHOLOGS BY SAMPLE (Horizontal Facets)
# ----------------------------------------
def plot_pathway_heatmap(df, selected_sample):
    """
    Cria um heatmap para visualizar a relação entre Pathways e compound_pathways com a contagem de KOs únicos,
    exibindo as facetas em formato horizontal com suporte à rolagem lateral.

    :param df: DataFrame agrupado por Pathway, compound_pathway e sample com a contagem de KOs únicos.
    :param selected_sample: Amostra selecionada para o filtro.
    :return: Objeto Figure com o heatmap.
    """
    from plotly.subplots import make_subplots
    import plotly.graph_objects as go

    # Filtrar o DataFrame pela amostra selecionada
    df = df[df['sample'] == selected_sample]

    # Obter as categorias únicas de compound_pathway
    compound_pathways = df['compound_pathway'].unique()
    n_cols = len(compound_pathways)  # Número de colunas será baseado no número de facetas

    # Configurar subplots com uma linha e múltiplas colunas
    fig = make_subplots(
        rows=1, cols=n_cols,
        shared_yaxes=False,  # Cada faceta terá um eixo Y independente
        horizontal_spacing=0.05,  # Espaçamento horizontal entre os gráficos
        subplot_titles=[f'Compound Pathway: {cp}' for cp in compound_pathways]  # Títulos das facetas
    )

    # Adicionar heatmap para cada compound_pathway
    for i, compound_pathway in enumerate(compound_pathways, start=1):
        # Filtrar o DataFrame para o pathway atual
        df_filtered = df[df['compound_pathway'] == compound_pathway]

        # Criar a matriz do heatmap
        heatmap_data = df_filtered.pivot_table(
            index='Pathway', columns='compound_pathway', values='ko_count', aggfunc='sum', fill_value=0
        )

        # Remover linhas/colunas vazias
        heatmap_data = heatmap_data.loc[(heatmap_data != 0).any(axis=1), (heatmap_data != 0).any(axis=0)]

        # Apenas adicionar se houver dados
        if not heatmap_data.empty:
            heatmap = go.Heatmap(
                z=heatmap_data.values,
                x=heatmap_data.columns,
                y=heatmap_data.index,
                colorscale='Oranges',
                colorbar=dict(
                    title='KO Count',
                    titleside='right',
                    x=1.02 + (i - 1) * 0.1,  # Ajustar posição horizontalmente para cada faceta
                    xanchor='left',
                    y=0.5,  # Centralizar verticalmente
                    lenmode='fraction',
                    len=0.6  # Tamanho da barra de cor
                )
            )
            fig.add_trace(heatmap, row=1, col=i)

        # Atualizar o eixo X para a coluna atual
        fig.update_xaxes(
            tickangle=45,  # Rotação dos rótulos no eixo X
            automargin=True,
            row=1, col=i
        )

    # Atualizar layout global
    fig.update_layout(
        height=600,  # Altura fixa para o gráfico (sem rolagem vertical)
        width=300 * n_cols,  # Largura proporcional ao número de colunas
        title=f'Heatmap of Pathway vs Compound Pathway for Sample {selected_sample}',
        template='simple_white',
        margin=dict(l=100, r=50, t=80, b=50),  # Ajustar margens globais
        xaxis_title='Compound Pathway',  # Título global para o eixo X
        yaxis_title='Pathway'  # Título global para o eixo Y
    )

    # Adicionar rolagem lateral para heatmaps grandes
    fig.update_layout(
        xaxis=dict(
            fixedrange=False  # Permitir rolagem lateral no eixo X
        )
    )

    return fig


# ----------------------------------------
# P12 HADEG HEATMAP ORTHOLOGS BY SAMPLE
# ----------------------------------------
def plot_pathway_heatmap(df, selected_sample):
    """
    Cria um heatmap para visualizar a relação entre Pathways e compound_pathways com a contagem de KOs únicos,
    exibindo as facetas em formato horizontal com um espaçamento fixo de 100 pixels.

    :param df: DataFrame agrupado por Pathway, compound_pathway e sample com a contagem de KOs únicos.
    :param selected_sample: Amostra selecionada para o filtro.
    :return: Objeto Figure com o heatmap.
    """
    from plotly.subplots import make_subplots
    import plotly.graph_objects as go

    # Filtrar o DataFrame pela amostra selecionada
    df = df[df['sample'] == selected_sample]

    # Obter as categorias únicas de compound_pathway
    compound_pathways = df['compound_pathway'].unique()
    n_cols = len(compound_pathways)  # Número de colunas será baseado no número de facetas

    # Configuração do espaço total com espaçamento fixo de 100px entre facetas
    subplot_width = 100  # Largura padrão de cada faceta
    spacing = 500  # Espaço fixo entre as facetas
    total_width = n_cols * subplot_width + (n_cols - 1) * spacing

    # Configurar subplots com uma linha e múltiplas colunas
    fig = make_subplots(
        rows=1, cols=n_cols,
        shared_yaxes=False,  # Cada faceta terá um eixo Y independente
        horizontal_spacing=spacing / total_width  # Converter espaço fixo para valor proporcional
    )

    # Adicionar heatmap para cada compound_pathway
    for i, compound_pathway in enumerate(compound_pathways, start=1):
        # Filtrar o DataFrame para o pathway atual
        df_filtered = df[df['compound_pathway'] == compound_pathway]

        # Criar a matriz do heatmap
        heatmap_data = df_filtered.pivot_table(
            index='Pathway', columns='compound_pathway', values='ko_count', aggfunc='sum', fill_value=0
        )

        # Remover linhas/colunas vazias
        heatmap_data = heatmap_data.loc[(heatmap_data != 0).any(axis=1), (heatmap_data != 0).any(axis=0)]

        # Apenas adicionar se houver dados
        if not heatmap_data.empty:
            heatmap = go.Heatmap(
                z=heatmap_data.values,
                x=heatmap_data.columns,
                y=heatmap_data.index,
                colorscale='Oranges',
                showscale=True,  # Exibe a barra de cores
                colorbar=dict(
                    title='KO Count',
                    titleside='right',
                    x=(subplot_width * (i - 1) + (i - 1) * spacing + subplot_width) / total_width,  # Ajusta a posição horizontal
                    xanchor='left',
                    y=0.5,
                    yanchor='middle',
                    lenmode='fraction',
                    len=0.6  # Tamanho da barra de cor
                )
            )
            fig.add_trace(heatmap, row=1, col=i)

        # Atualizar o eixo X para a coluna atual
        fig.update_xaxes(
            automargin=True,
            row=1, col=i
        )

    # Ajustar o layout global
    fig.update_layout(
        height=600,  # Altura total fixa
        width=total_width,  # Largura total com base no número de facetas e espaçamento
        title=f'Heatmap of Pathway vs Compound Pathway for Sample {selected_sample}',  # Título global removido
        yaxis_title='Pathway',  # Título global do eixo Y mantido
        template='simple_white',
        showlegend=False,  # Remove legendas redundantes
    )

    # Remover os títulos das facetas
    for annotation in fig['layout']['annotations']:
        annotation['text'] = ''

    return fig





##P13
def plot_sample_ko_scatter(scatter_data, selected_pathway):
    """
    Cria um scatter plot para mostrar os KOs associados a cada sample para uma via metabólica.

    :param scatter_data: DataFrame com sample e genesymbol.
    :param selected_pathway: A via metabólica selecionada (usada no título do gráfico).
    :return: Objeto Figure com o scatter plot.
    """
    # Define parâmetros base
    base_height = 400  # Altura base do gráfico
    base_width = 800   # Largura base do gráfico
    extra_width_per_label = 10  # Largura extra por rótulo adicional no eixo X
    label_limit_x = 20  # Limite de rótulos no eixo X antes de ajustar a largura

    # Calcula o número de rótulos únicos no eixo X (samples)
    num_labels_x = scatter_data['sample'].nunique()

    # Ajusta a largura do gráfico dinamicamente
    if num_labels_x > label_limit_x:
        width = base_width + (num_labels_x - label_limit_x) * extra_width_per_label
    else:
        width = base_width

    # Calcula a altura do gráfico com base nos rótulos do eixo Y (genesymbol)
    base_height = 400
    extra_height_per_label = 15
    num_labels_y = scatter_data['genesymbol'].nunique()
    label_limit_y = 1

    if num_labels_y > label_limit_y:
        height = base_height + (num_labels_y - label_limit_y) * extra_height_per_label
    else:
        height = base_height

    # Define espaçamento dinâmico para rótulos no eixo X
    tick_spacing_x = max(1, num_labels_x // 20)  # Exibe no máximo 20 rótulos no eixo X

    # Cria o scatter plot
    fig = px.scatter(
        scatter_data,
        x='sample',
        y='genesymbol',
        title=f'Scatter Plot of KOs by Sample for Pathway: {selected_pathway}',
        template='simple_white'
    )

    # Ajusta o layout do gráfico
    fig.update_layout(
        height=height,
        width=width,
        yaxis=dict(
            categoryorder='total ascending',
            title='Genesymbol',  # Rótulo do eixo Y
            tickmode='array',
            tickvals=scatter_data['genesymbol'].unique(),
            ticktext=scatter_data['genesymbol'].unique(),
            automargin=True,
            tickfont=dict(size=10),
        ),
        xaxis=dict(
            title='Sample',  # Rótulo do eixo X
            tickangle=45,  # Rotaciona rótulos no eixo X em 45 graus
            tickmode='linear',
            tickvals=scatter_data['sample'].unique()[::tick_spacing_x],
            ticktext=scatter_data['sample'].unique()[::tick_spacing_x],
            automargin=True,
        ),
        margin=dict(l=200, b=150)  # Margens para rótulos longos
    )

    return fig


# my_dash_app/utils/plot_processing.py


def plot_enzyme_activity_counts(enzyme_count_df, sample):
    """
    Plota um gráfico de barras das atividades enzimáticas únicas por amostra.

    :param enzyme_count_df: DataFrame com a contagem de atividades enzimáticas únicas.
    :param sample: Nome da amostra selecionada.
    :return: Objeto Figure com o gráfico de barras.
    """
    if enzyme_count_df.empty:
        raise ValueError("O DataFrame de contagem de atividades enzimáticas está vazio.")

    fig = px.bar(
        enzyme_count_df,
        x='enzyme_activity',
        y='unique_ko_count',
        title=f'Unique Enzyme Activities for {sample}',
        text='unique_ko_count',
        template="simple_white"
    )
    fig.update_layout(
        xaxis_title='Enzyme Activity',
        yaxis_title='Unique Gene Count',
        xaxis_tickangle=45
    )
    return fig

#P15
# my_dash_app/utils/plot_processing.py
from dash import html  # Importa o módulo html para criar componentes HTML
import matplotlib
matplotlib.use('Agg')  # Define o backend não interativo
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram
import base64
import io


# my_dash_app/utils/plot_processing.py
from dash import html
import matplotlib
matplotlib.use('Agg')  # Define o backend não interativo
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram
import base64
import io


def plot_dendrogram(clustering_matrix, sample_labels, distance_metric, method):
    """
    Plota o dendrograma com os nomes das amostras como rótulos no eixo X.

    :param clustering_matrix: Matriz de clustering gerada pela função `calculate_sample_clustering`.
    :param sample_labels: Lista de nomes das amostras para usar como rótulos no eixo X.
    :param distance_metric: Métrica de distância utilizada no clustering.
    :param method: Método de clustering utilizado.
    :return: Gráfico do dendrograma no formato Dash HTML.
    """
    # Criar o dendrograma em uma figura
    plt.figure(figsize=(10, 6))
    dendrogram(clustering_matrix, labels=sample_labels)  # Passa os nomes das amostras como labels

    # Adicionar o título dinâmico
    plt.title(f'Sample Clustering Dendrogram\nDistance: {distance_metric.capitalize()}, Method: {method.capitalize()}')
    plt.xlabel('Samples')
    plt.ylabel('Distance')

    # Ajustar o ângulo dos rótulos no eixo X
    plt.xticks(rotation=-45, ha='left')  # Gira os rótulos para -45 graus e alinha à esquerda

    # Converter a figura para base64
    buf = io.BytesIO()
    plt.savefig(buf, format='png', bbox_inches='tight')
    buf.seek(0)
    encoded_image = base64.b64encode(buf.read()).decode('utf-8')
    buf.close()

    # Fechar a figura para evitar conflitos com o Matplotlib
    plt.close()

    # Retornar apenas a imagem como Dash HTML
    return html.Img(src=f'data:image/png;base64,{encoded_image}', style={"width": "100%"})

#P16
# my_dash_app/utils/plot_processing.py
from upsetplot import from_memberships, plot
import matplotlib.pyplot as plt
import pandas as pd
import base64
import io
from sklearn.preprocessing import LabelEncoder



def render_upsetplot(stored_data, selected_samples):
    """
    Renderiza o gráfico UpSet Plot baseado nas amostras e KOs selecionados após merge com o database.

    :param stored_data: Dados armazenados no formato dicionário (stored-data).
    :param selected_samples: Lista de amostras selecionadas.
    :return: Imagem do gráfico UpSet Plot em formato base64.
    """
    # Verificar se há pelo menos 2 amostras selecionadas
    if len(selected_samples) < 2:
        raise ValueError("É necessário selecionar pelo menos duas amostras para renderizar o gráfico.")

    # Converter stored_data para DataFrame
    input_df = pd.DataFrame(stored_data)

    # Mesclar os dados do input com o banco de dados
    merged_data = merge_input_with_database(input_df)

    # Filtrar pelas amostras selecionadas
    filtered_df = merged_data[merged_data['sample'].isin(selected_samples)]

    # Garantir apenas valores únicos de `ko` para cada `sample`
    filtered_df = filtered_df[['sample', 'ko']].drop_duplicates()

    # Preparar os memberships para o UpSet Plot
    memberships = filtered_df.groupby('ko')['sample'].apply(list)
    memberships = memberships.apply(lambda x: list(set(x)))  # Remover duplicatas

    # Converter os memberships em dados do UpSet Plot
    upset_data = from_memberships(memberships)

    # Resolver duplicatas no índice
    upset_data = upset_data.groupby(upset_data.index).sum()

    # Validar e ajustar o índice dinamicamente usando os nomes originais das amostras
    try:
        # Determinar o número de níveis do índice
        num_levels = len(upset_data.index[0]) if isinstance(upset_data.index[0], tuple) else 1

        # Mapear nomes das amostras originais para os níveis
        index_names = selected_samples[:num_levels]  # Usar os nomes originais das amostras selecionadas

        # Ajustar o índice para usar os nomes das amostras
        new_index = pd.MultiIndex.from_tuples(upset_data.index, names=index_names)
        upset_data.index = new_index
    except Exception as e:
        raise ValueError("Falha ao criar MultiIndex: dados malformados ou inconsistentes.")

    # Gerar o gráfico
    plt.figure(figsize=(10, 6))
    plot(upset_data, orientation='horizontal')
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png', bbox_inches='tight')
    plt.close()
    buffer.seek(0)

    # Converter gráfico para base64
    image_data = base64.b64encode(buffer.read()).decode('utf-8')
    return f"data:image/png;base64,{image_data}"

#P17
# my_dash_app/utils/plot_processing.py
import networkx as nx
import plotly.graph_objects as go

def generate_gene_compound_network(network_data):
    """
    Gera um gráfico de rede Gene-Compound usando Plotly e NetworkX.

    :param network_data: DataFrame com colunas 'genesymbol' e 'cpd'.
    :return: Figura Plotly com a rede.
    """
    # Criar o grafo usando NetworkX
    G = nx.Graph()

    # Adicionar nós e arestas
    for _, row in network_data.iterrows():
        G.add_node(row['genesymbol'], type='gene')
        G.add_node(row['compoundname'], type='compound')
        G.add_edge(row['genesymbol'], row['compoundname'])


    # Posição dos nós (usando spring layout para distribuição)
    pos = nx.spring_layout(G, seed=42)

    # Extrair informações para plotly
    node_x = []
    node_y = []
    node_text = []
    node_color = []

    for node, position in pos.items():
        node_x.append(position[0])
        node_y.append(position[1])
        node_text.append(node)
        # Definir cor diferente para genes e compostos
        node_color.append('blue' if G.nodes[node]['type'] == 'gene' else 'green')

    edge_x = []
    edge_y = []
    for edge in G.edges():
        x0, y0 = pos[edge[0]]
        x1, y1 = pos[edge[1]]
        edge_x.extend([x0, x1, None])
        edge_y.extend([y0, y1, None])

    # Criar as arestas
    edge_trace = go.Scatter(
        x=edge_x, y=edge_y,
        line=dict(width=1, color='#888'),
        hoverinfo='none',
        mode='lines'
    )

    # Criar os nós
    node_trace = go.Scatter(
        x=node_x, y=node_y,
        mode='markers',
        hoverinfo='text',
        marker=dict(
            size=10,
            color=node_color,
            line=dict(width=2)
        ),
        text=node_text
    )

    # Criar o layout do gráfico
    fig = go.Figure(
        data=[edge_trace, node_trace],
        layout=go.Layout(
            title="Gene-Compound Network",
            titlefont_size=16,
            showlegend=False,
            margin=dict(b=0, l=0, r=0, t=40),
            xaxis=dict(showgrid=False, zeroline=False),
            yaxis=dict(showgrid=False, zeroline=False)
        )
    )

    return fig


#P18

def plot_heatmap_faceted(df):
    """
    Gera um heatmap faceted para as categorias de toxicidade com uma única legenda compartilhada e hover personalizado.

    :param df: DataFrame com 'compoundname', 'value', 'label', 'category' e 'subcategoria'.
    :return: Figura Plotly com facetas.
    """
    from plotly.subplots import make_subplots
    import plotly.graph_objects as go


    # Obter categorias únicas
    categories = df['category'].unique()

    n_cols = len(categories)
    if n_cols == 0:
        raise ValueError("Nenhuma categoria disponível para plotagem.")

    # Configurar subplots com eixos Y compartilhados e uma única legenda
    fig = make_subplots(
        rows=1, cols=n_cols,
        shared_yaxes=True,  # Compartilhar o eixo Y entre as facetas
        horizontal_spacing=0.05,
        subplot_titles=categories
    )

    # Adicionar heatmaps
    for i, category in enumerate(categories, start=1):
        subset = df[df['category'] == category]

        # Resolver duplicatas agrupando por 'compoundname', 'subcategoria', e 'label'
        subset_grouped = subset.groupby(['compoundname', 'subcategoria', 'label'], as_index=False)['value'].mean()

        # Criar pivot table para o heatmap
        heatmap_data = subset_grouped.pivot(index='compoundname', columns='subcategoria', values='value')

        if heatmap_data.empty:
            continue

        # Criar matriz para o hover personalizado
        hover_text = subset_grouped.pivot(index='compoundname', columns='subcategoria', values='label')

        # Adicionar o heatmap ao subplot
        heatmap = go.Heatmap(
            z=heatmap_data.values,
            x=heatmap_data.columns,
            y=heatmap_data.index,
            text=hover_text.values,  # Adicionar os labels no hover
            hovertemplate=(
                "<b>Compound:</b> %{y}<br>"
                "<b>Subcategory:</b> %{x}<br>"
                "<b>Label:</b> %{text}<br>"
                "<b>Toxicity Score:</b> %{z}<extra></extra>"
            ),
            colorscale="reds",
            showscale=(i == 1),  # Mostra a escala de cores apenas na primeira faceta
            colorbar=dict(
                title='Toxicity Score',  # Título global da escala
                len=0.8,  # Altura da legenda
                x=1.02  # Posição no lado direito
            ) if i == 1 else None  # Configura a legenda apenas para a primeira faceta
        )
        fig.add_trace(heatmap, row=1, col=i)

        # Atualizar os eixos X
        fig.update_xaxes(
            tickangle=45,  # Rotação de 45 graus nos rótulos
            automargin=True,  # Ajustar margens para evitar sobreposição
            row=1, col=i
        )

    # Layout global
    fig.update_layout(
        height=600,
        width=300 * n_cols,  # Largura proporcional ao número de facetas
        title="Faceted Heatmap of Toxicity Predictions with Subcategories on X-axis",
        template="simple_white",
        yaxis_title="Compound Names",  # Define o título global do eixo Y
        margin=dict(l=100, r=50, t=80, b=100)  # Ajusta as margens
    )

    return fig
