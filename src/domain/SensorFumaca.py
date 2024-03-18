import Sensor
import random

class SensorFumaca(Sensor):
    def __init__(self):
        nome = "Sensor de Fumaça",
        nome_bruto = "fumaca"
        fabricante = "TechFire"
        funcionalidade = "Detecta a presença de fumaça no ar"
        tipo = "float"
        unidade_medida = "ppm"
        min_val = "0"
        max_val = "100"
        regular_min_val = "0"
        regular_max_val = "0.5"
        is_anomalia = True

        super().__init__(nome, nome_bruto, fabricante, funcionalidade, tipo, unidade_medida, min_val, max_val, regular_min_val, regular_max_val, is_anomalia)

    def sortear_anomalia(self):
        return random.random() < 0.001

    def simular_dado(self, valor_anterior=None):
        if self.is_anomalia:
            if self.sortear_anomalia():
                return self.set_range_limite(random.uniform(0, 0.5))

        if valor_anterior:
            return self.set_range_limite(valor_anterior + random.choice([-0.1, 0.1]))
        else:
            return self.set_range_limite(random.uniform(eval(self.tipo(self.min), eval(self.tipo(self.max)))))