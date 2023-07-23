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


# exibe as linhas e colunas
print('Essa é a quantidade de linhas e colunas ');print('__________________________')
print(df.shape)

print('Essa é o nome das colunas ')
print(df.columns);print('______________________________')

print('tipos de dados ')
print(df.dtypes)


### Escrevendo no arquivo excel

nomes = []
idades = []
cidades = []

nome = input('Digite um nome')
idade = int(input('Digite uma idade'))
cidade = input('Digite uma cidade')

# PARA ADICIONAR O DATAFRAME PRECISA SER UMA LISTA 
nomes.append(nome)
idades.append(idade)
cidades.append(cidade)


dados = {
    'nome' : nomes,
    'idade' : idades,
    'cidade' : cidades
}
# Criar um DataFrame com os dados
df2 = pd.DataFrame(dados)
# Escrever o DataFrame no arquivo Excel
rota = "C:/Users/joth1/Documents/arquivo_excel.xlsx"
df2.to_excel(rota, index=False)

