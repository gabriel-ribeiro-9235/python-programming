class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def desconto(self, pct):
        self.preco -= pct * self.preco / 100

    # Getter do nome
    @property
    def nome(self):
        return self._nome

    # Setter do nome
    @nome.setter
    def nome(self, valor):
        self._nome = valor.title()

    # Getter preço
    @property
    def preco(self):
        return self._preco

    # Setter preço
    @preco.setter
    def preco(self, valor):
        if isinstance(valor, str):
            valor = float(valor.replace('R$', '',).replace(',', '.'))
        self._preco = valor
