from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

class ComodoMonitorado(Base):
    __tablename__ = 'comodo_monitorado'
    id = Column(Integer, primary_key=True)
    nome = Column(String)
    area = Column(Integer)
    altura = Column(Integer)
    residencia_id = Column(Integer, ForeignKey('residencia.id'))
    residencia = relationship("Residencia", back_populates="comodos_monitorados")