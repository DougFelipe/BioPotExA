# P3_compounds_callbacks.py

## Descrição
Este arquivo define os callbacks utilizados na análise dos compostos, incluindo a inicialização do dropdown de classes de compostos e a atualização do gráfico de dispersão com base na seleção do dropdown.

## Callbacks

### `initialize_compound_class_dropdown`
- **Descrição**: Inicializa as opções do dropdown de classes de compostos e o valor padrão após o processamento dos dados.
- **Entradas**:
  - `process-data`: Número de cliques no botão de processamento de dados.
  - `stored-data`: Dados armazenados no lado do cliente.
- **Saídas**:
  - `compound-class-dropdown`: Opções e valor padrão do dropdown de classes de compostos.

### `update_compound_scatter_plot`
- **Descrição**: Atualiza o gráfico de dispersão com base na seleção do dropdown de classes de compostos.
- **Entradas**:
  - `compound-class-dropdown`: Valor selecionado no dropdown de classes de compostos.
  - `stored-data`: Dados armazenados no lado do cliente.
- **Saídas**:
  - `compound-scatter-plot`: Figura do gráfico de dispersão dos compostos filtrados pela classe selecionada.

## Importações
- `dash`, `callback`: Utilizados para definir os callbacks.
- `dash.dependencies.Input`, `Output`, `State`: Utilizados para definir entradas, saídas e estados dos callbacks.
- `dash.exceptions.PreventUpdate`: Utilizado para prevenir atualizações desnecessárias nos callbacks.
- `pandas`: Utilizado para manipulação de dados.
- `app`: Importação da aplicação Dash.
- `utils.data_processing`: Funções para mesclagem e processamento de dados.
- `utils.plot_processing`: Funções para criação de gráficos.
