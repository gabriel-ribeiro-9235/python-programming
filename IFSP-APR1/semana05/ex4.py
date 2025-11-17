soma = cont = media = menor = mais30mais10 = de40a60 = maior20 = 0
print("-" * 40)
idade = int(input("Idade (negativa para sair): "))
while idade > 0:
    cont += 1
    contribuicao = int(input("Tempo de contribuição: "))
    salario = float(input("Sálario: R$"))
    soma += salario
    if cont == 1:
        menor = contribuicao
    else:
        if contribuicao < menor:
            menor = contribuicao
    if contribuicao > 30 and salario > 10000:
        mais30mais10 += 1
    if 40 < idade < 60 and contribuicao > 15:
        de40a60 += 1
    if contribuicao > 20 and salario > maior20:
        maior20 = salario
    print("-" * 40)
    idade = int(input("Idade (negativa para sair): "))
print("-" * 40)
if cont == 0:
    print("Nenhum trabalhador foi cadastrado.")
else:
    media = soma / cont
    print(f"""a) Média salarial = R${media:.2f}
b) Menor tempo de contribuição = {menor} anos
c) Mais de 30 anos de contribuição e mais de R$10.000,00 = {mais30mais10}
d) % com idade entre 40 e 60 anos com mais de 15 de contribuição = {de40a60/cont*100:.1f}%
e) Maior salário com mais de 20 anos de contribuição = R${maior20:.2f}""")
