print('{:=^26}'.format('DESAFIO 62'))
n = float(input('a1 = '))
if n == int(n):
    n = int(n)
r = float(input('r = '))
if r == int(r):
    r = int(r)
termo = n
c = 1
k = 1
print('_______________________________________')
print(f'Os primeiros 10 termos de uma PA com\nprimeiro termo {n} e razão {r} são:')
print('_______________________________________')
while c < 11:
    print(f'a{c:<2} = {termo}')
    termo += r
    c += 1
while k != 0:
    k = int(input('Mais quantos termos você quer mostrar? '))
    t = c + k
    while c < t:
        print(f'a{c:<2} = {termo}')
        termo += r
        c +=1
print('_______________________________________')
print(f'Foram mostrados {c - 1} termos!')
print('FIM')
