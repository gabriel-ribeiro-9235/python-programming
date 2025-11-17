from Exercícios.ex107.moeda import moeda

preco = float(input('Digite o preço: R$'))
print(f'A metade de {preco} é {moeda.metade(preco)}')
print(f'O dobro de {preco} é {moeda.dobro(preco)}')
print(f'{preco} com um aumento de 10% é {moeda.aumentar(preco, 10)}')
print(f'{preco} com um desconto de 13% é {moeda.diminuir(preco, 13)}')
