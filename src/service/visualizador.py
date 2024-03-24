from time import sleep

def escolher_cliente(clientes):
    print('Escolha o ID de cliente para visualizar os dados\n')
    
    for cliente in clientes:
        print(f"[\033[1m{cliente['id']}\033[0m] - {cliente['nome']}")

    id = input(f'\n\033[1m>\033[0m ')

    for cliente in clientes:
        if cliente['id'] == int(id):
            return cliente
        
    print('Cliente não encontrado')
    sleep(2)
    return

def escolher_sensor(dados):
    if not dados:
        print('Nenhum dado encontrado')
        sleep(2)
        return
    
    print(f"\033[1mEscolha o sensor para analisar os dados\033[0m\n")

    for i, dado in enumerate(dados):
        print(f"\033[1m[{i+1}]\033[0m - {dado[9]} em {dado[13]} - {dado[21]} ({dado[22]})")

    resp = input(f'\n\033[1m>\033[0m ')
    escolha = int(resp)-1

    for i, dado in enumerate(dados):
        if i == escolha:
           return dado[18]
        
    print('Sensor não encontrado')
    sleep(2)