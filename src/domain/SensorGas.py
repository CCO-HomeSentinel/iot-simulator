import random
from datetime import datetime
from .ModeloSensor import ModeloSensor


class SensorGas(ModeloSensor):
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
        return random.random() < 0.00005

    def set_range_limite(self, valor):
        return max(0, min(500, valor))

    def simular_dado(self, ultima_ocorrencia=None):
        hora_atual = int(datetime.now().strftime("%H"))

        if self.is_anomalia and self.sortear_anomalia():
            return self.set_range_limite(random.uniform(0, 1_000_000))

        if ultima_ocorrencia:
            if (11 <= hora_atual <= 13) or (
                17 <= hora_atual <= 20 and datetime.now().minute >= 30
            ):
                return self.set_range_limite(round(random.uniform(200, 450), 3))
            elif 22 <= hora_atual or hora_atual <= 6:
                return self.set_range_limite(round(random.uniform(0, 20), 3))
            else:
                return self.set_range_limite(
                    round(ultima_ocorrencia + random.uniform(-0.05, 0.05), 3)
                )
        else:
            if (11 <= hora_atual <= 13) or (
                17 <= hora_atual <= 20 and datetime.now().minute >= 30
            ):
                return self.set_range_limite(round(random.uniform(200, 450), 3))
            elif 22 <= hora_atual or hora_atual <= 6:
                return self.set_range_limite(round(random.uniform(0, 20), 3))
            else:
                return self.set_range_limite(
                    round(
                        random.uniform(
                            float(self.regular_min), float(self.regular_max)
                        ),
                        3,
                    )
                )
