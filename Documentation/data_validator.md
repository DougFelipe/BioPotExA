# Documentação do Script de Validação e Processamento de Inputs

Este script é projetado para validar e processar arquivos de texto carregados, decodificando conteúdos codificados em base64 e extraindo informações específicas através de expressões regulares, para finalmente estruturar os dados em um DataFrame do pandas.

## Importações Necessárias

- `pandas`: Utilizado para a criação e manipulação de DataFrames.
- `re`: Módulo de expressões regulares para busca de padrões específicos no texto.
- `base64`: Módulo para decodificação de strings codificadas em base64.

## Funções Principais

### `validate_and_process_input`

Essa função é responsável por validar o formato do arquivo, decodificar seu conteúdo se necessário, processar este conteúdo e retornar os dados em um DataFrame do pandas, juntamente com uma mensagem de erro, se aplicável.

- **Parâmetros**:
  - `contents`: String contendo o conteúdo do arquivo, que pode estar codificado em base64.
  - `filename`: String com o nome do arquivo, utilizado para validar a extensão do arquivo.

- **Retorno**: Tupla contendo um DataFrame pandas com os dados extraídos e uma mensagem de erro, se houver.

#### Etapas de Processamento:
1. **Verificação da Extensão do Arquivo**: Certifica que o arquivo é um `.txt`.
2. **Decodificação do Conteúdo**: Usa `decode_content_if_base64` para decodificar o conteúdo de base64, se aplicável.
3. **Processamento de Linhas**: Invoca `process_content_lines` para extrair dados das linhas de conteúdo.
4. **Criação de DataFrame**: Os dados extraídos são organizados em um DataFrame.

### Funções Auxiliares

#### `decode_content_if_base64`

Decodifica o conteúdo de base64 para string, se o conteúdo estiver codificado.

- **Parâmetros**:
  - `contents`: String potencialmente codificada em base64.

- **Retorno**: String decodificada.

#### `process_content_lines`

Processa cada linha do conteúdo, extraindo informações com expressões regulares e organizando-as em um formato estruturado.

- **Parâmetros**:
  - `content`: String contendo o conteúdo decodificado do arquivo.

- **Retorno**: Tupla contendo um DataFrame com os dados organizados e uma mensagem de erro, se aplicável.

#### Padrões de Expressões Regulares Utilizados:
- **Identificadores**: Expressão regular para identificar linhas que começam com `>` seguidas de caracteres (identificadores de amostra).
- **Dados (KOs)**: Expressão regular para extrair valores que começam com `K` seguidos de dígitos (ex: K01234).

## Exemplo de Uso

```python
# Supondo que 'uploaded_file_contents' e 'uploaded_file_name' sejam suas variáveis de conteúdo e nome de arquivo:

df, error = validate_and_process_input(uploaded_file_contents, uploaded_file_name)

if error:
    print(f"Erro: {error}")
else:
    print(df)
