print(f'{'DESAFIO 71':=^26}')
print('_' * (len('CAIXA ELETRONICO') + 8))
print('    CAIXA ELETRÔNICO')
print('_' * (len('CAIXA ELETRONICO') + 8))
c1 = 0
c10 = 0
c20 = 0
valor = int(input('Valor que quer sacar (inteiro): R$'))
while True:
    c50 = valor // 50
    if valor % 50 == 0:
        break
    valor = valor % 50
    c20 = valor // 20
    if valor % 20 == 0:
        break
    valor = valor % 20
    c10 = valor // 10
    if valor % 10 == 0:
        break
    valor = valor % 10
    c1 = valor
    break
print('_' * (len('CAIXA ELETRONICO') + 8))
print('EMITINDO...')
print('_' * (len('CAIXA ELETRONICO') + 8))
if c50 != 0:
    print(f'{c50:<2} notas de R$50,00' if c50>1 else '1 nota de R$50,00')
if c20 != 0:
    print(f'{c20:<2} notas de R$20,00' if c20>1 else '1 nota de R$10,00')
if c10 != 0:
    print(f'{c10:<2} notas de R$10,00' if c10>1 else '1 nota de R$10,00' )
if c1 != 0:
    print(f'{c1:<2} notas de R$ 1,00' if c1>1 else '1 nota de R$ 1,00')
