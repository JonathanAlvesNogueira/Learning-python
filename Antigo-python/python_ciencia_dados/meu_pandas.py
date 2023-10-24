import pandas as pd

### le o arquio
arq = pd.read_excel('C:/Users/joth1/Desktop/python/python_ciencia_dados/dadospandas.xlsx')
### Mostrando uma linha do excel
print(arq.head(1))

### imprime as colunas 
print(arq.columns)

### nomeia a coluna 
renomear = arq.rename(columns={'nome': 'name'})

### Entrega o numero de colunas e linhas. Sem parenteses 
print(arq.shape)

##Retorna os tipos de dados de cada coluna
print(arq.dtypes)


### retorna as ultimas linhas
print(arq.tail(1))

### usando describe 
print()
print(arq.describe)


### Usando uniques - RETORNA APENAS OS VALORES UNICOS DA COLUNA 'NOME'
print('Começo do unique')
print(arq['nome'].unique)


###Colocando numa variavel a linha - USANDO LOC
jonathan_variavel = arq.loc[arq['nome'] == 'jobathan']
print('Usando LOC')
print(jonathan_variavel)