#%% Importando Bibliotecas
import pandas as pd
import psycopg2 as pg
import matplotlib.pyplot as plt

#%% Conexão com o banco de dados
DB_HOST = "localhost"
DB_USER = "username"
DB_PASS = "password"
DB_NAME = "medidor"

TB_NAME = "medida"

conn = pg.connect(host=DB_HOST, database=DB_NAME, user=DB_USER, password=DB_PASS)
cur = conn.cursor()

#%% Consultando Banco de dados
df = pd.read_sql_query("SELECT * FROM {}".format(TB_NAME), con=conn)
df.info()

# %% Analise Exploratória
# Primeiros dados
print(df.head())

# %% Ultimos dados
print(df.tail())

#%% Criando colunas com dados de data_reg separados
df['ano']= df['data_reg'].dt.year
df['mes']= df['data_reg'].dt.month
df['dia']= df['data_reg'].dt.day
df['hora']= df['data_reg'].dt.time

print(df.head())

#%%
fig, ax = plt.subplots()
ax.plot(df["dia"], df["pulsacao"])

#%%
plt.plot(df["dia"], df["peso"])