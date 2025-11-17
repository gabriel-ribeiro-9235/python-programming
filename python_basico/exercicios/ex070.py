print(f'{'DESAFIO 70':=^26}')
barato = ''
precobarato = 0
total = 0
maismil = 0
print('_' * (len('CADASTRE SEUS PRODUTOS') + 6))
print('   CADESTRE SEUS PRODUTOS')
print('_' * (len('CADASTRE SEUS PRODUTOS') + 6))
while True:
    produto = str(input('Produto: ')).strip().title()
    preco = float(input('Preço: R$ '))
    if total == 0 or preco < precobarato:
        barato = produto
        precobarato = preco
    total += preco
    if preco > 1000:
        maismil += 1
    escolha = str(input('Deseja cadastrar mais produtos?[S/N] ')).strip().upper()[0]
    while escolha not in 'SN':
        print('Escolha inválida. Tente novamente.')
        escolha = str(input('Deseja cadastrar mais produtos?[S/N] ')).strip().upper()[0]
    if escolha == 'N':
        break
print('PRODUTOS CADASTRADOS!')
print('_' * 26)
print(f'Total: R${total:.2f}')
print(f'Quantidade de produtos que\ncustaram mais de R$1000,00: {maismil}')
print(f'O produto mais barato foi\n{barato} e custou R${precobarato:.2f}')
