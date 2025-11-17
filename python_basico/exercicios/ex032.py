print('{:=^26}'.format('DESAFIO 32'))
ano = int(input('Digite um ano: '))
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print('\033[32m{}\033[m é um ano \033[31mbissexto\033[m!'.format(ano))
else:
    print('\033[32m{}\033[m não é um ano \033[31mbissexto\033[m!'.format(ano))
