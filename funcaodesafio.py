def imparpar(numero):
    if(numero % 2 == 0):
        print(' par')
    else:
        print('é impar')

def multiplicaNums(*args):
    total = 1
    for numeros in args:
        total *= numeros
   
multiplicaNums(1,2,3,4,5,6)
print('fim programa')