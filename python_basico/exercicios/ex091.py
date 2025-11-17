from random import randint
from operator import itemgetter
from time import sleep
print(f'{'DESAFIO 91':=^26}')
jogo = dict()
rank = list()
for c in range(1, 5):
    jogo[f'Jogador {c}'] = randint(1, 6)
for k, v in jogo.items():
    print(f'O {k} tirou {v} no dado.')
    sleep(0.5)
rank = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('=~' * 30)
print('RANKING DOS JOGADORES')
for pos, c in enumerate(rank):
    print(f' -{pos+1}º lugar: {c[0]} com {c[1]}')
    sleep(0.7)
