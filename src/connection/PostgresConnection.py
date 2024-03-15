import os
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

engine = create_engine(f"postgresql://{os.getenv('POSTGRES_USERNAME')}:{os.getenv('POSTGRES_PASSWORD')}@{os.getenv('POSTGRES_HOST')}:{os.getenv('POSTGRES_PORT')}/{os.getenv('POSTGRES_DATABASE')}")
                       
class PostgresConnection:
    def __init__(self):
        load_dotenv()
        self.connection = self.set_postgres_connection()

    def set_postgres_connection(self):
        Session = sessionmaker(bind=engine)
        session = Session()

        Base = declarative_base()

    def get_postgres_connection(self):
        return self.connection
    