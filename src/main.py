from connection.MySQLConnection import MySQLConnection
from service.simulador import simular, refinar_sensores, ativar_sensores
from utils.functions import load_init, clear, load_sensores_disponiveis, load_not_found
from time import sleep
from dotenv import load_dotenv
import os
from datetime import datetime
from config.logger_config import Logger
import threading
from thread.thread_functions import tentar_enviar_json_periodicamente

load_dotenv()

ENABLE_LOGS = os.getenv("ENABLE_LOGS").lower() == "true"
INTERVALO_SIMULADOR = float(os.getenv("INTERVALO_SIMULADOR"))
INTERVALO_ENVIO = float(os.getenv("INTERVALO_ENVIO"))
OPEN_WEATHER_INTERVALO = int(os.getenv("OPEN_WEATHER_INTERVALO"))
SKIP_INTRO = load_init(skip=os.getenv("SKIP_INTRO") in ("True", "true", "1"))

if ENABLE_LOGS:
    logger = Logger()


def set_up():
    connMySQL = MySQLConnection(logger)

    sensores_banco = connMySQL.get_sensores()
    sensores_disponiveis = load_sensores_disponiveis(sensores_banco)
    sensores_clientes = connMySQL.get_sensores_para_simular()

    sensores = refinar_sensores(sensores_clientes, sensores_disponiveis)

    if not sensores:
        load_not_found()
        exit()

    instancias = connMySQL.load_sensores(sensores)
    ativar_sensores(instancias)

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
                        temperatura = sensor.consultar_open_weather(None, logger)
                    else:
                        temperatura = sensor.consultar_open_weather(temperatura, logger)
                    sensor.temperatura_memoria = temperatura
                    break

            ultima_temperatura_start = datetime.now()

        novos_dados = simular(instancias, ultimos_dados, logger)
        dados["registros"].extend(novos_dados)
        quantidade_rodadas += 1

        clear()
        print(
            f"{len(dados['registros'])} dados simulados\n{quantidade_envios} envios realizados\n{quantidade_rodadas} rodadas\n"
        )

        if (datetime.now() - start).seconds >= INTERVALO_ENVIO:
            envio_thread = threading.Thread(
                target=tentar_enviar_json_periodicamente, args=(dados,)
            )
            envio_thread.start()

            start = datetime.now()
            quantidade_envios += 1
            dados = {"registros": []}

        sleep(INTERVALO_SIMULADOR)


if __name__ == "__main__":
    main()
