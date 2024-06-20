# plot_processing.py

## Descrição
Este arquivo contém funções auxiliares para a criação de gráficos usando Plotly, incluindo gráficos de barras, gráficos de violino e gráficos de dispersão, para visualização de dados processados.

## Funções e Componentes
- `plot_ko_count`: Cria um gráfico de barras da contagem de KOs por amostra.
- `create_violin_plot`: Cria um gráfico de violino com caixa para a contagem de KOs únicos por amostra.
- `plot_pathway_ko_counts`: Plota um gráfico de barras dos KOs únicos para cada pathway na amostra selecionada.
- `plot_sample_ko_counts`: Plota um gráfico de barras dos KOs únicos para uma via metabólica selecionada em cada sample.
- `plot_compound_scatter`: Cria um gráfico de dispersão para visualizar a relação entre amostras e compostos, filtrados por classe de composto.
- `plot_sample_ranking`: Cria um gráfico de dispersão para visualizar o ranking das amostras com base no número de compostos únicos.

## Importações
- `plotly.express` (`px`): Utilizado para criar gráficos de visualização de dados.
- `plotly.graph_objects` (`go`): Utilizado para gráficos personalizados.

## Função `plot_ko_count`
- **`def plot_ko_count(ko_count_df):`**
  - **Parâmetros**:
    - `ko_count_df`: DataFrame com a contagem de KOs por amostra.
  - **Retorno**:
    - Objeto Figure com o gráfico de barras.

## Função `create_violin_plot`
- **`def create_violin_plot(ko_count_per_sample):`**
  - **Parâmetros**:
    - `ko_count_per_sample`: DataFrame com a contagem de KOs por amostra.
  - **Retorno**:
    - Objeto Figure com o gráfico de violino.

## Função `plot_pathway_ko_counts`
- **`def plot_pathway_ko_counts(pathway_count_df, selected_sample):`**
  - **Parâmetros**:
    - `pathway_count_df`: DataFrame com a contagem de KOs únicos por pathway por amostra.
    - `selected_sample`: Amostra selecionada para o plot.
  - **Retorno**:
    - Objeto Figure com o gráfico de barras.

## Função `plot_sample_ko_counts`
- **`def plot_sample_ko_counts(sample_count_df, selected_pathway):`**
  - **Parâmetros**:
    - `sample_count_df`: DataFrame com a contagem de KOs únicos por sample para a via selecionada.
    - `selected_pathway`: A via metabólica selecionada.
  - **Retorno**:
    - Objeto Figure com o gráfico de barras.

## Função `plot_compound_scatter`
- **`def plot_compound_scatter(df):`**
  - **Parâmetros**:
    - `df`: DataFrame filtrado contendo as colunas 'sample', 'compoundname', e 'compoundclass'.
  - **Retorno**:
    - Objeto Figure com o gráfico de dispersão.

## Função `plot_sample_ranking`
- **`def plot_sample_ranking(sample_ranking_df):`**
  - **Parâmetros**:
    - `sample_ranking_df`: DataFrame com as amostras e o número de compostos únicos associados.
  - **Retorno**:
    - Objeto Figure com o gráfico de dispersão.