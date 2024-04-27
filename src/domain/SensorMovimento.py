import random
from datetime import datetime
from .ModeloSensor import ModeloSensor

class SensorMovimento(ModeloSensor):
    def __init__(self, id, nome, nome_bruto, fabricante, funcionalidade, tipo, unidade_medida, min_val, max_val, regular_min_val, regular_max_val, is_anomalia):
        super().__init__(id, nome, nome_bruto, fabricante, funcionalidade, tipo, unidade_medida, min_val, max_val, regular_min_val, regular_max_val, is_anomalia)

    def calculate_probability(self, hour):
        switcher = {
            0: 0.01,   #  0h - Probabilidade muito baixa
            1: 0.01,   #  1h - Probabilidade muito baixa
            2: 0.01,   #  2h - Probabilidade muito baixa
            3: 0.01,   #  3h - Probabilidade muito baixa
            4: 0.01,   #  4h - Probabilidade muito baixa
            5: 0.02,   #  5h - Probabilidade baixa
            6: 0.02,   #  6h - Probabilidade baixa
            7: 0.03,   #  7h - Probabilidade baixa
            8: 0.03,   #  8h - Probabilidade baixa
            9: 0.04,   #  9h - Probabilidade um pouco baixa
            10: 0.05,  # 10h - Probabilidade um pouco baixa
            11: 0.06,  # 11h - Probabilidade um pouco baixa
            12: 0.07,  # 12h - Probabilidade baixa
            13: 0.07,  # 13h - Probabilidade baixa
            14: 0.07,  # 14h - Probabilidade baixa
            15: 0.07,  # 15h - Probabilidade baixa
            16: 0.07,  # 16h - Probabilidade baixa
            17: 0.07,  # 17h - Probabilidade baixa
            18: 0.06,  # 18h - Probabilidade um pouco baixa
            19: 0.05,  # 19h - Probabilidade um pouco baixa
            20: 0.04,  # 20h - Probabilidade um pouco baixa
            21: 0.03,  # 21h - Probabilidade um pouco baixa
            22: 0.02,  # 22h - Probabilidade baixa
            23: 0.01   # 23h - Probabilidade muito baixa
        }

        return switcher.get(hour, 0.01)

    def simular_dado(self, ultima_ocorrencia=None):
        hour = datetime.now().hour
        probability = self.calculate_probability(hour)

        if random.random() < probability:
            return True
        else:
            return False