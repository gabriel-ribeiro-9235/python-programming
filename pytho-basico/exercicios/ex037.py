print('{:=^26}'.format('DESAFIO 37'))
n = int(input('Digite um número inteiro: '))
print('_' * 26)
print('Para qual base você quer converter?')
print('[1] binário (base 2)')
print('[2] octal (base 8)')
print('[3] hexadecimal (base 16)')
k = int(input('Sua escolha: '))
print('_' * 26)
if k == 1:
    print('{} em binário é {}'.format(n, bin(n)[2:]))
elif k == 2:
    print('{} em octal é {}'.format(n, oct(n)[2:]))
elif k == 3:
    print('{} em hexadecimal é {}'.format(n, hex(n)[2:]))
else:
    print('Opção inválida!')
print('_' * 26)
