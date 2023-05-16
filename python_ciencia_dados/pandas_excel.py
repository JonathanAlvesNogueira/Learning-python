import pandas as pd


### lendo arquivo
arq = pd.read_excel('C:\\Users\\joth1\\Desktop\\python\\Aprendendo-python\\python_ciencia_dados\\dadospandas.xlsx')
arq1 = pd.read_excel('C:\\Users\\joth1\\Desktop\\python\\Aprendendo-python\\python_ciencia_dados\\dadospandas copy.xlsx')
arq2 = pd.read_excel('C:\\Users\\joth1\\Desktop\\python\\Aprendendo-python\\python_ciencia_dados\\dadospandas copy 2.xlsx')

# juntando arquivos 
arq_final= pd.concat([arq,arq1,arq2])

print(arq_final.head(30))

### verificando tipo de dados
print('tipos de dados ')
print(arq_final.dtypes)

# verificando itens aleatorios 
print('tipo sample')
print(arq_final.sample(10))

### Criando nova coluna
arq_final['receita'] = arq_final[' cep'] + 10
print(arq_final.columns)
print(arq_final)

### Retornando valor maximo da cep + 10
print(arq_final['receita'].max())

# pegando o minimo 
print(arq_final[' cep'].min())


###Pegando as linhas com maior receitas
print('maiores receitas')
print(arq_final.nlargest(5, 'receita'))

# pegando menos receitas
print('menores receitas:')
print(arq_final.nsmallest(3, 'receita'))