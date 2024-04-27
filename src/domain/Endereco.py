from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DECIMAL
from sqlalchemy.orm import relationship
from .base import Base

class Endereco(Base):
    __tablename__ = 'endereco'
    id = Column(Integer, primary_key=True)
    latitude = Column(DECIMAL(9, 6))
    longitude = Column(DECIMAL(9, 6))
    logradouro = Column(String(256))
    numero = Column(String(16))
    bairro = Column(String(64))
    cidade = Column(String(64))
    estado = Column(String(64))
    cep = Column(String(8))
    referencia = Column(String(64))
    habilitado = Column(Boolean)
    residencia_id = Column(Integer, ForeignKey('residencia.id', ondelete="NO ACTION", onupdate="NO ACTION"), nullable=False)
    residencia = relationship("Residencia", back_populates="enderecos")

    __table_args__ = {'extend_existing': True}