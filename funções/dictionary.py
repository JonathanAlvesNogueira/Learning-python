
### dictionary


pessoa = {
    'nome' : 'jonathan',
    'preco' : 1000,
    'objetivo' : 'desenvolvedor',
    'enderecos' : [
        {'rua': 'rua falcao gomes', 'numero': 'casa 7'},
        {'rua' : 'rua pedro albraves', 'numero' : 'casa 19'},        
    ],
}

for chave in pessoa:
    print(f'essa é a chave {chave} e essa é o valor {pessoa[chave]}' )



print(pessoa)