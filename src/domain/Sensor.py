from sqlalchemy import Column, Integer, String
from .base import Base

class Sensor(Base):
    __tablename__ = 'sensor'
    id = Column(Integer, primary_key=True)
    nome = Column(String)
    fabricante = Column(String)
    funcionalidade = Column(String)
    tipo = Column(String)
    unidade_medida = Column(String)
    min = Column(String)
    max = Column(String)
    regular_min = Column(String)
    regular_max = Column(String)
    is_anomalia = Column(String)

    __table_args__ = {'extend_existing': True}

def __init__(self, nome, fabricante, funcionalidade, tipo, unidade_medida, min_val, max_val, regular_min_val, regular_max_val, is_anomalia):
    self.nome = nome
    self.fabricante = fabricante
    self.funcionalidade = funcionalidade
    self.tipo = tipo
    self.unidade_medida = unidade_medida
    self.min = min_val
    self.max = max_val
    self.regular_min = regular_min_val
    self.regular_max = regular_max_val
    self.is_anomalia = is_anomalia

def set_range_limite(self, valor):
    if valor < eval(self.tipo(self.min)):
        return self.min
    elif valor > eval(self.tipo(self.max)):
        return self.max

def get_id(self):
    return self.id

def set_id(self, id):
    self.id = id

def get_nome(self):
    return self.nome

def set_nome(self, nome):
    self.nome = nome

def set_fabricante(self, fabricante):
    self.fabricante = fabricante

def get_fabricante(self):
    return self.fabricante

def set_funcionalidade(self, funcionalidade):
    self.funcionalidade = funcionalidade

def get_funcionalidade(self):
    return self.funcionalidade

def set_tipo(self, tipo):
    self.tipo = tipo

def get_tipo(self):
    return self.tipo

def set_unidade_medida(self, unidade_medida):
    self.unidade_medida = unidade_medida

def get_unidade_medida(self):
    return self.unidade_medida

def set_min(self, min_val):
    self.min = min_val

def get_min(self):
    return self.min

def set_max(self, max_val):
    self.max = max_val

def get_max(self):
    return self.max

def set_regular_min(self, regular_min_val):
    self.regular_min = regular_min_val

def get_regular_min(self):
    return self.regular_min

def set_regular_max(self, regular_max_val):
    self.regular_max = regular_max_val

def get_regular_max(self):
    return self.regular_max

def set_is_anomalia(self, is_anomalia):
    self.is_anomalia = is_anomalia

def get_is_anomalia(self):
    return self.is_anomalia