from dotenv import load_dotenv
import os
import sys
import json
from azure.iot.device import IoTHubDeviceClient, Message

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from config.logger import logger

load_dotenv()

IOT_HUB_CONNECTION_STRING = os.getenv('IOT_HUB_CONNECTION_STRING')

def formatter(dados):
    dados.get("registros", [])

    return dados


def enviar_json(dados):
    client = IoTHubDeviceClient.create_from_connection_string(IOT_HUB_CONNECTION_STRING)
    dados = formatter(dados)

    try:
        client.connect()
        json_content = json.dumps(dados)
        message = Message(json_content)
        client.send_message(message)
        logger.log("info", "Dados enviados para o Iot Hub")
    except Exception as ex:
        logger.log("error", f'Ocorreu um erro ao enviar os dados para o Iot Hub: {ex}')
    finally:
        client.disconnect()

