import random
from datetime import datetime
from .ModeloSensor import ModeloSensor

class SensorSom(ModeloSensor):
    def __init__(self, id, nome, nome_bruto, fabricante, funcionalidade, tipo, unidade_medida, min_val, max_val,
                regular_min_val, regular_max_val, is_anomalia, total_bateria, taxa_bateria, is_carregando):
        super().__init__(id, nome, nome_bruto, fabricante, funcionalidade, tipo, unidade_medida, min_val, max_val,
                        regular_min_val, regular_max_val, is_anomalia, total_bateria, taxa_bateria, is_carregando)

    def sortear_anomalia(self):
        return random.random() < 0.0001
    
    def validate_horario(self, horas):
        if 1 <= horas < 7:
            return round(random.uniform(0.1, 1), 3)
        elif 7 <= horas < 12:
            return round(random.uniform(20, 40), 3)
        elif 12 <= horas < 24:
            return round(random.uniform(40, 120), 3)
        else:
            return round(random.uniform(40, 120), 3)

    def set_range_limite(self, valor):
        return max(0, min(120, valor))

    def simular_dado(self, ultima_ocorrencia=None):
        hora_atual = int(datetime.now().strftime('%H'))
        if ultima_ocorrencia:
            if self.sortear_anomalia():
                return round(self.set_range_limite(random.uniform(200, 400)), 3)
            else:
                return round(self.set_range_limite(ultima_ocorrencia + random.uniform(-1, 1)), 3)
        else:
            return round(self.set_range_limite(self.validate_horario(hora_atual)), 3)