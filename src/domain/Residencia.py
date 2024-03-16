from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

class Residencia(Base):
    __tablename__ = 'residencia'
    id = Column(Integer, primary_key=True)
    nome = Column(String)
    habilitado = Column(Boolean)
    cliente_id = Column(Integer, ForeignKey('cliente.id'))
    cliente = relationship("Cliente", back_populates="residencias")