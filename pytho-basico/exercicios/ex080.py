print(f'{'DESAFIO 80':=^26}')
print('Insira 5 valores')
lista = []
for c in range(0, 5):
    lista.append(int(input(f'Digite o {c+1}º valor: ')))
for c in range(0, len(lista) - 1):
    for d in range(c + 1, len(lista)):
        if lista[c] > lista[d]:
            a = lista[c]
            lista[c] = lista[d]
            lista[d] = a
print('_' * 26)
print(f'''Os valores digitados em ordem
crescente foram {lista}''')
