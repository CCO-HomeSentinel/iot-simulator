import random
from datetime import datetime
from .ModeloSensor import ModeloSensor

class SensorMovimento(ModeloSensor):
    def __init__(self, id, nome, nome_bruto, fabricante, funcionalidade, tipo, unidade_medida, min_val, max_val, regular_min_val, regular_max_val, is_anomalia):
        super().__init__(id, nome, nome_bruto, fabricante, funcionalidade, tipo, unidade_medida, min_val, max_val, regular_min_val, regular_max_val, is_anomalia)

    def sortear_movimento(self, ultima_ocorrencia):
        hora_atual = int(datetime.now().strftime('%H'))
        if 0 <= hora_atual <= 7:
            return random.random() < 0.005
        elif ultima_ocorrencia == True:
            return random.random() < 0.75
        else:
            return random.random() < 0.2

    def simular_dado(self, ultima_ocorrencia=None):
        if ultima_ocorrencia is not None:
            return self.sortear_movimento(ultima_ocorrencia)
        else:
            return self.sortear_movimento(False)