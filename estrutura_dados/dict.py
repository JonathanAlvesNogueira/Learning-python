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


