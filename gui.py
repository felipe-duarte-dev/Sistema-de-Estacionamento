import customtkinter as ctk
import copy as cp

# CONFIGURAÇÕES INICIAIS ----------------------------------------------------------------------------------
ctk.set_appearance_mode('system') # Define aparência da janela
gui = ctk.CTk() # Cria janela principal
gui.title("Sistema de Estacionamento") # Atribui título a janela principal
gui.geometry('600x500') # Define tamanho da janela
dicionario_niveis = {} # Cria dicionário que vai armanezar níveis e vagas disponíveis
dicionario_padrao = {}
# ---------------------------------------------------------------------------------------------------------

# FUNÇÃO DE TROCA DE TELAS --------------------------------------------------------------------------------
def troca_telas(frame_desejado): # O método pack_forget() "apaga" as telas antes de exibir a próxima
    tela_inicial.pack_forget()
    tela_opcoes.pack_forget()
    tela_estacionar.pack_forget()
    tela_retirar.pack_forget()
    tela_listar.pack_forget()
    tela_encerramento.pack_forget()

    frame_desejado.pack(padx=20, pady=20, fill="both", expand=True)
#----------------------------------------------------------------------------------------------------------

# TELAS DO SISTEMA ----------------------------------------------------------------------------------------
tela_inicial = ctk.CTkFrame(master=gui) # Cria frame da tela inicial
tela_inicial.pack(padx=20, pady=20, fill='both', expand=True)

tela_opcoes = ctk.CTkFrame(master=gui) # Cria frame da tela de opções

tela_estacionar = ctk.CTkFrame(master=gui) # Cria frame da tela de estacionamento
#tela_estacionar.pack(padx=20, pady=20, fill='both', expand=True)
tela_retirar = ctk.CTkFrame(master=gui) # Cria frame da tela de retirada
#tela_retirar.pack(padx=20, pady=20, fill='both', expand=True)
tela_listar = ctk.CTkFrame(master=gui) # Cria frame da tela de listagem de vagas disponíveis
#tela_listar.pack(padx=20, pady=20, fill='both', expand=True)
tela_encerramento = ctk.CTkFrame(master=gui) # Cria frame da tela de encerramento
#tela_encerramento.pack(padx=20, pady=20, fill='both', expand=True)
#-----------------------------------------------------------------------------------------------------------

# FUNÇÃO PARA VALIDAR NÍVEIS E VAGAS -----------------------------------------------------------------------
def validar_inicio():
    global dicionario_padrao # Define o dicionario_padrao como variável global
    try:
        numero_niveis = int(entry_niveis.get()) # Recebe o número de níves
        numero_vagas = int(entry_vagas.get()) # Recebe o número de vagas

        if numero_niveis < 1 or numero_vagas < 1: # Verifica se os níveis e vagas são números positivos
            resultado_inicio.configure(text='Erro: Número de níveis ou vagas inválido!', text_color='red')
            return
        
    except ValueError: # Verifica se os níveis e vagas são números inteiros
        resultado_inicio.configure(text='Erro: Digite apenas números!', text_color='red')
        return

    resultado_inicio.configure(text='') # Apaga a mensagem de erro após a correta inserção dos dados
    nomes_niveis = [niveis for niveis in range(1, numero_niveis + 1)] # Lista de vagas
    
    for nivel in nomes_niveis: # Adiciona a lista de vagas a cada nível no dicionário
        dicionario_niveis[nivel] = [vagas for vagas in range(1, numero_vagas + 1)]

    dicionario_padrao = cp.deepcopy(dicionario_niveis) # Cria um espelho do dicionário de níveis

    resultado_inicio.configure(text='Níveis e vagas cadastrados com sucesso!', text_color='green') # Retorna mensagem de sucesso na tela inicial
    vagas_disponiveis(dicionario_niveis) # Atualiza as vagas disponíveis
    gui.after(1500, lambda: troca_telas(tela_opcoes)) # Troca para a tela de opções com delay de 1,5 segundos

    return dicionario_niveis, dicionario_padrao
#--------------------------------------------------------------------------------------------------------------
 
 # FUNÇÃO DE ESCOLHA DE OPÇÕES ----------------------------------------------------------------------------------
