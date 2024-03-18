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

if __name__ == "__main__":
    postgres_conn = PostgresConnection()
    
    session = postgres_conn.get_session()
    postgres_conn.close_connection()