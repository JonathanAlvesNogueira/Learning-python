"""
21.	Receba 4 notas bimestrais de um aluno. Calcule e mostre a média aritmética. Mostre a mensagem de acordo com a média:
a.	Se a média for >= 6,0 exibir “APROVADO”;
b.	Se a média for >= 3,0 ou < 6,0 exibir “EXAME”;
c.	Se a média for < 3,0 exibir “RETIDO”.
"""

lista_notas = [0,1,2,3,4,5,6,7,8,9,10]


try:
    nota = float(input("Informe a nota do aluno: "))
except:
    print("Informe um número")

if nota in lista_notas:
    if(nota >= 6.0):
        print("APROVADO")
    elif(nota<3.0):
        print("Retido")
    else:
        print("Exame")
else:
    print("Nota invalida")

print("Fim da execução")