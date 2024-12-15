# my_dash_app/utils/data_loader.py

# Importa o pandas para manipulação de dados.
import pandas as pd

# Função para carregar o banco de dados a partir de um arquivo Excel.
def load_database(filepath):
    """
    Carrega o banco de dados a partir de um arquivo Excel.

    :param filepath: Caminho para o arquivo Excel.
    :return: DataFrame pandas contendo os dados do arquivo.
    """
    df = pd.read_excel(filepath)  # Lê o arquivo Excel e armazena em um DataFrame.
    return df  # Retorna o DataFrame com os dados.
