# P1_KO_COUNT.py

## Descrição
Este arquivo define layouts específicos para a seção de contagem de KO, incluindo gráficos de barras e gráficos de violino/boxplot, cada um com seus respectivos filtros.

## Funções e Componentes

### Função `get_ko_count_bar_chart_layout`
- **Descrição**: Constrói o layout para o gráfico de barras da contagem de KO, incluindo filtros.
- **Retorno**: Uma `html.Div` contendo o gráfico de barras e os filtros.

### Função `get_ko_violin_boxplot_layout`
- **Descrição**: Constrói o layout para o gráfico de violino e boxplot da contagem de KO, incluindo filtros.
- **Retorno**: Uma `html.Div` contendo o gráfico de violino e boxplot e os filtros.

## Importações
- `html`, `dcc` do `dash`: Utilizados para construir componentes de layout.
- `create_card` de `utils.components`: Utilizado para criar componentes de cartão (comentado no código).
- `create_range_slider` de `utils.filters`: Utilizado para criar um componente de RangeSlider.

## Layouts Definidos

### Gráfico de Barras de Contagem de KO
- **Slider**: `ko-count-range-slider`
- **Descrição do Layout**:
  - Filtros por intervalo com RangeSlider.
  - Gráfico de barras (`dcc.Graph`) com ID `ko-count-bar-chart`.

### Gráfico de Violino e Boxplot de Contagem de KO
- **Dropdown**: `sample-dropdown`
- **Descrição do Layout**:
  - Filtros por amostra com Dropdown.
  - Gráfico de violino e boxplot (`dcc.Graph`) com ID `ko-violin-boxplot-chart`.