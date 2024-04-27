import random
from datetime import datetime
from .ModeloSensor import ModeloSensor

class SensorSom(ModeloSensor):
    def __init__(self, id, nome, nome_bruto, fabricante, funcionalidade, tipo, unidade_medida, min_val, max_val, regular_min_val, regular_max_val, is_anomalia):
        super().__init__(id, nome, nome_bruto, fabricante, funcionalidade, tipo, unidade_medida, min_val, max_val, regular_min_val, regular_max_val, is_anomalia)

    def sortear_anomalia(self):
        return random.random() < 0.001
    
    def validate_horario(self, horas):
        if 0 <= horas < 6:
            return random.randint(2, 20)
        elif 6 <= horas < 12:
            return random.randint(20, 40)
        elif 12 <= horas < 24:
            return random.randint(40, 60)
        else:
            return random.randint(40, 60)
        

    def simular_dado(self, ultima_ocorrencia=None):
        horas = int(datetime.now().strftime('%H'))
        if self.is_anomalia and self.sortear_anomalia():
            return self.set_range_limite(random.uniform(200, 400))

        if ultima_ocorrencia:
            if random.random() < 0.001:
                return round(self.validate_horario(horas), 3)
            else:
                return round(self.set_range_limite(ultima_ocorrencia + random.uniform(-0.1, 0.1)), 3)
        else:
            return round(self.set_range_limite(self.validate_horario(horas)), 3)