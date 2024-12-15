# components.py

## Descrição
Este arquivo contém funções auxiliares para a criação de componentes de layout reutilizáveis no Dash.

## Funções e Componentes
- `create_card`: Função para criar um card com título e descrição, estilizado para exibição de resultados de análise.

## Importações
- `dash`: 
  - `html`
  - `dcc`

## Função `create_card`
- **`def create_card(title, content):`**
  - **Parâmetros**:
    - `title`: O título a ser exibido no card.
    - `content`: A descrição ou conteúdo a ser exibido no card.
  - **Retorno**:
    - Um componente `html.Div` contendo um título (`html.H3`) e uma descrição (`html.P`), com classes CSS personalizadas para estilização.
