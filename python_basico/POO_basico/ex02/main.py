from POO2 import Pessoa

print('Com classmethod:')
p1 = Pessoa.get_idade('Gabriel', 2006)
print(p1.nome, p1.idade)
print(Pessoa.ano_atual - p1.idade)
print('_' * 20)
print('Sem classmethod')
p2 = Pessoa('Gabriel', 19)
print(p2.nome, p2.idade)
print(p2.get_ano_nascimento())
