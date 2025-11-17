print('{:=^26}'.format('DESAFIO 06'))
n = float(input('Digite um número: '))
if int(n) == n:
    n = int(n)
print('O dobro do número \033[32m{}\033[m é \033[32m{}\033[m, o triplo é \033[32m{}\033[m'.format(n, n*2, n*3), end=' ')
print('e a raiz quadrada é \033[32m{:.2f}\033[m'.format(n**(1/2)))
