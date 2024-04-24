from sqlalchemy import Column, Integer, String, Boolean, UniqueConstraint
from sqlalchemy.orm import relationship
from .base import Base
from .Residencia import Residencia

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
    residencias = relationship("Residencia", back_populates="cliente")

    __table_args__ = {'extend_existing': True}

    __table_args__ = (
        UniqueConstraint('cpf', name='cpf_UNIQUE'),
        UniqueConstraint('email', name='email_UNIQUE'),
        {'extend_existing': True}
    )