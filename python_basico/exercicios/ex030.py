print('{:=^26}'.format('DESAFIO 30'))
n = int(input('Digite um número: '))
print('\033[32m{}\033[m é'.format(n), '\033[35mPAR\033[m!' if n%2==0 else '\033[35mÍMPAR\033[m!')
