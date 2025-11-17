from random import randint
from time import sleep
print('{:=^26}'.format('DESAFIO 58'))
n = randint(0, 10)
print('\033[33m-=-' * 17)
print('\033[34mVou pensar em um número de 0 a 10. Tente adivinhar!')
print('\033[33m-=-' * 17)
c = 0
numero = 11
while numero != n:
    numero = int(input('\033[mEm qual número pensei? '))
    print('\033[34mPROCESSANDO...')
    sleep(1)
    if numero != n:
        print('\033[31mMais... Tente novamente.\033[m' if n > numero else '\033[31mMenos... Tente novamente.\033[m')
    c += 1
    print('\033[m___________________________________')
print('\033[32mParabéns, você acertou!\033[m')
print(f'Você precisou de {c} tentativa.'if c==1 else f'Você precisou de {c} tentativas.')
