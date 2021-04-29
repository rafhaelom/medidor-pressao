# -*- coding: utf-8 -*-
"""
@author: Rafhael Martins
"""

import psycopg2
cur = None
class Connect():
    global cur
    
    def __init__(self):
        #Conexão com o banco de dados
        self.DB_HOST = "localhost"
        self.DB_USER = "username"
        self.DB_PASS = "password"
        self.DB_NAME = "postgres"
        
        # Tratamento de exceções(erros)
        try:
            conn = psycopg2.connect(host=self.DB_HOST, database=self.DB_NAME, user=self.DB_USER, password=self.DB_PASS)
            self.cur = conn.cursor
            print("Conectado!\n")
        except (psycopg2.Error) as e:
            print("\nFalha de conexão!\n {}".format(e))

teste = Connect()