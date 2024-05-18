from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base


class ComodoMonitorado(Base):
    __tablename__ = "comodo_monitorado"
    id = Column(Integer, primary_key=True)
    nome = Column(String(64), nullable=False)
    area = Column(Integer, nullable=False)
    altura = Column(Integer)
    andar = Column(String(16))
    residencia_id = Column(
        Integer,
        ForeignKey("residencia.id", ondelete="NO ACTION", onupdate="NO ACTION"),
        nullable=False,
    )
    residencia = relationship("Residencia", back_populates="comodos_monitorados")

    __table_args__ = {"extend_existing": True}
