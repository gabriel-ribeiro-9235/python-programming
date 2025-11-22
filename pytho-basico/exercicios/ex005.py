print('{:=^26}'.format('DESAFIO 05'))
n = int(input('\033[97mDigite um númreo: '))
print('O sucessor de \033[1m{}\033[0;97m é \033[1;33m{}\033[0;97m e o antecessor é \033[1;35m{}\033[0;97m.'.format(n, n+1, n-1), '\033[m')
