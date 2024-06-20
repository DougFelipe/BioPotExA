# about.py

## Descrição
Este arquivo define o layout para a aba "About" da aplicação, que inclui uma introdução ao tema da biorremediação e uma descrição detalhada do BioPExA.

## Funções e Componentes
- Definição e retorno do layout para a aba "About".
- Descrição do BioPExA e sua importância para a biorremediação.
- Inclusão de imagens e lista de características do BioPExA.

## Importações
- `dash`:
  - `html`: Utilizado para criar componentes HTML.
- `components.about_features_list`:
  - `create_about_features_list`: Função para criar a lista de características do BioPExA.
  - `about_features_list`: Lista de características do BioPExA.

## Função `get_about_layout`
Define e retorna o layout para a aba "About".

**Descrição**:
Esta função constrói a interface da aba "About", que inclui uma introdução ao BioPExA, uma descrição detalhada de seu objetivo e importância, e uma lista de características.

**Retorno**:
- `html.Div`: Retorna um componente HTML Div contendo todo o layout da aba "About".

## Estrutura do Layout
1. **Título e Subtítulo**:
   - **Título**: "BioPExA".
   - **Subtítulo**: "Biorremediation Potential Explorer & Analyzer".
2. **Parágrafo de Introdução**:
   - Descrição detalhada do BioPExA, incluindo seu objetivo e importância.
3. **Container de Imagens**:
   - Imagens relacionadas aos Objetivos de Desenvolvimento Sustentável (SDGs).
4. **Lista de Características**:
   - Utilização da função `create_about_features_list` para gerar uma lista detalhada das características do BioPExA.

## Componentes HTML
- **`html.Div`**: Container principal para o layout.
- **`html.H3`**: Títulos e subtítulos.
- **`html.Hr`**: Linha horizontal para separação.
- **`html.P`**: Parágrafos de texto.
- **`html.Br`**: Quebra de linha.
- **`html.Img`**: Imagens.