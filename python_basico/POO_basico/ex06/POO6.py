class A:
    #private
    __dados = {}
    def __init__(self):
        pass

    def adiciona_cliente(self, identificacao, nome):
        if 'cliente' not in self.__dados:
            self.__dados['cliente'] = {'id': identificacao, 'nome': nome}
        else:
            self.tira_cliente(identificacao, nome)

    @classmethod
    def tira_cliente(cls, identificacao, name):
        cls.__dados['cliente'].update({'id': identificacao, 'nome': name})
