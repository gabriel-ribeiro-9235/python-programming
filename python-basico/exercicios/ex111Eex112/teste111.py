from Exercícios.ex111Eex112.utilidadesCeV import moeda

preco = float(input('Digite o preço: R$'))
moeda.resumo(preco, 80, 35)

p = float(input('Digite o preço: R$'))
print(f'A metade de {moeda.moeda(p)} é {moeda.metade(p, True)}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.dobro(preco, True)}')
print(f'{moeda.moeda(p)} com um aumento de 10% é {moeda.aumentar(p, 10, True)}')
print(f'{moeda.moeda(p)} com um desconto de 13% é {moeda.diminuir(p, 13, True)}')
