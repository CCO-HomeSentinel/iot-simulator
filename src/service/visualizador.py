from time import sleep

def escolher_cliente(clientes):
    print('Escolha o ID de cliente para visualizar os dados\n')
    
    for cliente in clientes:
        print(f"[\033[1m{cliente['id']}\033[0m] - {cliente['nome']}")

    id = input(f'\n\033[1m>\033[0m ')

    for cliente in clientes:
        if cliente['id'] == int(id):
            print(f'\nCliente escolhido: {cliente["nome"]}\n')
            return cliente
        
    print('Cliente não encontrado')
    sleep(2)
    return

def escolher_sensor(dados):
    print(dados)