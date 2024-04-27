from connection.MySQLConnection import MySQLConnection
from service.simulador import simular, refinar_sensores, ativar_sensores
from utils.functions import load_init, clear, load_sensores_disponiveis, load_not_found
from service.http_client import enviar_json
from time import sleep
from dotenv import load_dotenv
import os
from datetime import datetime
import utils.query as queries

load_dotenv()

def main():
    start = datetime.now()
    quantidade_envios = 0
    quantidade_rodadas = 0
    intervalo_geracao = float(os.getenv('INTERVALO_SIMULADOR'))
    intervalo_envio = float(os.getenv('INTERVALO_ENVIO'))

    dados = {'registros': []}

    load_init(skip=os.getenv('SKIP_INTRO') in ('True', 'true', '1'))
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

        novos_dados = simular(instancias, dados['registros'][-1] if dados['registros'] else None)
        dados['registros'].extend(novos_dados)
        quantidade_rodadas += 1
                
        clear()
        print(f"{len(dados['registros'])} dados simulados\n{quantidade_envios} envios realizados\n{quantidade_rodadas} rodadas\n")

        if (datetime.now() - start).seconds >= intervalo_envio:
            enviar_json(dados)
            start = datetime.now()
            quantidade_envios += 1
            
        sleep(intervalo_geracao)


if __name__ == '__main__':
    main()