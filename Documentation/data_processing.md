# Documentação do Script de Análise de Dados

Este script contém funções para mesclar, processar e visualizar dados relacionados a análises genômicas e biotecnológicas.

## Módulos Importados

- `pandas`: Utilizado para manipulação e análise de dados.
- `plotly.graph_objects` e `plotly.express`: Usados para criar visualizações interativas de dados.

## Funções de Mesclagem de Dados

### `merge_input_with_database`

Mescla os dados de entrada fornecidos pelo usuário com um banco de dados externo.

- **Parâmetros**:
  - `input_data`: DataFrame com os dados de entrada do usuário.
  - `database_filepath`: String opcional que indica o caminho do arquivo do banco de dados. Padrão: `'data/database.xlsx'`.

- **Retorno**: DataFrame resultante da mesclagem dos dados de entrada com o banco de dados.

### `merge_with_kegg`

Mescla os dados de entrada com informações do Kyoto Encyclopedia of Genes and Genomes (KEGG).

- **Parâmetros**:
  - `input_df`: DataFrame com os dados de entrada do usuário.
  - `kegg_path`: String opcional que indica o caminho do arquivo de dados do KEGG. Padrão: `'data/kegg_degradation_pathways.xlsx'`.

- **Retorno**: DataFrame resultante da mesclagem dos dados de entrada com os dados do KEGG.

## Funções de Processamento de Dados

### `process_ko_data`

Processa os dados mesclados para contar a ocorrência única de KOs (Orthologous Groups) por amostra e gera um gráfico de barras.

- **Parâmetros**:
  - `merged_df`: DataFrame contendo os dados mesclados.

- **Retorno**: Objeto `Figure` do Plotly contendo o gráfico de barras da contagem de KOs por amostra.

## Funções de Criação de Gráficos

### `create_violin_boxplot`

Cria um gráfico de violino com caixa embutida que mostra a distribuição da contagem de KOs únicos por amostra.

- **Parâmetros**:
  - `df`: DataFrame contendo os dados para plotagem.

- **Retorno**: Objeto `Figure` do Plotly contendo o gráfico de violino.
