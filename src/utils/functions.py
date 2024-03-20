import os
import time
from dotenv import load_dotenv

thumb = [
'',
'  _    _                                   _____                  _     _                  _ ',
' | |  | |                                 / ____|                | |   (_)                | |',
' | |__| |   ___    _ __ ___     ___      | (___     ___   _ __   | |_   _   _ __     ___  | |',
" |  __  |  / _ \  | '_ ` _ \   / _ \      \___ \   / _ \ | '_ \  | __| | | | '_ \   / _ \ | |",
' | |  | | | (_) | | | | | | | |  __/      ____) | |  __/ | | | | | |_  | | | | | | |  __/ | |',
' |_|  |_|  \___/  |_| |_| |_|  \___|     |_____/   \___| |_| |_|  \__| |_| |_| |_|  \___| |_|',
'',                                                                                                              
'']

bolder = '\033[1m'
not_bolder = '\033[0m'



def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def load_init(skip=False):
    clear()

    if skip == True:

        return
    
    for line in thumb:
        time.sleep(0.3)
        print(line)

    time.sleep(1)

def load_simulator():
    clear()
    print('Iniciando simulação...')
    time.sleep(1)

def load_menu():
    clear()
    print(f"{bolder}HOME SENTINEL{not_bolder}\n")
    print(f"{bolder}1{not_bolder} - Iniciar Simulação")
    print(f"{bolder}2{not_bolder} - Analisar Dados Gerados")
    print(f"{bolder}3{not_bolder} - Sair\n")
    resposta = input(f"{bolder}> {not_bolder}")

    if resposta == '1':
        return 1
    elif resposta == '2':
        return 2
    elif resposta == '3':
        load_exit()
    else:
        return 0

def load_sensores_disponiveis():
    sensores = ['fumaca', 'gas', 'inundacao', 'luminosidade', 'som', 'temperatura', 'umidade']
    
    for sensor in sensores:
        if not os.getenv(f'SENSOR_{sensor.upper()}') in ('True', 'true', '1'):
            sensores.remove(sensor)

    return sensores

def load_exit():
    clear()
    load_init()
    print('Até mais...')
    time.sleep(1)
    clear()
    exit()
    
def load_not_found():
    clear()
    print('Nenhum sensor disponível para simulação.')
    time.sleep(2)
    clear()