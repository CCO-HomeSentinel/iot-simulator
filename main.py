from src.connection.Connection import Connection
from src.service.simulator import simulate_and_insert_data
from src.utils.functions import load_init, load_simulator, clear

def main():
    load_init()
    conn = Connection()
    load_simulator()
    
    while True:
        clear()
        print(f"{simulate_and_insert_data(conn)} registros inseridos")
    

if __name__ == '__main__':
    main()