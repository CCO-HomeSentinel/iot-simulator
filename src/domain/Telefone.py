from sqlalchemy import Column, Integer, String, ForeignKey
from .base import Base

class Telefone(Base):
    __tablename__ = 'telefone'
    id = Column(Integer, primary_key=True)
    codigo_discagem = Column(Integer)
    codigo_area = Column(Integer)
    numero = Column(String)
    habilitado = Column(String)
    cliente_id = Column(Integer, ForeignKey('cliente.id'))