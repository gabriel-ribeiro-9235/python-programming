soma = cont = media = menor = menorrenda = mais50oumais20 = de3a8 = maior = 0
print("-" * 40)
renda = float(input("Renda (negativa para sair): R$"))
while renda >= 0:
    cont += 1
    divida = float(input("Dívida: R$"))
    soma += renda
    if cont == 1:
        menor = divida
        menorrenda = renda
    else:
        if divida < menor:
            menor = divida
        if renda < menorrenda:
            menorrenda = renda
    if divida /renda > 0.5 or divida > 20000:
        mais50oumais20 += 1
    if 3000 < renda < 8000 and divida / renda > 0.3:
        de3a8 += 1
    if renda > maior:
        maior = renda
    print("-" * 40)
    renda = float(input("Renda (negativa para sair): R$"))
print("-" * 40)
if cont == 0:
    print("Nenhuma pessoa foi cadastrada.")
else:
    media = soma / cont
    print(f"""a) Renda média = R${media:.2f}
b) Menor dívida = R${menor:.2f}
c) Dívida maior que 50% da renda ou dívida maior que R$20.000,00 = {mais50oumais20}
d) % com renda entre R$3.000,00 e R$8.000,00 e dívida maior que 30% da renda = {de3a8/cont*100:.1f}%
e) Diferença entre a maior e a menor renda = R${maior-menorrenda:.2f}""")
