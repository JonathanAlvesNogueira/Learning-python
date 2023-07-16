### Cria uma lista com  a string sendo a saida ['p', 'y', 't', 'h', 'o', 'n'] poi string é um elemento iteravel 
letras = list("Python")
print(letras)

### Cria uma lista de 10 elementos sendo [0,1,2,3,4,5,6,7,8,9]
numeros = list(range(10))
print(numeros)

### FATIAMENTO DE STRINGS 

### pega 2 primeiras letras , lembrando que sempre sera o indice passado -1, exemplo pegará o indice [0,1]
print(letras[:2])
### pega restante das letras pegando o indice passado até o final 
print(letras[2:])

### PEGARÁ O INDICE [2,3]
print(letras[2:4])
### PUXA TODOS OS INDICES
print(f' puxando todos os indices da lista {letras[::]}')
### puxando todos os indices da lista ao contrario 
print(f'Ao contrario {letras[::-1]}')


