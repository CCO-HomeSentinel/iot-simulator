import os
from dotenv import load_dotenv
from datetime import datetime
import json
from config.logger_config import Logger

load_dotenv()
ENABLE_LOGS = os.getenv('ENABLE_LOGS').lower() == 'true'

if ENABLE_LOGS:
    logger = Logger().get_logger()

path_atual = os.path.dirname(os.path.abspath(__file__))
dois_diretorios_acima = os.path.dirname(os.path.dirname(path_atual))

def transformar_dict_em_json_file(dados):
    try:
        filename = f"registros_{datetime.now().strftime('%Y%m%dT%H%M%S')}.json"
        full_path = os.path.join(dois_diretorios_acima, 'data', 'json', filename)
        path = os.path.dirname(full_path)

        if not os.path.exists(path):
            os.makedirs(path)

        with open(full_path, 'w') as file:
            json.dump(dados, file)

        return filename, full_path
    except Exception as e:
        logger.error(f'Erro ao transformar dict em json file. {e}')
        exit()

def destruir_arquivo(path):
    try:
        os.remove(path)
        logger.info(f'Arquivo deletado: {path}')
        return True
    except:
        logger.error(f'Erro ao deletar arquivo: {path}')
        return False