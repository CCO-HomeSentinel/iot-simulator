from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

sensor_funcao = {}

def ativar_sensores(instancias):
    for instancia in instancias:
        sensor_funcao[instancia.tipo] = instancia

    return sensor_funcao

def simular(sensores, ultima_ocorrencia):
    data_atual = datetime.now().isoformat().split('.')[0]
    sensor_error = None

    try:
        ocorrencias = []

        for sensor in sensores:
            sensor_data = {}
            sensor_data['timestamp'] = data_atual
            sensor_data['sensor_id'] = sensor.id
            sensor_error = sensor.id

            if ultima_ocorrencia is None:
                sensor_data['valor'] = sensor_funcao[sensor.tipo].simular_dado()
            else:
                sensor_data['valor'] = sensor_funcao[sensor.tipo].simular_dado(buscar_ultimo_dado(ultima_ocorrencia, sensor.id))

            ocorrencias.append(sensor_data)

        return ocorrencias
    except Exception as e:
        print(f'Erro ao inserir dados do sensor.id {sensor_error}: {e}')
        exit()

def buscar_ultimo_dado(ultimos_dados, sensor_id):
    for dado in ultimos_dados:
        if dado['sensor_id'] == sensor_id:
            return dado['valor']

    return None

def refinar_sensores(sensores_clientes, sensores_disponiveis):
    sensores_clientes_disponiveis = []

    for sensor in sensores_clientes:
        if sensor[12] in sensores_disponiveis:
            sensores_clientes_disponiveis.append(sensor)

    return sensores_clientes_disponiveis