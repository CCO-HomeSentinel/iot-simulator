import os
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

current_dir = os.path.dirname(os.path.abspath(__file__))
src_dir = os.path.join(current_dir, '..', '..')
sys.path.append(src_dir)

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

if __name__ == "__main__":
    postgres_conn = PostgresConnection()
    
    session = postgres_conn.get_session()
    postgres_conn.close_connection()