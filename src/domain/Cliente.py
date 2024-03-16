from sqlalchemy import Column, Integer, String, Boolean
from .base import Base

class Cliente(Base):
    __tablename__ = 'cliente'
    id = Column(Integer, primary_key=True)
    nome = Column(String)
    sobrenome = Column(String)
    cpf = Column(String)
    rg = Column(String)
    email = Column(String)
    senha = Column(String)
    habilitado = Column(Boolean)