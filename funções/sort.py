lista = [
    {'nome' : 'jonathan', 'mapa' : 'sao Paulo'},
    {'nome' : 'ana', 'mapa' : 'sao pedro'},
    {'nome' : 'kailany', 'mapa' : 'sao paulo'},
]
print(lista)


def ordena(item):
    return item['nome']

lista.sort(key=ordena)

print()

for item in lista:
    print(item)

### lambda
lista2 = [
    {'nome' : 'jonathan', 'mapa' : 'sao Paulo'},
    {'nome' : 'ana', 'mapa' : 'rio'},
    {'nome' : 'kailany', 'mapa' : 'acre'},
]
lista2.sort(key=lambda item : item['nome'])
print()
print()
print(lista2)

### oui podemos usar sorted assim ó 
li = sorted(lista2, key=lambda item: item['mapa'])
li2 = sorted(lista2, key=lambda item : item['nome'] )
