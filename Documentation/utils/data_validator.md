# data_validator.py

## Descrição
Este arquivo contém funções para validação e processamento de dados de entrada, especificamente para decodificação de arquivos de texto e extração de dados usando expressões regulares. As funções aqui são usadas para garantir que os dados de entrada estejam no formato correto e para extrair informações relevantes.

## Funções e Componentes

### Função de Validação e Processamento de Input
- `validate_and_process_input(contents, filename)`
  - Valida e processa o input, decodificando e extraindo dados de um arquivo de texto.
  - **Etapas**:
    1. Verificação do formato do arquivo.
    2. Decodificação do conteúdo se estiver em base64.
    3. Separação do conteúdo em linhas e processamento usando expressões regulares.
    4. Criação de um DataFrame pandas a partir dos dados extraídos.
  - **Parâmetros**:
    - `contents`: Conteúdo do arquivo (codificado em base64 se vindo de um upload).
    - `filename`: Nome do arquivo para verificar a extensão.
  - **Retorno**:
    - Tupla contendo um DataFrame pandas com os dados e uma mensagem de erro, se houver.

### Funções Auxiliares
- `decode_content_if_base64(contents)`
  - Decodifica o conteúdo de base64, se necessário.
  - **Parâmetros**:
    - `contents`: Conteúdo do arquivo, possivelmente codificado em base64.
  - **Retorno**:
    - Conteúdo decodificado como string.
- `process_content_lines(content)`
  - Separa o conteúdo em linhas e extrai dados usando expressões regulares.
  - **Parâmetros**:
    - `content`: Conteúdo decodificado do arquivo.
  - **Retorno**:
    - Tupla contendo um DataFrame com os dados extraídos e uma mensagem de erro, se houver.

## Importações
- `pandas` (`pd`): Utilizado para manipulação e análise de dados.
- `re`: Utilizado para operações com expressões regulares.
- `base64`: Utilizado para decodificação de conteúdo base64.