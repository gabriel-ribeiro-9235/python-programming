from datetime import date

def voto(ano):
    idade = date.today().year - ano
    if idade < 16:
        return f'Com {idade} anos: NÃO PODE VOTAR!'
    elif idade < 18 or idade > 70:
        return f'Com {idade} anos: VOTO OPCIONAL!'
    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO!'

print(f'{"DESAFIO 101":=^26}')
nasc = int(input('Digite o ano de nascimento: '))
print(voto(nasc))
