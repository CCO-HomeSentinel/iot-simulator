import os
import sys
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from domain.Cliente import Cliente
from domain.base import Base
from domain.ComodoMonitorado import ComodoMonitorado
from domain.Endereco import Endereco
from domain.Residencia import Residencia
from domain.Sensor import Sensor
from domain.ModeloSensor import ModeloSensor
from domain.Telefone import Telefone
from domain.SensorFumaca import SensorFumaca
from domain.SensorGas import SensorGas
from domain.SensorInundacao import SensorInundacao
from domain.SensorLuminosidade import SensorLuminosidade
from domain.SensorMovimento import SensorMovimento
from domain.SensorSom import SensorSom
from domain.SensorTemperatura import SensorTemperatura

from config.logger import logger


load_dotenv()

sensor_dict = {
    "fumaca": SensorFumaca,
    "gas": SensorGas,
    "inundacao": SensorInundacao,
    "luminosidade": SensorLuminosidade,
    "movimento": SensorMovimento,
    "som": SensorSom,
    "temperatura": SensorTemperatura,
}


class MySQLConnection:
    def __init__(self):
        try:
            self.engine = create_engine(
                f"mysql://{os.getenv('MYSQL_USERNAME')}:{os.getenv('MYSQL_PASSWORD')}@"
                f"{os.getenv('MYSQL_HOST')}:{int(os.getenv('MYSQL_PORT'))}/{os.getenv('MYSQL_DATABASE')}"
            )
            Session = sessionmaker(bind=self.engine)
            self.session = Session()
            self.Base = Base

            self.Base.metadata.create_all(self.engine)
        except Exception as e:
            logger.log("error", f"Erro ao conectar com o banco de dados. {e}")


    def get_session(self):
        return self.session


    def close_connection(self):
        self.session.close()


    def return_dict(self, obj):
        return {col.name: getattr(obj, col.name) for col in obj.__table__.columns}


    def get_clientes(self):
        dados = self.session.query(Cliente).all()
        return [self.return_dict(dado) for dado in dados]


    def get_dados_cliente(self, id):
        dados = self.session.query(Cliente).filter(Cliente.id == id).first()
        return self.return_dict(dados)


    def execute_select_query(self, query):
        with self.engine.connect() as connection:
            result = connection.execute(text(query))
            results = result.fetchall()
            return results


    def get_sensores(self):
        dados = self.session.query(ModeloSensor).all()
        return [self.return_dict(dado) for dado in dados]


    def get_sensores_comodos_monitorados(self):
        dados = (
            self.session.query(Sensor).filter(Sensor.comodo_monitorado_id != None).all()
        )
        return [self.return_dict(dado) for dado in dados]
    

    def load_sensores(self, sensores_disponivies):
        objetos_instanciados = []

        for sensor in sensores_disponivies:
            if sensor[12] in sensor_dict:
                objetos_instanciados.append(
                    sensor_dict[sensor[12]](
                        sensor[6],
                        sensor[11],
                        sensor[12],
                        sensor[13],
                        sensor[14],
                        sensor[15],
                        sensor[16],
                        sensor[17],
                        sensor[18],
                        sensor[19],
                        sensor[20],
                        sensor[21],
                        sensor[22],
                        sensor[23],
                        False,
                    )
                )

        return objetos_instanciados


    def get_sensores_para_simular(self):
        query = """
            SELECT * 
            FROM comodo_monitorado cm
	            JOIN sensor ss ON ss.comodo_monitorado_id = cm.id
	            JOIN modelo_sensor ms ON ss.modelo_sensor_id = ms.id;
        """
        return self.execute_select_query(query)
    
    def get_sensor_mapping(self, sensores_id):
        placeholders = ', '.join(['%s'] * len(sensores_id))

        query = f"""
            SELECT ms.id
            FROM home_sentinel.sensor ss 
	            JOIN home_sentinel.modelo_sensor ms 
		            ON ss.modelo_sensor_id = ms.id
                    WHERE ss.id IN ({placeholders});
        """
        return self.execute_select_query(query)
