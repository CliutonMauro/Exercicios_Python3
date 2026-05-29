import random as rd
aluno = str(input('Digite o nome do aluno: '))
aluno2 = str(input('Digite o nome do aluno: '))
aluno3 = str(input('Digite o nome do aluno: '))
aluno4 = str(input('Digite o nome do aluno: '))

aluno_escolhido = rd.choice([aluno, aluno2, aluno3, aluno4])
print(f"O aluno escolhido é: {aluno_escolhido}")