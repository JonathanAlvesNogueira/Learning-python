import pandas as pd
import os 
import time 
import mysql.connector as conexao

conexao1  = conexao.connect(
    host="localhost",
    user="root",
    password="sua_senha",
    database="exemplo"
)

cursor = conexao1.cursor()

use_banco = "USE EXEMPLO"
cursor.execute(use_banco)

selecao_dados = "SELECT * FROM PRODUTO"
cursor.execute(selecao_dados)
resultado = cursor.fetchall()

for linha in resultado:
    print(linha)

cursor.close()
conexao1.close()