def escolher_opcao(opcao): # Chama a função de troca de tela com base na opção escolhida
    if opcao == 'opcao_um':
        vagas_disponiveis(dicionario_niveis)
        troca_telas(tela_estacionar)
    elif opcao == 'opcao_dois':
        troca_telas(tela_retirar)
    elif opcao == 'opcao_tres':
        vagas_disponiveis(dicionario_niveis)
        troca_telas(tela_listar)
    elif opcao == 'opcao_quatro':
        troca_telas(tela_encerramento)
#--------------------------------------------------------------------------------------------------------------

# FUNÇÃO PARA ESTACIONAR CARRO --------------------------------------------------------------------------------
def validar_estacionamento(dicionario_niveis):
    try: # Verifica se as entradas de nível e vaga são números inteiros
        nivel_estacionar = int(entry_nivel_estacionar.get()) # Recebe o nível que o usuário deseja estacionar
        vaga_estacionar = int(entry_vaga_estacionar.get()) # Recebe a vaga que o usuário desejar estacionar

        if nivel_estacionar < 1 or vaga_estacionar < 1: # Verifica se o nível e a vaga são positivos
            resultado_estacionar.configure(text='Erro: Nível ou vaga inexistente!', text_color='red')
            return
    except ValueError:
        resultado_estacionar.configure(text='Erro: Digite apenas números!', text_color='red')
        return

    if nivel_estacionar not in dicionario_niveis: # Verifica se o nível existe
        resultado_estacionar.configure(text='Erro: Nível inexistente!', text_color='red') 
        return
    
    if vaga_estacionar in dicionario_niveis[nivel_estacionar]: # Verifica se a vaga está disponível dentro do dicionário
        dicionario_niveis[nivel_estacionar].remove(vaga_estacionar)
        resultado_estacionar.configure(text='Carro Estacionado!', text_color='green') # Exibe mensagem de sucesso na operação
        gui.after(1500, lambda: troca_telas(tela_opcoes)) # Retorna a tela de opções após um delay de 1,5 segundos
        return dicionario_niveis
    else: # Verifica se a vaga existe no nível dentro do dicionário de vagas
        resultado_estacionar.configure(text='Erro: Vaga ocupada ou inexistente!', text_color='red')
        return
#--------------------------------------------------------------------------------------------------------------

# FUNÇÃO PARA LISTAGEM DE VAGAS DISPONÍVEIS -------------------------------------------------------------------
def vagas_disponiveis(dicionario_niveis):

    vagas_disponiveis_texto = 'Vagas disponíveis: \n\n' # Mensagem inicial

    for nivel, vagas in dicionario_niveis.items(): # Formata mensagem de níveis e vagas para exibição na tela do usuário
        vagas_disponiveis_texto += f'Nível {nivel}: {vagas}\n'

    label_vagas_disponiveis.configure(text=vagas_disponiveis_texto,) # Altera a label de vagas disponíveis para a tela de estacionar
    label_listagem.configure(text=vagas_disponiveis_texto) # Altera a label de vagas disponíveis para a tela de vagas disponíveis
    return
#--------------------------------------------------------------------------------------------------------------

# FUNÇÃO PARA RETIRAR CARRO -----------------------------------------------------------------------------------
def validar_retirada(dicionario_niveis, dicionario_padrao):
    try: # Verifica se as entradas de nível e vaga são números inteiros
        nivel_retirar = int(entry_nivel_retirar.get()) # Recebe o nível que o usuário deseja retirar
        vaga_retirar = int(entry_vaga_retirar.get()) # Recebe a vaga que o usuário desejar retirar

        if nivel_retirar < 1 or vaga_retirar < 1: # Verifica se o nível e a vaga são positivos
            resultado_retirar.configure(text='Erro: Nível ou vaga inexistente!', text_color='red')
            return
    except ValueError:
        resultado_retirar.configure(text='Erro: Digite apenas números!', text_color='red')
        return

    if nivel_retirar not in dicionario_niveis: # Verifica se o nível digitado existe
        resultado_retirar.configure(text='Erro: Nível inexistente!', text_color='red')
        return

    if vaga_retirar not in dicionario_niveis[nivel_retirar] and vaga_retirar in dicionario_padrao[nivel_retirar]: # Verifica se a vaga está ocupada e dentro das vagas existentes
        dicionario_niveis[nivel_retirar].append(vaga_retirar) # Adciona a vaga novamente as vagas disponíveis para estacionar
        dicionario_niveis[nivel_retirar].sort() # Organiza o dicionário em ordem crescente
        gui.after(1500, lambda: troca_telas(tela_opcoes)) # Troca a tela após um delay 1,5 segundos
        resultado_retirar.configure(text='Carro retirado com sucesso!', text_color='green')
        return dicionario_niveis
    else:
        resultado_retirar.configure(text='Erro: A vaga não está ocupada ou não existe!', text_color='red')
        return
