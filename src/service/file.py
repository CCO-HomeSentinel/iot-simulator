import os
import sys
from datetime import datetime
import json
from service.iot_hub import formatter

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from config.logger import logger


path_atual = os.path.dirname(os.path.abspath(__file__))
dois_diretorios_acima = os.path.dirname(os.path.dirname(path_atual))


def transformar_dict_em_json_file(dados):
    try:
        dados_formatados = formatter(dados)
        filename = f"registros_{datetime.now().strftime('%Y%m%dT%H%M%S')}.json"
        full_path = os.path.join(dois_diretorios_acima, "data", "json", filename)
        path = os.path.dirname(full_path)

        if not os.path.exists(path):
            os.makedirs(path)

        with open(full_path, "w") as file:
            json.dump(dados_formatados, file)

        logger.log("info", f"Arquivo criado: {full_path}")

        return filename, full_path
    except Exception as e:
            logger.log("error", f"Erro ao transformar dict em json file. {e}")
            exit()


def destruir_arquivo(path):
    try:
        os.remove(path)
        logger.log("info", f"Arquivo deletado: {path}")
        return True
    except:
        logger.log("error", f"Erro ao deletar arquivo: {path}")
        return False
