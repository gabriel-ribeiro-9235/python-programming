from time import sleep
from random import choice
print('{:=^26}'.format('DESAFIO 45'))
print('\033[97m-=' * 13)
print('PEDRA, PAPEL, TESOURA')
print('-=' * 13, '\033[m')
computador = choice(['pedra', 'papel', 'tesoura'])
print("""\033[97m[1] para Pedra
[2] para Papel
[3] para Tesoura""")
jogada = str(input('\033[97mSua escolha: ')).strip()
if jogada.isnumeric():
    jogada = int(jogada)
    if jogada == 1:
        jogador = 'pedra'
    elif jogada == 2:
        jogador = 'papel'
    elif jogada == 3:
        jogador = 'tesoura'
    else:
        print('_' * 26)
        print('\033[31mJOGADA INVÁLIDA! Tente novamente.\033[m')
        exit()
else:
    jogador = jogada.lower()
    if not jogador in ['pedra', 'papel', 'tesoura']:
        print('_' * 26)
        print('\033[31mJOGADA INVÁLIDA! Tente novamente.\033[m')
        exit()
print('PEDRA, PAPEL, TESOURA...')
sleep(1.5)
print('\033[97m_' * 26)
print('Você jogou \033[32m{}\033[97m!'.format(jogador.title()))
print('O computador jogou \033[31m{}\033[97m!'.format(computador.title()))
print('_' * 26)
if jogador == computador:
    print('\033[1;36mEMPATE!\033[m')
elif (jogador == 'pedra' and computador == 'tesoura') or (jogador == 'papel' and computador == 'pedra') or (jogador == 'tesoura' and computador == 'papel'):
    print('\033[1;32mVOCÊ GANHOU!\033[m')
else:
    print('\033[1;31mVOCÊ PERDEU!\033[m')
