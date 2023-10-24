### 6.	Receba os valores em x e y. Efetua a troca de seus valores e mostre seus conteúdos.
try: 
    x = int(input("Digite o primeiro número: "))
    y = int(input("Digite o segundo número: "))
except:
    print("Informe um numero. ERRO")
aux = x
x = y
y = aux
print("Essa é a troca dos valores: \n valor A: " + str(x) +  "\n  Valor B: " + str(y))
