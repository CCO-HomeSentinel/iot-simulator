import random
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
        sensor_funcao[instancia.nome_bruto] = instancia

    return sensor_funcao
    
def criar_dados_simulados(sensores, ultima_ocorrencia=None):
    ocorrencia = {
        'timestamp': datetime.now().isoformat(),
        'sensores': {}
    }

    for sensor in sensores:   
        if ultima_ocorrencia is None:
            sensor_data = sensor_funcao[sensor['nome_bruto']].simular_dado()
        else: 
            # print(ultima_ocorrencia)
            sensor_data = sensor_funcao[sensor['nome_bruto']].simular_dado(ultima_ocorrencia[sensor['nome_bruto']]['valor'])

        ocorrencia['sensores'][sensor['nome_bruto']] = {}
        ocorrencia['sensores'][sensor['nome_bruto']]['comodo_monitorado_sensor_id'] = sensor['id_comodo_monitorado_sensor']
        ocorrencia['sensores'][sensor['nome_bruto']]['valor'] = sensor_data

    return ocorrencia

def simular(conn, sensores, ultima_ocorrencia=None):
    try:
        data = criar_dados_simulados(sensores, ultima_ocorrencia)
        dados_inseridos = conn.insert_data(data)
        # clear()

        return dados_inseridos
    except Exception as e:
        print(f'Erro ao inserir dados: {e}')
        exit()

def refinar_sensores(sensores, sensores_disponiveis):
    sensores_finais = []

    for nome_sensor in sensores_disponiveis:
        for sensor in sensores:
            if (nome_sensor == sensor['nome_bruto']):
                sensores_finais.append(sensor)
                
    return sensores_finais