# ---------- Bibliotecas ----------
from tkinter import *
from tkinter import messagebox # messagebox é a biblioteca de mensagem do tkinter.
from tkinter import ttk # ttk é a biblioteca gráfica do tkinter.
from datetime import datetime
import psycopg2

# ---------- Objeto da janela principal ----------
janela = Tk()

# ---------- Widgets - componentes da janela ----------
# --- Atributos ---
janela.title("Medição e monitoramento") # Título da janela.
janela.configure(bg="white") # Cor do backgroud da janela.
janela.resizable(width=False, height=False) # Tira a responsividade da janela.
janela.attributes("-alpha", 0.97) # Transparencia da janela.
janela.iconbitmap(default="icon/logo.ico")

# --- Carregando imagens ---
logo = PhotoImage(file="icon/logotipo.png")
# ------------------------------------------------------------------------------ 
# ------------------------------- Banco de dados ------------------------------- 
print("\nAbrindo e criando conexão com o Banco!\n")
# Conecção com o Banco de Dados PostgreSQL
DB_HOST = "localhost"
DB_USER = "postgres"
DB_PASS = "teste123"
DB_NAME = "medidor"

# Tratamento de exceções(erros)
try:
    # Faz uma conexão, se não puder ser feita haverá uma exceção.
    conn = psycopg2.connect(
        host= DB_HOST, 
        database= DB_NAME,
        user= DB_USER,
        password= DB_PASS)
    
    # conn.cursor() retornará um objeto do tipo cur que é utilizado para fazer consultas
    cur = conn.cursor()
    print("Conectado!\n")

except (psycopg2.Error) as e:
    print("\nFalha de conexão!\n%s" % (e))

# ------------------------------------------------------------------------------ 

# ------------------------------------------------------------------------------ 
# -------------------------- Funcoes para eventos - events ---------------------
def click_cadastrar():
    print("CLICOU CADASTRAR!")
    data_hora = datetime.now()
    peso = pesoEntry.get()
    sistolica = pasEntry.get()
    diastolica = padEntry.get()
    pulsacao = pulsacaoEntry.get()

    if (peso == "" and sistolica == "" and diastolica == "" and pulsacao == "" or peso == "" and sistolica == "" or diastolica == "" and pulsacao == ""or peso == "" or sistolica == "" or diastolica == "" or pulsacao == ""):
            messagebox.showerror(title="Cadastro Erro", message="Campo(s) vazio(s). Preencha todos os campos!")
    else:
        # Inserção no banco de dados
        sql = "INSERT INTO medida VALUES (%s, %s, %s, %s, %s)"
        cur.execute(sql, (data_hora, peso, sistolica, diastolica, pulsacao))
        conn.commit()

        messagebox.showinfo(title="Informação Cadastro", message="Dados cadastrados com Sucesso!")
        conn.close()
        print("Fechando conexão com o banco!")

def click_sair():
    print("CLICOU VOLTAR!")
    print("Fechando conexão com o banco!")
    conn.close()
    janela.destroy()
#---------------------------------------------------------------------------- 

# --- Frames ---
ladoEsquerdo = Frame(janela, width=300, height=400, bg="#50D99E", relief="raise")
ladoDireito = Frame(janela, width=497, height=400, bg="#64F0DA", relief="raise")
# --- Imagem Logo ---
logoLabel = Label(ladoEsquerdo, image=logo, bg="#50D99E")
# --- peso ---
pesoLabel = Label(ladoDireito, text="Peso:", font=("Indie Flower", 20), bg="#64F0DA", fg="white")
pesoEntry = ttk.Entry(ladoDireito, width=20)
# --- pas ---
pasLabel = Label(ladoDireito, text="Pressão Arterial Sistólica:", font=("Indie Flower", 20), bg="#64F0DA", fg="white")
pasEntry = ttk.Entry(ladoDireito, width=20)
# --- pad ---
padLabel = Label(ladoDireito, text="Pressão Arterial Diastólica:", font=("Indie Flower", 20), bg="#64F0DA", fg="white")
padEntry = ttk.Entry(ladoDireito, width=20)
# --- pulsacao ---
pulsacaoLabel = Label(ladoDireito, text="Pulsação:", font=("Indie Flower", 20), bg="#64F0DA", fg="white")
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
sairButton.place(x=100, y=320, height=30)
cadastrarButton.place(x=300, y=320, height=30)

# ---------- Tamanho da janela ----------
# --- widgth x heigth + left + topo ---
janela.geometry("800x400+250+180")
janela.mainloop()