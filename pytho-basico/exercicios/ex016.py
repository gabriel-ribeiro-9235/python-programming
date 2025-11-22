from math import trunc
print('{:=^26}'.format('DESAFIO 16'))
n = float(input('\033[7;97mInsira um número: '))
print('\033[mA parte inteira de \033[32m{}\033[m vale \033[31m{}\033[m'.format(n, trunc(n)))
