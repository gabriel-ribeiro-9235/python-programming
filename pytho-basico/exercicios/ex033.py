print('{:=^26}'.format('DESAFIO 33'))
a = float(input('\033[1;4mPrimeiro número\033[m: '))
if a == int(a):
    a = int(a)
b = float(input('\033[1;4mSegundo número\033[m: '))
if b == int(b):
    b = int(b)
c = float(input('\033[1;4mTerceiro número\033[m: '))
if c == int(c):
    c = int(c)
print('{:-^26}'.format(''))
if a >= b and a >= c:
    print('\033[32mMaior: {}'.format(a))
else:
    if b >= a and b >= c:
        print('\033[32mMaior: {}'.format(b))
    else:
        print('\033[32mMaior: {}'.format(c))
if a <= b and a <= c:
    print('\033[31mMenor: {}\033[m'.format(a))
else:
    if b <= a and b <= c:
        print('\033[31mMenor: {}\033[m'.format(b))
    else:
        print('\033[31mMenor: {}\033[m'.format(c))
