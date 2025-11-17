print(f'{'DESAFIO 93':=^26}')
jogador = dict()
gols = list()
jogador['Nome'] = str(input('Nome do jogador: ')).strip().title()
c = int(input(f'Quantas partidas {jogador['Nome']} jogou? '))
for i in range(0, c):
    gol = int(input(f'Quantos gols {jogador['Nome']} fez na {i+1:>2}ª partida? '))
    gols.append(gol)
jogador['Gols'] = gols
jogador['Total'] = sum(gols)
print('=~' * 30)
print(jogador)
print('=~' * 30)
for k, v in jogador.items():
    print(f'{k}: {v}')
print('=~' * 30)
print(f'{jogador['Nome']} jogou {len(gols)} partidas')
for pos, c in enumerate(gols):
    print(f'  =>Gols na {pos+1:>2}ª partida: {c}')
print(f'Fez um total de {sum(gols)} gols')
