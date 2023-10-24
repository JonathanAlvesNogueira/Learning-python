### 1.	Coletar o valor do lado de um quadrado, calcular sua área e apresentar o resultado.


try:
    quadrado = int(input("Digite um numero: "))
except:
    print("Erro não foi digitado um numero")

area = quadrado**2
print("Essa é a area: " + str(area))