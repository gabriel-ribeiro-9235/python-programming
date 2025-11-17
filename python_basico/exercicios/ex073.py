print(f'{'DESAFIO 73':=^26}')
tabela = ('Flamengo', 'Cruzeiro', 'RB Bragantino', 'Palmeiras',
          'Bahia', 'Fluminense', 'Atlético-MG', 'Botafogo',
          'Mirassol', 'Corinthians', 'Grêmio', 'Ceará', 'Vasco',
          'São Paulo', 'Santos', 'Vitória', 'Internacional',
          'Fortaleza', 'Juventude', 'Sport')
print(f'G5: {tabela[:5]}')
print(f'Z4: {tabela[-4:]}')
print(f'Times em ordem alfabética: {sorted(tabela)}')
print(f'O São Paulo está na {tabela.index('São Paulo')+1}ª posição')
