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