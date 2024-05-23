import re

# Definindo os padrões para os tokens
especificacoes_tokens = [
    ('NUMERO',   r'\d+(\.\d*)?'),   # Números inteiros ou decimais
    ('UNIDADE',  r'[°C|%|Pa]'),     # Unidades de medida
    ('ID',       r'[a-zA-Z_]\w*'),  # Identificadores (nomes de sensores)
    ('DOISPONTOS', r':'),           # Dois pontos
    ('IGNORAR',  r'[ \t]+'),        # Espaços e tabulações
    ('NOVA_LINHA', r'\n'),          # Quebras de linha
    ('ERRO',     r'.'),             # Qualquer outro caractere
]

# Compilando as expressões regulares em um único padrão
padrao_tokens = re.compile('|'.join(f'(?P<{nome}>{padrao})' for nome, padrao in especificacoes_tokens))

# Lista de identificadores esperados
identificadores_esperados = ["sensor_temp", "sensor_humidity", "pressure", "altitude"]

def distancia_levenshtein(s1, s2):
    if len(s1) < len(s2):
        return distancia_levenshtein(s2, s1)

    if len(s2) == 0:
        return len(s1)

    previous_row = range(len(s2) + 1)
    for i, c1 in enumerate(s1):
        current_row = [i + 1]
        for j, c2 in enumerate(s2):
            insertions = previous_row[j + 1] + 1
            deletions = current_row[j] + 1
            substitutions = previous_row[j] + (c1 != c2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row

    return previous_row[-1]

def analisar(texto):
    tokens = []
    for correspondencia in padrao_tokens.finditer(texto):
        tipo = correspondencia.lastgroup
        valor = correspondencia.group(tipo)
        if tipo == 'NUMERO':
            valor = float(valor) if '.' in valor else int(valor)
        elif tipo == 'NOVA_LINHA':
            pass
        elif tipo == 'IGNORAR':
            continue
        elif tipo == 'ERRO':
            raise RuntimeError(f'Caractere inesperado: {valor}')
        elif tipo == 'ID':
            # Calcular a distância de Levenshtein com identificadores esperados
            distancia_minima = float('inf')
            identificador_correto = valor
            for identificador in identificadores_esperados:
                distancia = distancia_levenshtein(valor, identificador)
                if distancia < distancia_minima:
                    distancia_minima = distancia
                    identificador_correto = identificador
            
            # Substituir valor pelo identificador correto, se necessário
            if distancia_minima <= 3:  # Tolerância de distância
                print(f"Corrigindo '{valor}' para '{identificador_correto}'")
                valor = identificador_correto

        tokens.append((tipo, valor))
    return tokens

def logar_tokens(tokens):
    for token in tokens:
        print(token)

# Exemplo de uso
texto_exemplo = """sensor_tamp: 23°C
sensor_humidty: 45%
pressur: 1013Pa"""
tokens = analisar(texto_exemplo)
logar_tokens(tokens)