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
        fig.update_xaxes(row=1, col=i, tickangle=-45, title_text=None)
    
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
    Cria um heatmap para visualizar a relação entre Pathways e compound_pathways com a contagem de KOs únicos.

    :param df: DataFrame agrupado por Pathway, compound_pathway e sample com a contagem de KOs únicos.
    :param selected_sample: Amostra selecionada para o filtro.
    :return: Objeto Figure com o heatmap.
    """
    df = df[df['sample'] == selected_sample]

    compound_pathways = df['compound_pathway'].unique()
    n_rows = len(compound_pathways)

    fig = make_subplots(
        rows=n_rows, cols=1,
        shared_xaxes=False,
        vertical_spacing=0.02,
        subplot_titles=[f'Compound Pathway: {cp}' for cp in compound_pathways]
    )

    for i, compound_pathway in enumerate(compound_pathways, start=1):
        df_filtered = df[df['compound_pathway'] == compound_pathway]
        heatmap_data = df_filtered.pivot_table(index='Pathway', columns='compound_pathway', values='ko_count', aggfunc='sum', fill_value=0)

        heatmap_data = heatmap_data.loc[(heatmap_data != 0).any(axis=1), (heatmap_data != 0).any(axis=0)]

        if not heatmap_data.empty:
            heatmap = go.Heatmap(
                z=heatmap_data.values,
                x=heatmap_data.columns,
                y=heatmap_data.index,
                colorscale='Oranges',
                colorbar=dict(
                    title='KO Count',
                    titleside='right',
                    x=1.02,  # Posiciona a barra de cores fora do heatmap
                    xanchor='left',
                    y=1 - (i-1)*(1/n_rows + 0.02),  # Ajusta a posição y para não sobrepor
                    yanchor='top',
                    lenmode='fraction',
                    len=1/n_rows - 0.02  # Divide o comprimento da barra de cores pelo número de linhas
                )
            )

            fig.add_trace(heatmap, row=i, col=1)

        fig.update_xaxes(ticktext=[''], row=i, col=1)

    fig.update_layout(
        height=300 * n_rows,
        title=f'Heatmap of Pathway vs Compound Pathway for Sample {selected_sample}',
    )

    return fig

##P13

def plot_sample_ko_scatter(scatter_data, selected_pathway):
    """
    Cria um scatter plot para mostrar os KOs associados a cada sample para uma via metabólica.

    :param scatter_data: DataFrame com `sample` e `ko`.
    :param selected_pathway: A via metabólica selecionada (usada no título do gráfico).
    :return: Objeto Figure com o scatter plot.
    """
    fig = px.scatter(
        scatter_data,
        x='sample',
        y='genesymbol',
        title=f'Scatter Plot of KOs by Sample for Pathway: {selected_pathway}',
        template='simple_white'
    )
    fig.update_layout(
        xaxis_title='',  # Remove título do eixo x
        yaxis_title='',  # Remove título do eixo y
        xaxis_tickangle=-45  # Rotaciona os rótulos do eixo x
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
    print("DEBUG: Dados armazenados carregados no DataFrame:")
    print(input_df.head())

    # Mesclar os dados do input com o banco de dados
    merged_data = merge_input_with_database(input_df)
    print("DEBUG: Dados após merge com o database:")
    print(merged_data.head())

    # Filtrar pelas amostras selecionadas
    filtered_df = merged_data[merged_data['sample'].isin(selected_samples)]
    print("DEBUG: Dados filtrados pelas amostras selecionadas:")
    print(filtered_df.head())

    # Garantir apenas valores únicos de `ko` para cada `sample`
    filtered_df = filtered_df[['sample', 'ko']].drop_duplicates()
    print("DEBUG: Dados após remoção de duplicatas (únicos por sample e KO):")
    print(filtered_df.head())

    # Preparar os memberships para o UpSet Plot
    memberships = filtered_df.groupby('ko')['sample'].apply(list)
    memberships = memberships.apply(lambda x: list(set(x)))  # Remover duplicatas
    print("DEBUG: Memberships gerados:")
    print(memberships.head())

    # Converter os memberships em dados do UpSet Plot
    upset_data = from_memberships(memberships)
    print("DEBUG: Dados do UpSet Plot gerados:")
    print(upset_data)

    # Resolver duplicatas no índice
    upset_data = upset_data.groupby(upset_data.index).sum()
    print("DEBUG: Dados após consolidação:")
    print(upset_data)

    # Validar e ajustar o índice dinamicamente usando os nomes originais das amostras
    try:
        # Determinar o número de níveis do índice
        num_levels = len(upset_data.index[0]) if isinstance(upset_data.index[0], tuple) else 1

        # Mapear nomes das amostras originais para os níveis
        index_names = selected_samples[:num_levels]  # Usar os nomes originais das amostras selecionadas
        print(f"DEBUG: Nomes do índice gerados dinamicamente: {index_names}")

        # Ajustar o índice para usar os nomes das amostras
        new_index = pd.MultiIndex.from_tuples(upset_data.index, names=index_names)
        upset_data.index = new_index
        print("DEBUG: Índice ajustado para MultiIndex:")
        print(upset_data.index)
    except Exception as e:
        print(f"DEBUG: Falha ao criar MultiIndex: {e}")
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
    print("DEBUG: Gráfico gerado com sucesso.")
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
        G.add_node(row['cpd'], type='compound')
        G.add_edge(row['genesymbol'], row['cpd'])

    print(f"DEBUG: Número de nós: {G.number_of_nodes()}, Número de arestas: {G.number_of_edges()}")

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
