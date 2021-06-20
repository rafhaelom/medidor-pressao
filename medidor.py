# ---------- Importando Bibliotecas ----------
from tkinter import *
from tkinter import messagebox # messagebox é a biblioteca de mensagem do tkinter.
from tkinter import ttk # ttk é a biblioteca gráfica do tkinter.
from datetime import datetime
import sqlite3

# ---------- Objeto da janela principal ----------
janela = Tk()

# ---------- Widgets - componentes da janela ----------
# --- Atributos ---
janela.title("Medição e monitoramento") # Título da janela.
janela.configure(bg="white") # Cor do backgroud da janela.
janela.resizable(width=False, height=False) # Tira a responsividade da janela.
janela.attributes("-alpha", 0.97) # Transparencia da janela.
#janela.iconbitmap(default="icon/logo.ico")

# --- Carregando imagens ---
logo = PhotoImage(file="icon/logo.png")

# ------------------------------------------------------------------------------ 
# ------------------------------- Banco de dados ------------------------------- 
#print("\nAbrindo e criando conexão com o Banco!\n")

# Tratamento de exceções(erros)
try:
    # Faz uma conexão, se não puder ser feita haverá uma exceção.
    # Conexão com o Banco de Dados SQLite.
    bd = sqlite3.connect("medidor.sqlite")

    # bd.cursor() retornará um objeto do tipo conn que é utilizado para fazer consultas.
    conn = bd.cursor()

    conn.execute("""CREATE TABLE IF NOT EXISTS medida (
                    data_hora text, 
                    peso real, 
                    sistolica interger, 
                    diastolica interger, 
                    pulsacao interger)""")

    #print("Conectado!\n")

except (sqlite3.Error) as e:
    print("\nFalha de conexão!\n {}".format(e))
    janela.destroy()


# ------------------------------------------------------------------------------ 

# ------------------------------------------------------------------------------ 
# -------------------------- Funcoes para eventos - events ---------------------
def click_cadastrar():
    #print("CLICOU CADASTRAR!")
    data_hora = datetime.now()
    peso = pesoEntry.get()
    sistolica = pasEntry.get()
    diastolica = padEntry.get()
    pulsacao = pulsacaoEntry.get()

    if (peso == "" and sistolica == "" and diastolica == "" and pulsacao == "" or peso == "" and sistolica == "" or diastolica == "" and pulsacao == ""or peso == "" or sistolica == "" or diastolica == "" or pulsacao == ""):
            messagebox.showerror(title="Cadastro Erro", message="Campo(s) vazio(s). Preencha todos os campos!")
    else:
        # Inserção no banco de dados
        conn.execute("""INSERT INTO medida VALUES('{}', {}, {}, {}, {})""".format(data_hora, peso, sistolica, diastolica, pulsacao))
        bd.commit()

        messagebox.showinfo(title="Informação Cadastro", message="Dados cadastrados com Sucesso!")
        #bd.close()
        #print("Fechando conexão com o banco!")

def click_sair():
    #print("CLICOU FECHAR JANELA!")
    if messagebox.askokcancel("Sair", "Deseja realmente sair e fechar o medidor?"):
        #print("Fechando janela e conexão do banco de dados!")
        bd.close()
        janela.destroy()
#---------------------------------------------------------------------------- 

# --- Frames ---
ladoEsquerdo = Frame(janela, width=300, height=400, bg="#329542", relief="raise")
ladoDireito = Frame(janela, width=497, height=400, bg="#63A355", relief="raise")
# --- Imagem Logo ---
logoLabel = Label(ladoEsquerdo, image=logo, bg="#329542")
# --- peso ---
pesoLabel = Label(ladoDireito, text="Peso:", font=("Indie Flower", 20), bg="#63A355", fg="white")
pesoEntry = ttk.Entry(ladoDireito, width=20)
# --- pas ---
pasLabel = Label(ladoDireito, text="Pressão Arterial Sistólica:", font=("Indie Flower", 20), bg="#63A355", fg="white")
pasEntry = ttk.Entry(ladoDireito, width=20)
# --- pad ---
padLabel = Label(ladoDireito, text="Pressão Arterial Diastólica:", font=("Indie Flower", 20), bg="#63A355", fg="white")
padEntry = ttk.Entry(ladoDireito, width=20)
# --- pulsacao ---
pulsacaoLabel = Label(ladoDireito, text="Pulsação:", font=("Indie Flower", 20), bg="#63A355", fg="white")
pulsacaoEntry = ttk.Entry(ladoDireito, width=20) 

# --- botoes ---
sairButton = ttk.Button(ladoDireito, text="Sair", width=20, command=click_sair)
cadastrarButton = ttk.Button(ladoDireito, text="Cadastrar", width=20, command=click_cadastrar)

# ---------- Layout - Gereciador de componetes da janela ----------
# ----- Inseri Componentes -----
# --- frames ---
ladoEsquerdo.pack(side=LEFT)
ladoDireito.pack(side=RIGHT)
# --- imagem logo ---
logoLabel.place(x=18, y=30)

# --- peso ---
pesoLabel.place(x=18, y=20)
pesoEntry.place(x=100, y=26, height=30)
# --- pas ---
pasLabel.place(x=18, y=89)
pasEntry.place(x=350, y=95, height=30)
# --- pad ---
padLabel.place(x=18, y=158)
padEntry.place(x=355, y=164, height=30)
# --- pulsacao ---
pulsacaoLabel.place(x=18, y=227)
pulsacaoEntry.place(x=150, y=233, height=30)

# --- botões ---
sairButton.place(x=300, y=320, height=30)
cadastrarButton.place(x=100, y=320, height=30)

# ---------- Tamanho da janela ----------
# --- widgth x heigth + left + topo ---
janela.geometry("800x400+250+180")
janela.protocol("WM_DELETE_WINDOW", click_sair)
janela.mainloop()