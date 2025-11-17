print(f'{'DESAFIO 67':=^26}')
while True:
    print('_' * 43)
    n = int(input('Digite um número (negativo para sair): '))
    if n < 0:
        break
    print(f'TABUADA DO {n}')
    for c in range(1, 11):
        print(f'{n} x {c:<2} = {n * c}')
print('_' * 43, '\nFIM')
