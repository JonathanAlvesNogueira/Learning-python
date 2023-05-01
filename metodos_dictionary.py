### dictionary
pessoa = {
    'nome' : 'Jonathan',
    'sobrenome' : 'Nogueira',
}
### pega as chaves
print(pessoa.keys())

### pega values
print(pessoa.values())

### Usando items = pegar chave e valor
novaPessoa = pessoa.items()
print(novaPessoa)
for chave, valor in novaPessoa:
    print(chave, valor)

### setdefault = set chave e valor se a chave nao existir ou nao tiver um valor
pessoa.setdefault('idade', 100)
print(pessoa['idade'])

###copy - shallow copy
copia = {
    'name' : 'jonathan',
    'empresa': 'gerdau',
    'lista' : [0,1,2] 
}

copia2 = copia.copy()
print(copia)
print(copia2)


###Usando get
print(pessoa.get('valor', 'nao existe'))


### Pop
nome = pessoa.pop('nome')
print(nome)
