print('{:=^26}'.format('DESAFIO 35'))
print('\033[33m-=' * 13)
print('\033[34mAnalisador de triângulos')
print('\033[33m-=' * 13, '\033[m')
l1 = float(input('Tamanho do lado 1: '))
l2 = float(input('Tamanho do lado 2: '))
l3 = float(input('Tamanho do lado 3: '))
print('_' * 26)
if int(l1) == float(l1):
    l1 = int(l1)
if int(l2) == float(l2):
    l2 = int(l2)
if int(l3) == float(l3):
    l3 = int(l3)
if l1 + l2 > l3 and l1 + l3 > l2 and l2 + l3 > l1:
    print('\033[32mEXISTE\033[m o triângulo com lados \033[36m{}\033[m, \033[36m{}\033[m, \033[36m{}\033[m!'.format(l1, l2, l3))
else:
    print('\033[31mNÃO EXISTE\033[m o triângulo com lados \033[36m{}\033[m, \033[36m{}\033[m, \033[36m{}\033[m!'.format(l1, l2, l3))
