import random
import sys
from datetime import datetime
import os
from dotenv import load_dotenv

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from domain.SensorFumaca import SensorFumaca


load_dotenv()

sensor_funcao = {
    'fumaca': SensorFumaca.simular_dado
}

# def gerar_dados_sensor(nome_sensor, ultimo_dado=None):
#     sensor_config = config[nome_sensor]
#     tipo_sensor = sensor_config['tipo']
#     is_anomalia = sensor_config['is_anomalia']

#     if tipo_sensor == 'float':
#         min_val = sensor_config['min']
#         max_val = sensor_config['max']

#         if is_anomalia:
#             regular_min = sensor_config['regular_min']
#             regular_max = sensor_config['regular_max']
#             if random.random() < 0.01:  # 1% de chance de ser uma anomalia
#                 return random.uniform(min_val, regular_min)
#             else:
#                 if ultimo_dado:
#                     return ultimo_dado + random.choice([-0.1, 0.1])
                
#                 return random.uniform(regular_min, regular_max)
#         else:
#             return random.uniform(min_val, max_val)

#     elif tipo_sensor == 'boolean':
#         if is_anomalia:
#             if random.random() < 0.01:  # 1% de chance de ser uma anomalia
#                 return not sensor_config['regular']
#             else:
#                 return sensor_config['regular']
#         else:
#             return random.choice([True, False])

def criar_dados_simulados(sensores, ultima_ocorrencia=None):
    ocorrencia = {
        'timestamp': datetime.now().isoformat(),
        'sensors': {}
    }

    for sensor in sensores:
        sensor_data = sensor_funcao[sensor['nome_bruto']](ultima_ocorrencia)

        exit()



    # for nome_sensor in config:
    #     if nome_sensor in sensores:
    #         ultimo_dado = None

    #         if ultimas_ocorrencias:
    #             for ocorrencia in ultimas_ocorrencias:
    #                 if nome_sensor in ocorrencia['sensors']:
    #                     ultimo_dado = ocorrencia['sensors'][nome_sensor]
    #         sensor_data = gerar_dados_sensor(nome_sensor, ultimo_dado)
    #         ocorrencia['sensors'][nome_sensor] = sensor_data

    # return ocorrencia

def simular(conn, sensores, ultima_ocorrencia=None):
    try:
        data = criar_dados_simulados(sensores, ultima_ocorrencia)

        dados_inseridos = conn.insert_data(data)
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