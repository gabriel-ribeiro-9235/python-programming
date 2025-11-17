def arqexiste(nome):
    try:
        a = open(nome, 'rt', encoding='utf-8')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criararq(arq):
    try:
        a = open(arq, 'wt+', encoding='utf-8')
        a.close()
    except:
        print('\033[31mHouve um erro no criação do arquivo!\033[m')
    else:
        print(f'Arquivo {arq} criado com sucesso!')


def lerarq(arq):
    try:
        a = open(arq, 'rt', encoding='utf-8')
    except:
        print('\033[31mErro ao ler arquivo!\033[m')
    else:
        print(a.read())
    finally:
        a.close()


def menu(arq):
    from Exercícios.ex111Eex112.utilidadesCeV.dado import leiaint
    from time import sleep
    while True:
        sleep(1)
        print('_' * 42)
        print('MENU PRINCIPAL'.center(42))
        print('_' * 42)
        print('\033[33m1 -\033[34m Ver pessoas cadastradas\033[33m')
        print('2 - \033[34mCadastrar pessoas\033[33m')
        print('3 - \033[34mSair do sistema\033[m')
        print('_' * 42)
        n = leiaint('\033[32mSua opção: \033[m')
        if n == 1:
            print('_' * 42)
            print('PESSOAS CADASTRADAS'.center(42))
            print('_' * 42)
            lerarq(arq)
        elif n == 2:
            print('_' * 42)
            print('OPÇÃO 2'.center(42))
            print('_' * 42)
        elif n == 3:
            print('_' * 42)
            print('SAINDO DO SISTEMA...'.center(42))
            print('_' * 42)
            sleep(1)
            break
        else:
            print('\033[31mERRO! Escolha uma opção válida!\033[m')
            continue
