import random
from .ModeloSensor import ModeloSensor
from datetime import datetime

class SensorFumaca(ModeloSensor):
    def __init__(self, id, nome, nome_bruto, fabricante, funcionalidade, tipo, unidade_medida, min_val, max_val, regular_min_val, regular_max_val, is_anomalia):
        super().__init__(id, nome, nome_bruto, fabricante, funcionalidade, tipo, unidade_medida, min_val, max_val, regular_min_val, regular_max_val, is_anomalia)

    def sortear_anomalia(self):
        return random.random() < 0.0001, 3

    def simular_dado(self, ultima_ocorrencia=None):
        if self.is_anomalia and self.sortear_anomalia():
            return round(self.set_range_limite(random.uniform(0, 1_000_000)), 3)

        if ultima_ocorrencia:
            return round(self.set_range_limite(ultima_ocorrencia + random.uniform(-0.1, 0.1)), 3)
        else:
            return round(self.set_range_limite(random.uniform(float(self.regular_min), float(self.regular_max))), 3)