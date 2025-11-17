print('{:=^26}'.format('DESAFIO 07'))
print('\033[34m{:-^26}'.format(''), '\033[m')
nome = input('\033[36mDigite o nome do aluno: ')
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: \033[m'))
media = (n1 + n2) / 2
print('\033[34m{:-^26}'.format(''), '\033[m')
if media >= 6:
    print('A média do aluno \033[1m{}\033[m foi \033[32m{:.2f}\033[m'.format(nome, media))
else:
    print('A média do aluno \033[1m{} foi \033[31m{:.2f}\033[m'.format(nome, media))
