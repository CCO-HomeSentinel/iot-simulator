import random
from .ModeloSensor import ModeloSensor


class SensorInundacao(ModeloSensor):
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
        return random.random() < 0.0001

    def simular_dado(self, ultima_ocorrencia=None):
        if ultima_ocorrencia is None:
            return self.sortear_anomalia()
        else:
            if random.random() < 0.0000001:
                return not ultima_ocorrencia
            else:
                return ultima_ocorrencia
