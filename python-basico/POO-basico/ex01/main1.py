from POO1 import Pessoa

p1 = Pessoa('Gabriel', 19)
print(f'{p1.nome} nasceu em {p1.get_ano()}')
p1.comer('maçã')
p1.falar('basquete')
p1.parar_comer()
p1.falar('futebol')
p1.comer('morango')
p1.parar_falar()
p1.comer('banana')
p1.parar_comer()
p1.parar_falar()
