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
    is_anomalia = Column(bool)