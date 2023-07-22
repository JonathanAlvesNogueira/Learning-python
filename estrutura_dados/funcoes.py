def imprimir_nome(nome):
    print(nome)

def imprimir_parametro(x,y):
    print(f'x={x}  y={y}')

imprimir_nome(nome='jonathan')
# Trocando parametros dentro da chamada da função 
imprimir_parametro(y=1, x=2); print()

#imprime a soma da lista FUNÇÃO SUM
def calcular_tudo(listaa):
    return sum(listaa)

listaa = [1,2,3]
print(f' esse é o valor da soma da lista: {calcular_tudo(listaa)}'); print()


# Retorno de 2 variaveis em python
def retorno(num):
    somado = num + 1
    subtraido = num - 1 
    return somado, subtraido

print(retorno(10)); print()

# bloqueia que seja passados valores sem usar chave valor 
def valores(*, nome, idade, ano):
    return f'Informações do usuario: {nome}, {idade}, {ano}'
print(valores(nome= 'Jonathan', idade=19, ano=2003))
# print(valores('jonathan', 19, 2003)) INVALIDO