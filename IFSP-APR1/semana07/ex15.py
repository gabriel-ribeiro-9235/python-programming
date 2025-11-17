#Verifica a string pura com espaços e maiúsulos, aqui 'Ana' e 'anotaram a data da maratona' não são palíndromos
'''def verificaPalindromo(string, n):
    if len(string) == 0:
        return ''
    else:
        nova = verificaPalindromo(string[1:], n) + string[0]
        if len(nova) == n:
            return nova == string
        else:
            return nova


txt = input("Digite algo: ")
print(verificaPalindromo(txt, len(txt)))
'''
#Verifica a string sem espaços e independentemente de maiúsculo ou minúsculo, aqui 'Ana' e
#'anotaram a data da maratona' são palíndromos'
def verificaPalindromo(string, n):
    if len(string) == 0:
        return ''
    else:
        if string[0] != ' ':
            nova = verificaPalindromo(string[1:], n) + string[0]
        else:
            nova = verificaPalindromo(string[1:], n)
        if len(nova) == n:
            return nova.lower() == string.lower()
        else:
            return nova


txt = input("Digite algo: ")
sespaco = ''
for letra in txt:
    if letra != ' ':
        sespaco += letra
print(verificaPalindromo(sespaco, len(sespaco)))
