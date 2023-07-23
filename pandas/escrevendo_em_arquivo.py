#importa pandas
import pandas as pd 

#Especifica o caminho 
rota = "C:/Users/joth1/Documents/arquivo_excel.xlsx"

# Verificar se o arquivo Excel já existe
try:
    # Ler o arquivo Excel em um DataFrame
    df = pd.read_excel(rota)
except Exception:
    # Se o arquivo não existir, crie um DataFrame vazio
    df = pd.DataFrame()

# Exibir os dados atuais
print("Dados atuais:")
print(df)

nomes = []
idades = []
cidades = []

while(True):
    continua = input('Quer continuar digite qualquer tecla, quer sair digite 9')
    if(continua != 9 ):
        nome = input('digite um nome')
        idade = input('digite um idade')
        cidade = input('digite uma cidade')
        nomes.append(nome)
        idades.append(idade)
        cidades.append(cidade)

novos_dados = {
    "Nome" : nomes,
    "Idade" : idade,
    "Cidades" : cidade

}
