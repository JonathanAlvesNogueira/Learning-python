### 4.	Receba a temperatura em graus Celsius. Calcule e mostre a sua temperatura convertida em fahrenheit F = (9*C+160) /5.
try:
    temp_celsius = int(input("Digite o grau celsius: "))
except:
    print("Numero invalido, digite um número")
temp_fahre = ((9 * temp_celsius + 160)/5)
print("Essa é a temperatura convertida: " + str(temp_fahre))