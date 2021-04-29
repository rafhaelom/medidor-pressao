# -*- coding: utf-8 -*-
"""
@author: Rafhael Martins
"""
# ---------- Bibliotecas ----------
from tkinter import *
from tkinter import messagebox # messagebox é a biblioteca de mensagem do tkinter.
from tkinter import ttk # ttk é a biblioteca gráfica do tkinter.
from datetime import datetime
from conexao import Connect

class Medidor():
    def __init__(self, master):
        janela.resizable(width=False, height=False) # Tira a responsividade da janela.
        janela.attributes("-alpha", 0.97) # Transparencia da janela.
        janela.iconbitmap(default="icon/logo.ico")

        # --- Carregando imagens ---
        self.logo = PhotoImage(file="icon/logotipo.png")

        # ---------- Widgets - componentes da janela ----------
        # --- Frames ---
        ladoEsquerdo = Frame(janela, width=300, height=400, bg="#50D99E", relief="raise")
        ladoDireito = Frame(janela, width=497, height=400, bg="#64F0DA", relief="raise")
        # --- Imagem Logo ---
        logoLabel = Label(ladoEsquerdo, image=logo, bg="#50D99E")
        
        pesoLabel = Label(ladoDireito, text="Peso:", font=("Indie Flower", 20), bg="#64F0DA", fg="white")
        pesoEntry = ttk.Entry(ladoDireito, width=20)
        pasLabel = Label(ladoDireito, text="Pressão Arterial Sistólica:", font=("Indie Flower", 20), bg="#64F0DA", fg="white")
        pasEntry = ttk.Entry(ladoDireito, width=20)
        padLabel = Label(ladoDireito, text="Pressão Arterial Diastólica:", font=("Indie Flower", 20), bg="#64F0DA", fg="white")
        padEntry = ttk.Entry(ladoDireito, width=20)
        pulsacaoLabel = Label(ladoDireito, text="Pulsação:", font=("Indie Flower", 20), bg="#64F0DA", fg="white")
        pulsacaoEntry = ttk.Entry(ladoDireito, width=20) 
        sairButton = ttk.Button(ladoDireito, text="Sair", width=20, command=click_sair)
        cadastrarButton = ttk.Button(ladoDireito, text="Cadastrar", width=20, command=click_cadastrar)

        # ---------- Layout - Gereciador de componetes da janela ----------
        # ----- Inseri Componentes -----
        # --- frames ---
        ladoEsquerdo.pack(side=LEFT)
        ladoDireito.pack(side=RIGHT)
        # --- imagem logo ---
        logoLabel.place(x=18, y=30)

        pesoLabel.place(x=18, y=20)
        pesoEntry.place(x=100, y=26, height=30)
        pasLabel.place(x=18, y=89)
        pasEntry.place(x=350, y=95, height=30)
        padLabel.place(x=18, y=158)
        padEntry.place(x=355, y=164, height=30)
        pulsacaoLabel.place(x=18, y=227)
        pulsacaoEntry.place(x=150, y=233, height=30)
        sairButton.place(x=100, y=320, height=30)
        cadastrarButton.place(x=300, y=320, height=30)
        
    def query(self):
        conn = Connect()
        q = conn.cur()
        q.execute('SELECT *FROM medida;')
        return q.fetchall()
 
    # -------------------------- Funcoes para eventos - events ---------------------
    def click_cadastrar(self):
        conn = Connect()
        q = conn.cur()
        print("CLICOU CADASTRAR!")
        data_hora = datetime.now()
        peso = self.pesoEntry.get()
        sistolica = self.pasEntry.get()
        diastolica = self.padEntry.get()
        pulsacao = self.pulsacaoEntry.get()

        if (peso == "" and sistolica == "" and diastolica == "" and pulsacao == "" or peso == "" and sistolica == "" or diastolica == "" and pulsacao == ""or peso == "" or sistolica == "" or diastolica == "" or pulsacao == ""):
                messagebox.showerror(title="Cadastro Erro", message="Campo(s) vazio(s). Preencha todos os campos!")
        else:
            # Inserção no banco de dados
            sql = "INSERT INTO medida VALUES (%s, %s, %s, %s, %s)"
            q.execute(sql, (data_hora, peso, sistolica, diastolica, pulsacao))
            q.commit()

            messagebox.showinfo(title="Informação Cadastro", message="Dados cadastrados com Sucesso!")
            conn.close()
            print("Fechando conexão com o banco!")

    def click_sair(self):
        conn = Connect()
        q = conn.cur()
        print("CLICOU VOLTAR!")
        print("Fechando conexão com o banco!")
        q.close()
        janela.destroy()
        

       
    

# ---------- Objeto da janela principal ----------
janela = Tk()
# --- Atributos ---
janela.title("Medição e monitoramento") # Título da janela.
janela.configure(bg="white") # Cor do backgroud da janela.
# ---------- Tamanho da janela ----------
# --- widgth x heigth + left + topo ---
janela.geometry("800x400+250+180")
janela.mainloop()

medidor = Medidor()