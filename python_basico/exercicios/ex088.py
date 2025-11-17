from random import randint
from time import sleep
print(f'{'DESAFIO 88':=^26}')
print('_' * 40)
print(f'{'GERADOR DE JOGOS DA MEGA SENA':^40}')
print('_' * 40)
jogos = list()
palpites = list()
n = int(input('Quantos jogos você quer fazer? '))
for c in range(0, n):
    for l in range(0, 6):
        k = randint(1, 60)
        while k in palpites:
            k = randint(1, 60)
        palpites.append(k)
    jogos.append(palpites[:])
    palpites.clear()
for c in range(0, n):
    jogos[c].sort()
for pos, p in enumerate(jogos):
    sleep(0.5)
    print(f'Jogo {pos+1:>2}: {p}')
print(f'{' < BOA SORTE! > ':~^40}')
