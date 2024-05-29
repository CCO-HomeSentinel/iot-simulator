from dotenv import load_dotenv
import time
import os
import importlib

load_dotenv()

USE_IOT_HUB = os.getenv('USE_IOT_HUB', 'false').lower() == 'true'
INTERVALO_TENTATIVA_ENVIO_JSON = int(os.getenv('INTERVALO_TENTATIVA_ENVIO_JSON'))

if USE_IOT_HUB:
    module = importlib.import_module('service.iot_hub')
else:
    module = importlib.import_module('service.http_client')

def tentar_enviar_json_periodicamente(dados):
    success = False

    while not success:
        success = module.enviar_json(dados)

        if not success:
            time.sleep(INTERVALO_TENTATIVA_ENVIO_JSON)