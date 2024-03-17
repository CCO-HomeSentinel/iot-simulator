import json
import random
from datetime import datetime
import os

dir_path = os.path.dirname(os.path.realpath(__file__))

with open('data/config.json') as config_file:
    config = json.load(config_file)

def gerar_dados_sensor(nome_sensor):
    sensor_config = config[nome_sensor]
    tipo_sensor = sensor_config['tipo']
    is_anomalia = sensor_config['is_anomalia']

    if tipo_sensor == 'float':
        min_val = sensor_config['min']
        max_val = sensor_config['max']

        if is_anomalia:
            regular_min = sensor_config['regular_min']
            regular_max = sensor_config['regular_max']
            if random.random() < 0.01:  # 1% de chance de ser uma anomalia
                return random.uniform(min_val, regular_min)
            else:
                return random.uniform(regular_max, max_val)
        else:
            return random.uniform(min_val, max_val)

    elif tipo_sensor == 'boolean':
        if is_anomalia:
            if random.random() < 0.01:  # 1% de chance de ser uma anomalia
                return not sensor_config['regular']
            else:
                return sensor_config['regular']
        else:
            return random.choice([True, False])

def criar_dados_simulados():
    ocorrencia = {
        'timestamp': datetime.now().isoformat(),
        'sensors': {}
    }

    for nome_sensor in config:
        sensor_data = gerar_dados_sensor(nome_sensor)
        ocorrencia['sensors'][nome_sensor] = sensor_data

    return ocorrencia

def simulate(conn):
    try:
        data = criar_dados_simulados()
        conn.insert_data([data])
        return 1
    except Exception as e:
        print(f'Erro ao inserir dados: {e}')
        return 0