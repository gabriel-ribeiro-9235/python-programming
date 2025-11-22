print('{:=^26}'.format('DESAFIO 61'))
n = float(input('a1 = '))
if n == int(n):
    n = int(n)
r = float(input('r = '))
if r == int(r):
    r = int(r)
c = 1
termo = n
print('_______________________________________')
print(f'Os primeiros 10 termos de uma PA com\nprimeiro termo {n} e razão {r} são:')
print('_______________________________________')
while c < 11:
    print(f'a{c:<2} = {termo}')
    termo += r
    c += 1
print('_______________________________________')
