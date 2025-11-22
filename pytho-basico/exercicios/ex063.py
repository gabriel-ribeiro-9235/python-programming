print('{:=^26}'.format('DESAFIO 63'))
n = int(input('Quantos termos você quer? '))
a = [0, 1, 0]
c = 1
print(f'''________________________________________________________
Os {n} primeiros termos da sequência de Fibonacci são:''')
while c <= n:
    if c == 1 or c == 2:
        print(f'a{c:<2} = {a[c - 1]}')
    else:
        a[2] = a[1] + a[0]
        print(f'a{c:<2} = {a[2]}')
        a[0] = a[1]
        a[1] = a[2]
    c +=1
print('________________________________________________________')
