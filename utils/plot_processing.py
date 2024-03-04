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