#--------------------------------------------------------------------------------------------------------------

 # TELA INICIAL------------------------------------------------------------------------------------------------
label_niveis = ctk.CTkLabel(master=tela_inicial, text='Número de Níveis:',) # Label número de níveis
label_niveis.place(relx=0.5, rely=0.1, anchor='center')

entry_niveis = ctk.CTkEntry(master=tela_inicial, placeholder_text="Digite o número de níveis: ", width=200, height=35) # Entrada para digitar o número de níveis
entry_niveis.place(relx=0.5, rely=0.2, anchor='center')

label_vagas = ctk.CTkLabel(master=tela_inicial, text='Número de vagas:') # Label número de vagas
label_vagas.place(relx=0.5, rely=0.3, anchor='center')

entry_vagas = ctk.CTkEntry(master=tela_inicial, placeholder_text="Digite o número de vagas: ", width=200, height=35) # Entrada para digitar o número de vagas
entry_vagas.place(relx=0.5, rely=0.4, anchor='center')

button_inicial = ctk.CTkButton(master=tela_inicial, command=validar_inicio, text='Confirmar', width=200, height=35) # Botão para validação de número de níveis e vagas
button_inicial.place(relx=0.5, rely=0.55, anchor='center')

resultado_inicio = ctk.CTkLabel(master=tela_inicial, text='') # Feedback da validação inicial
resultado_inicio.place(relx=0.5, rely=0.65, anchor='center')
#----------------------------------------------------------------------------------------------------------------

# TELA DE OPÇÕES ------------------------------------------------------------------------------------------------
button_opc1 = ctk.CTkButton(master=tela_opcoes, command=lambda: escolher_opcao('opcao_um'), text='Estacionar carro', width=200, height=50) # Opção para estacionar carro
button_opc1.place(relx=0.5, rely=0.2, anchor='center')

button_opc2 = ctk.CTkButton(master=tela_opcoes, command=lambda: escolher_opcao('opcao_dois'), text='Retirar carro', width=200, height=50) # Opção para retirar carro
button_opc2.place(relx=0.5, rely=0.4, anchor='center')

button_opc3 = ctk.CTkButton(master=tela_opcoes, command=lambda: escolher_opcao('opcao_tres'), text='Listar vagas disponíveis', width=200, height=50) # Opção para listar vagas
button_opc3.place(relx=0.5, rely=0.6, anchor='center')

button_opc4 = ctk.CTkButton(master=tela_opcoes, command=lambda: escolher_opcao('opcao_quatro'), text='Encerrar operação', width=200, height=50) # Opção para encerrar operações
button_opc4.place(relx=0.5, rely=0.8, anchor='center')
#----------------------------------------------------------------------------------------------------------------

# TELA DE ESTACIONAR --------------------------------------------------------------------------------------------
label_estacionar = ctk.CTkLabel(master=tela_estacionar, text='Nível em que deseja estacionar:') # Label
label_estacionar.place(relx=0.5, rely=0.1, anchor='center')

entry_nivel_estacionar = ctk.CTkEntry(master=tela_estacionar, placeholder_text='Ex: 1', width=200, height=35) # Entrada para digitar nível que o usuário deseja estacionar
entry_nivel_estacionar.place(relx=0.5, rely=0.2, anchor='center')

label_vaga_estacionar = ctk.CTkLabel(master=tela_estacionar, text='Vaga em que deseja estacionar:') # Label
label_vaga_estacionar.place(relx=0.5, rely=0.3, anchor='center')

