import random
from .Sensor import Sensor

class SensorGas(Sensor):
    def __init__(self, nome, nome_bruto, fabricante, funcionalidade, tipo, unidade_medida, min_val, max_val, regular_min_val, regular_max_val, is_anomalia):
        super().__init__(nome, nome_bruto, fabricante, funcionalidade, tipo, unidade_medida, min_val, max_val, regular_min_val, regular_max_val, is_anomalia)

    def sortear_anomalia(self):
        return random.random() < 0.001

    @staticmethod
    def simular_dado(self, valor_anterior=None):
        # a desenvolver
        return 2