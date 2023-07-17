### Cria uma lista com  a string sendo a saida ['p', 'y', 't', 'h', 'o', 'n'] poi string é um elemento iteravel 
letras = list("Python")
print(letras); print()

### Cria uma lista de 10 elementos sendo [0,1,2,3,4,5,6,7,8,9]
numeros = list(range(10))
print(numeros); print()

### FATIAMENTO DE STRINGS 

### pega 2 primeiras letras , lembrando que sempre sera o indice passado -1, exemplo pegará o indice [0,1]
print(letras[:2]); print()
### pega restante das letras pegando o indice passado até o final 
print(letras[2:]); print()

### PEGARÁ O INDICE [2,3]
print(letras[2:4]); print()
### PUXA TODOS OS INDICES
print(f' puxando todos os indices da lista {letras[::]}')
### puxando todos os indices da lista ao contrario 
print(f'Ao contrario {letras[::-1]}'); print()




### REVENDO ENUMERATE 
for indice, objeto in enumerate(letras):
    print(f'indice: {indice}    Esse é o objeto: {objeto }'); print()

### FORMA DE COLOCAR ITENS EM UMA LISTA 
    numeros = [1,2,3,4,5,6,7,8,9]
    pares = []
    for numero in numeros:
        ### se for par 
        if(numero % 2 == 0):
            pares.append(numero)

print(pares ); print()


###  FORMA 2 DE COLOCAR ITENS EM UMA LISTA
impares = [ numero for numero in numeros if numero % 2 != 0]
print(impares )

### LIMPA A LISTA
print(impares.clear()); print()

### copia valor da lista sem pegar o endereço de memoria 
copia = pares.copy()
print(f'id da copia: {id(copia)} id do par: {id(pares)} SÃO DIFERENTES '); print()


### COUNT 
cores = ['vermelho', 'azul', 'verde', 'verde']
### RETORNA QUANTAS VEZE O ITEM APARECE NA LISTA 
quant = cores.count('verde')
print(f' quantidade de vezes que aparece a cor verde: {quant}'); print()

### EXTEND JUNTA LISTA 
lista1 = ['java', 'c']
lista2 = ['python', 'c']
lista1.extend(lista2)
print(f' LISTAS DEPOIS DE SEREM JUNTADAS COM EXTEND : {lista1}'); print()


### USANDO POP  ->    PILHA
pilha = [1,2,3,4]
print(f'elemento tirado {pilha.pop()}') # 4
print(f'elemento tirado {pilha.pop()}') # 3
print(f'elemento tirado {pilha.pop()}'); print()  # 2

### USANDO INDEX 
linguas = ['pt-br', 'us-en', 'arabe']
print(linguas.index('pt-br')); print() # retorna o indice 0


### Usando SORT

alfa = ["Jonathan", "Delfi", "Zebra", "Golf", "Zé", "Alfa "]
print(f' lista normal {alfa}')
alfa.sort()
### Organizando lista
print(f' lista organizada : {alfa}'); print()

### Lista reversa 
alfa.sort(reverse=True)
print(alfa); print()

alfa.sort(key=lambda x : len(x) )
print(f' Organizando por tamanho de letra {alfa}')