from sqlalchemy import Column, Integer, String, Boolean, Double
from .base import Base

class ModeloSensor(Base):
    __tablename__ = 'modelo_sensor'
    id = Column(Integer, primary_key=True)
    nome = Column(String(64))
    tipo = Column(String(64))
    fabricante = Column(String(45))
    funcionalidade = Column(String(45))
    tipo_medida = Column(String(16))
    unidade_medida = Column(String(16))
    min = Column(String(16))
    max = Column(String(16))
    regular_min = Column(String(16))
    regular_max = Column(String(16))
    is_anomalia = Column(Boolean)
    total_bateria = Column(Double)

    __table_args__ = {'extend_existing': True}

    def __init__(self, id, nome, tipo, fabricante, funcionalidade, tipo_medida, unidade_medida, min_val, max_val, regular_min_val, 
                    regular_max_val, is_anomalia, total_bateria, taxa_bateria, is_carregando):
        self.id = id
        self.nome = nome
        self.tipo = tipo
        self.fabricante = fabricante
        self.funcionalidade = funcionalidade
        self.tipo_medida = tipo_medida
        self.unidade_medida = unidade_medida
        self.min = min_val
        self.max = max_val
        self.regular_min = regular_min_val
        self.regular_max = regular_max_val
        self.is_anomalia = is_anomalia
        self.total_bateria = total_bateria
        self.taxa_bateria = taxa_bateria
        self.is_carregando = is_carregando

    def set_range_limite(self, valor):
        if valor < eval(self.tipo_medida)(self.min):
            return eval(self.tipo_medida)(self.min)
        
        elif valor > eval(self.tipo_medida)(self.max):
            return eval(self.tipo_medida)(self.max)
        
        else:
            return eval(self.tipo_medida)(valor)
        
    def get_battery_alert(self):
        return round((self.total_bateria / 100) * 15, 3)
    
    def simular_bateria(self, ultima_ocorrencia=None):
        if ultima_ocorrencia is None:
            self.is_carregando = False
            return self.total_bateria, self.is_carregando
        
        if ultima_ocorrencia < 15:
            self.is_carregando = True
        elif ultima_ocorrencia >= self.total_bateria:
            self.is_carregando = False

        if self.is_carregando:
            nova_ocorrencia = min(ultima_ocorrencia + (self.taxa_bateria * 0.0001), self.total_bateria)
        else:
            nova_ocorrencia = max(ultima_ocorrencia - (self.taxa_bateria * 0.0001), self.get_battery_alert())

        return round(nova_ocorrencia, 3), self.is_carregando
        
    def to_string(self):
        return f'ID: {self.id},\nNome: {self.nome},\nTipo: {self.tipo},\nFabricante: {self.fabricante},\nFuncionalidade: {self.funcionalidade},\nTipo Medida: {self.tipo_medida},\nUnidade de Medida: {self.unidade_medida},\nMin: {self.min},\nMax: {self.max},\nRegular Min: {self.regular_min},\nRegular Max: {self.regular_max},\nIs Anomalia: {self.is_anomalia}, Total Bateria: {self.total_bateria}'