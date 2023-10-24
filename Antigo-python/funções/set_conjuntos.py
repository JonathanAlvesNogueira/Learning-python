set1 = set() ### set sem dados

set2 ={'nome', 1,2,33,4.5}
print(type(set2))

### Set remove valor duplicado, set nao garante ordem
set3 ={1,2,3,1,2,3,1,2,3}
print(set3)

set3.add(10)
set3.add(11)
print(set3)
### aryaliz, usamos tuplas, para enviar a string completa
set3.update(('ola mundo', 'jonathan'))
print(set3)
### Funciona como pop
set3.discard('ola mundo')
print(set3)


set3.clear()
print(set3)