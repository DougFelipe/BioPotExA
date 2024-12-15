# P2_KO_20PATHWAY_callbacks.py

## Descrição
Este arquivo define os callbacks utilizados na análise das vias KO. Os callbacks incluem a inicialização do dropdown e gráfico de barras, e a atualização do gráfico de barras com base na seleção do dropdown.

## Callbacks

### `initialize_dropdown_and_chart`
- **Descrição**: Inicializa as opções do dropdown e o valor padrão do gráfico de barras após o processamento dos dados.
- **Entradas**:
  - `process-data`: Número de cliques no botão de processamento de dados.
  - `stored-data`: Dados armazenados no lado do cliente.
- **Saídas**:
  - `pathway-sample-dropdown`: Opções e valor padrão do dropdown para seleção de amostras.

### `update_bar_chart`
- **Descrição**: Atualiza o gráfico de barras com base na seleção do dropdown.
- **Entradas**:
  - `pathway-sample-dropdown`: Valor selecionado no dropdown.
  - `stored-data`: Dados armazenados no lado do cliente.
- **Saídas**:
  - `pathway-ko-bar-chart`: Figura do gráfico de barras de contagem de KO por vias.

### `initialize_via_dropdown`
- **Descrição**: Inicializa as opções do dropdown das vias após o processamento dos dados.
- **Entradas**:
  - `process-data`: Número de cliques no botão de processamento de dados.
  - `stored-data`: Dados armazenados no lado do cliente.
- **Saídas**:
  - `via-dropdown`: Opções e valor padrão do dropdown para seleção de vias.

### `update_bar_chart_for_via`
- **Descrição**: Atualiza o gráfico de barras com base na seleção do dropdown das vias.
- **Entradas**:
  - `via-dropdown`: Valor selecionado no dropdown das vias.
  - `stored-data`: Dados armazenados no lado do cliente.
- **Saídas**:
  - `via-ko-bar-chart`: Figura do gráfico de barras de contagem de KO por sample para a via selecionada.

## Importações
- `dash`, `html`, `dcc`: Utilizados para construir componentes de layout e callbacks.
- `dash.dependencies.Input`, `Output`, `State`: Utilizados para definir entradas, saídas e estados dos callbacks.
- `dash.exceptions.PreventUpdate`: Utilizado para prevenir atualizações desnecessárias nos callbacks.
- `pandas`: Utilizado para manipulação de dados.
- `app`: Importação da aplicação Dash.
- `utils.data_processing`: Funções para mesclagem e processamento de dados.
- `utils.plot_processing`: Funções para criação de gráficos.
