#%% Importando Bibliotecas
import pandas as pd
import psycopg2 as pg

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
# %% Analise Exploratória
df.head(5)
# %%
df.tail()
# %%
