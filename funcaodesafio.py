def imparpar(numero):
    if(numero % 2 == 0):
        return print(' par')
    else:
       return print('é impar')

def multiplicaNums(*args):
    total = 1
    for numeros in args:
        total *= numeros
    return total
   
variavel = multiplicaNums(1,2,3,4,5)
epar = imparpar(variavel)
print(epar)
print(variavel)

print('fim programa')