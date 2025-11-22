from Exercícios.ex108.moeda import moeda

preco = float(input('Digite o preço: R$'))
print(f'A metade de {moeda.moeda(preco)} é {moeda.moeda(moeda.metade(preco))}')
print(f'O dobro de {moeda.moeda(preco)} é {moeda.moeda(moeda.dobro(preco))}')
print(f'{moeda.moeda(preco)} com um aumento de 10% é {moeda.moeda(moeda.aumentar(preco, 10))}')
print(f'{moeda.moeda(preco)} com um desconto de 13% é {moeda.moeda(moeda.diminuir(preco, 13))}')
