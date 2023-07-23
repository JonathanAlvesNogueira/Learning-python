import pandas as pd

# Substitua 'dados.xlsx' pelo caminho completo do seu arquivo Excel, usando barras invertidas.
caminho_arquivo = ('C:/Users/joth1/Documents/arquivo_excel.xlsx')


# Substituir as barras invertidas por barras normais
caminho_arquivo = caminho_arquivo.replace("\\", "/")

# Carregar o arquivo Excel em um DataFrame
df = pd.read_excel(caminho_arquivo)
# print(df.head(3))

df = df.rename(columns={'nome': 'names', 'Ano':'Years'})
# Exibir as 5 primeiras linhas do DataFrame
print(df.head(5))


# exibe as linhas e colunas
print('Essa é a quantidade de linhas e colunas ');print('__________________________')
print(df.shape)

print('Essa é o nome das colunas ')
print(df.columns);print('______________________________')

print('tipos de dados ')
print(df.dtypes); print('_____________________________________')

#puxa as 3 ultimos registros/linhas 
print(df.tail(3)); print('______________')

# traz a media da coluna, uma contagem das linhas, desvio padrao, valor minimo, traz os quartis(25%, 50%, 75%, 100%) eo valor maximo 
print(df.describe()); print('_____________')

# puxa as linhas da coluna nome, e o unique especifica que so quer os registros unicos, se tiver 2 jonathan trara so um
print(df['Nome'].unique())
