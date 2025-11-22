print('{:=^26}'.format('DESAFIO 50'))
s = 0
print('Digite 6 valores inteiros')
for c in range(1, 7):
    n = int(input('{}º valor: '.format(c)))
    if n % 2 == 0:
        s += n
print('A soma dos valores pares vale \033[32m{}\033[m'.format(s))
