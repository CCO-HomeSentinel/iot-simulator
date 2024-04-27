import os
from datetime import datetime
import json

path_atual = os.path.dirname(os.path.abspath(__file__))
dois_diretorios_acima = os.path.dirname(os.path.dirname(path_atual))

def transformar_dict_em_json_file(dados):
    filename = f"registros_{datetime.now().strftime('%Y%m%dT%H%M%S')}.json"
    path = os.path.join(dois_diretorios_acima, 'data', 'json', filename)

    with open(path, 'w') as file:
        json.dump(dados, file)

    return filename, path

def destruir_arquivo(path):
    os.remove(path)
    return True