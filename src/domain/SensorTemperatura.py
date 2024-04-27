import random
from .ModeloSensor import ModeloSensor
from datetime import datetime

class SensorTemperatura(ModeloSensor):
    def __init__(self, id, nome, nome_bruto, fabricante, funcionalidade, tipo, unidade_medida, min_val, max_val, regular_min_val, regular_max_val, is_anomalia):
        super().__init__(id, nome, nome_bruto, fabricante, funcionalidade, tipo, unidade_medida, min_val, max_val, regular_min_val, regular_max_val, is_anomalia)

    def sortear_anomalia(self):
        return random.random() < 0.001
    
    def validate_horario(self, horas):
        if 0 <= horas < 6:
            return random.randint(8, 14)
        elif 6 <= horas < 9:
            return random.randint(14, 20)
        elif 10 <= horas < 18:
            return random.randint(20, 33)
        elif 18 <= horas < 21:
            return random.randint(16, 24)
        elif 21 <= horas < 24:
            return random.randint(8, 14)

    def simular_dado(self, ultima_ocorrencia=None):
        if self.is_anomalia and self.sortear_anomalia():
            return self.set_range_limite(random.uniform(60, 400))

        if ultima_ocorrencia:
            if random.random() < 0.0001:
                return round(self.validate_horario(int(datetime.now().strftime('%H'))), 3)
            else:
                return round(self.set_range_limite(ultima_ocorrencia + random.uniform(-0.001, 0.001)), 3)
        else:
            return round(self.set_range_limite(self.validate_horario(int(datetime.now().strftime('%H')))), 3)