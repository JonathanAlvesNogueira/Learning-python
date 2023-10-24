### 32.	Receba um número inteiro. Calcule e mostre o seu fatorial.

try:
    num = int(input("Informe um numero "))
except:
    print("Informe um numero, não um caracter")
fat = 1
for i in range(num, 1, -1):
    fat = fat * i
print("Esse é o fatorial " + str(fat))
print("Fim execução")