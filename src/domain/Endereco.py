from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

class Endereco(Base):
    __tablename__ = 'endereco'
    id = Column(Integer, primary_key=True)
    logradouro = Column(String)
    numero = Column(String)
    bairro = Column(String)
    cidade = Column(String)
    estado = Column(String)
    cep = Column(String)
    referencia = Column(String)
    habilitado = Column(Boolean)
    residencia_id = Column(Integer, ForeignKey('residencia.id'))
    residencia = relationship("Residencia", back_populates="enderecos")

    __table_args__ = {'extend_existing': True} 