# my_dash_app/utils/data_validator.py
import pandas as pd
import re
import base64

# ----------------------------------------
# Função de Validação e Processamento de Input
# ----------------------------------------

def validate_and_process_input(contents, filename):
    """
    Valida e processa o input, decodificando e extraindo dados de um arquivo de texto.
    
    Etapas:
    1. Verificação do formato do arquivo.
    2. Decodificação do conteúdo se estiver em base64.
    3. Separação do conteúdo em linhas e processamento usando expressões regulares.
    4. Criação de um DataFrame pandas a partir dos dados extraídos.
    
    :param contents: Conteúdo do arquivo (codificado em base64 se vindo de um upload).
    :param filename: Nome do arquivo para verificar a extensão.
    :return: Tupla contendo um DataFrame pandas com os dados e uma mensagem de erro, se houver.
    """
    
    # 1. Verifica se o arquivo é um .txt
    if not filename.endswith('.txt'):
        return None, "O arquivo não é um .txt"
    
    # 2. Decodifica o conteúdo se estiver em base64
    content = decode_content_if_base64(contents)
        
    # 3. Processa as linhas do conteúdo
    df, error = process_content_lines(content)
    
    return df, error

# Função auxiliar para decodificar conteúdo base64
def decode_content_if_base64(contents):
    """
    Decodifica o conteúdo de base64, se necessário.
    
    :param contents: Conteúdo do arquivo, possivelmente codificado em base64.
    :return: Conteúdo decodificado como string.
    """
    if contents.startswith('data'):
        content_type, content_string = contents.split(',')
        decoded = base64.b64decode(content_string)
        return decoded.decode('utf-8')
    else:
        return contents

# Função auxiliar para processar as linhas de conteúdo
def process_content_lines(content):
    """
    Separa o conteúdo em linhas e extrai dados usando expressões regulares.
    
    :param content: Conteúdo decodificado do arquivo.
    :return: Tupla contendo um DataFrame com os dados extraídos e uma mensagem de erro, se houver.
    """
    lines = content.split('\n')
    identifier_pattern = re.compile(r'^>([^\n]+)')
    data_pattern = re.compile(r'^(K\d+)')
    
    data = []
    current_identifier = None
    
    for line in lines:
        identifier_match = identifier_pattern.match(line)
        data_match = data_pattern.match(line)
        
        if identifier_match:
            current_identifier = identifier_match.group(1).strip()
        elif data_match and current_identifier:
            ko_value = data_match.group(1).strip()
            data.append({'sample': current_identifier, 'ko': ko_value})
        elif line.strip() == '':
            continue
        else:
            return None, f"File must be in valid format, such as in sample data! Invalid characters identified: {line}"
    
    if not data:
        return None, "O arquivo não contém dados válidos."
    
    return pd.DataFrame(data), None
