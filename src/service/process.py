from time import sleep
from datetime import datetime
from config.logger import logger
from utils.functions import clear
from service.simulador import simular


def start(instances, module, SIMULATION_INTERVAL, SENDING_INTERVAL, OPEN_WEATHER_INTERVAL):
    start = datetime.now()
    ultima_temperatura_start = datetime.now()
    dados = {"registros": []}
    quantidade_envios = 0
    quantidade_rodadas = 0
    temperatura = None
    
    while True:        
        ultimos_dados = (
            dados["registros"][-len(instances) :] if dados["registros"] else None
        )

        if (
            temperatura == None
            or (datetime.now() - ultima_temperatura_start).seconds
            >= OPEN_WEATHER_INTERVAL
        ):
            for sensor in instances:
                if sensor.tipo == "temperatura":
                    if temperatura == None:
                        temperatura = sensor.consultar_open_weather(None)
                    else:
                        temperatura = sensor.consultar_open_weather(temperatura)
                    sensor.temperatura_memoria = temperatura
                    break

            ultima_temperatura_start = datetime.now()

        novos_dados = simular(instances, ultimos_dados)
        dados["registros"].extend(novos_dados)
        quantidade_rodadas += 1

        clear()
        print(f"{len(dados['registros'])} dados simulados\n{quantidade_envios} envios realizados\n{quantidade_rodadas} rodadas\n")

        if (datetime.now() - start).seconds >= SENDING_INTERVAL:
            try:
                module.enviar_json(dados)
            except Exception as ex:
                logger.log("error", f"Ocorreu um erro ao enviar os dados para o API Gateway: {ex}")

            start = datetime.now()
            quantidade_envios += 1
            dados = {"registros": []}

        sleep(SIMULATION_INTERVAL)