from connection.MySQLConnection import MySQLConnection
from utils.functions import load_init, load_sensores_disponiveis, load_not_found
from service.simulador import refinar_sensores, ativar_sensores
from config.logger import logger
from dotenv import load_dotenv
import os
import importlib


load_dotenv()

SIMULATION_INTERVAL = float(os.getenv("SIMULATION_INTERVAL"))
USE_IOT_HUB = os.getenv('USE_IOT_HUB', 'false').lower() == 'true'
SENDING_INTERVAL = float(os.getenv("SENDING_INTERVAL"))
OPEN_WEATHER_INTERVAL = int(os.getenv("OPEN_WEATHER_INTERVAL"))
SKIP_INTRO = load_init(skip=os.getenv("SKIP_INTRO") in ("True", "true", "1"))


if USE_IOT_HUB:
    logger.log("info", "Using Azure IoT Hub")
    module = importlib.import_module('service.iot_hub')
else:
    logger.log("info", "Using HTTP Client (AWS S3 Storage via API Gateway)")
    module = importlib.import_module('service.http_client')


def setup():
    connMySQL = MySQLConnection()
    logger.log("info", f"Conexão estabelecida com o banco: [{connMySQL.get_database()}]")

    sensores_banco = connMySQL.get_sensores()
    logger.log("info", f"Modelos de sensores carregados com sucesso. [{len(sensores_banco)}] sensores encontrados.")

    sensores_disponiveis = load_sensores_disponiveis(sensores_banco)
    logger.log("info", f"Modelos de sensores disponíveis: {sensores_disponiveis}")

    sensores_clientes = connMySQL.get_sensores_para_simular()
    logger.log("info", f"Quantidade de sensores para simular: [{len(sensores_clientes)}]")

    sensores = refinar_sensores(sensores_clientes, sensores_disponiveis)
    logger.log("info", f"Quantidade de sensores refinados: [{len(sensores)}]")

    if not sensores:
        logger.log("error", "Nenhum sensor encontrado para simulação.")
        load_not_found()
        exit()

    instancias = connMySQL.load_sensores(sensores)
    ativar_sensores(instancias)

    ids = [sensor.id for sensor in instancias]
    mapper = connMySQL.get_sensor_mapping(ids)
    logger.log("info", f"Mapeamento de sensores carregado com sucesso. [{len(mapper)}] sensores mapeados para o IoT Hub.")

    connMySQL.close_connection()

    return instancias, module, SIMULATION_INTERVAL, SENDING_INTERVAL, OPEN_WEATHER_INTERVAL