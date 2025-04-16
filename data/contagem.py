import pandas as pd

# Caminho do arquivo
arquivo = r"D:\Doutorado\my_dash\my_dash_app\data\database.csv"

# Ler o arquivo Excel
df = pd.read_excel(arquivo)

# Contar valores únicos na coluna "ko"
valores_unicos = df['compoundname'].nunique()

print(f"Número de valores únicos na coluna 'ko': {valores_unicos}")
