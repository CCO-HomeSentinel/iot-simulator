import random
from .ModeloSensor import ModeloSensor
from datetime import datetime
from dotenv import load_dotenv
import os
from service.http_client import receber_clima

load_dotenv()
OPEN_WEATHER_ACTIVE = os.getenv('OPEN_WEATHER_ACTIVE') == 'True'
MAX_BATERIA = 100
MIN_BATERIA = 0
TAXA_CARGA = 0.01

class SensorTemperatura(ModeloSensor):
    def __init__(self, id, nome, nome_bruto, fabricante, funcionalidade, tipo, unidade_medida, min_val, max_val, regular_min_val, regular_max_val, is_anomalia, total_bateria, is_carregando):
        super().__init__(id, nome, nome_bruto, fabricante, funcionalidade, tipo, unidade_medida, min_val, max_val, regular_min_val, regular_max_val, is_anomalia, total_bateria, is_carregando)
        self.temperatura_memoria = None

    def simular_dado(self, ultima_ocorrencia=None):
        if OPEN_WEATHER_ACTIVE:
            return self.temperatura_memoria
        if ultima_ocorrencia is not None:
            variacao = random.uniform(-0.1, 0.1)
            return self.atualizar_temperatura(ultima_ocorrencia + variacao)
        else:
            return self.simular_temperatura_inicial()

    def consultar_open_weather(self):
        clima = receber_clima(0)
        return round(clima - 273.15, 2)

    def simular_temperatura_inicial(self):
        hora_atual = int(datetime.now().strftime('%H'))
        if 22 <= hora_atual <= 7:
            return round(random.uniform(10, 15), 2)
        elif 7 <= hora_atual < 12:
            return round(random.uniform(15, 25), 2)
        elif 12 <= hora_atual < 17:
            return round(random.uniform(25, 35), 2)
        else:
            return round(random.uniform(15, 25), 2)

    def atualizar_temperatura(self, temperatura):
        hora_atual = int(datetime.now().strftime('%H'))
        if 22 <= hora_atual <= 7:
            return round(max(10, min(15, temperatura)), 2)
        elif 7 <= hora_atual < 12:
            return round(max(15, min(25, temperatura)), 2)
        elif 12 <= hora_atual < 17:
            return round(max(25, min(35, temperatura)), 2)
        else:
            return round(max(15, min(25, temperatura)), 2)
        
    def simular_bateria(self, ultima_ocorrencia):
        if ultima_ocorrencia is None:
            self.is_carregando = False
            return MAX_BATERIA, self.is_carregando
        
        if ultima_ocorrencia < 15:
            self.is_carregando = True
        elif ultima_ocorrencia >= MAX_BATERIA:
            self.is_carregando = False

        if self.is_carregando:
            nova_ocorrencia = min(ultima_ocorrencia + TAXA_CARGA, MAX_BATERIA)
        else:
            nova_ocorrencia = max(ultima_ocorrencia - TAXA_CARGA, MIN_BATERIA)

        return nova_ocorrencia, self.is_carregando
            