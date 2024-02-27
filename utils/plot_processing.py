import plotly.express as px

def plot_ko_count(ko_count_df):
    """
    Cria um gráfico de barras da contagem de KOs por amostra com base no DataFrame processado.

    :param ko_count_df: DataFrame com a contagem de KOs por amostra.
    :return: Objeto Figure com o gráfico de barras.
    """
    fig = px.bar(ko_count_df, x='sample', y='ko_count', title="Contagem de KO por Sample")
    fig.update_layout(xaxis_tickangle=-45)  # Atualizar os rótulos do eixo x para ficarem em um ângulo de 45 graus
    
    return fig
