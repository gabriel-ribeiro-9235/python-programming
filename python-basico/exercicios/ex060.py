print('{:=^26}'.format('DESAFIO 60'))
print('Calculadora de fatorial')
print('_' * 26)
n = int(input('Insira o número: '))
q = n
k = 1
if n == 0:
    print('0! = 1')
else:
    while k < q:
        n *= k
        k += + 1
    print(f'{q}! = {n}')

'''n = int(input('Insira o número: '))
f = 1
print(f'{n}! = ', end='')
if n == 0 or n == 1:
    print('1')
else:
    for c in range(n, 0, -1):
        print(f'{c} x ' if c > 1 else f'{c} =', end='')
        f *= c
    print(f' {f}')'''
