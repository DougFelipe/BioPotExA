import plotly.express as px
import plotly.graph_objects as go


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



def plot_compound_scatter(filtered_df):
    """
    Cria um gráfico de pontos para a relação de amostras com compostos.

    :param filtered_df: DataFrame com os dados filtrados.
    :return: Objeto Figure com o gráfico de pontos.
    """
    fig = px.scatter(filtered_df, x='sample', y='compoundname', color='compoundclass', template="simple_white")
    fig.update_layout(
        xaxis_title='Sample',
        yaxis_title='Compound',
        title='Scatter Plot of Samples vs Compounds'
    )
    return fig
