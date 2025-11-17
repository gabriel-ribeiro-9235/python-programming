def leaidin(msg):
    k = str(input(msg)).strip().replace(',', '.')
    valido = False
    while not valido:
        if k.isalpha() or k == '':
            print(f'\033[31mERRO! \"{k}\" não é um preço válido!\033[m')
            k = str(input(msg)).strip().replace(',', '.')
        else:
            valido = True
    return float(k)


def leiaint(msg):
    while True:
        try:
            k = int(input(msg))
        except KeyboardInterrupt:
            print('\n\033[31mO usuário não quis digitar nenhum valor inteiro.\033[m')
            k = 0
            break
        except (ValueError, TypeError):
            print('\033[31mERRO! Digite um número inteiro válido.\033[m')
        else:
            break
    return k


def leiafloat(msg):
    while True:
        try:
            k = float(input(msg))
        except KeyboardInterrupt:
            print('\n\033[31mO usuário não quis digitar nenhum valor inteiro.\033[m')
            k = 0
            break
        except (ValueError, TypeError):
            print('\033[31mERRO! Digite um número real válido.\033[m')
        else:
            break
    return k


def verificasite(url):
    import requests
    try:
        r = requests.get(url)
        print('\033[32mO site do pudim está acessível!\033[m')
    except requests.ConnectionError:
        print('\033[31mO site do pudim não está acessível!\033[m')
