# P4_rank_compounds_callbacks.py

## Descrição
Este arquivo define os callbacks utilizados para o ranking das amostras com base no número de compostos únicos associados. Inclui a atualização do gráfico de dispersão que mostra o ranking das amostras.

## Callbacks

### `update_rank_compounds_plot`
- **Descrição**: Atualiza o gráfico de dispersão que mostra o ranking das amostras baseado no número de compostos únicos associados.
- **Entradas**:
  - `process-data`: Número de cliques no botão de processamento de dados.
  - `stored-data`: Dados armazenados no lado do cliente.
- **Saídas**:
  - `rank-compounds-scatter-plot`: Figura do gráfico de dispersão das amostras ranqueadas.

## Importações
- `dash`, `callback`: Utilizados para definir os callbacks.
- `dash.dependencies.Input`, `Output`, `State`: Utilizados para definir entradas, saídas e estados dos callbacks.
- `dash.exceptions.PreventUpdate`: Utilizado para prevenir atualizações desnecessárias nos callbacks.
- `pandas`: Utilizado para manipulação de dados.
- `app`: Importação da aplicação Dash.
- `utils.data_processing`: Funções para mesclagem e processamento de dados.
- `utils.plot_processing`: Funções para criação de gráficos.
