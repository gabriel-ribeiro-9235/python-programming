print('{:=^26}'.format('DESAFIO 49'))
n = int(input('Digite um número: '))
print('_' * 20)
print('TABUADA DO {}:'.format(n))
for c in range(1, 11):
    print('{} x {:<2} = {}'.format(n, c, c*n))
print('_' * 20)
