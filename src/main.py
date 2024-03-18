from connection.MongoConnection import MongoConnection
from connection.PostgresConnection import PostgresConnection
from service.simulador import simular, refinar_sensores
from utils.functions import load_init, load_simulator, clear, load_menu, load_sensores_disponiveis
import os
from time import sleep
from dotenv import load_dotenv

load_dotenv()

def main():
    ocorrencias_inseridas = 0
    ultimos_dados = None
    load_init(skip=os.getenv('SKIP_INTRO') in ('True', 'true', '1'))
    connMongo = MongoConnection()
    connPostgres = PostgresConnection()
    
    while True:
        clear()

        clientes = connPostgres.get_clientes() # será utilizado para criar o relatório
        sensores_refinados = refinar_sensores(connPostgres.get_sensores_para_simular())
        exit()

        resp = load_menu()

        if resp == 1:
            while True:
                sensores = load_sensores_disponiveis()

                if not sensores:
                    break

                novos_dados = simular(connMongo, sensores, ultimos_dados)
                if novos_dados:
                    ocorrencias_inseridas+=1
                    ultimos_dados = novos_dados

                print(f"{ocorrencias_inseridas} dados inseridos\n")
                sleep(0.25)
                clear()

        if resp == 2:
            print(f"A desenvolver...")
            input("Pressione Enter para continuar...")

        if resp == 3:
            connMongo.close_connection()
            connPostgres.close_connection()
            break

        clear()

if __name__ == '__main__':
    main()