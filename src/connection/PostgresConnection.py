import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from domain.base import Base
from dotenv import load_dotenv
from domain.cliente import Cliente
from domain.residencia import Residencia

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