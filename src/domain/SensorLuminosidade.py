import random
from datetime import datetime
from .ModeloSensor import ModeloSensor

class SensorLuminosidade(ModeloSensor):
    def __init__(self, id, nome, nome_bruto, fabricante, funcionalidade, tipo, unidade_medida, min_val, max_val, regular_min_val, regular_max_val, is_anomalia):
        super().__init__(id, nome, nome_bruto, fabricante, funcionalidade, tipo, unidade_medida, min_val, max_val, regular_min_val, regular_max_val, is_anomalia)

    def sortear_anomalia(self):
        return random.random() < 0.02
    
    def horario_validator(self, minutos):
        if 240 <= minutos < 330:  # 4:00 - 5:29
            luminosidade_base = random.randint(20, 40)
        elif 330 <= minutos < 450:  # 5:30 - 7:29
            luminosidade_base = random.randint(40, 60)
        elif 450 <= minutos < 660:  # 7:30 - 10:59
            luminosidade_base = random.randint(60, 75)
        elif 660 <= minutos < 900:  # 11:00 - 14:59
            luminosidade_base = random.randint(75, 90)
        elif 900 <= minutos < 1050:  # 15:00 - 17:29
            luminosidade_base = random.randint(60, 75)
        elif 1050 <= minutos < 1170:  # 17:30 - 19:29
            luminosidade_base = random.randint(40, 60)
        elif 1170 <= minutos < 1260:  # 19:30 - 21:59
            luminosidade_base = random.randint(20, 40)
        else:  # 22:00 - 3:59
            luminosidade_base = random.randint(10, 20)

        if 125 <= minutos < 155 and random.random() < 0.1:  # 02:05 - 2:45
            luminosidade_base = min(luminosidade_base + 60, 70)
        elif 660 <= minutos < 900 and random.random() < 0.1:  # 11:00 - 14:59
            luminosidade_base = max(luminosidade_base - 20, 0)

        return self.set_range_limite(luminosidade_base)

    def simular_dado(self, valor_anterior=None):
        minutos = int(datetime.now().strftime('%H')) * 60 + int(datetime.now().strftime('%M'))

        if valor_anterior is None:
            return self.horario_validator(minutos)
        else:
            if self.is_anomalia and self.sortear_anomalia():
                return self.horario_validator(minutos)
            else:
                return round(self.set_range_limite(valor_anterior + random.uniform(-0.1, 0.1)), 3)