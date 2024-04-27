from sqlalchemy import Column, Integer, String, Boolean
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

    __table_args__ = {'extend_existing': True}

    def __init__(self, id, nome, tipo, fabricante, funcionalidade, tipo_medida, unidade_medida, min_val, max_val, regular_min_val, regular_max_val, is_anomalia):
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

    def set_range_limite(self, valor):
        if valor < eval(self.tipo_medida)(self.min):
            return eval(self.tipo_medida)(self.min)
        
        elif valor > eval(self.tipo_medida)(self.max):
            return eval(self.tipo_medida)(self.max)
        
        else:
            return eval(self.tipo_medida)(valor)
        
    def to_string(self):
        return f'ID: {self.id},\nNome: {self.nome},\nTipo: {self.tipo},\nFabricante: {self.fabricante},\nFuncionalidade: {self.funcionalidade},\nTipo Medida: {self.tipo_medida},\nUnidade de Medida: {self.unidade_medida},\nMin: {self.min},\nMax: {self.max},\nRegular Min: {self.regular_min},\nRegular Max: {self.regular_max},\nIs Anomalia: {self.is_anomalia}'