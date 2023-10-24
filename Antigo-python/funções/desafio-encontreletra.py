i = 0
nome = 'joth10'
palavra_secreta = '******'
secreto = palavra_secreta.count('*')
while  secreto != 0:
    letra = input('digite a letra')
    if(len(letra) > 1):
        break
    if(nome.count(letra)):
        
        while i < len(nome):
            if nome[i] == letra:
                i = i + 1
                palavra_secreta[i] = nome[i]
            else:
                continue
    print(nome)
    print(palavra_secreta)
print('fim da execução')