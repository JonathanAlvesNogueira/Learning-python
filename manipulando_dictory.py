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



##Imprime pessoa restantes
print(pessoa)