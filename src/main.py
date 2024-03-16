from connection.MongoConnection import MongoConnection
from connection.PostgresConnection import PostgresConnection
from service.simulator import simulate
from utils.functions import load_init, load_simulator, clear

def main():
    inserted_data = 0
    load_init()
    connMongo = MongoConnection()
    connPostgres = PostgresConnection()
    load_simulator()
    
    while True:
        clear()
        inserted_data += simulate(connMongo)
        print(f'{inserted_data} registros inseridos')
    

if __name__ == '__main__':
    main()