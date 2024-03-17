class SensorFumaca():
    def __init__(self, config):
        self.config = config

    # def simular_ocorrencia(valor_anterior=None):
    #     if valor_anterior is None:
    #     else:
    #         return False
        
    def get_tipo(self):
        return self.config['tipo']
    
    def get_min(self):
        return self.config['min']

    def get_max(self):
        return self.config['max']
    
    def get_regular_min(self):
        return self.config['regular_min']
    
    def get_regular_max(self):
        return self.config['regular_max']
    
    def get_is_anomalia(self):
        return self.config['is_anomalia']
    