entry_vaga_estacionar = ctk.CTkEntry(master=tela_estacionar, placeholder_text='Ex: 1', width=200, height=35) # Entrada para digitar vaga que o usuário deseja estacionar
entry_vaga_estacionar.place(relx=0.5, rely=0.4, anchor='center')

button_estacionar = ctk.CTkButton(master=tela_estacionar, command=lambda: validar_estacionamento(dicionario_niveis), text='Confirmar', width=200, height=35) # Botão para confirmar estacionamento
button_estacionar.place(relx=0.5, rely=0.55, anchor='center')

resultado_estacionar = ctk.CTkLabel(master=tela_estacionar, text='',) # Feedback da validação de estacionamento
resultado_estacionar.place(relx=0.5, rely=0.05, anchor='center')

label_vagas_disponiveis = ctk.CTkLabel(master=tela_estacionar, text='') # Exibe vagas disponíveis para estacionamento
label_vagas_disponiveis.place(relx=0.5, rely=0.8, anchor='center')
#---------------------------------------------------------------------------------------------------------------- 

# TELA DE RETIRAR CARRO -----------------------------------------------------------------------------------------
label_retirar = ctk.CTkLabel(master=tela_retirar, text='Nível em que desejar realizar a retirada:') # Label
label_retirar.place(relx=0.5, rely=0.1, anchor='center')

entry_nivel_retirar = ctk.CTkEntry(master=tela_retirar, placeholder_text='Ex: 1', width=200, height=35) # Entrada para digitar nível de retirada
entry_nivel_retirar.place(relx=0.5, rely=0.2, anchor='center')

label_vaga_retirar = ctk.CTkLabel(master=tela_retirar, text='Vaga que deseja retirar:') # Label
label_vaga_retirar.place(relx=0.5, rely=0.3, anchor='center')

entry_vaga_retirar = ctk.CTkEntry(master=tela_retirar, placeholder_text='Ex: 1', width=200, height=35) # Entrada para digitar a vaga a ser retirada
entry_vaga_retirar.place(relx=0.5, rely=0.4, anchor='center')

button_retirar = ctk.CTkButton(master=tela_retirar, command=lambda: validar_retirada(dicionario_niveis, dicionario_padrao), text='Confirmar', width=200, height=35)
button_retirar.place(relx=0.5, rely=0.55, anchor='center') # Botão para confirmar e validar retirada

resultado_retirar = ctk.CTkLabel(master=tela_retirar, text='') # Feedback da validação de retirada
resultado_retirar.place(relx=0.5, rely=0.65, anchor='center')
#----------------------------------------------------------------------------------------------------------------

# TELA DE LISTAGEM DE VAGAS DISPONÍVEIS ------------------------------------------------------------------------- 
label_listagem = ctk.CTkLabel(master=tela_listar, text='') # Label com as vagas disponíveis
label_listagem.place(relx=0.5, rely=0.2, anchor='center')

button_voltar = ctk.CTkButton(master=tela_listar, command=lambda: troca_telas(tela_opcoes), text='Voltar', width=200, height=35)
button_voltar.place(relx=0.5, rely=0.7, anchor='center') # Botão para retornar a tela de opções
#----------------------------------------------------------------------------------------------------------------

# TELA DE ENCERRAMENTO ------------------------------------------------------------------------------------------
label_encerramento = ctk.CTkLabel(master=tela_encerramento, text='Desejar encerrar a sessão?') # Label
label_encerramento.place(relx=0.5, rely=0.2, anchor='center')

button_encerrar = ctk.CTkButton(master=tela_encerramento, command=lambda: troca_telas(tela_inicial), text='Confirmar', width=200, height=50)
button_encerrar.place(relx=0.25, rely=0.5, anchor='center') # Botão para confirmar encerramento

button_cancelar = ctk.CTkButton(master=tela_encerramento, command=lambda: troca_telas(tela_opcoes), text='Voltar', width=200, height=50)
button_cancelar.place(relx=0.75, rely=0.5, anchor='center') # Botão para voltar a tela de opções
#----------------------------------------------------------------------------------------------------------------

gui.mainloop() # Inicia a janela
