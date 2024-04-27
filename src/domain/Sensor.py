from sqlalchemy import Column, Integer, ForeignKey
from .base import Base

class Sensor(Base):
    __tablename__ = 'sensor'
    id = Column(Integer, primary_key=True)
    modelo_sensor_id = Column(Integer, ForeignKey('modelo_sensor.id'), nullable=False)
    comodo_monitorado_id = Column(Integer, ForeignKey('comodo_monitorado.id'), nullable=False)
    comodo_monitorado_residencia_id = Column(Integer, ForeignKey('comodo_monitorado.residencia_id'), nullable=False)