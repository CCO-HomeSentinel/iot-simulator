from datetime import datetime
from dotenv import load_dotenv
from .lexer import analisar, logar_tokens
from time import sleep
import os
from config.logger_config import Logger

load_dotenv()
ENABLE_LOGS = os.getenv('ENABLE_LOGS').lower() == 'true'

if ENABLE_LOGS:
    logger = Logger().get_logger()
    
sensor_funcao = {}

def ativar_sensores(instancias):
    for instancia in instancias:
        sensor_funcao[instancia.tipo] = instancia

    return sensor_funcao

def processar_tokens(tokens):
    valor = None
    unidade = None
    for token in tokens:
        if token[0] == 'NUMERO':
            valor = token[1]
        elif token[0] == 'UNIDADE':
            unidade = token[1]
        else:
            logger.error(f'Token inesperado: {token}')
            exit()
            
    return valor, unidade

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
                dados_bateria = sensor_funcao[sensor.tipo].simular_bateria()
                sensor_data['bateria'] = dados_bateria[0]
                sensor_data['is_carregando'] = dados_bateria[1]
            else:
                dados_ocorrencia = buscar_ultimo_dado(ultima_ocorrencia, sensor.id)
                sensor_data['valor'] = sensor_funcao[sensor.tipo].simular_dado(dados_ocorrencia[0])
                novos_dados = sensor_funcao[sensor.tipo].simular_bateria(dados_ocorrencia[1])
                sensor_data['bateria'] = novos_dados[0]
                sensor_data['is_carregando'] = novos_dados[1]
                tokens = analisar(str(novos_dados[0]))
                valor, unidade = processar_tokens(tokens)
                logar_tokens([valor, unidade])
                sleep(0.01)

            ocorrencias.append(sensor_data)

        return ocorrencias
    except Exception as e:
        print(f'Erro ao inserir dados do sensor.id {sensor_error}: {e}')
        exit()

def buscar_ultimo_dado(ultimos_dados, sensor_id):
    for dado in ultimos_dados:
        if dado['sensor_id'] == sensor_id:
            return dado['valor'], dado['bateria']

def refinar_sensores(sensores_clientes, sensores_disponiveis):
    sensores_clientes_disponiveis = []

    for sensor in sensores_clientes:
        if sensor[12] in sensores_disponiveis:
            sensores_clientes_disponiveis.append(sensor)

    return sensores_clientes_disponiveis