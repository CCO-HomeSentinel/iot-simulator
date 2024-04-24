from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base
from .Endereco import Endereco

class Residencia(Base):
    __tablename__ = 'residencia'
    id = Column(Integer, primary_key=True)
    nome = Column(String(64), nullable=False)
    habilitado = Column(Boolean)
    cliente_id = Column(Integer, ForeignKey('cliente.id', ondelete="NO ACTION", onupdate="NO ACTION"), nullable=False)
    cliente = relationship("Cliente", back_populates="residencias")
    comodos_monitorados = relationship("ComodoMonitorado", back_populates="residencia")
    enderecos = relationship("Endereco", back_populates="residencia")