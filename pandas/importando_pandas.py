import pandas as pd

# Substitua 'dados.xlsx' pelo caminho completo do seu arquivo Excel, usando barras invertidas.
caminho_arquivo = ('C:\\Users\\joth1\\Downloads\\dados.xlsx')  # Usando barras invertidas

# Substituir as barras invertidas por barras normais
caminho_arquivo = caminho_arquivo.replace("\\", "/")

# Carregar o arquivo Excel em um DataFrame
df = pd.read_excel(caminho_arquivo)
# print(df.head(3))

df = df.rename(columns={'nome': 'names', 'Ano':'Years'})
# Exibir as 5 primeiras linhas do DataFrame
print(df.head(5))