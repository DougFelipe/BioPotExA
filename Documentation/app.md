# app.py

## Descrição
Este arquivo inicializa a aplicação Dash, aplicando um tema externo do Bootstrap e configurando opções adicionais.

## Funções e Componentes
- Criação da instância principal da aplicação Dash.
- Aplicação de um tema Bootstrap.
- Configuração para suprimir exceções de callbacks.

## Importações
- `dash`: 
  - `Dash`
- `dash_bootstrap_components`: 
  - `dbc`

## Instância da Aplicação
- **`app = Dash(__name__, external_stylesheets=[dbc.themes.MINTY], suppress_callback_exceptions=True)`**
  - **Parâmetros**:
    - `__name__`: Define o nome do módulo da aplicação.
    - `external_stylesheets=[dbc.themes.MINTY]`: Aplica o tema Minty do Bootstrap.
    - `suppress_callback_exceptions=True`: Configuração para suprimir exceções de callbacks, permitindo a definição de callbacks antes dos componentes serem renderizados.

## Tema Bootstrap
- **`external_stylesheets=[dbc.themes.MINTY]`**: Utiliza o tema Minty do Bootstrap para estilização da aplicação.

## Suprimir Exceções de Callbacks
- **`suppress_callback_exceptions=True`**: Permite a definição de callbacks antes que todos os componentes sejam renderizados no layout, útil para grandes aplicações com múltiplos layouts.
