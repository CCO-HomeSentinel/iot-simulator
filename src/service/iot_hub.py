from dotenv import load_dotenv
import os
import json
from config.logger_config import Logger
from azure.iot.device import IoTHubDeviceClient, Message

load_dotenv()

IOT_HUB_CONNECTION_STRING = os.getenv('IOT_HUB_CONNECTION_STRING')

ENABLE_LOGS = os.getenv('ENABLE_LOGS').lower() == 'true'

if ENABLE_LOGS:
    logger = Logger().get_logger()

def enviar_json(dados):
    client = IoTHubDeviceClient.create_from_connection_string(IOT_HUB_CONNECTION_STRING)
    try:
        client.connect()
        json_content = json.dumps(dados)
        message = Message(json_content)
        client.send_message(message)
    except Exception as ex:
        logger.error(f'Ocorreu um erro ao enviar os dados para o Iot Hub: {ex}')
    finally:
        client.disconnect()

