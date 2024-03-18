from sqlalchemy import Column, Integer, ForeignKey
from .base import Base

class ComodoMonitoradoSensor(Base):
    __tablename__ = 'comodo_monitorado_sensor'
    id = Column(Integer, primary_key=True)
    comodo_monitorado_id = Column(Integer, ForeignKey('comodo_monitorado.id'))
    sensor_id = Column(Integer, ForeignKey('sensor.id'))

    __table_args__ = {'extend_existing': True} 