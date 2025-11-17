from time import sleep
print('{:=^26}'.format('DESAFIO 47'))
print('PARES ENTRE 1 E 50:')
for c in range(1, 50):
    if c % 2 == 0:
        if c == 30:
            print('\n{},'.format(c), end=' ')
        elif c == 46:
            print('{} e'.format(c), end=' ')
        elif c == 48:
            print('{}.'.format(c))
        else:
            print('{},'.format(c), end=' ')
    sleep(0.1)
