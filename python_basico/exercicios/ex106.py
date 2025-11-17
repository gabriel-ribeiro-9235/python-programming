def painel():
    print('\033[m\033[97;42m~' * 27)
    print('  SISTEMA DE AJUDA PyHELP')
    print('~' * 27)

def funcoes(msg):
    print('\033[97;44m~' * (36+len(msg)))
    print(f"  Acessando o manual do comando '{msg}'")
    print('~' * (36+len(msg)))
    print('\033[m\033[7;97;40m', end='')
    help(msg)


print(f'{"DESAFIO 106":=^26}')
while True:
    painel()
    funcao = str(input("\033[mFunção ou Biblioteca ('FIM' para sair) > ")).strip().lower()
    if funcao == 'fim':
        break
    funcoes(funcao)
print('\033[m\033[97;41m~' * 13)
print(f'  ATÉ LOGO!')
print('~' * 13, '\n\033[m')
