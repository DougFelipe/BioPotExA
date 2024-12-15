# index.py

## Descrição
Este arquivo inicializa a aplicação Dash, define o layout principal e configura a navegação entre as abas.

## Funções e Componentes
- Importações de componentes essenciais do Dash e layouts personalizados.
- Configuração do layout principal da aplicação.
- Inicialização do servidor.

## Importações
- `dash`: 
  - `Dash`, `dcc`, `html`
- `components.header`: 
  - `Header`
- `layouts`: 
  - `get_about_layout`, `get_dataAnalysis_layout`
- `callbacks`: 
  - `P1_COUNT_KO_callbacks`, `P2_KO_20PATHWAY_callbacks`, `callbacks`, `P3_compounds_callbacks`, `P4_rank_compounds_callbacks`
- `app`: 
  - Instância principal da aplicação Dash

## Layout
### Cabeçalho
- **Header**: Inclui o componente de cabeçalho personalizado.

### Abas de Navegação
- **dcc.Tabs**: Navegação entre as páginas 'About' e 'Data Analysis'.
  - **Propriedades**:
    - `id="tabs"`
    - `value='tab-about'`
    - `className='main-tabs'`
    - `children`: 
      - `dcc.Tab(label='About', value='tab-about', className='tab', selected_className='tab--selected')`
      - `dcc.Tab(label='Data Analysis', value='tab-data-analysis', className='tab', selected_className='tab--selected')`

### Conteúdo das Abas
- **html.Div (tabs-content)**: Atualizado dinamicamente com base na aba selecionada.
  - **Propriedades**:
    - `id='tabs-content'`
    - `className='tabs-content'`

### Armazenamento de Dados no Lado do Cliente
- **dcc.Store**: Utilizado para compartilhar dados entre callbacks sem afetar o layout.
  - **Propriedades**:
    - `id='stored-data'`

### Container para Gráficos (Inicialmente Oculto)
- **html.Div (output-graphs)**: Pode ser utilizado para exibir gráficos com base em dados processados.
  - **Propriedades**:
    - `id='output-graphs'`
    - `style={'display': 'none'}`

## Inicialização
- **`app.run_server(debug=True)`**: Inicia o servidor em modo de depuração.
