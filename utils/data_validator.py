import pandas as pd
import re
import base64

# Função corrigida de validação e processamento de input
def validate_and_process_input(contents, filename):
    # 1 - Verifique se o arquivo é um .txt
    if not filename.endswith('.txt'):
        return None, "O arquivo não é um .txt"
    
    # 2 - Decodifique o conteúdo se estiver em base64
    if contents.startswith('data'):
        content_type, content_string = contents.split(',')
        decoded = base64.b64decode(content_string)
        content = decoded.decode('utf-8')
    else:
        content = contents
        
    # 3 - Separe o conteúdo em linhas
    lines = content.split('\n')
    
    # 4 - Prepare os padrões regex para identificador e dados
    identifier_pattern = re.compile(r'^>([^\n]+)')
    data_pattern = re.compile(r'^(K\d+)')
    
    # 5 - Processe as linhas
    current_identifier = None
    data = []
    for line in lines:
        identifier_match = identifier_pattern.match(line)
        data_match = data_pattern.match(line)
        if identifier_match:
            current_identifier = identifier_match.group(1).strip()  # Atualiza o identificador
        elif data_match and current_identifier:
            ko_value = data_match.group(1).strip()  # Separa o valor KO
            data.append({'sample': current_identifier, 'ko': ko_value})
        elif line.strip() == '':  # Ignora linhas em branco
            continue
        else:
            # Se a linha não corresponder ao padrão e não for vazia, o arquivo é inválido
            return None, f"O arquivo contém linhas inválidas: {line}"
    
    # 6 - Verifique se os dados foram coletados
    if not data:
        return None, "O arquivo não contém dados válidos."
    
    # 7 - Crie um DataFrame com os dados no formato tidy
    df = pd.DataFrame(data)
    
    return df, None  # Retorna o DataFrame e None para o erro