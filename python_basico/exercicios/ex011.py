print('{:=^26}'.format('DESAFIO 11'))
altura = float(input('Qual é a altura da parede (m): '))
if altura == int(altura):
    altura = int(altura)
largura = float(input('Qual é a largura da parede (m): '))
if largura == int(largura):
    largura = int(largura)
litros_de_tinta = (altura * largura) / 2
print('A sua parede tem dimensões de \033[32m{}\033[m m x \033[32m{}\033[m m'.format(altura, largura), end='')
print(', o que dará uma área de \033[32m{}\033[m m² a ser pintada,'.format(altura * largura))
print('e você precisará de \033[31m{:.1f}\033[m litros de tinta para pintá-la!'.format(litros_de_tinta))
