#%% Importando Bibliotecas
import pandas as pd
import numpy
from datetime import datetime
import psycopg2 as pg
import matplotlib.pyplot as plt

#%% Conexão com o banco de dados
DB_HOST = "localhost"
DB_USER = "postgres"
DB_PASS = "teste123"
DB_NAME = "medidor"

TB_NAME = "medida"

conn = pg.connect(host=DB_HOST, database=DB_NAME, user=DB_USER, password=DB_PASS)
cur = conn.cursor()

#%% Consultando Banco de dados
df = pd.read_sql_query("SELECT * FROM {}".format(TB_NAME), con=conn)
df.info()

#%% Analise Exploratória
# Primeiros dados
print(df.head())

#%% Ultimos dados
print(df.tail())

#%% Criando colunas com dados de data_reg separados
df['ano']= df['data_reg'].dt.year
df['mes']= df['data_reg'].dt.month
df['dia']= df['data_reg'].dt.day

#df['hora']= df['data_reg'].dt.time

print(df.head())

#%% formatando a data e hora
df['data'] = df.data_reg.apply(lambda x: x.strftime('%d/%m/%Y')) 
df['hora'] = df.data_reg.apply(lambda x: x.strftime('%H:%M'))
# %%
print(df)
# %% Obtendo dia da semana e periodo da hora se é AM ou PM
df['dia_semana'] = df.data_reg.apply(lambda x: x.strftime('%A')) 
df['periodo_hora'] = df.data_reg.apply(lambda x: x.strftime('%p'))
# %%
print(df)
# %%
df.peso.plot()
# %%
df.peso.hist()
# %%
