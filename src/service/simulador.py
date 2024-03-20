import random
import sys
from datetime import datetime
import os
from dotenv import load_dotenv

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from domain.SensorFumaca import SensorFumaca


load_dotenv()

sensor_funcao = {}

def ativar_sensores(instancias):
    for instancia in instancias:
        sensor_funcao[instancia.nome_bruto] = instancia

    return sensor_funcao
    
def criar_dados_simulados(sensores, ultima_ocorrencia=None):
    ocorrencia = {
        'timestamp': datetime.now().isoformat(),
        'sensors': {}
    }

    for sensor in sensores:
        sensor_data = sensor_funcao[sensor['nome_bruto']].simular_dado(ultima_ocorrencia)
        ocorrencia['sensors'][sensor['nome_bruto']] = sensor_data

    return ocorrencia

def simular(conn, sensores, ultima_ocorrencia=None):
    try:
        data = criar_dados_simulados(sensores, ultima_ocorrencia)

        dados_inseridos = conn.insert_data(data)
        print(dados_inseridos)
        exit()
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