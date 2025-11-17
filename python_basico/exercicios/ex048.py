print('{:=^26}'.format('DESAFIO 48'))
s = 0
cont = 0
print('SOMA DOS ÍMPARES E MÚLTIPLOS DE 3 DE 1 A 500:')
for c in range(1, 501):
    if c % 3 == 0 and c % 2 == 1:
        cont += 1
        s += c
print('O somatório dos {} números vale {}'.format(cont, s))
