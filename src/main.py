from connection.MySQLConnection import MySQLConnection
from service.simulador import simular, refinar_sensores, ativar_sensores
from service.iot_hub import enviar_json
from utils.functions import load_init, clear, load_sensores_disponiveis, load_not_found
from time import sleep
from dotenv import load_dotenv
import os
from datetime import datetime
from config.logger import logger
from service.iot_hub import setup
import importlib
import threading
from thread.thread_functions import tentar_enviar_json_periodicamente

load_dotenv()

INTERVALO_SIMULADOR = float(os.getenv("INTERVALO_SIMULADOR"))
USE_IOT_HUB = os.getenv('USE_IOT_HUB', 'false').lower() == 'true'
INTERVALO_ENVIO = float(os.getenv("INTERVALO_ENVIO"))
OPEN_WEATHER_INTERVALO = int(os.getenv("OPEN_WEATHER_INTERVALO"))
SKIP_INTRO = load_init(skip=os.getenv("SKIP_INTRO") in ("True", "true", "1"))
if USE_IOT_HUB:
    module = importlib.import_module('service.iot_hub')
else:
    module = importlib.import_module('service.http_client')


def set_up():
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

    setup(mapper)

    connMySQL.close_connection()

    return instancias


def main():
    instancias = set_up()

    start = datetime.now()
    quantidade_envios = 0
    quantidade_rodadas = 0
    temperatura = None
    ultima_temperatura_start = None
    dados = {"registros": []}

    while True:
        ultimos_dados = (
            dados["registros"][-len(instancias) :] if dados["registros"] else None
        )

        if (
            temperatura == None
            or (datetime.now() - ultima_temperatura_start).seconds
            >= OPEN_WEATHER_INTERVALO
        ):
            for sensor in instancias:
                if sensor.tipo == "temperatura":
                    if temperatura == None:
                        temperatura = sensor.consultar_open_weather(None)
                    else:
                        temperatura = sensor.consultar_open_weather(temperatura)
                    sensor.temperatura_memoria = temperatura
                    break

            ultima_temperatura_start = datetime.now()

        novos_dados = simular(instancias, ultimos_dados)
        dados["registros"].extend(novos_dados)
        quantidade_rodadas += 1

        clear()
        print(f"{len(dados['registros'])} dados simulados\n{quantidade_envios} envios realizados\n{quantidade_rodadas} rodadas\n")

        if (datetime.now() - start).seconds >= INTERVALO_ENVIO:
            try:
                module.enviar_json(dados)
            except Exception as ex:
                logger.log("error", f"Ocorreu um erro ao enviar os dados para o API Gateway: {ex}")

            start = datetime.now()
            quantidade_envios += 1
            dados = {"registros": []}

        sleep(INTERVALO_SIMULADOR)


if __name__ == "__main__":
    main()
