import os
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from domain.Cliente import Cliente
from domain.base import Base
from domain.ComodoMonitorado import ComodoMonitorado
from domain.ComodoMonitoradoSensor import ComodoMonitoradoSensor
from domain.Endereco import Endereco
from domain.Residencia import Residencia
from domain.Sensor import Sensor
from domain.Telefone import Telefone

load_dotenv()

class PostgresConnection:
    def __init__(self):
        self.engine = create_engine(
            f"postgresql://{os.getenv('POSTGRES_USERNAME')}:{os.getenv('POSTGRES_PASSWORD')}@"
            f"{os.getenv('POSTGRES_HOST')}:{os.getenv('POSTGRES_PORT')}/{os.getenv('POSTGRES_DATABASE')}"
        )
        Session = sessionmaker(bind=self.engine)
        self.session = Session()
        self.Base = Base

        self.Base.metadata.create_all(self.engine)

    def get_session(self):
        return self.session

    def close_connection(self):
        self.session.close()

    def return_dict(self, obj):
        return {col.name: getattr(obj, col.name) for col in obj.__table__.columns}

    def get_clientes(self):
        dados = self.session.query(Cliente).all()
        return [self.return_dict(dado) for dado in dados]
    
    def get_sensores(self):
        dados = self.session.query(Sensor).all()
        return [self.return_dict(dado) for dado in dados]
    
    def get_sensores_comodos_monitorados(self):
        dados = self.session.query(ComodoMonitoradoSensor).all()
        return [self.return_dict(dado) for dado in dados]
    
    def get_sensores_para_simular(self):
        sensores_a_monitorar = []
        sensores = self.get_sensores()
        sensores_comodos_monitorados = self.get_sensores_comodos_monitorados()

        for sensor_comodo in sensores_comodos_monitorados:
            sensor_a_adicionar = {}

            for sensor in sensores:
                if sensor['id'] == sensor_comodo['sensor_id']:
                    sensor_a_adicionar['id_comodo_monitorado_sensor'] = sensor_comodo['id']
                    sensor_a_adicionar['id_comodo'] = sensor_comodo['comodo_monitorado_id']
                    sensor_a_adicionar['id_sensor'] = sensor['id']
                    sensor_a_adicionar['nome'] = sensor['nome']
                    sensor_a_adicionar['nome_bruto'] = sensor['nome_bruto']
                    sensor_a_adicionar['fabricante'] = sensor['fabricante']
                    sensor_a_adicionar['funcionalidade'] = sensor['funcionalidade']
                    sensor_a_adicionar['tipo'] = sensor['tipo']
                    sensor_a_adicionar['unidade_medida'] = sensor['unidade_medida']
                    sensor_a_adicionar['min'] = sensor['min']
                    sensor_a_adicionar['max'] = sensor['max']
                    sensor_a_adicionar['regular_min'] = sensor['regular_min']
                    sensor_a_adicionar['regular_max'] = sensor['regular_max']
                    sensor_a_adicionar['is_anomalia'] = sensor['is_anomalia']
                    break

            sensores_a_monitorar.append(sensor_a_adicionar)

        return sensores_a_monitorar

if __name__ == "__main__":
    postgres_conn = PostgresConnection()
    
    session = postgres_conn.get_session()
    postgres_conn.close_connection()