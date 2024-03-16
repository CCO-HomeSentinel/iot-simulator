from sqlalchemy import Column, Integer, String
from .base import Base

class Sensor(Base):
    __tablename__ = 'sensor'
    id = Column(Integer, primary_key=True)
    nome = Column(String)
    fabricante = Column(String)
    funcionalidade = Column(String)