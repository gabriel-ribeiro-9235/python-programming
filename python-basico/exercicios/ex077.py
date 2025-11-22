print(f'{'DESAFIO 77':=^26}')
listagem = ('noite', 'dia', 'vogal', 'Alto', 'tio', 'tia', 'pai', 'bola', 'futebol', 'baseball', 'secretaria', 'escola', 'arma', 'exercito')
print(f'{'PROCURANDO VOGAIS...':^40}')
print('_' * 40)
for c in listagem:
    print(f'\nA palavra {c.upper()} tem ', end='')
    if 'a' in c.lower():
        print('"a"', end=' ')
    if 'e' in c.lower():
        print('"e"', end=' ')
    if 'i' in c.lower():
        print('"i"', end=' ')
    if 'o' in c.lower():
        print('"o"', end=' ')
    if 'u' in c.lower():
        print('"u"', end=' ')
print()
print('_' * 40)
print('FIM')
