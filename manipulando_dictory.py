pessoa = {}

## cria chaves 
chave = 'nome'
sobrenome = 'nogueira'

## Cria valor para chave
pessoa[chave] = 'Jonathan'
pessoa[sobrenome] = 'nogueira'
##Imprime nogueira
print(pessoa[sobrenome])
##deleta chave valor
del pessoa[sobrenome]

if pessoa.get('nome') is not None:
    print('pessoa existe')
    pessoa1 = pessoa['nome']
    print(f'essa é a pessoa {pessoa1}' )
else:
    print('pessoa nao existe')
    

##Imprime pessoa restantes
print(pessoa)