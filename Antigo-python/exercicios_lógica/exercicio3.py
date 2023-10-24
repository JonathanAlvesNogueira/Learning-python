
### 3.	Receba a base e a altura de um triângulo. Calcule e mostre a sua área.
try:
    base = float(input("Digite a medida da base do triângulo: "))
    altura = float(input("Digite a medida da altura do triângulo: "))
except:
    print("Reveja os dados informados, algum foi digitado errado")

area = (base * altura) / 2

print("A área do triângulo é:", area)