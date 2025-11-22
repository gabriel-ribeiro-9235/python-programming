print(f'{'DESAFIO 95':=^26}')
jogador = dict()
gols = list()
lista = list()
while True:
    jogador['Nome'] = str(input('Nome do jogador: ')).strip().title()
    c = int(input(f'Quantas partidas {jogador['Nome']} jogou? '))
    for i in range(0, c):
        gol = int(input(f'Quantos gols {jogador['Nome']} fez na {i+1:>2}ª partida? '))
        gols.append(gol)
    jogador['Gols'] = gols[:]
    jogador['Total'] = sum(gols)
    lista.append(jogador.copy())
    gols.clear()
    jogador.clear()
    print('=~' * 30)
    resp = str(input('Quer inserir mais jogadores?[S/N] ')).strip().upper()[0]
    while resp not in 'SN':
        resp = str(input('Opção inválida! Quer inserir mais jogadores?[S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
    print('=~' * 30)
print('=~' * 30)
for i in lista:
    for k, v in i.items():
        print(f'{k}: {v}')
    print('=~' * 30)
while True:
    print('Nº   Jogador')
    for pos, i in enumerate(lista):
        print(f'{pos + 1:<3}{i['Nome']:^11}')
    n = int(input('Escolha o número do jogador que você deseja ver os detalhes (999 para sair) '))
    while n not in range(1, len(lista) + 1) and n != 999:
        n = int(input('Escolha inválida! Tente novamente. '))
    print('=~' * 30)
    if n == 999:
        break
    else:
        print(f'{lista[n-1]['Nome']} jogou {len(lista[n-1]['Gols'])} partidas.')
        for k, v in enumerate(lista[n-1]['Gols']):
            print(f'  =>Gols na {k+1:>2}ª partida: {v}')
        print(f'Foi um total de {sum(lista[n-1]['Gols'])} gols.')
        print('=~' * 30)
print('FIM')
