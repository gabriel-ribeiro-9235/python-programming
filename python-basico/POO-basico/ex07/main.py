from POO7 import *

escritor = Escritor('Luiz')
caneta = Caneta('Bic')
maquina = MaquinaDeEscrever()
print(escritor.nome)
print(caneta.marca)
escritor.ferramenta = caneta
escritor.ferramenta.escrever()
escritor.ferramenta = maquina
escritor.ferramenta.escrever()
