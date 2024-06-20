# data_processing.py

## Descrição
Este arquivo contém funções auxiliares para mesclagem e processamento de dados. As funções são usadas para mesclar dados de entrada com bancos de dados e processar esses dados para diferentes análises, como contagem de KOs e gráficos de compostos.

## Funções e Componentes

### Funções de Mesclagem de Dados
- `merge_input_with_database(input_data, database_filepath='data/database.xlsx')`
  - Mescla os dados de entrada com os dados do banco de dados.
  - **Parâmetros**:
    - `input_data`: DataFrame com os dados de entrada.
    - `database_filepath`: Caminho para o arquivo do banco de dados.
  - **Retorno**:
    - DataFrame resultante da mesclagem.
- `merge_with_kegg(input_df, kegg_path='data/kegg_20degradation_pathways.xlsx')`
  - Mescla os dados de entrada com os dados do KEGG.
  - **Parâmetros**:
    - `input_df`: DataFrame com os dados de entrada.
    - `kegg_path`: Caminho para o arquivo de dados do KEGG.
  - **Retorno**:
    - DataFrame resultante da mesclagem.

### Funções de Processamento de Dados
- `process_ko_data(merged_df)`
  - Processa os dados de KO, contando os KOs únicos por amostra.
  - **Parâmetros**:
    - `merged_df`: DataFrame com os dados mesclados ou uma lista de dicionários que possa ser convertida para DataFrame.
  - **Retorno**:
    - DataFrame com a contagem de KOs únicos por amostra.
- `process_ko_data_violin(df)`
  - Processa os dados para obter a contagem de KOs únicos por amostra.
  - **Parâmetros**:
    - `df`: DataFrame com os dados de entrada.
  - **Retorno**:
    - DataFrame com a contagem de KOs por amostra.
- `count_ko_per_pathway(merged_df)`
  - Conta os KOs únicos para cada pathway em cada amostra.
  - **Parâmetros**:
    - `merged_df`: DataFrame resultante da mesclagem com os dados do KEGG.
  - **Retorno**:
    - DataFrame com a contagem de KOs únicos por pathway por amostra.
- `count_ko_per_sample_for_pathway(merged_df, selected_pathway)`
  - Conta os KOs únicos para uma via metabólica em cada sample.
  - **Parâmetros**:
    - `merged_df`: DataFrame resultante da mesclagem com os dados do KEGG.
    - `selected_pathway`: A via metabólica selecionada.
  - **Retorno**:
    - DataFrame com a contagem de KOs únicos por sample para a via selecionada.
- `process_compound_data(merged_df)`
  - Processa os dados para o gráfico de pontos de compostos.
  - **Parâmetros**:
    - `merged_df`: DataFrame com os dados mesclados.
  - **Retorno**:
    - DataFrame processado.
- `process_sample_ranking(merged_df)`
  - Processa os dados para calcular o ranking das amostras com base no número de compostos únicos.
  - **Parâmetros**:
    - `merged_df`: DataFrame mesclado.
  - **Retorno**:
    - DataFrame com as amostras e o número de compostos únicos associados, ordenado por número de compostos.

## Importações
- `pandas` (`pd`): Utilizado para manipulação e análise de dados.
- `plotly.graph_objects` (`go`): Utilizado para criação de gráficos com Plotly.
- `plotly.express` (`px`): Utilizado para criação de gráficos simplificados com Plotly.
