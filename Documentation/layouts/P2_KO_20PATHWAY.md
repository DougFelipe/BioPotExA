# P2_KO_20PATHWAY.py

## Descrição
Este arquivo define layouts específicos para a análise das vias KO, incluindo gráficos de barras com filtros para amostras e vias selecionadas.

## Funções e Componentes

### Função `get_pathway_ko_bar_chart_layout`
- **Descrição**: Constrói o layout para o gráfico de barras da análise das vias KO, incluindo filtros.
- **Retorno**: Uma `html.Div` contendo o gráfico de barras e os filtros.

### Função `get_sample_ko_pathway_bar_chart_layout`
- **Descrição**: Constrói o layout para o gráfico de barras da análise dos KOs em samples para a via selecionada, incluindo filtros.
- **Retorno**: Uma `html.Div` contendo o gráfico de barras e os filtros.

## Importações
- `html`, `dcc` do `dash`: Utilizados para construir componentes de layout.
- `create_card` de `utils.components`: Utilizado para criar componentes de cartão (comentado no código).

## Layouts Definidos

### Gráfico de Barras de Análise das Vias KO
- **Dropdown**: `pathway-sample-dropdown`
- **Descrição do Layout**:
  - Filtros por amostra com Dropdown.
  - Gráfico de barras (`dcc.Graph`) com ID `pathway-ko-bar-chart`.

### Gráfico de Barras de Análise dos KOs em Samples para a Via Selecionada
- **Dropdown**: `via-dropdown`
- **Descrição do Layout**:
  - Filtros por sample com Dropdown.
  - Gráfico de barras (`dcc.Graph`) com ID `via-ko-bar-chart`.

