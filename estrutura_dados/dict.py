### FORMA UM DE DECLARAR UM DICT 
pessoa = {
    'nome' : 'jonathan', 
    'idade' : 19
}
print( f'forma 1 de declarar  {pessoa}'); print()

### FORMA 2 DE DECLARAR UM DICT 
pessoa2 = dict(nome='jonathan', idade=19)
print(f'forma 2 de declarar : {pessoa2}'); print()

pessoa['cidade'] = 'São Paulo'
print(f' ADICIONANDO MAIS UM ELEMENTO CHAVE-VALOR {pessoa}') ; print()


### puxando valor do dict 
print('informações usuarios: ')
print(pessoa['nome'])
print(pessoa['idade'])
print(pessoa['cidade']); print()

### Atualizando registros 
pessoa['nome'] = 'Ana'
pessoa['idade'] = 28
pessoa['cidade'] = 'Rio de Janeiro'
print(f'pessoa atualizada {pessoa }'); print('////////////////////////////////////////////////////////////////////////////')


### DICTONARY ANINHADO 
print('DICTIONARY ANINHADO')
person = {
    'jonathan@gmail.com' : {'nome' : 'jonathan', 'idade': 19 },
    'aninha@gmail.com' : {'nome' : 'ana' , 'idade' : 21},
    'agata@gmail.com' : {'nome' : 'agata', 'idade' : 24}
}
# imprime chave valor COM O COMANDO ITEMS 
for chave, valor in person.items():
    print(chave, valor)
print('////////////////////////////////////////////////////////////////////////'); print()
