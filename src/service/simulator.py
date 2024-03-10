import json
import random
from datetime import datetime
import os

dir_path = os.path.dirname(os.path.realpath(__file__))

with open('data/config.json') as config_file:
    config = json.load(config_file)

def generate_sensor_data(sensor_name):
    sensor_config = config[sensor_name]
    sensor_type = sensor_config['type']
    is_anomaly = sensor_config['is_anomaly']

    if sensor_type == 'float':
        min_val = sensor_config['min']
        max_val = sensor_config['max']

        if is_anomaly:
            regular_min = sensor_config['regular_min']
            regular_max = sensor_config['regular_max']
            if random.random() < 0.1:  # 10% de chance de ser uma anomalia
                return random.uniform(min_val, regular_min)
            else:
                return random.uniform(regular_max, max_val)
        else:
            return random.uniform(min_val, max_val)

    elif sensor_type == 'boolean':
        if is_anomaly:
            if random.random() < 0.1:  # 10% de chance de ser uma anomalia
                return not sensor_config['regular']
            else:
                return sensor_config['regular']
        else:
            return random.choice([True, False])

# Função para criar um registro de dados simulados
def create_simulated_data():
    data = {
        "timestamp": datetime.now().isoformat(),
        "sensors": {}
    }

    for sensor_name in config:
        sensor_data = generate_sensor_data(sensor_name)
        data["sensors"][sensor_name] = sensor_data

    return data

# Gerar dados simulados e inserir no MongoDB
def simulate_and_insert_data(conn):
    data = create_simulated_data()
    conn.insert_data([data])
