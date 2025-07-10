import customtkinter as ctk

# CONFIGURAÇÕES INICIAIS ---------------------------------------------------------------------------------
ctk.set_appearance_mode('system') # Define aparência da janela
gui = ctk.CTk() # Cria janela principal
gui.title("Sistema de Estacionamento") # Atribui título a janela principal
gui.geometry('600x500') # Define tamanho da janela
dicionario_niveis = {} # Cria dicionário que vai armanezar níveis e vagas disponíveis
# ---------------------------------------------------------------------------------------------------------

# FUNÇÃO DE TROCA DE TELAS --------------------------------------------------------------------------------
def troca_telas(frame_desejado): # O método pack_forget() "apaga" as telas antes de exibir a próxima
    tela_inicial.pack_forget()
    tela_opcoes.pack_forget()
    tela_estacionar.pack_forget()
    tela_retirar.pack_forget()
    tela_listar.pack_forget()

    frame_desejado.pack(padx=20, pady=20, fill="both", expand=True)
#----------------------------------------------------------------------------------------------------------

# TELAS DO SISTEMA ----------------------------------------------------------------------------------------
tela_inicial = ctk.CTkFrame(master=gui) # Cria frame da tela inicial
tela_inicial.pack(padx=20, pady=20, fill='both', expand=True)

tela_opcoes = ctk.CTkFrame(master=gui) # Cria frame da tela de opções

tela_estacionar = ctk.CTkFrame(master=gui) # Cria frame da tela de estacionamento
#tela_estacionar.pack(padx=20, pady=20, fill='both', expand=True)
tela_retirar = ctk.CTkFrame(master=gui) # Cria frame da tela de retirada

tela_listar = ctk.CTkFrame(master=gui) # Cria frame da tela de listagem de vagas disponíveis

tela_encerramento = ctk.CTkFrame(master=gui) # Cria frame da tela de encerramento
#-----------------------------------------------------------------------------------------------------------

# FUNÇÃO PARA VALIDAR NÍVEIS E VAGAS -----------------------------------------------------------------------
def validar_inicio():
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

    resultado_inicio.configure(text='Níveis e vagas cadastrados com sucesso!', text_color='green') # Retorna mensagem de sucesso na tela inicial
    vagas_disponiveis(dicionario_niveis) # Atualiza as vagas disponíveis
    gui.after(1500, lambda: troca_telas(tela_opcoes)) # Troca para a tela de opções com delay de 1,5 segundos

    return dicionario_niveis
#--------------------------------------------------------------------------------------------------------------
 
 # FUNÇÃO DE ESCOLHA DE OPÇÕES ----------------------------------------------------------------------------------
def escolher_opcao(opcao): # Chama a função de troca de tela com base na opção escolhida
    if opcao == 'opcao_um':
        vagas_disponiveis(dicionario_niveis)
        troca_telas(tela_estacionar)
    elif opcao == 'opcao_dois':
        troca_telas(tela_retirar)
    elif opcao == 'opcao_tres':
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

    label_vagas_disponiveis.configure(text=vagas_disponiveis_texto,) # Altera a label de vagas disponíveis
    return
#--------------------------------------------------------------------------------------------------------------

 # TELA INICIAL------------------------------------------------------------------------------------------------
label_niveis = ctk.CTkLabel(master=tela_inicial, text='Número de Níveis:',) # Label número de níveis
label_niveis.place(relx=0.5, rely=0.1, anchor='center')

entry_niveis = ctk.CTkEntry(master=tela_inicial, placeholder_text="Digite o número de níveis: ", width=200, height=35) # Entry número de níveis
entry_niveis.place(relx=0.5, rely=0.2, anchor='center')

label_vagas = ctk.CTkLabel(master=tela_inicial, text='Número de vagas:') # Label número de vagas
label_vagas.place(relx=0.5, rely=0.3, anchor='center')

entry_vagas = ctk.CTkEntry(master=tela_inicial, placeholder_text="Digite o número de vagas: ", width=200, height=35) # Entry número de vagas
entry_vagas.place(relx=0.5, rely=0.4, anchor='center')

button_inicial = ctk.CTkButton(master=tela_inicial, command=validar_inicio, text='Confirmar', width=200, height=35) # Button validação de número de níveis e vagas
button_inicial.place(relx=0.5, rely=0.55, anchor='center')

resultado_inicio = ctk.CTkLabel(master=tela_inicial, text='') # Feedback da validação
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

resultado_estacionar = ctk.CTkLabel(master=tela_estacionar, text='',) # Feedback da validação
resultado_estacionar.place(relx=0.5, rely=0.05, anchor='center')

label_vagas_disponiveis = ctk.CTkLabel(master=tela_estacionar, text='') # Exibe vagas disponíveis para estacionamento
label_vagas_disponiveis.place(relx=0.5, rely=0.8, anchor='center')
#---------------------------------------------------------------------------------------------------------------- 

# TELA DE RETIRAR CARRO -----------------------------------------------------------------------------------------

#---------------------------------------------------------------------------------------------------------------- 

gui.mainloop() # Inicia a janela

