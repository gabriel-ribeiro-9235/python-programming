from random import randint
from time import sleep
print('{:=^26}'.format('DESAFIO 28'))
n = randint(0, 5)
print('\033[33m-=-' * 17)
print('\033[34mVou pensar em um número de 0 a 5. Tente adivinhar!')
print('\033[33m-=-' * 17)
numero = int(input('\033[mEm qual número pensei? '))
print('\033[34mPROCESSANDO...')
sleep(2)
if numero == n:
    print('\033[32mParabéns, você acertou!\033[m')
else:
    print('\033[31mVocê errou! Eu pensei no número {}.\033[m'.format(n))
