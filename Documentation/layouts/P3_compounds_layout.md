# P3_compounds_layout.py

## Descrição
Este arquivo define o layout para o gráfico de dispersão dos compostos, incluindo um filtro por classe de composto. Ele é utilizado para visualizar a relação entre amostras e compostos, filtrados por suas classes.

## Funções e Componentes

### Função `get_compound_scatter_layout`
- **Descrição**: Constrói o layout para o gráfico de dispersão dos compostos, incluindo um filtro por classe de composto.
- **Retorno**: Uma `html.Div` contendo o gráfico de dispersão e o filtro.

## Importações
- `html`, `dcc` do `dash`: Utilizados para construir componentes de layout.
- `dbc` do `dash_bootstrap_components`: Utilizado para criar componentes estilizados com Bootstrap.

## Layout Definido

### Gráfico de Dispersão de Compostos
- **Dropdown**: `compound-class-dropdown`
  - Permite seleção única.
  - Placeholder: 'Select a Compound Class'.
- **Gráfico de Dispersão**: `dcc.Graph` com ID `compound-scatter-plot`.
- **Card**: Utiliza `dbc.Card` e `dbc.CardBody` para estilização.
- **Estilização**:
  - Classe `graph-container` adicionada para estilização.
  - Altura definida como `auto` e rolagem vertical permitida com `overflowY: auto`.
