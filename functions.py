# Função para estacionar um carro em uma vaga disponível dos níveis existentes
def estacionar_carro(dicionario_niveis, niveis_estacionamento):
    #Verifica se o nível é um número inteiro
    while True:
        try:
            nivel_estacionar = input(f"Digite o nível para estacionar (1 a {niveis_estacionamento}) (ou 0 para cancelar): ") # Recebe o nível que o usuário deseja estacionar
            nivel_estacionar = int(nivel_estacionar) 

            # Caso o nível não esteja entre os níveis existentes o código executa novamente o loop
            if nivel_estacionar not in dicionario_niveis:
                print("Nível inexistente!")
                continue
            # Cancela a operação
            elif nivel_estacionar == 0:
                print("Operação cancelada!")
                return dicionario_niveis
            
            break

        except ValueError:
            print("Nível inválido!")

    #Verifica se a vaga escolhida é um número inteiro
    while True:
        try:
            print(f"Vagas disponíveis no nível {nivel_estacionar}: {dicionario_niveis[nivel_estacionar]}") # Exibe as vagas disponíveis para estacionar no nível escolhido
            vaga_estacionar = input("Digite o número da vaga (ou 0 para cancelar): ") # Recebe a vaga que o usuário deseja estacionar
            vaga_estacionar = int(vaga_estacionar)

            # Cancela a operação
            if vaga_estacionar == 0:
                print("Operação cancelada!")
                return dicionario_niveis
            
            dicionario_niveis[nivel_estacionar].remove(vaga_estacionar) # Atualiza o dicionário, retirando a vaga ocupada
            print("Operação realizada com sucesso!") 
            return dicionario_niveis # Encerra a operação e retorna o dicionário atualizado com a vaga preenchida
        
        except ValueError:
            print("Vaga inexistente!")

# Função para retirar um carro em uma vaga ocupada dos níveis existentes
def retirar_carro(dicionario_niveis, vagas_nivel):
    # Verifica se o nível é um número inteiro
    while True:
        try:
            nivel_retirar = input("Digite o nível do carro (ou 0 para cancelar): ") # Recebe o nível que o usuário deseja fazer a retirada
            nivel_retirar = int(nivel_retirar)

            if nivel_retirar not in dicionario_niveis: # Verifica se o nível faz parte dos níveis existentes
               print("Nível inexistente!")
               continue
            elif nivel_retirar == 0: # Cancela a operação
                print("Operação cancelada!")
                return dicionario_niveis
            
            break
        
        except ValueError:
            print("Nível inválido!")
    
    #Verifica se o número da vaga é um número inteiro
    while True:
        try:
            vaga_retirar = input("Digite o número da vaga (ou 0 para cancelar): ") # Recebe a vaga que o carro está estacionado
            vaga_retirar = int(vaga_retirar)

        except ValueError:
            print("Entrada inválida, digite apenas números!")
            continue

        if vaga_retirar in dicionario_niveis[nivel_retirar]: # Verifica se a vaga está no dicionário, caso ela esteja significa que a vaga não está ocupada
            print(f"A vaga {vaga_retirar} não está ocupada!")
            continue # Reinicia o loop até o usuário digitar uma vaga ocupada
        elif vaga_retirar not in range(1, vagas_nivel + 1): # Verifica se a vaga está dentro das vagas existentes
            print(f"A vaga {vaga_retirar} não existe!")
            continue
        elif vaga_retirar == 0: # Cancela a operação
            print("Operação cancelada!")
            return dicionario_niveis

        dicionario_niveis[nivel_retirar].append(vaga_retirar) # Adiciona a vaga novamente ao dicionário, listando ela como disponível
        dicionario_niveis[nivel_retirar].sort() # Ordena em ordem crescente as vagas disponíveis
        print("Você ficou no estacionamento entre 20h às 21h \nOperação realizada com sucesso!")
        return dicionario_niveis # Encerra a operação e retorna o dicionário atualizado

# Função para listar todas as vagas disponíveis nos níveis existentes
def listar_vagas(dicionario_niveis):
    print("Vagas disponíveis: ")

    for contador in dicionario_niveis: # Lista todas as vagas disponíveis por níveis
        print(f"Nível {contador}: {dicionario_niveis[contador]}")
    
    return dicionario_niveis