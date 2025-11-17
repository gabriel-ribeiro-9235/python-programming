import random
print('{:=^26}'.format('DESAFIO 19'))
aluno1 = input('\033[32mAluno 1: ')
aluno2 = input('Aluno 2: ')
aluno3 = input('Aluno 3: ')
aluno4 = input('Aluno 4: ')
print('\033[31m{}\033[m vai limpar o quadro!'.format(random.choice([aluno1, aluno2, aluno3, aluno4])))
