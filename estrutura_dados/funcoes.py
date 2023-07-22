def imprimir_nome(nome):
    print(nome); print('____________________________')

def imprimir_parametro(x,y):
    print(f'x={x}  y={y}')

imprimir_nome(nome='jonathan')
# Trocando parametros dentro da chamada da função 
imprimir_parametro(y=1, x=2); print('__________________________________')

#imprime a soma da lista FUNÇÃO SUM
def calcular_tudo(listaa):
    return sum(listaa)

listaa = [1,2,3]
print(f' esse é o valor da soma da lista: {calcular_tudo(listaa)}'); print('________________________')


# Retorno de 2 variaveis em python
def retorno(num):
    somado = num + 1
    subtraido = num - 1 
    return somado, subtraido

print(retorno(10)); print('________________________________')

# bloqueia que seja passados valores sem usar chave valor 
def valores(*, nome, idade, ano):
    return f'Informações do usuario: {nome}, {idade}, {ano}'
print(valores(nome= 'Jonathan', idade=19, ano=2003)); print('________________________')
# print(valores('jonathan', 19, 2003)) INVALIDO


# PASSANDO FUNÇÃO COMO PARAMETRO
def soma(a, b):
    return a + b

def imprime_resultado(a,b, funcao):
    resultado = funcao(a,b)
    return(f'Esse é o resultado de {a} + {b} = {resultado}')

print(imprime_resultado(1,2,soma)); print('________________________________')


# Usando GLOBAL para referenciar uma variavel global
salario = 1000
lista = [1]
def variavel_global(valor):
    global salario
    global lista
    # usa method copy para não copiar o endereço de memória 
    lista2 = lista.copy()
    novo_salario = salario + 500
    lista2.append(novo_salario)
    return novo_salario, lista2

print(variavel_global(500))