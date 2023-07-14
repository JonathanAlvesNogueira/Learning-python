#### 2.	Receba o salário de um funcionário e mostre o novo salário com reajuste de 15%.
try:
    salario = float(input("Digite um numero"))
except:
    print("Digite um numero")

novo_salario = salario + (salario*0.15)
print("Esse é o salario do funcionário com reajuste: " + str(novo_salario))