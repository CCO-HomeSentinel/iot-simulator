import random
from datetime import datetime
from .ModeloSensor import ModeloSensor


class SensorLuminosidade(ModeloSensor):
    def __init__(
        self,
        id,
        nome,
        nome_bruto,
        fabricante,
        funcionalidade,
        tipo,
        unidade_medida,
        min_val,
        max_val,
        regular_min_val,
        regular_max_val,
        is_anomalia,
        total_bateria,
        taxa_bateria,
        is_carregando,
    ):
        super().__init__(
            id,
            nome,
            nome_bruto,
            fabricante,
            funcionalidade,
            tipo,
            unidade_medida,
            min_val,
            max_val,
            regular_min_val,
            regular_max_val,
            is_anomalia,
            total_bateria,
            taxa_bateria,
            is_carregando,
        )

    def sortear_anomalia(self):
        return random.random() < 0.02

    def horario_validator(self, minutos):
        if 240 <= minutos < 330:
            luminosidade_base = random.randint(20, 40)
        elif 330 <= minutos < 450:
            luminosidade_base = random.randint(40, 60)
        elif 450 <= minutos < 660:
            luminosidade_base = random.randint(60, 75)
        elif 660 <= minutos < 900:
            luminosidade_base = random.randint(75, 90)
        elif 900 <= minutos < 1050:
            luminosidade_base = random.randint(60, 75)
        elif 1050 <= minutos < 1170:
            luminosidade_base = random.randint(40, 60)
        elif 1170 <= minutos < 1260:
            luminosidade_base = random.randint(20, 40)
        else:  # 22:00 - 3:59
            luminosidade_base = random.randint(5, 15)

        if 125 <= minutos < 155 and random.random() < 0.1:
            luminosidade_base = min(luminosidade_base + 5, 100)
        elif 660 <= minutos < 900 and random.random() < 0.1:
            luminosidade_base = max(luminosidade_base - 5, 0)

        return luminosidade_base

    def set_range_limite(self, valor):
        return max(0, min(100, valor))

    def simular_dado(self, ultima_ocorrencia=None):
        minutos = int(datetime.now().strftime("%H")) * 60 + int(
            datetime.now().strftime("%M")
        )

        if ultima_ocorrencia is None:
            return round(self.horario_validator(minutos), 3)
        else:
            if self.sortear_anomalia():
                return round(self.horario_validator(minutos), 3)
            else:
                return round(
                    self.set_range_limite(
                        ultima_ocorrencia + random.uniform(-0.5, 0.5)
                    ),
                    3,
                )
