from connection.MongoConnection import MongoConnection
from connection.MySQLConnection import MySQLConnection
from service.simulador import simular, refinar_sensores, ativar_sensores
from utils.functions import load_init, clear, load_sensores_disponiveis, load_not_found
import os
from time import sleep
from dotenv import load_dotenv
import utils.query as queries

load_dotenv()

def main():
    intervalo_geracao = float(os.getenv('INTERVALO_SIMULADOR'))
    intervalo_envio = float(os.getenv('INTERVALO_ENVIO'))

    ocorrencias_inseridas = 0
    ultimos_dados = dict()

    load_init(skip=os.getenv('SKIP_INTRO') in ('True', 'true', '1'))
    connMongo = MongoConnection()
    connMySQL = MySQLConnection()

    sensores_banco = connMySQL.get_sensores()
    sensores_disponiveis = load_sensores_disponiveis(sensores_banco)
    sensores_clientes = connMySQL.get_sensores_para_simular()

    sensores = refinar_sensores(sensores_clientes, sensores_disponiveis)
    instancias = connMySQL.load_sensores(sensores)
    ativar_sensores(instancias)

    while True:
        clear()

        if not sensores:
            load_not_found()
            break

        novos_dados = simular(connMongo, sensores, ultimos_dados)

        if novos_dados:
            ocorrencias_inseridas+=1
            ultimos_dados = novos_dados
                
            clear()
            print(f"{ocorrencias_inseridas} dados inseridos\n")

            if intervalo_geracao:
                sleep(intervalo_geracao)


if __name__ == '__main__':
    main()