### 5.	Receba os coeficientes A, B e C de uma equação do 2º grau (AX²+BX+C=0). Calcule e mostre as raízes reais (considerar que a equação possue2 raízes).

import math

a = int(input("Digite o valor de A"))
b = int(input("Digite o valor de B"))
c = int(input("Digite o valor de C"))
delta = (b**2) - (4*a*c)
if (delta > 0):
    x1 = -(b) + math.sqrt(delta)/2*a
    x2 = -(b) - math.sqrt(delta)/2*a
else:
    print("Não existe 2 raizes, logo não deve ser desconsiderada")

print()