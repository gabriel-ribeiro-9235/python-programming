import random
print('{:=^26}'.format('DESAFIO 20'))
print('\033[97m_' * 15)
aluno1 = input('Insira um aluno: ')
aluno2 = input('Insira outro aluno: ')
aluno3 = input('Insira outro aluno: ')
aluno4 = input('Insira o último aluno: ')
lista = [aluno1, aluno2, aluno3, aluno4]
random.shuffle(lista)
print('_' * 15)
print('A ordem será:\n1º aluno: \033[31m{}\033[97m\n2º aluno: \033[31m{}\033[97m\n3º aluno: \033[31m{}\033[97m\n4º aluno: \033[31m{}\033[97m'.format(lista[0], lista[1], lista[2], lista[3]))
