import sys
from datetime import datetime
import os
from dotenv import load_dotenv

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from domain.SensorFumaca import SensorFumaca

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.functions import clear

load_dotenv()

sensor_funcao = {}

def ativar_sensores(instancias):
    for instancia in instancias:
        sensor_funcao[instancia.tipo] = instancia

    return sensor_funcao

    return ocorrencia

def simular(sensores, ultima_ocorrencia):
    print(sensores)
    print(ultima_ocorrencia)
    data_atual = datetime.now().isoformat().split('.')[0]

    try:
        ocorrencias = []

        for sensor in sensores:
            sensor_data = {}
            sensor_data['timestamp'] = data_atual
            sensor_data['sensor_id'] = sensor.id

            if ultima_ocorrencia is None:
                sensor_data['valor'] = sensor_funcao[sensor.tipo].simular_dado()
            else: 
                sensor_data['valor'] = sensor_funcao[sensor.tipo].simular_dado(None) #alterar depois

            print(sensor_data)
            ocorrencias.append(sensor_data)

        return ocorrencias
    except Exception as e:
        print(f'Erro ao inserir dados: {e}')
        exit()

def refinar_sensores(sensores_clientes, sensores_disponiveis):
    sensores_clientes_disponiveis = []

    for sensor in sensores_clientes:
        if sensor[12] in sensores_disponiveis:
            sensores_clientes_disponiveis.append(sensor)

    return sensores_clientes_disponiveis