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
        tokens.append((tipo, valor))
    return tokens

def logar_tokens(tokens):
    for token in tokens:
        print(token)