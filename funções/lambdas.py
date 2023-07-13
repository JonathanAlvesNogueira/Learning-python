lista = [31,19,11,8,6,1]
print(lista.sort())

lista2 = [
    {'nome' : 'jonathan', 'sobrenome' : 'alves'},
    {'nome' : 'alex', 'sobrenome': 'cleber'},
    {'nome' : 'douglas', 'sobrenome' : 'teves'}
]
print(lista2)

print()


def ordena(item):
    return item['nome']

lista2.sort(key=ordena)
print(lista2)