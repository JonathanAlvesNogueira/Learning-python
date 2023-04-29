numero_1 = input("Digite o primeir numero")
numero_2 = input("Digite o Segundo numero")

operador = input("Digite um operador: + - * /")
resultado = 0

while(True):
    try:
        numero_1 = int(numero_1)
        numero_2 = int(numero_2)
        if len(operador) > 1:
            print("Você digitou mais que um numero, Informe novamente")
            
    except:
        print("Houve um erro na digitação do numero, tente informar numeros inteiros")

    if(operador == '+'):
        resultado = numero_1 + numero_2
    elif(operador == '-'):
        resultado = numero_1 - numero_2
    elif(operador == '*'):
        resultado = numero_1 * numero_2
    elif(operador == '/'):
        resultado = numero_1 / numero_2
    else:
        print("operador não existe")


    print(f'Esse aqui é o valor da operação {resultado}' )
    break
print("Fim execução")