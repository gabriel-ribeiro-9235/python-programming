print('{:=^26}'.format('DESAFIO 08'))
n = float(input('Digite uma distância em metros: '))
if int(n) == n:
    n = int(n)
print('\033[32m{}\033[m m = \033[32m{}\033[m cm\n\033[32m{}\033[m m = \033[32m{}\033[m mm'.format(n, n*100, n, n*1000))
