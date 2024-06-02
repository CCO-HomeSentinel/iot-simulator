from dotenv import load_dotenv
import os
import sys
import json
from config.logger import Logger
from azure.iot.device import IoTHubDeviceClient, Message

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from config.logger import logger

load_dotenv()

IOT_HUB_CONNECTION_STRING = os.getenv('IOT_HUB_CONNECTION_STRING')

def enviar_json(dados):
    client = IoTHubDeviceClient.create_from_connection_string(IOT_HUB_CONNECTION_STRING)
    try:
        client.connect()
        json_content = json.dumps(dados)
        message = Message(json_content)
        client.send_message(message)
        logger.log("info", f'Dados enviados para o Iot Hub: {json_content}')
    except Exception as ex:
        logger.log("error", f'Ocorreu um erro ao enviar os dados para o Iot Hub: {ex}')
    finally:
        client.disconnect()

