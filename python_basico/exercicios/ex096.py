def area(a, b):
    print(f'A área de um terreno {a}m x {b}m é {a*b}m²')

print(f'{'DESAFIO 96':=^26}')
print('CALCULADORA DE ÁREA')
print('-=' * 20)
largura = float(input('Largura (m): '))
if largura == int(largura):
    largura = int(largura)
comprimento = float(input('Comprimento (m): '))
if comprimento == int(comprimento):
    comprimento = int(comprimento)
area(largura, comprimento)
