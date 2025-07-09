import customtkinter as ctk

# CONFIGURAÇÕES INICIAIS ---------------------------------------------------------------------------------
ctk.set_appearance_mode('system') # Define aparência da janela
gui = ctk.CTk() # Cria janela principal
gui.title("Sistema de Estacionamento") # Atribui título a janela principal
gui.geometry('500x500') # Define tamanho da janela
dicionario_niveis = {}
# ---------------------------------------------------------------------------------------------------------

# FUNÇÃO DE TROCA DE TELAS --------------------------------------------------------------------------------
def troca_telas(frame_desejado):
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

tela_retirar = ctk.CTkFrame(master=gui) # Cria frame da tela de retirada

tela_listar = ctk.CTkFrame(master=gui) # Cria frame da tela de listagem de vagas disponíveis

tela_encerramento = ctk.CTkFrame(master=gui) # Cria frame da tela de encerramento
#-----------------------------------------------------------------------------------------------------------

# FUNÇÃO PARA VALIDAR NÍVEIS E VAGAS -----------------------------------------------------------------------
def validar_inicio():
    try:
        numero_niveis = int(entry_niveis.get())
        numero_vagas = int(entry_vagas.get())

        if numero_niveis < 1 or numero_vagas < 1:
            resultado_inicio.configure(text='Erro: Número de níveis ou vagas inválido!', text_color='red')
            return
        
    except ValueError:
        resultado_inicio.configure(text='Erro: Digite apenas números!', text_color='red')
        return

    resultado_inicio.configure(text='')
    nomes_niveis = [niveis for niveis in range(1, numero_niveis + 1)]
    
    for nivel in nomes_niveis:
        dicionario_niveis[nivel] = [vagas for vagas in range(1, numero_vagas + 1)]

    troca_telas(tela_opcoes)

    return dicionario_niveis
#--------------------------------------------------------------------------------------------------------------
 
 # FUNÇÃO DE ESCOLHER OPÇÕES ----------------------------------------------------------------------------------
def escolher_opcao(opcao):
    if opcao == 'opcao_um':
        troca_telas(tela_estacionar)
    elif opcao == 'opcao_dois':
        troca_telas(tela_retirar)
    elif opcao == 'opcao_tres':
        troca_telas(tela_listar)
    elif opcao == 'opcao_quatro':
        troca_telas(tela_encerramento)
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
button_opc1 = ctk.CTkButton(master=tela_opcoes, command=lambda: escolher_opcao('opcao_um'), text='Estacionar carro', width=200, height=50)
button_opc1.place(relx=0.5, rely=0.2, anchor='center')

button_opc2 = ctk.CTkButton(master=tela_opcoes, command=lambda: escolher_opcao('opcao_dois'), text='Retirar carro', width=200, height=50)
button_opc2.place(relx=0.5, rely=0.4, anchor='center')

button_opc3 = ctk.CTkButton(master=tela_opcoes, command=lambda: escolher_opcao('opcao_tres'), text='Listar vagas disponíveis', width=200, height=50)
button_opc3.place(relx=0.5, rely=0.6, anchor='center')

button_opc4 = ctk.CTkButton(master=tela_opcoes, command=lambda: escolher_opcao('opcao_quatro'), text='Encerrar operação', width=200, height=50)
button_opc4.place(relx=0.5, rely=0.8, anchor='center')
#----------------------------------------------------------------------------------------------------------------

# TELA DE ESTACIONAR -----------------------------------------------------------------------------------------------




gui.mainloop() # Inicia a janela

