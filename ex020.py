import random as rd

aluno = str(input('Digite o nome do aluno: '))
aluno2 = str(input('Digite o nome do aluno: '))
aluno3 = str(input('Digite o nome do aluno: '))
aluno4 = str(input('Digite o nome do aluno: '))

lista_random = rd.shuffle([aluno, aluno2, aluno3, aluno4])
print(f"A ordem de apresentação será: {lista_random}")