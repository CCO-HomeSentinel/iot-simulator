import random
from .ModeloSensor import ModeloSensor

class SensorFumaca(ModeloSensor):
    def __init__(self, id, nome, nome_bruto, fabricante, funcionalidade, tipo, unidade_medida, min_val, max_val, regular_min_val, regular_max_val, is_anomalia):
        super().__init__(id, nome, nome_bruto, fabricante, funcionalidade, tipo, unidade_medida, min_val, max_val, regular_min_val, regular_max_val, is_anomalia)

    def sortear_anomalia(self):
        return random.random() < 0.001

    def simular_dado(self, ultima_ocorrencia=None):
        if self.is_anomalia:
            if self.sortear_anomalia():
                return self.set_range_limite(random.uniform(0, 0.5))

        if ultima_ocorrencia:
            return self.set_range_limite(ultima_ocorrencia + random.choice([-0.1, 0.1]))
        else:
            return self.set_range_limite(random.uniform(float(self.min), float(self.max)))