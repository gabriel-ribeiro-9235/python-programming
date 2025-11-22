from POO4 import Produto

p1 = Produto('CAMISETA', 'R$50,00')
p1.desconto(10)
print(f'{p1.nome}: R${p1.preco:.2f}'.replace('.', ','))
