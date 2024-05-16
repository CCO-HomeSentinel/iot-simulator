from dotenv import load_dotenv
from service.http_client import enviar_json
import time
import os

load_dotenv()

INTERVALO_TENTATIVA_ENVIO_JSON = int(os.getenv('INTERVALO_TENTATIVA_ENVIO_JSON'))

def tentar_enviar_json_periodicamente(dados):
    success = False

    while not success:
        success = enviar_json(dados)

        if not success:
            time.sleep(INTERVALO_TENTATIVA_ENVIO_JSON)