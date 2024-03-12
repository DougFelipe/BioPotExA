import plotly.express as px
import plotly.graph_objects as go


def plot_ko_count(ko_count_df):
    """
    Cria um gráfico de barras da contagem de KOs por amostra com base no DataFrame processado.

    :param ko_count_df: DataFrame com a contagem de KOs por amostra.
    :return: Objeto Figure com o gráfico de barras.
    """
    fig = px.bar(ko_count_df, x='sample', y='ko_count', title="Contagem de KO por Sample")
    fig.update_layout(xaxis_tickangle=-45)  # Atualizar os rótulos do eixo x para ficarem em um ângulo de 45 graus
    
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
                    hover_name='sample', hover_data={'sample': False, 'ko_count': True})
    

    
    fig.update_traces(marker=dict(size=5, opacity=1),
                      line=dict(width=1),
                      jitter=0.3, pointpos=0)

    # Atualiza o layout do gráfico
    fig.update_layout(title_text="Distribuição da Contagem de KOs Únicos por Sample",
                      yaxis_title='Contagem de KOs Únicos',
                      showlegend=False, template='plotly_white',
                      #yaxis=dict(range=[0, ko_count_per_sample['ko_count'].max() + 100]),
                      xaxis_title='')  # Definindo o título do eixo x como vazio

    return fig




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
        title=f'Contagem Única de KOs para {selected_sample}',
        text='unique_ko_count'  # Adiciona o valor da contagem sobre as barras
    )

    # Ajustar o layout do gráfico, se necessário
    fig.update_layout(
        xaxis_title='Pathway',
        yaxis_title='Contagem de KOs Únicos',
        xaxis={'categoryorder':'total descending'}  # Garante que a ordenação será mantida no gráfico
    )

    return fig
