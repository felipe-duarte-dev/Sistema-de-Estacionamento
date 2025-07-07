from functions import estacionar_carro, retirar_carro, listar_vagas # Importa as funções do arquivo functions

print("=== Sistema de Estacionamento XXXX Shopping ===")

while True:
    # Verifica se a entrada do usuário é um número inteiro
    try:
        niveis_estacionamento = input("Quantos níveis o estacionamento possui? (mínimo 1): ") # A variável niveis_estacionamento recebe uma string e em seguida converte para um inteiro
        niveis_estacionamento = int(niveis_estacionamento)

        if niveis_estacionamento < 1: # Verifica se o número de níveis é positivo
            print("Número de níveis inválido")
            continue
        break
    
    except ValueError:
        print("Número de níveis inválido!")

while True:
    # Verifica se a entrada do usuário é um número inteiro
    try:
        vagas_nivel = input("Quantas vagas por nível? ") # A variável vagas_nivel recebe uma string e em seguida converte para um inteiro
        vagas_nivel = int(vagas_nivel)

        if vagas_nivel < 1: # Verifica se o número de vagas é positivo
            print("Número de vagas inválido")
            continue
        break

    except ValueError:
        print("Número de vagas inválido!")


dicionario_niveis = {} # Cria um dicionário para guardar o níveis (chaves) e os números de vagas (valores)
nomes_niveis = [niveis for niveis in range(1, niveis_estacionamento + 1)] # Cria uma lista para armazenar as chaves do dicionário

for nivel in nomes_niveis:
    dicionario_niveis[nivel] = [vagas for vagas in range(1, vagas_nivel + 1)] # Adiciona o número de vagas por nível a cada nível {nível: [vagas]}

print("Opções \n1 - Estacionar carro \n2 - Sair com carro \n3 - Listar vagas disponíveis \n4 - Encerrar sistema") # Mostra as opções de funções ao usuário

while True:
    # Verifica se a opção é um valor inteiro
    try:
        opcao = input("Escolha uma opção: ")
        opcao = int(opcao)
        # Verifica se é uma opção válida dentre as opções existentes
        if opcao not in [1, 2, 3, 4]:
            print("Opção Inválida")

    except ValueError:
        print("Opção Inválida")

    # Executa a função associada a opção escolhida pelo usuário
    match opcao:
        case 1:
            dicionario_niveis = estacionar_carro(dicionario_niveis, niveis_estacionamento) # Atualiza o dicionário de níveis e vagas
        case 2:
            dicionario_niveis = retirar_carro(dicionario_niveis, vagas_nivel)  # Atualiza o dicionário de níveis e vagas
        case 3:
            listar_vagas(dicionario_niveis)
        case 4:
            print("Encerrando o sistema...")
            break