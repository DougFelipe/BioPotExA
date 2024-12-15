# Documentação dos Callbacks do Dash App

Este documento descreve os callbacks utilizados na aplicação Dash, explicando a função, os inputs e outputs de cada um.

## Callbacks de Navegação

### `render_tab_content`
- **Descrição**: Atualiza o conteúdo principal com base na aba selecionada pelo usuário.
- **Inputs**: 
  - `'tabs', 'value'`: Valor da aba selecionada.
- **Outputs**: 
  - `'tabs-content', 'children'`: Conteúdo a ser exibido na aba selecionada.

## Callbacks de Processamento de Arquivos

### `handle_upload`
- **Descrição**: Processa o arquivo carregado pelo usuário, validando e armazenando os dados.
- **Inputs**: 
  - `'upload-data', 'contents'`: Conteúdo do arquivo carregado.
- **States**: 
  - `'upload-data', 'filename'`: Nome do arquivo carregado.
- **Outputs**: 
  - `'stored-data', 'data'`: Dados processados armazenados para uso futuro.
  - `'process-data', 'disabled'`: Estado do botão de processamento (habilitado/desabilitado).
  - `'alert-container', 'children'`: Mensagem de alerta sobre o status do processamento.

### `update_table`
- **Descrição**: Atualiza a tabela na interface do usuário com os dados processados após o usuário clicar em "Processar Arquivo".
- **Inputs**: 
  - `'process-data', 'n_clicks'`: Número de cliques no botão de processamento.
- **States**: 
  - `'stored-data', 'data'`: Dados armazenados após o processamento.
- **Outputs**: 
  - `'output-data-upload', 'children'`: Tabela atualizada com os dados processados.

## Callbacks de Visualização de Dados

### `update_database_table`
- **Descrição**: Mostra os dados do banco de dados na interface do usuário após o processamento do arquivo.
- **Inputs**: 
  - `'process-data', 'n_clicks'`: Número de cliques no botão de processamento.
- **Outputs**: 
  - `'database-data-table', 'children'`: Tabela contendo os dados do banco de dados.

### `update_ko_count_table`
- **Descrição**: Atualiza a tabela de contagem de KO com os dados processados.
- **Inputs**: 
  - `'process-data', 'n_clicks'`: Número de cliques no botão de processamento.
- **States**: 
  - `'stored-data', 'data'`: Dados armazenados após o processamento.
- **Outputs**: 
  - `'ko-count-table-container', 'children'`: Tabela de contagem de KO atualizada.

### `toggle_additional_analysis_visibility`
- **Descrição**: Alterna a visibilidade das seções de análise adicional na interface do usuário.
- **Inputs**: 
  - `'process-data', 'n_clicks'`: Número de cliques no botão de processamento.
- **Outputs**: 
  - `'additional-analysis-container', 'style'`: Estilo CSS que controla a visibilidade da seção de análise adicional.

### `update_ko_count_chart`
- **Descrição**: Atualiza o gráfico de barras de contagem de KO com base nos dados processados.
- **Inputs**: 
  - `'process-data', 'n_clicks'`: Número de cliques no botão de processamento.
- **States**: 
  - `'stored-data', 'data'`: Dados armazenados após o processamento.
- **Outputs**: 
  - `'ko-count-bar-chart', 'figure'`: Gráfico de barras atualizado.

### `update_ko_violin_boxplot_chart`
- **Descrição**: Atualiza o gráfico de violino e boxplot com base nos dados processados.
- **Inputs**: 
  - `'process-data', 'n_clicks'`: Número de cliques no botão de processamento.
- **States**: 
  - `'stored-data', 'data'`: Dados armazenados após o processamento.
- **Outputs**: 
  - `'ko-violin-boxplot-chart', 'figure'`: Gráfico de violino e boxplot atualizado.

### `update_merged_table`
- **Descrição**: Atualiza a tabela com dados mesclados após o processamento.
- **Inputs**: 
  - `'process-data', 'n_clicks'`: Número de cliques no botão de processamento.
- **States**: 
  - `'stored-data', 'data'`: Dados armazenados após o processamento.
- **Outputs**: 
  - `'output-merge-table', 'children'`: Tabela atualizada com dados mesclados.

## Callbacks de Controle UI

### `toggle_graph_visibility`
- **Descrição**: Alterna a visibilidade dos gráficos na interface do usuário com base na aba selecionada.
- **Inputs**: 
  - `'tabs', 'value'`: Valor da aba selecionada.
- **Outputs**: 
  - `'output-graphs', 'style'`: Estilo CSS que controla a visibilidade dos gráficos.
