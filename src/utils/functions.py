import os
import time

thumb = [
"",
"  _    _                                   _____                  _     _                  _ ",
" | |  | |                                 / ____|                | |   (_)                | |",
" | |__| |   ___    _ __ ___     ___      | (___     ___   _ __   | |_   _   _ __     ___  | |",
" |  __  |  / _ \  | '_ ` _ \   / _ \      \___ \   / _ \ | '_ \  | __| | | | '_ \   / _ \ | |",
" | |  | | | (_) | | | | | | | |  __/      ____) | |  __/ | | | | | |_  | | | | | | |  __/ | |",
" |_|  |_|  \___/  |_| |_| |_|  \___|     |_____/   \___| |_| |_|  \__| |_| |_| |_|  \___| |_|",
"",                                                                                                              
""]

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def load_init():
    clear()
    for line in thumb:
        time.sleep(0.3)
        print(line)

    time.sleep(1)

def load_simulator():
    clear()
    print("Iniciando simulação...")
    time.sleep(1)
