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

ENABLE_LOGS = os.getenv('ENABLE_LOGS').lower() == 'true'

if ENABLE_LOGS:
    logger = Logger()

def main():
    start = datetime.now()
    quantidade_envios = 0
    quantidade_rodadas = 0
    intervalo_geracao = float(os.getenv('INTERVALO_SIMULADOR'))
    intervalo_envio = float(os.getenv('INTERVALO_ENVIO'))
    temperatura = None
    ultima_temperatura_start = None
    intervalo_requisicao_temperatura = int(os.getenv('OPEN_WEATHER_INTERVALO'))

    dados = {'registros': []}

    load_init(skip=os.getenv('SKIP_INTRO') in ('True', 'true', '1'))
    connMySQL = MySQLConnection()

    sensores_banco = connMySQL.get_sensores()
    sensores_disponiveis = load_sensores_disponiveis(sensores_banco)
    sensores_clientes = connMySQL.get_sensores_para_simular()

    sensores = refinar_sensores(sensores_clientes, sensores_disponiveis)
    instancias = connMySQL.load_sensores(sensores)
    ativar_sensores(instancias)

    if not sensores:
        load_not_found()
        exit()

    while True:
        ultimos_dados = dados['registros'][-len(instancias):] if dados['registros'] else None

        if temperatura == None or (datetime.now() - ultima_temperatura_start).seconds >= intervalo_requisicao_temperatura:
            for sensor in instancias:
                if sensor.tipo == 'temperatura':
                    temperatura = sensor.consultar_open_weather()
                    sensor.temperatura_memoria = temperatura
                    break

            ultima_temperatura_start = datetime.now()

        novos_dados = simular(instancias, ultimos_dados)
        dados['registros'].extend(novos_dados)
        quantidade_rodadas += 1

        clear()
        print(f"{len(dados['registros'])} dados simulados\n{quantidade_envios} envios realizados\n{quantidade_rodadas} rodadas\n")

        if (datetime.now() - start).seconds >= intervalo_envio:
            envio_thread = threading.Thread(target=tentar_enviar_json_periodicamente, args=(dados,))
            envio_thread.start()

            start = datetime.now()
            quantidade_envios += 1
            dados = {'registros': []}
            
        sleep(intervalo_geracao)

if __name__ == '__main__':
    main()