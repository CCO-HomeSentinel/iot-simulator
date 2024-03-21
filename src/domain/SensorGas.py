import random
from .Sensor import Sensor

class SensorGas(Sensor):
    def __init__(self, nome, nome_bruto, fabricante, funcionalidade, tipo, unidade_medida, min_val, max_val, regular_min_val, regular_max_val, is_anomalia):
        super().__init__(nome, nome_bruto, fabricante, funcionalidade, tipo, unidade_medida, min_val, max_val, regular_min_val, regular_max_val, is_anomalia)

    def sortear_anomalia(self):
        return random.random() < 0.001

    def simular_dado(self, valor_anterior=None):
        if self.is_anomalia:
            if self.sortear_anomalia():
                return self.set_range_limite(random.uniform(0, 0.5))