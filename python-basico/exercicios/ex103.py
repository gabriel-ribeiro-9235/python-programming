def ficha(nome='<desconhecido>', gol=0):
    return f'O jogador {nome} fez {gol} gol(s).'


print(f'{"DESAFIO 103":=^26}')
jogador = str(input('Nome do jogador: ')).strip().title()
golos = input('Gols: ')
if golos.isnumeric():
    golos = int(golos)
if golos == '' and jogador == '':
    print(ficha())
elif golos == '':
    print(ficha(jogador))
elif jogador == '':
    print(ficha(gol=golos))
else:
    print(ficha(jogador, golos))
