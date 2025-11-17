print('{:=^26}'.format('DESAFIO 53'))
print('TESTE DE PRIMOS')
n = int(input('Digite um número inteiro: '))
print('_' * 30)
s = 0
k = 0
if n == 1:
    print('1 NÃO É PRIMO!')
    exit()
for c in range(1, n + 1):
    if n % c == 0:
        k += 1
        s += c
        if s == c:
            print('{} é divisível por {}'.format(n, c), end='')
        elif c != n:
            print(', por {}'.format(c), end='')
        else:
            print(' e por ele mesmo,')

if k == 2:
    print('então É PRIMO!'.format(n))
else:
    print('então NÃO É PRIMO!')
