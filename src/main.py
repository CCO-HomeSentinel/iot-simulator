from connection.MongoConnection import MongoConnection
from connection.PostgresConnection import PostgresConnection
from service.simulator import simulate
from utils.functions import load_init, load_simulator, clear, load_menu
import os
from dotenv import load_dotenv

load_dotenv()

def main():
    inserted_data = 0
    load_init(skip=os.getenv('SKIP_INTRO') in ('True', 'true', '1'))
    connMongo = MongoConnection()
    connPostgres = PostgresConnection()
    
    while True:
        clear()
        resp = load_menu()

        if resp == 1:
            while True:
                inserted_data += simulate(connMongo)
                print(f"{inserted_data} dados inseridos\n")
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