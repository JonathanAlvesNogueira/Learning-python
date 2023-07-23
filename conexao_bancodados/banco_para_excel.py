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

cursor.close()
conexao.close()