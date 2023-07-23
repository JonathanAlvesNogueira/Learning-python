import mysql.connector

# Conectar ao servidor MySQL
conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="sua_senha",
    database="exemplo"
)

# Criar um objeto cursor para executar comandos SQL
cursor = conexao.cursor()

# Criar o banco de dados (caso ainda não exista)
# cursor.execute("CREATE DATABASE IF NOT EXISTS nome_do_banco_de_dados")

# Usar o banco de dados
cursor.execute("USE exemplo")

# Criar a tabela (caso ainda não exista)
# cursor.execute("""
#     CREATE TABLE IF NOT EXISTS nome_da_tabela (
#         id INT AUTO_INCREMENT PRIMARY KEY,
#         nome VARCHAR(255),
#         idade INT
#     )
# """)

# Inserir dados na tabela
dados = [
    ("João", 30.0),
    ("Maria", 25.0),
    ("Carlos", 40.0)
]

sql = "INSERT INTO produto (nome, preco) VALUES (%s, %s)"
cursor.executemany(sql, dados)

# Comitar as alterações
conexao.commit()

# Fechar o cursor e a conexão
cursor.close()
conexao.close()
print('inserido com sucesso')