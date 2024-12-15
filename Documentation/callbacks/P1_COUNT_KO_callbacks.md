# P1_COUNT_KO_callbacks.py

## Descrição
Este arquivo define os callbacks utilizados na análise de contagem de KOs. Os callbacks incluem a atualização do gráfico de barras, gráfico de violino e boxplot, RangeSlider e as opções do dropdown baseados nos dados carregados.

## Callbacks

### `update_ko_count_chart`
- **Descrição**: Atualiza o gráfico de barras de contagem de KO com base nos valores do RangeSlider.
- **Entradas**:
  - `ko-count-range-slider`: Valores do RangeSlider para filtrar a contagem de KO.
  - `stored-data`: Dados armazenados no lado do cliente.
- **Saídas**:
  - `ko-count-bar-chart`: Figura do gráfico de barras de contagem de KO.

### `update_range_slider_values`
- **Descrição**: Atualiza os valores máximos, valores atuais e marcas do RangeSlider com base nos dados carregados.
- **Entradas**:
  - `process-data`: Número de cliques no botão de processamento de dados.
  - `stored-data`: Dados armazenados no lado do cliente.
- **Saídas**:
  - `ko-count-range-slider`: Valores atualizados do RangeSlider.

### `update_ko_violin_boxplot_chart`
- **Descrição**: Atualiza o gráfico de violino e boxplot com base na seleção do dropdown e no clique do botão de processamento de dados.
- **Entradas**:
  - `process-data`: Número de cliques no botão de processamento de dados.
  - `sample-dropdown`: Valores selecionados no dropdown.
  - `stored-data`: Dados armazenados no lado do cliente.
- **Saídas**:
  - `ko-violin-boxplot-chart`: Figura do gráfico de violino e boxplot.

### `update_dropdown_options`
- **Descrição**: Atualiza as opções do dropdown com base nos dados carregados.
- **Entradas**:
  - `process-data`: Número de cliques no botão de processamento de dados.
  - `stored-data`: Dados armazenados no lado do cliente.
- **Saídas**:
  - `sample-dropdown`: Opções atualizadas do dropdown.

## Importações
- `dash`, `html`, `dash_table`, `dcc`: Utilizados para construir componentes de layout e callbacks.
- `dash.dependencies.Input`, `Output`, `State`: Utilizados para definir entradas, saídas e estados dos callbacks.
- `dash.exceptions.PreventUpdate`: Utilizado para prevenir atualizações desnecessárias nos callbacks.
- `pandas`: Utilizado para manipulação de dados.
- `app`: Importação da aplicação Dash.
- `utils.data_processing`: Funções para mesclagem e processamento de dados.
- `utils.plot_processing`: Funções para criação de gráficos.

