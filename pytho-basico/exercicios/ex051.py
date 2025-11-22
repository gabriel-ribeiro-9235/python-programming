print('{:=^26}'.format('DESAFIO 51'))
print('Insira as informações da PA')
a1 = float(input('a1: '))
if a1 == int(a1):
    a1 = int(a1)
r = float(input('razão: '))
if r == int(r):
    r = int(r)
print('Os 10 primeiros termos de uma PA com primeiro termo {} e razão {} são:'.format(a1, r))
for c in range(1, 11):
    print('a{:<2} = {}'.format(c, a1+(c-1)*r))
