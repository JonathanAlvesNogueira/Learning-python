# importa pandas para o excel, importa os para abrir o excel, importa time para cronometrar e importa o mysql
import pandas as pd
import os 
import time 
import mysql.connector as conexao

# cria conexao com o banco de dados 
conexao1  = conexao.connect(
    host="localhost",
    user="root",
    password="sua_senha",
    database="exemplo"
)
# cria o cursor 
cursor = conexao1.cursor()

# seleciona DB
use_banco = "USE EXEMPLO"
cursor.execute(use_banco)

# seleciona os itens 
selecao_dados = "SELECT * FROM PRODUTO"
cursor.execute(selecao_dados)
resultado = cursor.fetchall()

# imprime todas as linhas 
for linha in resultado:
    print(linha)

# fecha conexões 
cursor.close()
conexao1.close()