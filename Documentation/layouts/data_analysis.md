# data_analysis.py

## Descrição
Este arquivo configura a página de Análise de Dados na aplicação Dash. Ele define o layout principal da página de análise de dados, incluindo componentes para upload e processamento de dados, além de exibir os resultados da análise.

## Funções e Componentes
- `get_dataAnalysis_page()`: Função que cria e retorna a página principal de Análise de Dados.
- `get_dataAnalysis_layout()`: Função que compila e retorna o layout completo de Análise de Dados.
- `create_card(title, content)`: Função auxiliar para criar um card com título e conteúdo.

## Importações
- `dash`: `dcc`, `html`
- `dash.dependencies`: `Input`, `Output`, `State`
- `dash_bootstrap_components`: `dbc`
- `components.step_guide`: `create_step_guide`
- `components.features_list`: `create_list_card`, `features_list_1`
- `layouts.results`: `get_results_layout`

## Estrutura do Código

### Importações
Importa os componentes essenciais do Dash, dependências, componentes de terceiros (Bootstrap) e funções auxiliares específicas do aplicativo.

### Função `get_dataAnalysis_page()`
- **Armazena o estado da página**: Utiliza `dcc.Store` para armazenar o estado da página (`page-state`).
- **Conteúdo Inicial**:
  - **Título e Guia de Passos**: Adiciona um título "How to Use" e um componente de guia de passos.
  - **Upload e Processamento de Dados**:
    - Componente de upload (`dcc.Upload`).
    - Botão para processar dados (`html.Button`).
    - Botão para visualizar resultados (`html.Button`), inicialmente oculto.
  - **Lista de Características**: Adiciona uma lista de características da análise de dados.
- **Conteúdo dos Resultados**: Div para exibir os resultados da análise de dados, inicialmente oculta, que é atualizada dinamicamente com o layout de resultados (`get_results_layout`).

### Função `get_dataAnalysis_layout()`
Compila e retorna o layout completo de Análise de Dados, chamando a função `get_dataAnalysis_page`.

### Função `create_card(title, content)`
Cria e retorna um card HTML com um título (`title`) e conteúdo (`content`), usado para exibir informações em formato de card.
