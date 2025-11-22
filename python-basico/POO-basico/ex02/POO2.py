from datetime import date

class Pessoa:
    ano_atual = date.today().year

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        ano_nascimento = self.ano_atual - self.idade
        return ano_nascimento

    @classmethod
    def get_idade(cls, nome, ano_nascimento):
        idade = cls.ano_atual - ano_nascimento
        return cls(nome, idade)
