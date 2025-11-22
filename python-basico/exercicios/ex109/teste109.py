from Exercícios.ex109.moeda import moeda

preco = float(input('Digite o preço: R$'))
print(f'A metade de {moeda.moeda(preco)} é {moeda.metade(preco, True)}')
print(f'O dobro de {moeda.moeda(preco)} é {moeda.dobro(preco, True)}')
print(f'{moeda.moeda(preco)} com um aumento de 10% é {moeda.aumentar(preco, 10, True)}')
print(f'{moeda.moeda(preco)} com um desconto de 13% é {moeda.diminuir(preco, 13, True)}')
